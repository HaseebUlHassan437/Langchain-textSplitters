
# LangChain Text Splitters

This repository demonstrates various **text splitting techniques** using LangChain. Text splitters help break large documents or strings into manageable chunks, which is crucial for tasks like embedding, retrieval, and LLM interaction.

---

## 📁 Repository Structure

| File | Description |
|------|-------------|
| **python_code_based_splitting.py** | Splits Python source code using `RecursiveCharacterTextSplitter` with `Language.PYTHON`. |
| **markdown_splitter.py** | Splits Markdown-formatted text based on structural elements using `Language.MARKDOWN`. |
| **length_based.py** | Splits a PDF document (`The Ultimate NLP Guide`) using a simple character-based chunker. |
| **text_structured_based.py** | Splits plain text using `RecursiveCharacterTextSplitter` with a defined chunk size. |
| **semantic_meaning_based.py** | Uses `SemanticChunker` with **Google Gemini Embeddings** to split text based on semantic meaning. |

---

## 🚀 Quick Start

1. Clone this repo  
   ```bash
   git clone https://github.com/HaseebUlHassan437/Langchain-textSplitters.git
   cd Langchain-textSplitters
   ```

2. Create & activate a virtual environment  
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
   ```

3. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```

4. Add your API key to a `.env` file (for Gemini embedding support)  
   ```
   GOOGLE_API_KEY=your_gemini_api_key_here
   ```

5. Run any example script  
   ```bash
   python semantic_meaning_based.py
   python length_based.py
   ```

---

## 🔧 Tech Stack

- **LangChain** — Modular LLM framework  
- **Text Splitters** — `RecursiveCharacterTextSplitter`, `CharacterTextSplitter`, `SemanticChunker`  
- **Google Generative AI (Gemini)** — Semantic embeddings  
- **dotenv** — API key management  

---

## 📫 Contact

Questions or suggestions?  
Reach out to **haseebulhassan1172003@gmail.com**
```

