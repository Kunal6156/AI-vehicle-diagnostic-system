import google.generativeai as genai
from PIL import Image
import json
import os
from config import Config

class GeminiService:
    """Service class for interacting with Google Gemini API"""
    
    def __init__(self):
        """Initialize Gemini service with API key"""
        if not Config.GEMINI_API_KEY:
            raise ValueError("Gemini API key not found in configuration")
        
        genai.configure(api_key=Config.GEMINI_API_KEY)
        self.model = genai.GenerativeModel(Config.GEMINI_MODEL)
        
        # Load Alto knowledge base
        knowledge_base_path = 'data/alto_knowledge_base.json'
        if os.path.exists(knowledge_base_path):
            with open(knowledge_base_path, 'r') as f:
                self.knowledge_base = json.load(f)
        else:
            self.knowledge_base = {}
    
    def analyze_image(self, image_path):
        """
        Analyze car component image using Gemini Vision
        
        Args:
            image_path: Path to the image file
            
        Returns:
            dict: Analysis results with component identification and details
        """
        try:
            # Load image
            img = Image.open(image_path)
            
            # Create comprehensive prompt for Alto car analysis
            prompt = f"""You are an expert automotive technician specializing in Maruti Suzuki Alto cars.

Analyze this image carefully and provide:

1. COMPONENT IDENTIFICATION: What car component, button, indicator, or part is shown?
2. FUNCTION: What is its purpose and how does it work?
3. LOCATION: Where is this located in the Alto car (dashboard, engine bay, interior, etc.)?
4. CONDITION ASSESSMENT: Based on the image, does it appear normal, damaged, or show any issues?
5. COMMON PROBLEMS: What are typical problems with this component in Alto cars?
6. TROUBLESHOOTING: If there's an issue visible, what could be the cause?
7. SOLUTION: What steps should be taken to fix or maintain this component?
8. SEARCH KEYWORDS: Provide 3-5 specific keywords for YouTube searches related to this component or issue.

Additional Context - Maruti Suzuki Alto Information:
{json.dumps(self.knowledge_base, indent=2)}

Provide a detailed, practical response that would help an Alto car owner understand and potentially fix issues."""

            # Generate response
            response = self.model.generate_content([prompt, img])
            
            return {
                'success': True,
                'analysis': response.text,
                'component_type': self._extract_component_type(response.text)
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'analysis': f"Error analyzing image: {str(e)}"
            }
    
    def analyze_text_query(self, query):
        """
        Analyze text query about Alto car
        
        Args:
            query: User's text question
            
        Returns:
            dict: Analysis results with answer and search keywords
        """
        try:
            prompt = f"""You are an expert automotive technician specializing in Maruti Suzuki Alto cars.

User Question: {query}

Alto Car Knowledge Base:
{json.dumps(self.knowledge_base, indent=2)}

Provide a comprehensive answer that includes:
1. Direct answer to the question
2. Detailed explanation
3. Step-by-step troubleshooting if applicable
4. Safety precautions if relevant
5. 3-5 specific YouTube search keywords for video tutorials

Format your response clearly with proper sections."""

            response = self.model.generate_content(prompt)
            
            return {
                'success': True,
                'analysis': response.text,
                'search_keywords': self._extract_search_keywords(response.text)
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'analysis': f"Error processing query: {str(e)}"
            }
    
    def analyze_video_frame(self, video_path, frame_path=None):
        """
        Analyze video or video frame for car issues
        
        Args:
            video_path: Path to video file
            frame_path: Path to extracted frame (optional)
            
        Returns:
            dict: Analysis results
        """
        try:
            # For simplicity, we'll analyze the first frame
            # In production, you might want to analyze multiple frames
            
            if frame_path and os.path.exists(frame_path):
                img = Image.open(frame_path)
            else:
                # Extract first frame using PIL or OpenCV
                return {
                    'success': False,
                    'error': 'Video frame extraction not implemented',
                    'analysis': 'Please upload an image for analysis'
                }
            
            prompt = """You are an expert automotive technician specializing in Maruti Suzuki Alto cars.

Analyze this video frame showing a car issue or component.

Provide:
1. What is happening in this video/image?
2. Is there any visible problem or malfunction?
3. What component or system is involved?
4. What could be causing this issue?
5. Recommended diagnosis and repair steps
6. YouTube search keywords for related repair videos

Be specific to Maruti Alto cars when possible."""

            response = self.model.generate_content([prompt, img])
            
            return {
                'success': True,
                'analysis': response.text,
                'component_type': 'video_analysis'
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'analysis': f"Error analyzing video: {str(e)}"
            }
    
    def _extract_component_type(self, text):
        """Extract component type from analysis text"""
        text_lower = text.lower()
        
        # Check for common components
        components = {
            'dashboard': ['dashboard', 'instrument cluster', 'speedometer', 'odometer'],
            'warning_light': ['warning light', 'indicator light', 'check engine', 'warning lamp'],
            'button': ['button', 'switch', 'control'],
            'engine': ['engine', 'motor', 'cylinder'],
            'brake': ['brake', 'braking system'],
            'electrical': ['electrical', 'wiring', 'fuse', 'battery'],
            'ac': ['air conditioning', 'a/c', 'ac', 'cooling'],
            'tire': ['tire', 'tyre', 'wheel']
        }
        
        for comp_type, keywords in components.items():
            if any(keyword in text_lower for keyword in keywords):
                return comp_type
        
        return 'general'
    
    def _extract_search_keywords(self, text):
        """Extract search keywords from analysis text"""
        # Simple extraction - look for keyword patterns
        keywords = []
        lines = text.split('\n')
        
        for line in lines:
            if 'keyword' in line.lower() or 'search' in line.lower():
                # Extract keywords from this line
                parts = line.split(':')
                if len(parts) > 1:
                    potential_keywords = parts[1].strip().split(',')
                    keywords.extend([k.strip() for k in potential_keywords[:5]])
        
        return keywords[:5] if keywords else ['Alto car repair', 'Maruti Alto maintenance']
