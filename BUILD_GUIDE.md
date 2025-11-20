# Complete Build Guide: Multi-Agent System from Scratch

## 📋 Overview
This guide will take you from zero to a fully working multi-agent AI system. Follow each step in order.

---

## 🎯 Step 1: Environment Setup

### 1.1 Install Dependencies
```powershell
# Create virtual environment (if not already done)
python -m venv .venv

# Activate it
.\.venv\Scripts\Activate.ps1

# Install all packages
pip install -r requirements.txt
```

### 1.2 Get OpenRouter API Key
1. Go to https://openrouter.ai/
2. Sign up (free tier available)
3. Get your API key from dashboard
4. Create `.env` file in project root:

```powershell
# Create .env file
New-Item -Path .env -ItemType File
```

Add this to `.env`:
```
OPENROUTER_API_KEY=your_api_key_here
```

**✅ Checkpoint:** Run `python -c "from config.settings import OpenRouterLLMConfig; print('Config OK')"` - should print "Config OK"

---

## 🗄️ Step 2: Build RAG Vector Database

The RAG (Retrieval-Augmented Generation) tool needs a vector database to search through documents.

### 2.1 Check Documents
- Documents go in `rag/documents/sample_docs.txt`
- This is your knowledge base that agents can search

### 2.2 Build Vector Store
```powershell
python rag\build_vector_db.py
```

**Expected Output:** `Vector store saved to .../rag/vectorstore`

**✅ Checkpoint:** Verify `rag/vectorstore/` folder exists with files inside

---

## 🤖 Step 3: Complete Agent Prompts

Agents are the "workers" in your system. Each needs clear instructions.

### 3.1 Planner Agent (`agents/planner.py`)

**Purpose:** Creates the initial plan/roadmap

**Fill in:**
```python
name="Workshop Planner"
role="Architect the workshop roadmap and align deliverables"
goal="Produce a milestone-driven execution plan covering research, authoring, and review"
backstory="You are an expert workshop designer. You excel at breaking down ambiguous goals into concrete, evidence-backed steps. You think strategically about learning outcomes and participant experience."
SYSTEM_PROMPT="You are the Workshop Planner. Analyze the given topic and create a structured plan with clear milestones, required resources, and a realistic timeline. Focus on actionable steps."
```

### 3.2 Researcher Agent (`agents/researcher.py`)

**Purpose:** Gathers information using tools

**Fill in:**
```python
name="Research Specialist"
role="Curate authoritative context for workshop deliverables"
goal="Blend RAG insights with verified web findings to back every recommendation"
backstory="You are a meticulous researcher. You validate claims, cite sources, and prepare concise summaries. You use both local knowledge base and live web search to ensure accuracy."
SYSTEM_PROMPT="You are the Research Specialist. Use the RAG tool to search local documents and DuckDuckGo for current information. Validate all claims and provide citations. Prepare bullet summaries for the writer."
```

### 3.3 Writer Agent (`agents/writer.py`)

**Purpose:** Creates the final content

**Fill in:**
```python
name="Content Writer"
role="Author workshop scripts, lab guides, and deployment notes"
goal="Produce polished, instructor-ready materials grounded in researched evidence"
backstory="You are a technical writer specializing in educational content. You translate complex AI workflows into accessible, hands-on content. You maintain clarity and actionable takeaways."
SYSTEM_PROMPT="You are the Content Writer. Transform research findings and plans into compelling narratives. Use Markdown formatting. Include sections for Goals, Agenda, Labs, and Resources. Keep it practical and instructor-friendly."
```

### 3.4 Reviewer Agent (`agents/reviewer.py`)

**Purpose:** Quality checks the output

**Fill in:**
```python
name="Quality Reviewer"
role="Ensure every deliverable is accurate, actionable, and polished"
goal="Deliver constructive critiques and sign-off criteria before publication"
backstory="You are a quality assurance expert. You safeguard against gaps, errors, and unclear guidance. You provide actionable feedback to improve content."
SYSTEM_PROMPT="You are the Quality Reviewer. Audit the draft for factual accuracy, completeness, pedagogy, and deployment readiness. Provide an executive summary with strengths, gaps, and concrete improvement suggestions."
```

**✅ Checkpoint:** All 4 agent files should have filled prompts (no "Add..." placeholders)

