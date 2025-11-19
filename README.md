# Agentic AI Workshop: Multi-Agent Systems From Idea to Deployment

A hands-on workshop template that demonstrates how to orchestrate CrewAI agents for planning, research, writing, and review workflows. The stack combines CrewAI with LangChain tools, a FAISS-backed Retrieval-Augmented Generation (RAG) pipeline, and a Streamlit frontend. All large language model calls are routed through the OpenRouter API using the model `meta-llama/llama-3.3-70b-instruct:free`.

## Workshop Goals

- Teach students how to structure multi-agent systems with CrewAI.
- Illustrate how RAG augments agents with curated context via FAISS.
- Showcase live web search and deterministic calculation tooling.
- Provide an end-to-end example from initial idea to reviewed deliverable.
- Offer a Streamlit interface that makes the pipeline demo-ready for classes and talks.

## Project Structure

```
agentic-workshop/
├── .env.example
├── requirements.txt
├── README.md
├── main.py
├── crew.py
├── tasks.py
├── config/
│   └── settings.py
├── agents/
│   ├── __init__.py
│   ├── planner.py
│   ├── researcher.py
│   ├── writer.py
│   └── reviewer.py
├── tools/
│   ├── __init__.py
│   ├── rag_tool.py
│   ├── web_search.py
│   └── calculator.py
├── rag/
│   ├── build_vector_db.py
│   ├── documents/
│   │   └── sample_docs.txt
│   └── vectorstore/
└── frontend/
    ├── app.py
    └── requirements.txt
```

## Prerequisites

- Python 3.10+
- An OpenRouter account and API key (free tier available)
- (Optional) A virtual environment manager such as `venv`, `conda`, or `pipenv`

## Installation

1. **Clone the repository**
   ```powershell
   git clone https://github.com/your-org/agentic-workshop.git
   cd agentic-workshop
   ```

2. **Create and activate a virtual environment**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. **Install backend dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```powershell
   copy .env.example .env
   # Edit .env and paste your actual OpenRouter API key
   ```

5. **Build the FAISS vector store (one-time setup)**
   ```powershell
   python rag\build_vector_db.py
   ```

## Running the Backend Pipeline

Execute the crew directly from the command line:

```powershell
python main.py --topic "Agentic AI Workshop on Robotics Deployments"
```

The script loads environment variables, constructs the CrewAI workflow, and prints the reviewed deliverable to stdout.

### Using `run_pipeline` Programmatically

Import `run_pipeline` from `main.py` to embed the workflow inside other applications:

```python
from main import run_pipeline

result = run_pipeline("Multi-Agent Workshop for Healthcare AI")
print(result)
```

## Running the Streamlit Frontend

1. Install frontend dependencies (optional if you already installed the backend requirements):
   ```powershell
   pip install -r frontend\requirements.txt
   ```

2. Launch the UI:
   ```powershell
   streamlit run frontend\app.py
   ```

3. Enter a workshop topic in the sidebar and click **Run Pipeline**. The output panel displays the aggregated crew result when the run completes.

## Customising Agents and Tasks

- **Agent Prompts**: Update the placeholder system prompts in `agents/planner.py`, `agents/researcher.py`, `agents/writer.py`, and `agents/reviewer.py` to align with your scenario.
- **Task Objectives**: Adjust the descriptions and expected outputs in `tasks.py` to fit new deliverables or grading rubrics.
- **Tools**: Extend `tools/` with new integrations (e.g., GitHub search, deployment triggers) and register them in `tools/__init__.py` plus the relevant tasks.
- **LLM Settings**: Tweak `config/settings.py` to experiment with temperatures, token limits, or alternative OpenRouter models.
- **Knowledge Base**: Replace `rag/documents/sample_docs.txt` with your own corpus and re-run `python rag\build_vector_db.py`.

## Troubleshooting Tips

- **Missing Vector Store**: If the research task fails to load the FAISS index, ensure `rag/vectorstore/` contains the generated files. Re-run the build script if needed.
- **Authentication Errors**: Double-check that `OPENROUTER_API_KEY` is present in your environment. The app raises an explicit error if it is missing.
- **Slow Runs**: The free tier of `meta-llama/llama-3.3-70b-instruct` can be rate limited. Consider changing the topic or upgrading your OpenRouter plan for better throughput.
- **Dependency Issues**: Match the Python version requirement and reinstall with `pip install --upgrade -r requirements.txt` when packages change.

## Next Steps for Students

1. Experiment with parallel task execution (`Process.parallel`) inside `crew.py` and evaluate trade-offs.
2. Introduce an evaluation agent that scores drafts against rubrics and stores metrics.
3. Deploy the Streamlit app to a cloud host (Streamlit Community Cloud, Azure, etc.) using environment secrets.
4. Add unit tests for custom tools or RAG pipelines to promote reproducibility.

Happy building! Customize freely to turn this template into a polished workshop experience.
