# Brand Tone Checker

**Capstone Project – Marketing AI | FastAPI + Ollama + ChromaDB**

An AI-powered system that helps marketing teams ensure their content matches their brand voice through vector embeddings, semantic similarity, and LLM-based analysis.

---

## 🚀 Overview

Brand Tone Checker enables marketing teams to maintain consistent brand voice across all content. Users define their brand tone through keywords and sample texts, which are converted to vector embeddings and stored in ChromaDB. New content is analyzed using cosine similarity and reviewed by an LLM to determine tone alignment.

**Key Capabilities:**
- Define brand tone using keywords (e.g., friendly, premium, playful)
- Store sample brand texts as reference material
- Analyze new content against established brand voice
- Receive AI-powered feedback and rewrite suggestions
- Persistent vector storage for multiple brands

This approach mirrors enterprise tools like Grammarly, Jasper, and Copy.ai for tone alignment.

---

## 🧠 Core Concept

The system combines multiple technologies to deliver intelligent tone analysis:

| Technology | Purpose |
|------------|---------|
| **LLM (Ollama)** | Language understanding & content rewriting |
| **Vector Embeddings** | Numerical representation of tone and meaning |
| **Cosine Similarity** | Measures alignment between content and brand voice |
| **ChromaDB** | Persistent vector database for brand profiles |
| **FastAPI** | High-performance backend API |
| **Streamlit** | Interactive user interface |

---

## 🔁 System Flow

1. **Brand Definition**: User provides tone keywords and sample texts
2. **Embedding Generation**: Combined text converted to vector embeddings
3. **Storage**: Brand profile stored in ChromaDB
4. **Content Submission**: User submits new marketing content for analysis
5. **Similarity Analysis**: Content embedding compared with brand embedding
6. **Scoring**: Cosine similarity score calculated
7. **LLM Evaluation**: AI determines verdict:
   - **PASS**: Explains why tone matches brand voice
   - **FAIL**: Identifies missing elements, suggests improvements, and rewrites content

---

## 🏗 Architecture

```
┌─────────────────┐
│  Streamlit UI   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  FastAPI        │
│  (routes.py)    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ tone_service.py │
└────────┬────────┘
         │
         ├──► embeddings.py  → Ollama embeddings
         ├──► vector_db.py   → ChromaDB operations
         └──► llm.py         → Ollama LLM analysis
```

---

## 🧩 Key Features

- ✅ **Multi-Brand Support**: Store and manage multiple brand profiles
- ✅ **Persistent Storage**: ChromaDB vector database
- ✅ **Semantic Similarity**: Cosine similarity scoring
- ✅ **AI Explanations**: Detailed tone analysis and reasoning
- ✅ **Content Rewriting**: AI-powered suggestions for tone alignment
- ✅ **API Testing**: Comprehensive PyTest suite
- ✅ **Interactive Dashboard**: User-friendly Streamlit interface

---

## 📂 Project Structure

```
BrandToneChecker/
├── app/
│   ├── main.py           # FastAPI application entry point
│   ├── routes.py         # API endpoints
│   ├── schemas.py        # Pydantic models
│   ├── embeddings.py     # Embedding generation
│   ├── llm.py            # LLM interaction
│   ├── vector_db.py      # ChromaDB operations
│   ├── tone_service.py   # Core business logic
│   └── config.py         # Configuration settings
├── chroma_db/            # Vector storage directory
├── streamlit_app.py      # Streamlit frontend
├── tests/
│   ├── test_api.py       # API endpoint tests
│   ├── test_brands.py    # Brand management tests
│   └── test_tone_check.py # Tone analysis tests
├── requirements.txt      # Python dependencies
└── README.md            # Project documentation
```

---

## ⚙️ Tech Stack