---

## 📝 Step 4: Define Tasks

Tasks tell agents WHAT to do. Edit `tasks.py`:

### 4.1 Planning Task
```python
description=(
    "Analyze the workshop topic '{topic}' and craft a milestone-based execution plan. "
    "List required assets, responsible roles, tooling, and a realistic timeline."
),
expected_output=(
    "A structured plan including objectives, three to five milestones, resource requirements, "
    "risk mitigation ideas, and success metrics."
),
name="Planning",
```

### 4.2 Research Task
```python
description=(
    "Use the local knowledge base and live web results to validate the plan for '{topic}'. "
    "Cite at least three trustworthy sources and capture data points that justify each milestone."
),
expected_output=(
    "A bullet list of insights with inline citations, key statistics, and references to the RAG documents."
),
name="Research",
```

### 4.3 Writing Task
```python
description=(
    "Draft the workshop narrative for '{topic}', including an overview, prerequisites, step-by-step labs, and deployment notes. "
    "Incorporate the research insights and calculator results where helpful."
),
expected_output=(
    "A Markdown-formatted workshop guide with sections for Goals, Agenda, Hands-on Labs, Deployment, and Resources."
),
name="Writing",
```

### 4.4 Review Task
```python
description=(
    "Review the draft content for '{topic}' for accuracy, completeness, and pedagogy. Provide an executive summary of strengths, "
    "list gaps or issues, and suggest concrete improvements."
),
expected_output=(
    "A review report with sections for Summary, Major Findings, Minor Suggestions, and Final Recommendation."
),
name="Reviewing",
```

**✅ Checkpoint:** All tasks have proper descriptions and expected outputs

---

## 🧪 Step 5: Test Basic Pipeline

### 5.1 Run from Command Line
```powershell
python main.py --topic "Introduction to Multi-Agent Systems"
```

**What happens:**
1. Planner creates a plan
2. Researcher gathers info
3. Writer creates content
4. Reviewer checks quality
5. Final output printed

**Expected:** You'll see agent logs and final output

**Common Issues:**
- **Missing API key:** Check `.env` file
- **Missing vectorstore:** Run Step 2 again
- **Import errors:** Activate venv and reinstall requirements

**✅ Checkpoint:** Pipeline runs without errors and produces output

---

## 🖥️ Step 6: Test Frontend (Streamlit)

### 6.1 Launch UI
```powershell
python -m streamlit run frontend\app.py
```

**What happens:**
- Browser opens at `http://localhost:8501`
- Enter topic in sidebar
- Click "Run Pipeline"
- See output in main panel

**✅ Checkpoint:** UI loads and can run pipeline successfully

---

## 🛠️ Step 7: Create a Custom Tool (Practice)

Let's create a simple "Text Analyzer" tool as practice.

### 7.1 Create Tool File
Create `tools/text_analyzer.py`:

```python
"""Text analysis tool for agents."""
from __future__ import annotations

from crewai.tools import BaseTool

class TextAnalyzerTool(BaseTool):
    name: str = "text_analyzer"
    description: str = (
        "Analyze text to count words, characters, and sentences. "
        "Useful for content quality checks."
    )

    def _run(self, text: str) -> str:
        words = len(text.split())
        chars = len(text)
        sentences = text.count('.') + text.count('!') + text.count('?')
        
        return (
            f"Text Analysis:\n"
            f"- Words: {words}\n"
            f"- Characters: {chars}\n"
            f"- Sentences: {sentences}"
        )

def create_text_analyzer_tool() -> TextAnalyzerTool:
    """Create a text analyzer tool instance."""
    return TextAnalyzerTool()
```

### 7.2 Register in `tools/__init__.py`
Add to imports:
```python
from .text_analyzer import create_text_analyzer_tool
```

Add to `__all__`:
```python
__all__ = [
    "create_rag_tool",
    "create_web_search_tool",
    "create_calculator_tool",
    "create_text_analyzer_tool",  # NEW
    "get_default_toolkit",
]
```

### 7.3 Add to Toolkit (Optional)
In `get_default_toolkit()`, add:
```python
return [
    create_rag_tool(),
    create_web_search_tool(),
    create_calculator_tool(),
    create_text_analyzer_tool(),  # NEW
]
```

