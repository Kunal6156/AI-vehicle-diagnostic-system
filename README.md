# Alto Car Digital Manual - DRDO Project

An AI-powered multimodal digital manual system for Maruti Suzuki Alto cars that uses Google Gemini AI for image/video analysis and YouTube API for repair tutorials.

## 🚀 Features

- **Image Analysis**: Upload photos of car components, dashboard, warning lights, or issues
- **Video Analysis**: Upload videos showing car problems
- **Text Queries**: Ask questions about your Alto car
- **AI Diagnostics**: Powered by Google Gemini 1.5 Flash for accurate analysis
- **Video Tutorials**: Automatic YouTube video recommendations for repairs
- **Knowledge Base**: Comprehensive Alto car information database
- **Responsive Design**: Works on desktop, tablet, and mobile devices

## 📋 Prerequisites

- Python 3.8 or higher
- Google Gemini API Key
- YouTube Data API v3 Key
- Internet connection

## 🔧 Installation

### Step 1: Clone or Download the Project

```bash
cd alto_car_manual
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Get API Keys

#### Google Gemini API Key:
1. Go to https://makersuite.google.com/app/apikey
2. Click "Create API Key"
3. Copy the API key

#### YouTube Data API Key:
1. Go to https://console.cloud.google.com/
2. Create a new project or select existing one
3. Enable "YouTube Data API v3"
4. Go to Credentials → Create Credentials → API Key
5. Copy the API key

### Step 5: Configure Environment Variables

Copy the example environment file:
```bash
cp .env.example .env
```

Edit `.env` file and add your API keys:
```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
YOUTUBE_API_KEY=your_actual_youtube_api_key_here
FLASK_SECRET_KEY=any_random_secret_key_here
```

## 🚀 Running the Application

### Start the Server

```bash
python app.py
```

The application will start on `http://localhost:5000`

### Access the Application

Open your web browser and navigate to:
```
http://localhost:5000
```

## 📁 Project Structure

```
alto_car_manual/
│
├── app.py                          # Main Flask application
├── config.py                       # Configuration management
├── requirements.txt                # Python dependencies
├── .env.example                    # Environment variables template
├── .env                           # Your API keys (create this)
│
├── data/
│   └── alto_knowledge_base.json   # Alto car information database
│
├── models/
│   ├── gemini_service.py          # Gemini AI integration
│   └── youtube_service.py         # YouTube API integration
│
├── static/
│   ├── css/
│   │   └── style.css              # Main stylesheet
│   ├── js/
│   │   ├── main.js                # Core JavaScript
│   │   └── analysis.js            # Analysis functionality
│   ├── images/                    # Static images
│   └── uploads/                   # User uploaded files
│
└── templates/
    ├── base.html                  # Base template
    ├── index.html                 # Home page
    ├── manual.html                # Manual reference page
    ├── 404.html                   # Error page
    └── 500.html                   # Error page
```

## 🎯 Usage Guide

### 1. Image Analysis

1. Click on "📷 Image Analysis" tab
2. Upload an image of car component, dashboard, warning light, etc.
3. Click "Analyze Image"
4. View AI analysis and related YouTube tutorials

### 2. Video Analysis

1. Click on "🎥 Video Analysis" tab
2. Upload a video showing the car issue
3. Click "Analyze Video"
4. View analysis results

### 3. Text Query

1. Click on "💬 Ask Question" tab
2. Type your question or describe the problem
3. Click "Get Answer & Videos"
4. View detailed answer and tutorial videos

### Example Queries:

- "My Alto AC is not cooling, what could be the problem?"
- "What does the red engine light mean?"
- "How to change engine oil in Alto 800?"
- "Alto car making strange noise while braking"

## 🔍 Features in Detail

### AI Analysis
- Identifies car components from images
- Diagnoses visible problems
- Provides troubleshooting steps
- Suggests maintenance tips