- **Python 3.10+**: Core programming language
- **FastAPI**: Modern web framework for building APIs
- **Streamlit**: Interactive web application framework
- **Ollama**: Local LLM inference
- **ChromaDB**: Vector database for embeddings
- **NumPy**: Numerical computing
- **Requests**: HTTP library
- **PyTest**: Testing framework

---

## 🔌 Required Ollama Models

Install the following models before running the application:

```bash
ollama pull nomic-embed-text  # For generating embeddings
ollama pull llama3.2          # For LLM analysis and rewriting
```

---

## ▶️ Getting Started

### Prerequisites

1. Install Python 3.10 or higher
2. Install Ollama from [ollama.ai](https://ollama.ai)
3. Pull required Ollama models (see above)

### Installation

1. Clone the repository:
```bash
git clone 
cd BrandToneChecker
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

**1️⃣ Start Ollama Service**
```bash
ollama serve
```

**2️⃣ Start FastAPI Backend**
```bash
uvicorn app.main:app --reload
```
API will be available at `http://localhost:8000`

**3️⃣ Start Streamlit Frontend**
```bash
streamlit run streamlit_app.py
```
UI will open at `http://localhost:8501`

---

## 🧪 Testing

Run the complete test suite:

```bash
pytest -v
```

The tests verify:
- Brand creation and storage
- Vector database operations
- Tone matching accuracy
- API endpoint functionality
- End-to-end workflows

---

## 🧠 How It Works

### Cosine Similarity Explained

Each brand profile is converted into a high-dimensional vector through embeddings:

```
Brand tone + sample texts → embedding vector (e.g., 768 dimensions)
```

New content is similarly converted:

```
New marketing text → embedding vector
```

Similarity is computed using cosine distance:

```
similarity_score = 1 - cosine_distance(brand_vector, content_vector)
```

**Score interpretation:**
- **0.8 - 1.0**: Excellent match
- **0.6 - 0.8**: Good match, minor adjustments
- **< 0.6**: Poor match, rewrite recommended

### LLM's Role

While cosine similarity provides quantitative analysis, the LLM adds qualitative insight:

1. **Explains** why content matches or fails to match
2. **Identifies** specific missing tone elements
3. **Suggests** appropriate tone words and phrases
4. **Rewrites** content to better align with brand voice

This combination of mathematical precision and human-like understanding creates a powerful content analysis system.

---

## 🏆 Real-World Applications

This system simulates enterprise-grade tools used for:

- **Brand QA & Compliance**: Ensure all content matches brand guidelines
- **AI Copywriting Assistants**: Generate on-brand content at scale
- **Marketing Governance**: Automated content approval workflows
- **Agency Management**: Maintain consistency across multiple client brands

**Suitable for:**
- Marketing agencies managing multiple brands
- SaaS platforms offering content tools
- Enterprise marketing teams
- Content approval and governance workflows

---

## 📌 Example Output

```json
{
  "brand_name": "TechStartup",
  "score": 0.69,
  "tone_keywords": "friendly, playful",
  "llm_result": {
    "verdict": "FAIL",
    "explanation": "Content lacks warmth and excitement expected from your brand voice",
    "missing_elements": ["warmth", "excitement", "approachability"],
    "suggestions": ["happy", "welcome", "delightful", "excited to"],
    "rewrite": "We're excited to welcome you! Our team is delighted to provide friendly service that makes your experience truly special."
  }
}
```

---

## 🛠 API Endpoints

- `POST /brands/` - Create new brand profile
- `GET /brands/{brand_name}` - Retrieve brand details
- `POST /check-tone/` - Analyze content against brand voice
- `GET /brands/` - List all stored brands

Full API documentation available at `http://localhost:8000/docs` when running.

---

## 🔮 Future Enhancements

- Multi-language support
- Batch content analysis
- Historical tone drift tracking
- Integration with content management systems
- Custom LLM fine-tuning for specific industries
- A/B testing for tone variations


**Technologies**: FastAPI, Ollama, ChromaDB, Streamlit, Python

