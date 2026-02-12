# Alto Car Digital Manual - Quick Start Guide

Get up and running in 5 minutes! ⚡

## Prerequisites Check

✅ Python 3.8+ installed  
✅ Internet connection  
✅ Google Gemini API Key  
✅ YouTube Data API Key  

Don't have API keys? See [Getting API Keys](#getting-api-keys) below.

---

## Installation (Choose One)

### Option A: Automated Setup (Recommended)

**Windows**:
```cmd
setup.bat
```

**Linux/Mac**:
```bash
chmod +x setup.sh
./setup.sh
```

### Option B: Manual Setup

```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate it
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Copy environment file
cp .env.example .env
```

---

## Configuration

### 1. Get API Keys

#### Gemini API Key (2 minutes):
1. Visit: https://makersuite.google.com/app/apikey
2. Click "Create API Key"
3. Copy the key

#### YouTube API Key (3 minutes):
1. Visit: https://console.cloud.google.com/
2. Create new project
3. Enable "YouTube Data API v3"
4. Create API Key under Credentials
5. Copy the key

### 2. Update .env File

Edit `.env` and paste your keys:

```env
GEMINI_API_KEY=AIza...your_key_here
YOUTUBE_API_KEY=AIza...your_key_here
FLASK_SECRET_KEY=any_random_string_here
```

---

## Running the Application

```bash
# Make sure virtual environment is activated
python app.py
```

Open browser: **http://localhost:5000**

---

## First Test

### Test 1: Health Check
Visit: http://localhost:5000/health

Should show:
```json
{
  "status": "healthy",
  "services": {
    "gemini": true,
    "youtube": true
  }
}
```

### Test 2: Ask a Question
1. Go to home page
2. Click "💬 Ask Question"
3. Type: "What does the check engine light mean?"
4. Click "Get Answer & Videos"
5. ✅ You should see AI analysis + YouTube videos

---

## Common Quick Fixes

### "API key not found"
- Check `.env` file exists in project root
- No spaces around `=` in .env
- Restart server after editing .env

### "Port 5000 in use"
- Change port in `app.py`: `app.run(port=8000)`
- Or kill process using port 5000

### "Module not found"
- Activate virtual environment
- Run: `pip install -r requirements.txt`

---

## What to Do Next

📖 Read full [README.md](README.md) for detailed features  
📘 Check [INSTALLATION_GUIDE.md](INSTALLATION_GUIDE.md) for troubleshooting  
📊 Review [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md) for architecture  

---

## Quick Reference

### Project Structure
```
alto_car_manual/
├── app.py              # Main application
├── config.py           # Configuration
├── requirements.txt    # Dependencies
├── .env               # Your API keys (create this)
├── models/            # AI services
├── templates/         # HTML pages
├── static/            # CSS, JS, images
└── data/              # Knowledge base
```

### Important Files
- `app.py` - Start server here
- `.env` - API keys configuration
- `templates/index.html` - Main UI
- `data/alto_knowledge_base.json` - Car information

### Key Endpoints
- `/` - Home page
- `/manual` - Reference manual
- `/analyze` - API endpoint
- `/health` - Status check

---

## Need Help?

1. Check [INSTALLATION_GUIDE.md](INSTALLATION_GUIDE.md) for detailed steps
2. Review error messages in terminal
3. Verify API keys are correct
4. Ensure virtual environment is activated

---

## Success! 🎉

You're ready to use the Alto Car Digital Manual!

Try uploading a car image or asking a question.

**For DRDO Presentation**:
- Review [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md)
- Prepare demo scenarios
- Test with sample images

---

**Time to First Analysis**: < 5 minutes ⚡
