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

## Open decisions
- Which LLM provider and model to use
- CLI or minimal local web page for the Phase 1 interface
- Where to store sessions and the story library (e.g. JSON files vs SQLite)
