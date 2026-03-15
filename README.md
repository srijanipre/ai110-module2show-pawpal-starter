# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.


## Smarter Scheduling
PawPal+ now includes several simple algorithms to improve task management:

• Tasks can be sorted by time to create an ordered daily schedule.
• Tasks can be filtered by completion status.
• Recurring tasks automatically generate their next occurrence.
• The scheduler detects basic conflicts when two tasks are scheduled at the same time.

## Testing PawPal+

The PawPal+ system includes an automated pytest suite to verify core functionality.
Tests cover sorting tasks by time, filtering pending tasks, detecting scheduling conflicts, and verifying recurring task behavior.

And you can run the tests locally by saying into your terminal:

python -m pytest

These tests confirm that the scheduler logic behaves correctly under normal conditions and common edge cases.

### Confidence Level
(4/5)

The test suite covers the main scheduling algorithms and common edge cases such as empty task lists and conflicting task times. While the system appears reliable for basic scheduling, more complex time overlap logic could be added in the future.

## Features

- **Time-sorted scheduling** — tasks are ordered by their scheduled time to produce a clean daily plan
- **Pending task filtering** — only incomplete tasks are shown, keeping the schedule focused
- **Recurring task automation** — daily and weekly tasks automatically reschedule to their next due date when completed
- **Conflict detection** — the scheduler flags any two tasks assigned to the same date and time
- **Streamlit interface** — add pets and tasks, then generate and view your schedule in an interactive web app
