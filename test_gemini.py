"""
Test script to check which Gemini models are available with your API key
"""
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('GEMINI_API_KEY')

if not api_key:
    print("ERROR: GEMINI_API_KEY not found in .env file")
    exit(1)

print(f"Testing with API key: {api_key[:10]}...")

# Configure API
genai.configure(api_key=api_key)

# Try to list available models
print("\nAttempting to list available models...\n")
try:
    models = genai.list_models()
    print("Available models:")
    for model in models:
        if 'generateContent' in model.supported_generation_methods:
            print(f"  - {model.name}")
except Exception as e:
    print(f"Error listing models: {e}")

# Try different model names
model_names_to_try = [
    'gemini-pro',
    'gemini-1.5-pro',
    'gemini-1.5-flash',
    'models/gemini-pro',
    'models/gemini-1.5-pro',
    'models/gemini-1.5-flash',
]

print("\n" + "="*50)
print("Testing model names:")
print("="*50)

for model_name in model_names_to_try:
    try:
        print(f"\nTrying: {model_name}")
        model = genai.GenerativeModel(model_name)
        response = model.generate_content("Say 'test successful'")
        print(f"  ✅ SUCCESS: {model_name} works!")
        print(f"  Response: {response.text[:50]}...")
        print(f"\n  >>> USE THIS MODEL NAME: {model_name}")
        break
    except Exception as e:
        print(f"  ❌ FAILED: {str(e)[:100]}")
        continue
else:
    print("\n⚠️ None of the standard model names worked.")
    print("Please check your Gemini API key at: https://makersuite.google.com/app/apikey")
