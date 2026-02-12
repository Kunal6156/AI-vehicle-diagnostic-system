# 🚀 RENDER DEPLOYMENT GUIDE - Step by Step

## Complete Guide to Deploy Alto Car Manual to Render (100% FREE)

---

## ✅ Prerequisites

Before starting, make sure you have:
- [ ] Your project files (downloaded from earlier)
- [ ] Gemini API Key
- [ ] YouTube API Key
- [ ] GitHub account (free)
- [ ] Render account (free - we'll create this)

---

## 📝 STEP 1: Prepare Your Project for Deployment

### 1.1 Download the Updated Project

Download the **alto_car_manual.zip** file again (I've updated it with deployment files).

**New files added:**
- `build.sh` - Build script for Render
- `render.yaml` - Render configuration
- Updated `requirements.txt` - Added gunicorn
- Updated `app.py` - Port configuration for Render

### 1.2 Extract the ZIP file

Extract to a folder like: `C:\Users\kunal\alto_car_manual\`

---

## 📦 STEP 2: Push to GitHub

### 2.1 Create a GitHub Account (if you don't have one)

1. Go to: https://github.com
2. Click "Sign up"
3. Create your account (free)

### 2.2 Create a New Repository

1. Once logged in, click the **"+"** icon (top right)
2. Select **"New repository"**
3. Fill in:
   - **Repository name**: `alto-car-manual`
   - **Description**: "AI-Powered Alto Car Digital Manual"
   - **Visibility**: Select **Public** or **Private** (both work)
   - **DO NOT** check "Add a README file"
4. Click **"Create repository"**

### 2.3 Upload Your Code to GitHub

**Option A: Using GitHub Desktop (Easier for beginners)**

1. Download GitHub Desktop: https://desktop.github.com/
2. Install and sign in
3. Click "Add" → "Add existing repository"
4. Browse to your `alto_car_manual` folder
5. Click "Publish repository"

**Option B: Using Git Command Line**

Open terminal in your project folder and run:

```bash
# Initialize git
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit - Alto Car Manual"

# Connect to GitHub (replace YOUR-USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR-USERNAME/alto-car-manual.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**IMPORTANT:** When pushing, it will ask for credentials. Use your GitHub username and **Personal Access Token** (not password).

To create a token:
1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token → Select "repo" scope → Copy the token

---

## 🌐 STEP 3: Create Render Account

1. Go to: https://render.com
2. Click **"Get Started for Free"**
3. **Sign up with GitHub** (recommended - makes deployment easier)
4. Authorize Render to access your GitHub account

---

## 🚀 STEP 4: Deploy to Render

### 4.1 Create New Web Service

1. Once logged into Render, click **"New +"** (top right)
2. Select **"Web Service"**

### 4.2 Connect Your Repository

1. You'll see a list of your GitHub repositories
2. Find **"alto-car-manual"** and click **"Connect"**

**If you don't see your repository:**
- Click "Configure account" 
- Give Render access to your repositories
- Return and refresh

### 4.3 Configure the Web Service

Fill in these settings:

**Name:** `alto-car-manual` (or any name you prefer)

**Region:** Choose closest to you (e.g., Singapore for India)

**Branch:** `main`

**Root Directory:** Leave blank

**Runtime:** `Python 3`

**Build Command:** `./build.sh`

**Start Command:** `gunicorn app:app`

**Instance Type:** Select **"Free"** ✅

### 4.4 Add Environment Variables

Scroll down to **"Environment Variables"** section.

Click **"Add Environment Variable"** and add these **ONE BY ONE**:

| Key | Value |
|-----|-------|
| `GEMINI_API_KEY` | Your actual Gemini API key |
| `YOUTUBE_API_KEY` | Your actual YouTube API key |
| `FLASK_SECRET_KEY` | Any random string (e.g., `my-secret-key-12345`) |
| `FLASK_ENV` | `production` |
| `FLASK_DEBUG` | `False` |
| `PYTHON_VERSION` | `3.11.4` |

**Example for GEMINI_API_KEY:**
- Key: `GEMINI_API_KEY`
- Value: `AIzaSyXXXXXXXXXXXXXXXXXXX` (your actual key)

### 4.5 Deploy!

1. Click **"Create Web Service"** at the bottom
2. Render will start deploying your app
3. You'll see a build log - **wait 3-5 minutes**

---

## ✅ STEP 5: Verify Deployment

### 5.1 Check Build Status

Watch the logs. You should see:
```
==> Installing dependencies
==> Starting service
```

### 5.2 Get Your Live URL

Once deployed successfully:
- Render will show: **"Your service is live 🎉"**
- You'll get a URL like: `https://alto-car-manual.onrender.com`

### 5.3 Test Your Application

1. Click on your live URL
2. You should see your Alto Car Manual application!
3. Try uploading an image or asking a question

---

## 🐛 TROUBLESHOOTING

### Issue 1: Build Failed

**Error:** `Permission denied: ./build.sh`

**Solution:**
Add this to your GitHub repo:
```bash
chmod +x build.sh
git add build.sh
git commit -m "Make build.sh executable"
git push
```

Then in Render:
- Go to your service
- Click "Manual Deploy" → "Deploy latest commit"

### Issue 2: Service Starts but Shows Error

**Check the Logs:**
1. In Render dashboard → Your service
2. Click "Logs" tab
3. Look for errors

**Common errors:**
- `GEMINI_API_KEY not found` → Check environment variables
- `Module not found` → Check requirements.txt has all dependencies

### Issue 3: "This site can't be reached"

**Wait 2-3 minutes** - Render free tier can take a moment to spin up after inactivity.

### Issue 4: API Keys Not Working

1. Go to Render dashboard → Your service
2. Click "Environment" tab
3. Verify all keys are set correctly
4. Click "Save Changes"
5. Service will auto-redeploy

---

## 🎉 SUCCESS! Your App is Live

Your application is now:
- ✅ Live on the internet
- ✅ Accessible from anywhere
- ✅ FREE hosting on Render
- ✅ Auto-deploys when you push to GitHub

**Your URL:** `https://your-service-name.onrender.com`

Share this URL for your DRDO presentation! 🚀

---

## 📱 Optional: Custom Domain

Want a custom domain like `alto-manual.com`?

1. Buy a domain from Namecheap/GoDaddy (~$10/year)
2. In Render → Your service → "Settings"
3. Add custom domain
4. Update DNS records (Render will guide you)

---

## 🔄 How to Update Your App

When you make changes:

1. **Update code locally**
2. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Updated feature X"
   git push
   ```
3. **Render auto-deploys!** (within 2-3 minutes)

---

## 💰 Cost Breakdown

**FREE TIER includes:**
- ✅ 750 hours/month (enough for your app)
- ✅ Auto-sleep after 15 min inactivity
- ✅ 100GB bandwidth/month
- ✅ Free SSL certificate

**Limitations:**
- App sleeps after 15 min of no activity
- First request after sleep takes 30-60 seconds to wake up
- Perfect for student projects and demos!

**Upgrade ($7/month):**
- No sleeping
- Faster performance
- More resources

---

## 📞 Need Help?

1. **Check Render Logs:** Dashboard → Logs
2. **Render Docs:** https://render.com/docs
3. **GitHub Issues:** Check if files committed correctly

---

## ✨ Final Checklist

Before DRDO presentation:
- [ ] App deployed and accessible
- [ ] Test image upload
- [ ] Test text query
- [ ] Test video search results
- [ ] Take screenshots as backup
- [ ] Note down your live URL

**Good luck with your presentation!** 🎓🚀

---

## 🎯 Quick Reference Commands

### Git Commands:
```bash
# Check status
git status

# Add all changes
git add .

# Commit changes
git commit -m "Your message"

# Push to GitHub
git push

# Pull latest
git pull
```

### Render Manual Deploy:
1. Render Dashboard → Your Service
2. "Manual Deploy" → "Deploy latest commit"

---

**Deployment Date:** February 2026  
**Status:** Ready for Production ✅  
**Platform:** Render (Free Tier)
