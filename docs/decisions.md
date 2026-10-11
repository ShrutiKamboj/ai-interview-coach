# Decisions

One short entry per real decision: what was decided, why, and what was traded off. Newest at the bottom.

---

## 001 — Interviewer is an agent; grader is a workflow
**Date:** 2026-10-11

**Decision:** The interviewer is built as an agent (the model chooses the next step and uses tools). The grader is a fixed workflow (same steps every time, structured output).

**Why:** A good interviewer adapts: it probes vague answers, switches competency, and decides when it has enough signal. That needs adaptive control flow. Grading needs the opposite: the same answer should get the same score, which a fixed rubric and a fixed workflow support far better.

**Trade-off:** The agent is harder to test and less predictable. That's acceptable for asking questions, but not for scoring.

---

## 002 — Rubric stored as config, not hardcoded
**Date:** 2026-10-11

**Decision:** Rubric criteria and level descriptions live in a config file, not in prompt strings in code.

**Why:** Phase 2 will add rubrics for other job roles. Keeping the rubric as data means adding a role is a config change, not a rewrite.

**Trade-off:** A bit more structure up front than Phase 1 strictly needs.

---

## 003 — Phase 1 is text-only, single-user, local
**Date:** 2026-10-11

**Decision:** No voice, auth, deployment, or polished UI in Phase 1.

**Why:** The time budget is limited (about 1 hour per weekday plus weekends). The core learning and the core value are in the interviewer and grader, not the surrounding features.

**Trade-off:** It isn't shareable with others until Phase 3.

---

## 004 — Python
**Date:** 2026-10-11

**Decision:** Build in Python.

**Why:** It has the widest AI tooling and examples, and learning it is an explicit goal of this project.

**Trade-off:** Learning a new language alongside AI concepts in the first weeks.

---

## 005 — Public repo from day one
**Date:** 2026-10-11

**Decision:** The repository is public from the first commit.

**Why:** Progress is visible as it happens.

**Trade-off:** Secrets must never be committed: API keys go in `.env`, which is git-ignored. Sample answers in the eval set must be generic or anonymized, with no real employer details.

---

## 006 — Layered rubric: base, job family, role level, company
**Date:** 2026-10-11

**Decision:** Evaluation config is split into layers:
- `config/rubrics/` — role-neutral criteria that judge any answer (structure, ownership, impact, scope, reflection)
- `config/families/<family>/family.yaml` — per job family (e.g. software engineering): what each scope level looks like, and the full pool of competencies
- `config/families/<family>/roles/<level>.yaml` — per level (e.g. Lead, Staff): the minimum score that meets the bar for each criterion, and which competencies to emphasise
- `config/companies/` (later) — optional company values overlay

Roles are nested inside their family's folder, so the folder is the single source of truth for which family a role belongs to (no `family:` field to fall out of sync), and level names can repeat across families without clashing.

**Why:** Most criteria are the same for any job. What varies by job is what "scope" looks like and which competencies exist; what varies by level is the bar and the competency focus. Separating them means a new level or a new job family is a small config file, with no change to the base rubric or code.

**Trade-off:** More files and a lookup step to join them by id, instead of one self-contained file.

---

## Open decisions
- Which LLM provider and model to use
- CLI or minimal local web page for the Phase 1 interface
- Where to store sessions and the story library (e.g. JSON files vs SQLite)
