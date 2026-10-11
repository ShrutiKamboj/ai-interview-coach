# AI Interview Coach

An AI-powered coach for behavioral interviews. It runs mock interview sessions with adaptive follow-up questions, then scores your answers against a structured rubric, with feedback grounded in what you actually said.

## Why

- Practice behavioral rounds with realistic follow-ups instead of a static question list
- Get consistent, evidence-based feedback rather than generic praise
- Build and track a library of your own stories, mapped to competencies

## Status

**Phase 1 — in progress.** Planning and setup. Setup instructions will be added once there is something to run.

## Phase 1 scope

**In scope**
- One role: Lead/Staff software engineer, behavioral interviews only
- Text answers only
- Rubric with 4–5 criteria, stored as config (not hardcoded)
- Grader: a score plus quoted evidence for each rubric criterion
- Interviewer agent: asks questions, probes with follow-ups, switches competency, ends the session
- Story library: save stories and tag them by competency
- A small hand-labeled eval set to measure grading consistency
- Runs locally, single user

**Out of scope for now**
- Voice input
- Roles other than software engineering
- Login / multi-user
- Deployed web app
- Polished UI

## Roadmap

1. **Phase 1:** Build for a single user (tech, Lead/Staff level)
2. **Phase 2:** Configurable rubrics per role, so it works for any job, not just tech
3. **Phase 3:** Roll out to a small group of users and improve it from their feedback

## Design notes

- The **interviewer** is an agent: it decides what to ask next based on your answers.
- The **grader** is a fixed workflow: scoring needs to be consistent and repeatable.

See [docs/decisions.md](docs/decisions.md) for the reasoning behind design choices and [docs/devlog.md](docs/devlog.md) for progress notes.

## Tech

- Python
