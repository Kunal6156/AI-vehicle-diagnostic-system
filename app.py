from flask import Flask, render_template, request, jsonify, send_from_directory
import os
from werkzeug.utils import secure_filename
import json
from datetime import datetime

from config import Config
from models.gemini_service import GeminiService
from models.youtube_service import YouTubeService

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize services
try:
    gemini_service = GeminiService()
    youtube_service = YouTubeService()
    services_initialized = True
except Exception as e:
    print(f"Warning: Services initialization error: {e}")
    services_initialized = False


@app.route('/')
def index():
    """Render main page"""
    return render_template('index.html', 
                         app_name=Config.APP_NAME,
                         version=Config.APP_VERSION)


@app.route('/manual')
def manual():
    """Render digital manual page"""
    return render_template('manual.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    """
    Main analysis endpoint - handles image, video, and text queries
    """
    if not services_initialized:
        return jsonify({
            'success': False,
            'error': 'Services not properly configured. Please check API keys.'
        }), 500
    
    try:
        # Get request type
        request_type = request.form.get('type', 'text')
        
        if request_type == 'text':
            # Handle text query
            query = request.form.get('query', '')
            if not query:
                return jsonify({'success': False, 'error': 'Query is required'}), 400
            
            # Analyze with Gemini
            analysis_result = gemini_service.analyze_text_query(query)
            
            if analysis_result['success']:
                # Search YouTube videos
                search_keywords = analysis_result.get('search_keywords', [query])
                youtube_result = youtube_service.search_multiple_queries(search_keywords)
                
                return jsonify({
                    'success': True,
                    'type': 'text',
                    'analysis': analysis_result['analysis'],
                    'videos': youtube_result.get('videos', []),
                    'timestamp': datetime.now().isoformat()
                })
            else:
                return jsonify(analysis_result), 500
        
        elif request_type == 'image':
            # Handle image upload
            if 'file' not in request.files:
                return jsonify({'success': False, 'error': 'No file uploaded'}), 400
            
            file = request.files['file']
            if file.filename == '':
                return jsonify({'success': False, 'error': 'No file selected'}), 400
            
            if not Config.allowed_file(file.filename, 'image'):
                return jsonify({'success': False, 'error': 'Invalid file type'}), 400
            
            # Save file
            filename = secure_filename(file.filename)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"{timestamp}_{filename}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Analyze with Gemini
            analysis_result = gemini_service.analyze_image(filepath)
            
            if analysis_result['success']:
                # Extract search keywords from analysis
                analysis_text = analysis_result['analysis']
                
                # Generate search queries based on analysis
                search_queries = [
                    f"Alto {analysis_result.get('component_type', 'repair')}",
                    "Alto car maintenance"
                ]
                
                # Search YouTube
                youtube_result = youtube_service.search_multiple_queries(search_queries)
                
                return jsonify({
                    'success': True,
                    'type': 'image',
                    'analysis': analysis_result['analysis'],
                    'component_type': analysis_result.get('component_type', 'unknown'),
                    'videos': youtube_result.get('videos', []),
                    'image_url': f'/uploads/{filename}',
                    'timestamp': datetime.now().isoformat()
                })
            else:
                return jsonify(analysis_result), 500
        
        elif request_type == 'video':
            # Handle video upload (simplified - analyze first frame)
            if 'file' not in request.files:
                return jsonify({'success': False, 'error': 'No file uploaded'}), 400
            
            file = request.files['file']
            if not Config.allowed_file(file.filename, 'video'):
                return jsonify({'success': False, 'error': 'Invalid file type'}), 400
            
            # Save file
            filename = secure_filename(file.filename)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"{timestamp}_{filename}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # For now, return a message that video analysis requires frame extraction
            return jsonify({
                'success': True,
                'type': 'video',
                'analysis': 'Video uploaded successfully. For detailed analysis, please extract a frame showing the issue and upload as an image.',
                'videos': [],
                'video_url': f'/uploads/{filename}',
                'timestamp': datetime.now().isoformat()
            })
        
        else:
            return jsonify({'success': False, 'error': 'Invalid request type'}), 400
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/knowledge-base')
def knowledge_base():
    """Get Alto car knowledge base"""
    try:
        with open('data/alto_knowledge_base.json', 'r') as f:
            kb = json.load(f)
        return jsonify({'success': True, 'data': kb})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/popular-videos')
def popular_videos():
    """Get popular Alto maintenance videos"""
    if not services_initialized:
        return jsonify({
            'success': False,
            'error': 'YouTube service not configured'
        }), 500
    
    try:
        result = youtube_service.get_popular_alto_videos()
        return jsonify(result)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """Serve uploaded files"""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'services': {
            'gemini': bool(Config.GEMINI_API_KEY),
            'youtube': bool(Config.YOUTUBE_API_KEY),
            'initialized': services_initialized
        },
        'version': Config.APP_VERSION
    })


@app.errorhandler(404)
def not_found(e):
    """Handle 404 errors"""
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(e):
    """Handle 500 errors"""
    return render_template('500.html'), 500


if __name__ == '__main__':
    # Get port from environment variable (Render provides this)
    port = int(os.environ.get('PORT', 5000))
    
    # Check if API keys are configured
    if not Config.GEMINI_API_KEY:
        print("\n⚠️  WARNING: GEMINI_API_KEY not configured!")
        print("Please set it in Render environment variables\n")
    
    if not Config.YOUTUBE_API_KEY:
        print("\n⚠️  WARNING: YOUTUBE_API_KEY not configured!")
        print("Please set it in Render environment variables\n")
    
    print(f"\n🚗 {Config.APP_NAME} v{Config.APP_VERSION}")
    print(f"🌐 Starting server on port {port}")
    print(f"📊 Environment: {os.environ.get('FLASK_ENV', 'development')}\n")
    
    # Bind to 0.0.0.0 for Render
    app.run(host='0.0.0.0', port=port, debug=Config.DEBUG)
