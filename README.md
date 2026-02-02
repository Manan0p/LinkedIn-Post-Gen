# LinkedIn Post Gen

**LinkedIn Post Gen** is a lightweight AI-powered app that helps you **analyze existing LinkedIn posts**, **extract metadata**, and **generate new posts** in a similar writing style using Groq-hosted LLMs.

**🌐 Live Demo:** https://manan0p-linkedin-post-gen.hf.space/

## 🖼️ Product Tour

Here’s a quick look at the flow — from preprocessing posts to generating new content.

### Post Generator

Select a topic, length, and language to generate a LinkedIn post in the same writing style as prior examples.

![LinkedIn Post Generator UI](public/Post%20Generator.png)

---

## 🎯 What This Project Does

LinkedIn Post Gen follows a simple flow: **collect posts → enrich metadata → unify tags → generate new posts with few-shot guidance**.

It helps you:
- Extract line counts, language, and tags from raw posts
- Normalize tags into a clean, unified taxonomy
- Generate new posts by topic, length, and language
- Reuse topically similar examples for stylistic consistency

---

## ✨ Core Features

- **🧠 Metadata Extraction** - LLM-based parsing of post length, language, and tags
- **🏷️ Tag Unification** - Consolidates similar tags into clean canonical forms
- **🧩 Few-Shot Prompting** - Reuses matching examples to guide style
- **🗣️ Hinglish Support** - Generates mixed Hindi-English content in Latin script
- **🖥️ Streamlit UI** - Simple interactive interface for generation

---

## 👥 Who Is This For?

Great for learning/building:
- **LLM pipelines**: prompt templates + JSON parsing
- **Few-shot generation**: style and topic alignment
- **Streamlit apps**: quick UI for AI demos
- **Tag normalization**: taxonomy cleanup with LLMs

---

## 🛠 Tech Stack

### Frontend
- **Streamlit** - UI for interactive generation

### Backend & AI
- **Python 3.11+**
- **LangChain Core** - Prompting + JSON parsing
- **LangChain Groq** - Groq-hosted LLMs
- **Pandas** - Data normalization and filtering
- **python-dotenv** - Environment variables

### Deployment
- **Docker** - Containerized runtime

---

## 📁 Project Structure

```text
LinkedIn Post Gen/
├── data/
│   ├── raw_posts.json            # Raw input posts
│   └── processed_posts.json      # Enriched posts with metadata
├── few_shot.py                   # Loads and filters example posts
├── llm_helper.py                 # Groq LLM client
├── main.py                       # Streamlit app entry
├── post_generator.py             # Prompting + generation
├── preprocess.py                 # Metadata extraction + tag unification
├── requirements.txt              # Python dependencies
├── Dockerfile                    # Container config
└── README.md
```

---

## 🚀 Quick Start

### 1) Prerequisites

- Python 3.11+
- A Groq API key

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

### 3) Environment variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

### 4) Preprocess posts (one-time or as needed)

```bash
python preprocess.py
```

### 5) Run the Streamlit app

```bash
streamlit run main.py
```

Open http://localhost:8501

---

## 📊 How It Works (End-to-End)

1. **Raw posts are loaded** from data/raw_posts.json
2. **Metadata extraction** detects line count, language, and tags
3. **Tag unification** merges similar tags into a clean set
4. **Processed posts are saved** to data/processed_posts.json
5. **Streamlit UI** lets users select topic, length, and language
6. **Few-shot examples** are injected into the prompt
7. **LLM generates** a new LinkedIn post

---

## 🐛 Troubleshooting

| Issue | Likely Cause | Fix |
|------|--------------|-----|
| LLM errors or empty output | Missing/invalid `GROQ_API_KEY` | Add key to `.env` and restart |
| No topics in dropdown | `processed_posts.json` missing or empty | Run `python preprocess.py` |
| Docker app won’t start | Dockerfile expects a different entry | Update Dockerfile to use `main.py` |

---

## 🚢 Building for Production (Docker)

```bash
docker build -t linkedin-post-gen .
docker run -p 8501:8501 linkedin-post-gen
```

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

**Copyright © 2026 Manan**

---

## 👨‍💻 Author

Built by Manan.

---

**Ready to generate posts faster? Run the app and start creating.**
