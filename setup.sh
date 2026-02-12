#!/bin/bash

# Alto Car Digital Manual - Quick Setup Script

echo "================================================"
echo "Alto Car Digital Manual - Setup Script"
echo "================================================"
echo ""

# Check Python version
echo "Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Python version: $python_version"
echo ""

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv
echo "✓ Virtual environment created"
echo ""

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo "✓ Virtual environment activated"
echo ""

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt
echo "✓ Dependencies installed"
echo ""

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "Creating .env file..."
    cp .env.example .env
    echo "✓ .env file created"
    echo ""
    echo "⚠️  IMPORTANT: Edit .env file and add your API keys!"
    echo ""
else
    echo "✓ .env file already exists"
    echo ""
fi

# Create uploads directory
echo "Creating uploads directory..."
mkdir -p static/uploads
echo "✓ Uploads directory created"
echo ""

echo "================================================"
echo "Setup Complete!"
echo "================================================"
echo ""
echo "Next steps:"
echo "1. Edit .env file and add your API keys:"
echo "   - GEMINI_API_KEY"
echo "   - YOUTUBE_API_KEY"
echo ""
echo "2. Run the application:"
echo "   python app.py"
echo ""
echo "3. Open browser and go to:"
echo "   http://localhost:5000"
echo ""
echo "================================================"
