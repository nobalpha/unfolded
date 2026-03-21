# 📖 Unfolded - Biography Generator

A beautiful web application that helps capture life stories through voice-enabled conversations and generates literary biographies.

![Vue.js](https://img.shields.io/badge/Vue.js-3.x-4FC08D?logo=vue.js)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-009688?logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python)

## ✨ Features

- 🎙️ **Voice Input** - Speak your stories naturally
- 💬 **Real-time Chat** - WebSocket-powered instant responses
- 🤖 **AI Interviewer** - Empathetic questions powered by Gemini
- 📚 **Literary Output** - Transforms Q&A into flowing narrative prose
- 📄 **Export Options** - Download as Word (.docx) or Text (.txt)
- 🎨 **Elegant Design** - Modern, chic interface

## 🚀 Quick Start

### Local Development

```bash
# Clone and navigate
cd unfolded

# Install dependencies
pip install -r requirements.txt

# Start the server
cd backend
uvicorn main:app --reload --port 8000
```

Then open http://localhost:8000 in your browser.

### Windows Users
Simply double-click `start.bat`

---

## 🌐 Deployment Options

### Option 1: ngrok (Fastest for Testing)

1. Install ngrok: https://ngrok.com/download
2. Run `deploy_ngrok.bat` or:
   ```bash
   ngrok http 8000
   ```
3. Share the HTTPS URL with your cofounder!

### Option 2: Railway (Recommended)

1. Push to GitHub
2. Go to [railway.app](https://railway.app)
3. Click "New Project" → "Deploy from GitHub"
4. Select your repo
5. Railway auto-detects the config and deploys!

Your app will be live at `https://your-app.up.railway.app`

### Option 3: Render

1. Push to GitHub
2. Go to [render.com](https://render.com)
3. New → Web Service → Connect your repo
4. Render uses `render.yaml` automatically
5. Deploy!

### Option 4: Docker

```bash
# Build
docker build -t unfolded .

# Run
docker run -p 8000:8000 unfolded
```

### Option 5: Vercel + Railway (Production)

For better performance, deploy frontend and backend separately:

**Frontend (Vercel):**
1. Push `frontend/` to a separate repo
2. Deploy on Vercel
3. Update `API_URL` in index.html to your Railway backend URL

**Backend (Railway):**
1. Deploy backend on Railway
2. Enable CORS for your Vercel domain

---

## 📁 Project Structure

```
unfolded/
├── backend/
│   ├── main.py              # FastAPI server + WebSocket
│   └── requirements.txt
├── frontend/
│   └── index.html           # Vue.js SPA
├── data/                    # Generated biographies
├── Dockerfile               # Docker deployment
├── railway.toml             # Railway config
├── render.yaml              # Render config
├── start.bat                # Windows launcher
└── deploy_ngrok.bat         # ngrok deployment
```

## 🔧 Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | Server port | 8000 |
| `GEMINI_API_KEY` | Google Gemini API key | (set in code) |

## 📝 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Serve frontend |
| `/api/session/start` | POST | Start new interview |
| `/api/chat` | POST | Send message |
| `/api/biography/generate/{id}` | POST | Generate biography |
| `/api/biography/download/{id}/{format}` | GET | Download file |
| `/ws/{session_id}` | WebSocket | Real-time chat |

## 🤝 Contributing

Pull requests welcome! For major changes, please open an issue first.

## 📄 License

MIT
