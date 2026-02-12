from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from config import Config
import json

class YouTubeService:
    """Service class for searching YouTube videos"""
    
    def __init__(self):
        """Initialize YouTube service with API key"""
        if not Config.YOUTUBE_API_KEY:
            raise ValueError("YouTube API key not found in configuration")
        
        self.youtube = build('youtube', 'v3', developerKey=Config.YOUTUBE_API_KEY)
        self.max_results = Config.YOUTUBE_MAX_RESULTS
    
    def search_videos(self, query, max_results=None):
        """
        Search YouTube for videos related to query
        
        Args:
            query: Search query string
            max_results: Maximum number of results (default from config)
            
        Returns:
            list: List of video information dictionaries
        """
        if max_results is None:
            max_results = self.max_results
        
        try:
            # Add "Alto car" to query for better relevance
            enhanced_query = f"Maruti Alto {query} repair tutorial"
            
            # Execute search
            search_response = self.youtube.search().list(
                q=enhanced_query,
                part='id,snippet',
                maxResults=max_results,
                type='video',
                relevanceLanguage='en',
                safeSearch='strict',
                order='relevance'
            ).execute()
            
            videos = []
            for item in search_response.get('items', []):
                video_id = item['id']['videoId']
                snippet = item['snippet']
                
                video_info = {
                    'video_id': video_id,
                    'title': snippet['title'],
                    'description': snippet['description'],
                    'thumbnail': snippet['thumbnails']['medium']['url'],
                    'channel': snippet['channelTitle'],
                    'published_at': snippet['publishedAt'],
                    'url': f'https://www.youtube.com/watch?v={video_id}',
                    'embed_url': f'https://www.youtube.com/embed/{video_id}'
                }
                videos.append(video_info)
            
            return {
                'success': True,
                'videos': videos,
                'query': enhanced_query
            }
            
        except HttpError as e:
            return {
                'success': False,
                'error': str(e),
                'videos': []
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'videos': []
            }
    
    def search_multiple_queries(self, queries, max_per_query=2):
        """
        Search for multiple queries and combine results
        
        Args:
            queries: List of search query strings
            max_per_query: Max results per query
            
        Returns:
            dict: Combined search results
        """
        all_videos = []
        
        for query in queries[:3]:  # Limit to 3 queries to avoid API quota
            result = self.search_videos(query, max_results=max_per_query)
            if result['success']:
                all_videos.extend(result['videos'])
        
        # Remove duplicates based on video_id
        unique_videos = []
        seen_ids = set()
        
        for video in all_videos:
            if video['video_id'] not in seen_ids:
                unique_videos.append(video)
                seen_ids.add(video['video_id'])
        
        return {
            'success': True,
            'videos': unique_videos[:self.max_results],
            'total_found': len(unique_videos)
        }
    
    def get_popular_alto_videos(self):
        """
        Get popular Alto car maintenance and repair videos
        
        Returns:
            dict: Popular video results
        """
        popular_queries = [
            "Maruti Alto complete service",
            "Alto car common problems",
            "Alto maintenance guide",
            "Alto troubleshooting"
        ]
        
        return self.search_multiple_queries(popular_queries, max_per_query=2)
