"""
🚀 UNFOLDED - Biography Generator
Quick start script for the web application
"""

import subprocess
import sys
import os
import webbrowser
import time
from pathlib import Path

def main():
    print("\n" + "="*60)
    print("  📖 UNFOLDED - Biography Generator")
    print("  Starting Web Application...")
    print("="*60 + "\n")
    
    # Get the project root
    root = Path(__file__).parent
    backend_dir = root / "backend"
    frontend_dir = root / "frontend"
    
    # Check if dependencies are installed
    print("📦 Checking dependencies...")
    try:
        import fastapi
        import uvicorn
        print("   ✅ FastAPI installed")
    except ImportError:
        print("   ⚠️  Installing FastAPI...")
        subprocess.run([sys.executable, "-m", "pip", "install", "fastapi", "uvicorn[standard]", "websockets"])
    
    try:
        import google.genai
        print("   ✅ Google Genai installed")
    except ImportError:
        print("   ⚠️  Installing Google Genai...")
        subprocess.run([sys.executable, "-m", "pip", "install", "google-genai"])
    
    try:
        import docx
        print("   ✅ python-docx installed")
    except ImportError:
        print("   ⚠️  Installing python-docx...")
        subprocess.run([sys.executable, "-m", "pip", "install", "python-docx"])
    
    # Create data directory
    data_dir = root / "data"
    data_dir.mkdir(exist_ok=True)
    
    print("\n🌐 Starting server...")
    print("   Backend: http://localhost:8000")
    print("   Frontend: Open frontend/index.html in your browser")
    print("\n   Press Ctrl+C to stop the server\n")
    
    # Open browser after a short delay
    def open_browser():
        time.sleep(2)
        frontend_path = frontend_dir / "index.html"
        webbrowser.open(f"file://{frontend_path}")
    
    import threading
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.start()
    
    # Start the backend server
    os.chdir(backend_dir)
    subprocess.run([sys.executable, "-m", "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"])

if __name__ == "__main__":
    main()