**✅ Checkpoint:** Tool can be imported and used

---

## 👥 Step 8: Create Additional Agent (Practice)

Let's add a "Fact Checker" agent.

### 8.1 Create Agent File
Create `agents/fact_checker.py`:

```python
"""Fact checker agent for validation."""
from __future__ import annotations

from typing import Any, Iterable, Optional
from crewai import Agent
from config.settings import build_crewai_llm

SYSTEM_PROMPT = (
    "You are a Fact Checker. Verify claims made in content against "
    "reliable sources. Use web search and RAG tools to validate information."
)

def create_fact_checker_agent(
    tools: Optional[Iterable[object]] = None,
    llm_overrides: dict[str, Any] | None = None,
) -> Agent:
    return Agent(
        name="Fact Checker",
        role="Verify factual accuracy of content",
        goal="Ensure all claims are backed by reliable sources",
        backstory="You are meticulous about accuracy. You cross-reference information and flag unverified claims.",
        llm=build_crewai_llm(**(llm_overrides or {})),
        allow_delegation=False,
        verbose=True,
        system_prompt=SYSTEM_PROMPT,
        tools=list(tools or []),
    )
```

### 8.2 Register in `agents/__init__.py`
```python
from .fact_checker import create_fact_checker_agent

__all__ = [
    "create_planner_agent",
    "create_researcher_agent",
    "create_writer_agent",
    "create_reviewer_agent",
    "create_fact_checker_agent",  # NEW
]
```

### 8.3 Add to Crew (`crew.py`)
In `create_workshop_crew()`:
```python
from agents import create_fact_checker_agent  # Add import

# Inside function:
fact_checker = create_fact_checker_agent(tools=get_default_toolkit())

# Add to tasks (create task in tasks.py first)
tasks = build_workshop_tasks(planner, researcher, writer, reviewer, fact_checker)

# Add to crew
return Crew(
    agents=[planner, researcher, writer, reviewer, fact_checker],  # Added
    tasks=tasks,
    process=Process.sequential,
    verbose=True,
)
```

**✅ Checkpoint:** New agent works in pipeline

---

## 🎓 Understanding the Flow

```
User Input (Topic)
    ↓
main.py → run_pipeline()
    ↓
crew.py → create_workshop_crew()
    ↓
Agents Created (with tools)
    ↓
Tasks Created (linked to agents)
    ↓
Crew.kickoff() → Sequential Execution:
    1. Planner → Creates plan
    2. Researcher → Gathers info (uses tools)
    3. Writer → Creates content
    4. Reviewer → Reviews output
    ↓
Final Result Returned
```

---

## 🔧 Troubleshooting

### Issue: "OPENROUTER_API_KEY is missing"
**Fix:** Check `.env` file exists and has correct key

### Issue: "Vector store not found"
**Fix:** Run `python rag\build_vector_db.py`

### Issue: Import errors
**Fix:** 
1. Activate venv: `.\.venv\Scripts\Activate.ps1`
2. Reinstall: `pip install -r requirements.txt`

### Issue: Agents produce empty output
**Fix:** Check agent prompts are filled (not placeholders)

### Issue: Tasks not executing
**Fix:** Verify task descriptions use `{topic}` placeholder correctly

---

## 🚀 Next Steps (Advanced)

1. **Custom RAG Documents:** Add your own docs to `rag/documents/`
2. **Different Models:** Change model in `config/settings.py`
3. **Parallel Processing:** Change `Process.sequential` to `Process.hierarchical`
4. **Deployment:** Follow README.md deployment section
5. **Add More Tools:** API integrations, databases, file operations

---

## 📚 Key Concepts Learned

✅ **Agents:** Workers with specific roles and goals  
✅ **Tasks:** What agents need to accomplish  
✅ **Tools:** Capabilities agents can use (RAG, search, calculator)  
✅ **Crew:** Orchestrates agents and tasks  
✅ **RAG:** Retrieval-Augmented Generation for knowledge base  
✅ **Sequential Process:** Agents work one after another  

---

## ✨ You're Done!

You now have a working multi-agent system! Experiment with:
- Different agent prompts
- New tools
- Different task flows
- Custom knowledge bases

Happy building! 🎉

