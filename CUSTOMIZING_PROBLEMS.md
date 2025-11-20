# 🎯 Changing the Problem You're Solving

## ✅ YES! You Can Absolutely Change the Problem

The multi-agent system is **completely flexible**. The current setup solves "workshop creation," but you can adapt it to solve **any problem** that benefits from a sequential workflow.

---

## 🔄 How to Change the Problem

### Step 1: Redefine What You're Building
The current flow is:
- **Problem:** Create workshop materials
- **Flow:** Plan → Research → Write → Review

You can change this to **anything**:

### Step 2: Update Agent Roles & Goals
Modify the `role` and `goal` in each agent file to match your new problem.

### Step 3: Update Task Descriptions
Modify `tasks.py` to reflect what each agent should do for your problem.

### Step 4: Update System Prompts
Adjust the `SYSTEM_PROMPT` in each agent to guide them for your specific use case.

---

## 💡 Example Problem Transformations

### Example 1: **News Article Creation**
**Problem:** Create a comprehensive news article from a topic

**Agents:**
- **Planner** → Creates article outline and structure
- **Researcher** → Gathers facts, quotes, statistics
- **Writer** → Writes the article
- **Reviewer** → Fact-checks and edits

**Tasks:**
- Plan article structure
- Research topic thoroughly
- Write article draft
- Review for accuracy and style

---

### Example 2: **Product Launch Strategy**
**Problem:** Create a complete product launch plan

**Agents:**
- **Planner** → Strategic launch roadmap
- **Researcher** → Market analysis, competitor research
- **Writer** → Marketing materials, press releases
- **Reviewer** → Validate strategy completeness

**Tasks:**
- Create launch timeline
- Research market and competitors
- Write marketing content
- Review strategy gaps

---

### Example 3: **Study Companion / Learning Assistant**
**Problem:** Create study guides for any topic

**Agents:**
- **Planner** → Learning path structure
- **Researcher** → Gather educational resources
- **Writer** → Create study materials
- **Reviewer** → Ensure educational quality

**Tasks:**
- Plan learning milestones
- Research topic thoroughly
- Write study guide
- Review for clarity and completeness

---

### Example 4: **Business Plan Generator**
**Problem:** Create comprehensive business plans

**Agents:**
- **Planner** → Business plan structure
- **Researcher** → Market research, financial data
- **Writer** → Write business plan sections
- **Reviewer** → Validate business logic

**Tasks:**
- Create business plan outline
- Research market and finances
- Write business plan
- Review for viability

---

### Example 5: **Code Review System**
**Problem:** Review and improve code

**Agents:**
- **Planner** → Review checklist and priorities
- **Researcher** → Find best practices, patterns
- **Writer** → Document findings and suggestions
- **Reviewer** → Final code quality assessment

**Tasks:**
- Plan review approach
- Research coding standards
- Document review findings
- Final quality check

---

### Example 6: **Recipe & Meal Planning**
**Problem:** Create meal plans with recipes

**Agents:**
- **Planner** → Meal plan structure
- **Researcher** → Find recipes, nutritional info
- **Writer** → Create recipe cards and meal plans
- **Reviewer** → Check nutritional balance

**Tasks:**
- Plan weekly meals
- Research recipes and nutrition
- Write meal plan and recipes
- Review for balance and feasibility

---

## 🛠️ Quick Change Template

### For Any New Problem:

1. **Identify the workflow:**
   - What needs to be planned?
   - What needs to be researched?
   - What needs to be written/created?
   - What needs to be reviewed?

2. **Update agents** (`agents/*.py`):
   ```python
   role="[Detailed description of what this agent does for YOUR problem]"
   goal="[What this agent should achieve for YOUR problem]"
   ```

3. **Update tasks** (`tasks.py`):
   ```python
   description="[What this task does for YOUR problem, using {topic} placeholder]"
   expected_output="[What output is expected for YOUR problem]"
   ```

4. **Update system prompts** (in agent files):
   ```python
   SYSTEM_PROMPT="[Instructions specific to YOUR problem]"
   ```

---

## 🎨 Customization Levels

### Level 1: **Simple** - Just Change Topics
- Keep everything the same
- Just use different topics when running
- Example: "AI Ethics" vs "Cloud Computing"

### Level 2: **Medium** - Change Problem Domain
- Update agent roles and goals
- Update task descriptions
- Keep the same 4-agent structure
- Example: Workshop → News Article

### Level 3: **Advanced** - Add/Remove Agents
- Add new agents (e.g., Fact Checker, Designer)
- Remove agents you don't need
- Change the workflow order
- Example: Add a "Designer" agent for visual content

### Level 4: **Expert** - Custom Tools & Workflows
- Create domain-specific tools
- Change from sequential to hierarchical process
- Add custom knowledge bases
- Example: Add a "Database Query" tool for data analysis

---

## 📝 Example: Converting to "News Article Creator"

### 1. Update Planner Agent
```python
role=(
    "You are an editorial strategist who creates comprehensive article outlines. "
    "You analyze news topics and create structured plans with key sections, "
    "interview questions, required sources, and narrative flow..."
)
goal="Create a detailed article outline with sections, sources, and angle"
```

### 2. Update Researcher Agent
```python
role=(
    "You are an investigative journalist who gathers facts, quotes, statistics, "
    "and expert opinions. You verify sources and ensure all information is "
    "current and accurate..."
)
goal="Gather verified facts, quotes, and statistics for the article"
```

### 3. Update Writer Agent
```python
role=(
    "You are a news writer who crafts engaging, factual articles. You write "
    "with journalistic integrity, using the inverted pyramid structure, "
    "including quotes, and maintaining objectivity..."
)
goal="Write a complete, publication-ready news article"
```

### 4. Update Tasks
```python
# Planning task
description="Create a comprehensive article outline for '{topic}' including headline, lead, body structure, and conclusion"

# Research task  
description="Research '{topic}' thoroughly, gathering facts, quotes from experts, statistics, and recent developments"

# Writing task
description="Write a complete news article for '{topic}' following journalistic standards"

# Review task
description="Review the article for factual accuracy, journalistic integrity, and editorial quality"
```

---

## 🚀 Your Current Setup

Right now, your system is configured for:
- **Problem:** Workshop creation
- **Output:** Workshop guides with labs, deployment notes, etc.

But you can change it to **anything** that follows a similar workflow!

---

## 💭 Questions to Ask Yourself

When adapting to a new problem:

1. **What's the end goal?** (e.g., workshop guide, news article, business plan)
2. **What needs planning?** (structure, outline, roadmap)
3. **What needs research?** (facts, data, best practices)
4. **What needs creation?** (content, code, documents)
5. **What needs review?** (quality, accuracy, completeness)

---

## ✨ The Beauty of This System

The multi-agent architecture is **problem-agnostic**. The same structure works for:
- Educational content
- Business documents
- Creative writing
- Technical documentation
- Research papers
- Marketing materials
- And much more!

**Just update the prompts, roles, and tasks to match your domain!**

---

## 🎯 Next Steps

1. **Decide your problem** - What do you want to solve?
2. **Map the workflow** - Plan → Research → Create → Review?
3. **Update agents** - Modify roles and goals
4. **Update tasks** - Change descriptions
5. **Test it** - Run with your new problem domain

**The system is yours to customize! 🚀**

