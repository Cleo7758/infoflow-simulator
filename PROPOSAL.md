### Capstone Proposal: InfoFlow Simulator

**A Telemetry Dashboard for Information Engagement Analytics**

---

**Course:** Programming & Data Analysis for Journalism and Communication in the Age of AI

**Instructor:** Yuan (John) Yao

**Team Members:** Yicheng Jiang (Team Lead), Shuoyang Jin, Jiaxin Wang, Quanquan Lu

**Date:** July 10, 2026

---

#### 1. Project Title

**InfoFlow Simulator: A Telemetry Dashboard for Information Engagement Analytics**

---

#### 2. Research Problem & Rationale

In the AI-driven media environment, understanding *why* audiences lose attention is as important as understanding *what* they engage with. Traditional communication research methods (e.g., surveys, interviews) rely on self-reported data, which suffers from social desirability bias and inaccurate recall. Laboratory methods (e.g., eye-tracking, EEG) are precise but expensive and not scalable.

Our project bridges this gap by proposing a **third path**: a lightweight, behavior-based telemetry approach that tracks **"information engagement"** through simulated user interactions. We ask:

> *How does information complexity affect user attention retention and cognitive load?*

By building an interactive simulation environment, we can generate granular behavioral data—click paths, dwell time, dropout points—and visualize these patterns through a public dashboard. This demonstrates a **reproducible, scalable methodology** for evaluating information effectiveness without relying on costly equipment or subjective surveys.

**Methodological Iteration:** This project evolved from an earlier game-analytics concept. We retained the simulation-telemetry-dashboard pipeline but repositioned the application domain to information engagement—a direct response to the course's emphasis on journalism and communication contexts. Given the 1.5-week timeline, our methodology prioritizes **completeness over complexity**, delivering a fully deployed, reproducible prototype.

---

#### 3. Dataset

We will use a **self-generated synthetic dataset** created by a Python-based simulation engine. The dataset simulates virtual "users" navigating through information mazes (puzzle-like levels) of varying complexity. Each generated log includes:

- `user_id` (virtual agent ID)
- `level_id` (information complexity tier)
- `action_timestamp`
- `action_type` (enter/click/exit)
- `dwell_time` (seconds spent per node)
- `dropout_flag` (whether the user abandoned the task)

**Data volume target:** ~500–1,000 behavioral logs. The dataset is fully reproducible and requires no external API access or ethical clearance, allowing the team to focus on the core analytics pipeline.

---

#### 4. Methodology & Technical Approach

Our analysis pipeline follows a structured workflow:

| Stage | Task | Tools |
| :--- | :--- | :--- |
| **Data Generation** | Simulate virtual user behaviors in a controlled information maze | Python (random logic, CSV export) |
| **Storage** | Import logs into a relational database and run structured queries | SQLite + Python `sqlite3` |
| **Exploratory Analysis** | Compute descriptive statistics; generate visualizations | pandas + matplotlib/seaborn |
| **Predictive Modeling** | Train baseline regression + classification models to predict dropout | scikit-learn (LinearRegression / LogisticRegression) |
| **Dashboard Deployment** | Build interactive 3-tab web dashboard; deploy to public cloud | Streamlit + Render |

All code will be version-controlled via GitHub with clear commit history and reproducible dependencies (`requirements.txt`).

---

#### 5. Connection to Journalism & Communication

This project aligns with the course's emphasis on **audience interaction analysis**. Our telemetry framework can be directly applied to real-world journalism contexts, such as:

- Evaluating how different narrative formats (text-only vs. multimedia) affect reader retention
- Identifying "dropout points" in long-form investigative journalism
- A/B testing information architectures for news apps

While we use simulated data for this prototype, the methodology itself is transferable to real user behavior tracking (e.g., via web analytics or in-app event logging). The dashboard serves as a **decision-support tool** for newsrooms and communication designers.

---

#### 6. Team Roles & Responsibilities

| Role | Team Member | Core Responsibilities |
| :--- | :--- | :--- |
| **Team Lead / Architect** | Yicheng Jiang | Simulation engine, data schema, final presentation, overall integration |
| **Data Analyst / Modeler** | Shuoyang Jin | SQL queries, pandas cleaning, regression/classification models |
| **Frontend / Dashboard** | Jiaxin Wang | Streamlit UI development, deployment configuration |
| **Narrative / Communication** | Quanquan Lu | Report writing, README, PPT, theoretical framing, AI usage disclosure |

---

#### 7. Timeline (Two-Week Sprint)

| Date | Task |
| :--- | :--- |
| Jul 9–10 | Simulation engine development; CSV generation |
| Jul 10–11 | SQL import + queries; EDA + visualizations |
| Jul 11–12 | Regression + classification baselines; Dashboard prototyping |
| Jul 12 | **Submit 1-page Proposal** |
| Jul 13–14 | Dashboard completion; deployment to Render |
| Jul 14–15 | Report writing; AI disclosure; PPT preparation |
| Jul 16 | **Final Submission: deployed link + GitHub repo + report** |

---

#### 8. AI Usage Disclosure (Proposed)

In accordance with the course policy, AI tools (ChatGPT, Copilot) are used exclusively for:

- Generating boilerplate Streamlit UI components
- Debugging error messages and suggesting fixes
- Explaining unfamiliar library syntax (e.g., scikit-learn)

**All code generated by AI is reviewed, tested, and understood** by the team member who integrates it. The final report's narrative will be written entirely by the team, without AI-generated prose. The full AI-use disclosure will be appended to the final submission, detailing specific tools, prompts used, and verification steps taken.

See [AI_DISCLOSURE.md](AI_DISCLOSURE.md) for the complete statement.

---

#### 9. Limitations & Future Work

**Current limitations:** The dataset is synthetic; findings reflect simulated behaviors, not real human responses. The predictive models are baseline only and not intended for high-stakes decision-making.

**Future directions:** For CHI 2027, we plan to:
- Replace virtual agents with human participants (IRB-approved)
- Introduce multimodal variables (text/video/audio)
- Apply survival analysis to model attention decay over time

---

#### 10. Repository & Deployment Plan

- **GitHub repo:** `https://github.com/[team-name]/infoflow-simulator`
- **Deployment platform:** Render (free tier)
- **Final deliverables:** deployed dashboard link + GitHub repo + 4–5 page report + AI-use note

---

*This proposal is submitted as part of the capstone planning requirement for Lesson 7.*
