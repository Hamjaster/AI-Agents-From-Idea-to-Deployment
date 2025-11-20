# 🚀 Quick Start Checklist

Follow these steps to get your multi-agent system running:

## ✅ Step-by-Step Setup

### 1️⃣ Environment Setup
```powershell
# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Create .env file
echo "OPENROUTER_API_KEY=your_key_here" > .env
```
**Get API key:** https://openrouter.ai/ (free tier available)

### 2️⃣ Build RAG Database
```powershell
python rag\build_vector_db.py
```
**Expected:** `Vector store saved to .../rag/vectorstore`

### 3️⃣ Test the Pipeline
```powershell
python main.py --topic "Introduction to AI Agents"
```

### 4️⃣ Launch Frontend (Optional)
```powershell
python -m streamlit run frontend\app.py
```

---

## 📁 What's Already Done ✅

- ✅ All 4 agents have complete prompts
- ✅ All 4 tasks are fully defined
- ✅ Tools are ready (RAG, Web Search, Calculator)
- ✅ Crew orchestration is configured

## 🎯 What You Need to Do

1. **Get OpenRouter API Key** → Add to `.env`
2. **Build Vector DB** → Run `python rag\build_vector_db.py`
3. **Test It** → Run `python main.py --topic "Your Topic"`

---

## 🔍 Understanding the Flow

```
User Input
    ↓
Planner Agent → Creates roadmap
    ↓
Researcher Agent → Gathers info (uses tools)
    ↓
Writer Agent → Creates content
    ↓
Reviewer Agent → Quality checks
    ↓
Final Output
```

---

## 📚 Next Steps

- Read `BUILD_GUIDE.md` for detailed explanations
- Customize agent prompts in `agents/` folder
- Add your own documents to `rag/documents/`
- Create new tools in `tools/` folder
- Add more agents following the pattern

---

## 🆘 Troubleshooting

**"OPENROUTER_API_KEY is missing"**
→ Check `.env` file exists and has correct key

**"Vector store not found"**
→ Run `python rag\build_vector_db.py`

**Import errors**
→ Activate venv and reinstall: `pip install -r requirements.txt`

---

**You're ready to go! 🎉**

