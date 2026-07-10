# InfoFlow Simulator

**A Telemetry Dashboard for Information Engagement Analytics**

> *Course:* Programming & Data Analysis for Journalism and Communication in the Age of AI
> *Instructor:* Yuan (John) Yao
> *Team:* Yicheng Jiang (Lead), Shuoyang Jin, Jiaxin Wang, Quanquan Lu
> *Date:* July 2026

---

## Project Overview

InfoFlow Simulator is a lightweight, simulation-driven telemetry dashboard that models how virtual "users" engage with information of varying complexity. The engine generates behavioral logs—dwell time, click paths, dropout points—which we analyze using SQL and scikit-learn to identify attention-retention patterns. The final output is an interactive 3-tab Streamlit dashboard (Cognitive Heatmap, Dropout Alert, Future Research Blueprint) deployed on Render.

This is a **methodological prototype**, not a human-subject study. Given our 1.5-week sprint, we prioritize a clean, reproducible pipeline over extensive experimentation. No IRB, no survey bias—just synthetic data and a scalable analytics framework that speaks to both HCI (CHI) and communication (ICA) audiences.

---

## Version Note: From Game Analytics to Information Engagement

This project began as a game-analytics telemetry study (original title: *Playtesting with Data*). We retained the core DNA—synthetic data generation, SQL-backed telemetry, dropout as a key metric, and an interactive dashboard—but pivoted the application domain for two reasons:

| Factor | Original (Jul 7) | Current (Jul 9) |
| :--- | :--- | :--- |
| **Course alignment** | HCI/games focus | Journalism & communication audience analytics |
| **Timeline** | Open-ended | 1.5-week sprint (Jul 9–16) |
| **Team capacity** | 2 members, recruiting | 4 members, fulfilled |
| **Analytical question** | Cognitive bottleneck in puzzles | Information engagement & attention retention |
| **Predictive output** | Stuck rates | Dropout probability (regression + classification) |

**What stayed unchanged:** the technical infrastructure (Python simulation → SQLite storage → EDA → baseline models → Streamlit dashboard), the commitment to reproducibility (GitHub + requirements.txt + deployment), and the transparent disclosure of AI assistance.

For a detailed version log, see [VERSION_LOG.md](VERSION_LOG.md).

---

## Repository Structure

```
infoflow-simulator/
├── data/               # Synthetic dataset (generated)
├── notebooks/          # EDA and modeling notebooks
├── src/                # Simulation engine and SQL scripts
├── dashboard/          # Streamlit app
├── docs/               # Report and supplementary materials
├── requirements.txt    # Python dependencies
├── README.md           # This file
├── PROPOSAL.md         # Capstone proposal
├── AI_DISCLOSURE.md    # AI use disclosure statement
└── VERSION_LOG.md      # Version evolution log
```

---

## Team Members & Roles

| Role | Team Member | Core Responsibilities |
| :--- | :--- | :--- |
| **Team Lead / Architect** | Yicheng Jiang | Simulation engine, data schema, final presentation, overall integration |
| **Data Analyst / Modeler** | Shuoyang Jin | SQL queries, pandas cleaning, regression/classification models |
| **Frontend / Dashboard** | Jiaxin Wang | Streamlit UI development, deployment configuration |
| **Narrative / Communication** | Quanquan Lu | Report writing, README, PPT, theoretical framing, AI usage disclosure |

---

## Timeline (Two-Week Sprint)

| Date | Task |
| :--- | :--- |
| Jul 9–10 | Simulation engine development; CSV generation |
| Jul 10–11 | SQL import + queries; EDA + visualizations |
| Jul 11–12 | Regression + classification baselines; Dashboard prototyping |
| Jul 12 | Submit 1-page Proposal |
| Jul 13–14 | Dashboard completion; deployment to Render |
| Jul 14–15 | Report writing; AI disclosure; PPT preparation |
| Jul 16 | Final Submission: deployed link + GitHub repo + report |

---

## Deployment & Deliverables

- **GitHub repo:** `https://github.com/[team-name]/infoflow-simulator`
- **Deployment platform:** Render (free tier)
- **Final deliverables:** deployed dashboard link + GitHub repo + 4–5 page report + AI-use note

---

## AI Usage Disclosure

We use AI coding assistants (ChatGPT, Copilot) for boilerplate code generation, debugging, and syntax explanation. All AI-generated code is reviewed, tested, and understood by team members before inclusion. The final report includes a full disclosure section documenting specific AI tools used and verification steps taken.

See [AI_DISCLOSURE.md](AI_DISCLOSURE.md) for the complete statement.

---

## Contact

Our team is currently at full capacity and not recruiting. However, if you're interested in our work—whether for the methodology, the dashboard design, or the communication angle—we'd love to hear from you. Ideas, feedback, code reviews, and general encouragement are all welcome.

When reaching out, please include **"InfoFlow"** in your subject line.

---

## License

[MIT](LICENSE)