### YouTube Integration
- Automatically searches relevant repair videos
- Filters for Alto-specific content
- Shows video thumbnails and descriptions
- Direct links to watch on YouTube

### Knowledge Base
- Dashboard components guide
- Warning lights reference
- Common problems and solutions
- Maintenance schedule
- Button and control explanations

## ⚙️ Configuration Options

Edit `config.py` to customize:

- `GEMINI_MODEL`: AI model to use (default: gemini-1.5-flash)
- `YOUTUBE_MAX_RESULTS`: Number of videos to show (default: 5)
- `MAX_UPLOAD_SIZE`: Maximum file size in bytes (default: 16MB)
- `ALLOWED_EXTENSIONS`: Permitted file types

## 🐛 Troubleshooting

### API Key Issues

**Error: "Gemini API key not found"**
- Ensure `.env` file exists in project root
- Check GEMINI_API_KEY is set correctly
- No spaces around the `=` sign

**Error: "YouTube API key not found"**
- Ensure YOUTUBE_API_KEY is set in `.env`
- Verify the API is enabled in Google Cloud Console

### Upload Issues

**Error: "File too large"**
- Maximum size is 16MB
- Compress your image/video before uploading

**Error: "Invalid file type"**
- Supported images: PNG, JPG, JPEG, GIF
- Supported videos: MP4, AVI, MOV

### Server Issues

**Error: "Port 5000 already in use"**
```bash
# Kill the process using port 5000
# On Windows:
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# On Linux/Mac:
lsof -ti:5000 | xargs kill -9
```

## 📊 API Usage Limits

### Gemini API
- Free tier: 60 requests per minute
- If exceeded, wait or upgrade to paid plan

### YouTube API
- Free quota: 10,000 units per day
- Search costs 100 units per request
- ~100 searches per day with free tier

## 🔒 Security Notes

- Never commit `.env` file to version control
- Keep API keys private
- Use environment variables for sensitive data
- Don't share your API keys publicly

## 🎓 For DRDO Presentation

### Key Points to Highlight:

1. **AI Integration**: Uses latest Gemini 1.5 Flash model
2. **Multimodal**: Handles text, images, and videos
3. **Practical Application**: Solves real automotive problems
4. **Cost Effective**: Uses free tier APIs
5. **User Friendly**: Simple web interface
6. **Extensible**: Easy to add more car models

### Demo Flow:

1. Show dashboard warning light image → Get AI diagnosis
2. Ask text query about common problem → Get solution + videos
3. Show knowledge base and manual reference
4. Explain architecture and data flow

## 📝 Technical Details

### Technologies Used:
- **Backend**: Flask (Python web framework)
- **AI/ML**: Google Gemini 1.5 Flash (multimodal AI)
- **API**: YouTube Data API v3
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Image Processing**: PIL (Python Imaging Library)

### Data Flow:
1. User uploads media or text query
2. Flask backend receives request
3. Gemini AI analyzes and provides diagnosis
4. System extracts keywords from analysis
5. YouTube API searches for relevant videos
6. Results displayed to user with tutorials

## 🤝 Contributing

This is a DRDO project. For improvements:
1. Test thoroughly before deploying
2. Document all changes
3. Follow existing code style
4. Update README if needed

## 📄 License

This project is developed for DRDO educational purposes.

## 👥 Authors

**DRDO Project Team**
- Data Science & AI/ML Project
- Maruti Suzuki Alto Digital Manual System

## 📞 Support

For issues or questions:
1. Check troubleshooting section above
2. Verify API keys are configured correctly
3. Check Python and package versions
4. Review server logs for errors

## 🎉 Acknowledgments

- Google Gemini AI for powerful multimodal analysis
- YouTube for educational repair content
- Flask framework for easy web development
- Maruti Suzuki for Alto car specifications

---

**Version**: 1.0.0  
**Last Updated**: 2024  
**Status**: Production Ready ✅
