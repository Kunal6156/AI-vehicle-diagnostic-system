# Alto Car Digital Manual - Installation Guide

Complete step-by-step installation guide for the Alto Car Digital Manual project.

## Table of Contents
1. [System Requirements](#system-requirements)
2. [Quick Installation](#quick-installation)
3. [Manual Installation](#manual-installation)
4. [Getting API Keys](#getting-api-keys)
5. [Running the Application](#running-the-application)
6. [Verification](#verification)
7. [Common Issues](#common-issues)

---

## System Requirements

### Minimum Requirements:
- **Operating System**: Windows 10/11, macOS, or Linux
- **Python**: Version 3.8 or higher
- **RAM**: 4GB minimum (8GB recommended)
- **Storage**: 500MB free space
- **Internet**: Active internet connection for API calls

### Check Python Installation:
```bash
python --version
# or
python3 --version
```

If Python is not installed, download from: https://www.python.org/downloads/

---

## Quick Installation

### For Windows:

1. **Extract the project folder** to your desired location

2. **Run the setup script**:
   ```cmd
   setup.bat
   ```

3. **Configure API keys** (see [Getting API Keys](#getting-api-keys))

4. **Start the application**:
   ```cmd
   python app.py
   ```

### For Linux/Mac:

1. **Extract the project folder** to your desired location

2. **Make setup script executable**:
   ```bash
   chmod +x setup.sh
   ```

3. **Run the setup script**:
   ```bash
   ./setup.sh
   ```

4. **Configure API keys** (see [Getting API Keys](#getting-api-keys))

5. **Start the application**:
   ```bash
   python app.py
   ```

---

## Manual Installation

### Step 1: Navigate to Project Directory

```bash
cd path/to/alto_car_manual
```

### Step 2: Create Virtual Environment

**Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Create .env File

```bash
# Copy the example file
cp .env.example .env

# On Windows:
copy .env.example .env
```

### Step 5: Configure Environment Variables

Edit the `.env` file with your favorite text editor:

```env
# Google Gemini API Key
GEMINI_API_KEY=your_actual_gemini_api_key_here

# YouTube Data API Key
YOUTUBE_API_KEY=your_actual_youtube_api_key_here

# Flask Secret Key (generate random string)
FLASK_SECRET_KEY=your_random_secret_key_here
```

---

## Getting API Keys

### Google Gemini API Key

1. **Visit Google AI Studio**:
   - Go to: https://makersuite.google.com/app/apikey
   
2. **Sign in** with your Google account

3. **Create API Key**:
   - Click "Create API Key" button
   - Select project or create new one
   - Copy the generated API key

4. **Add to .env file**:
   ```env
   GEMINI_API_KEY=AIza...your_actual_key_here
   ```

### YouTube Data API Key

1. **Go to Google Cloud Console**:
   - Visit: https://console.cloud.google.com/

2. **Create/Select Project**:
   - Click "Select a project" → "New Project"
   - Enter project name: "Alto Car Manual"
   - Click "Create"

3. **Enable YouTube Data API**:
   - In the left menu, go to "APIs & Services" → "Library"
   - Search for "YouTube Data API v3"
   - Click on it and press "Enable"

4. **Create Credentials**:
   - Go to "APIs & Services" → "Credentials"
   - Click "Create Credentials" → "API Key"
   - Copy the generated API key
   - (Optional) Click "Restrict Key" to add restrictions

5. **Add to .env file**:
   ```env
   YOUTUBE_API_KEY=AIza...your_actual_key_here
   ```

### Generate Flask Secret Key

You can use Python to generate a random secret key:

```python
import secrets
print(secrets.token_hex(32))
```

Or use any random string (at least 32 characters).

---

## Running the Application

### Start the Server

1. **Activate virtual environment** (if not already activated):

   **Windows:**
   ```cmd
   venv\Scripts\activate
   ```

   **Linux/Mac:**
   ```bash
   source venv/bin/activate
   ```

2. **Run the application**:
   ```bash
   python app.py
   ```

3. **Expected Output**:
   ```
   🚗 Alto Car Digital Manual v1.0.0
   🌐 Starting server on http://localhost:5000
   📊 Debug mode: True
   
   * Running on http://127.0.0.1:5000
   ```

### Access the Application

Open your web browser and navigate to:
```
http://localhost:5000
```

---

## Verification

### 1. Check Health Endpoint

Visit: http://localhost:5000/health

You should see:
```json
{
  "status": "healthy",
  "services": {
    "gemini": true,
    "youtube": true,
    "initialized": true
  },
  "version": "1.0.0"
}
```

### 2. Test Image Analysis

1. Go to home page: http://localhost:5000
2. Click "📷 Image Analysis" tab
3. Upload a car image
4. Click "Analyze Image"
5. Should receive AI analysis and video recommendations

### 3. Test Text Query

1. Click "💬 Ask Question" tab
2. Type: "What does the check engine light mean?"
3. Click "Get Answer & Videos"
4. Should receive detailed answer and tutorials

---

## Common Issues

### Issue 1: "Python not found"

**Solution**:
- Install Python from https://www.python.org/downloads/
- Make sure to check "Add Python to PATH" during installation
- Restart terminal/command prompt after installation

### Issue 2: "pip not found"

**Solution**:
```bash
# Windows
python -m ensurepip --upgrade

# Linux/Mac
python3 -m ensurepip --upgrade
```

### Issue 3: "Permission denied" (Linux/Mac)

**Solution**:
```bash
# Make script executable
chmod +x setup.sh

# Or use sudo for installation
sudo pip install -r requirements.txt
```

### Issue 4: "Port 5000 already in use"

**Solution**:

**Windows**:
```cmd
netstat -ano | findstr :5000
taskkill /PID <PID_NUMBER> /F
```

**Linux/Mac**:
```bash
lsof -ti:5000 | xargs kill -9
```

Or change port in `app.py`:
```python
app.run(host='0.0.0.0', port=8000, debug=Config.DEBUG)
```

### Issue 5: "API key not configured"

**Symptoms**:
- Error message: "Gemini API key not found"
- Health check shows: `"gemini": false`

**Solution**:
1. Verify `.env` file exists in project root
2. Check API keys are correctly set (no spaces, no quotes)
3. Restart the server after editing `.env`

### Issue 6: "Module not found" errors

**Solution**:
```bash
# Make sure virtual environment is activated
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Issue 7: "SSL Certificate" errors

**Solution**:
```bash
# Update certifi package
pip install --upgrade certifi

# Or install with SSL fix
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
```

### Issue 8: Videos not loading

**Symptoms**:
- "No related videos found"
- YouTube API errors

**Solution**:
1. Verify YouTube API key is correct
2. Check YouTube Data API v3 is enabled in Google Cloud Console
3. Verify you haven't exceeded API quota (10,000 units/day)
4. Check internet connection

---

## Updating the Application

### Pull Latest Changes:
```bash
git pull origin main
```

### Update Dependencies:
```bash
pip install --upgrade -r requirements.txt
```

### Restart Server:
```bash
# Stop server: Ctrl+C
python app.py
```

---

## Uninstallation

### Remove Virtual Environment:
```bash
# Windows
rmdir /s venv

# Linux/Mac
rm -rf venv
```

### Remove Project:
Simply delete the project folder.

**Note**: Your API keys in `.env` will also be deleted.

---

## Additional Help

### Check Logs

Server logs appear in the terminal where you ran `python app.py`. Look for:
- Error messages
- API call failures
- File upload issues

### Debug Mode

Edit `config.py` to enable detailed debugging:
```python
DEBUG = True
```

### Contact

For project-specific issues:
- Check README.md
- Review code comments
- Contact project maintainers

---

## Next Steps

After successful installation:

1. ✅ Read the [README.md](README.md) for usage guide
2. ✅ Explore the manual reference at: http://localhost:5000/manual
3. ✅ Try analyzing different car images
4. ✅ Prepare demo for DRDO presentation

---

**Installation Complete!** 🎉

You're now ready to use the Alto Car Digital Manual system.
