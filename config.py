import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Application configuration class"""
    
    # Flask Configuration
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'dev-secret-key-change-in-production')
    DEBUG = os.getenv('FLASK_DEBUG', 'True') == 'True'
    
    # API Keys
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')
    YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY', '')
    
    # Upload Configuration
    UPLOAD_FOLDER = 'static/uploads'
    MAX_CONTENT_LENGTH = int(os.getenv('MAX_UPLOAD_SIZE', 16 * 1024 * 1024))  # 16MB
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'avi', 'mov'}
    ALLOWED_IMAGE_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    ALLOWED_VIDEO_EXTENSIONS = {'mp4', 'avi', 'mov'}
    
    # Application Info
    APP_NAME = os.getenv('APP_NAME', 'Alto Car Digital Manual')
    APP_VERSION = os.getenv('APP_VERSION', '1.0.0')
    
    # Gemini Model Configuration
    GEMINI_MODEL = 'gemini-1.5-pro-latest'
    GEMINI_TEMPERATURE = 0.7
    GEMINI_MAX_TOKENS = 2048
    
    # YouTube Search Configuration
    YOUTUBE_MAX_RESULTS = 5
    
    @staticmethod
    def allowed_file(filename, file_type='all'):
        """Check if file extension is allowed"""
        if '.' not in filename:
            return False
        ext = filename.rsplit('.', 1)[1].lower()
        
        if file_type == 'image':
            return ext in Config.ALLOWED_IMAGE_EXTENSIONS
        elif file_type == 'video':
            return ext in Config.ALLOWED_VIDEO_EXTENSIONS
        else:
            return ext in Config.ALLOWED_EXTENSIONS
