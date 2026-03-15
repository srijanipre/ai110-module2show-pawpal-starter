from dataclasses import dataclass, field
from collections import defaultdict
from datetime import date, timedelta


@dataclass
class Task:
    title: str
    description: str
    due_date: str
    frequency: str        # e.g. "daily", "weekly", "once"
    time: str = "00:00"   # "HH:MM" format
    completed: bool = False

    def complete(self):
        """Mark the task as completed."""
        self.completed = True

    def reset(self):
        """Reset the task completion status."""
        self.completed = False

    def advance(self):
        """Complete the task and schedule the next occurrence if recurring.

        - "daily"  → due_date advances by 1 day, task resets to pending
        - "weekly" → due_date advances by 7 days, task resets to pending
        - "once"   → task stays completed with no new date
        """
        self.complete()
        delta = {"daily": timedelta(days=1), "weekly": timedelta(weeks=1)}.get(self.frequency)
        if delta:
            next_date = date.fromisoformat(self.due_date) + delta
            self.due_date = next_date.isoformat()
            self.completed = False

    def __str__(self):
        status = "done" if self.completed else "pending"
        return f"[{status}] {self.title} ({self.frequency}) — due {self.due_date}"


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: list = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a new task to this pet."""
        self.tasks.append(task)

    def remove_task(self, task: Task):
        """Remove a task from this pet."""
        self.tasks.remove(task)

    def list_tasks(self):
        """Print all tasks for this pet."""
        if not self.tasks:
            print(f"{self.name} has no tasks.")
        for task in self.tasks:
            print(f"  {task}")

    def pending_tasks(self):
        """Return all incomplete tasks for this pet."""
        return [t for t in self.tasks if not t.completed]

    def __str__(self):

        return f"{self.name} ({self.species}, age {self.age})"


class Owner:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.pets: list[Pet] = []

    def add_pet(self, pet: Pet):
        """Add a pet to this owner's account."""
        self.pets.append(pet)

    def remove_pet(self, pet: Pet):
        """Remove a pet from this owner."""
        self.pets.remove(pet)

    def list_pets(self):
        """Print all pets owned by this user."""
        if not self.pets:
            print(f"{self.name} has no pets.")
        for pet in self.pets:
            print(f"  {pet}")

    def all_tasks(self):
        
        """Return every task across all pets."""
        return [task for pet in self.pets for task in pet.tasks]

    def __str__(self):
        return f"Owner: {self.name} ({self.email})"


class Scheduler:
    def __init__(self):
        self.pets: list[Pet] = []

    def add_pet(self, pet: Pet):
        """Register a pet with the scheduler."""
        self.pets.append(pet)

    def get_pending_tasks(self, pet: Pet):
        """Return all incomplete tasks for a specific pet."""
        return pet.pending_tasks()

    def complete_task(self, task: Task):
        """Mark a task as completed."""
        task.complete()

    def daily_summary(self):
        """Print a summary of pending tasks across all managed pets."""
        print("=== Daily Summary ===")
        any_pending = False
        for pet in self.pets:
            pending = pet.pending_tasks()
            if pending:
                any_pending = True
                print(f"\n{pet.name}:")
                for task in pending:
                    print(f"  {task}")
        if not any_pending:
            print("All tasks are complete!")

    def sort_by_time(self, tasks: list) -> list:
        """Return tasks sorted by their time attribute (HH:MM string)."""
        return sorted(tasks, key=lambda task: task.time)

    def filter_incomplete(self, tasks: list) -> list:
        """Return only incomplete tasks from a given list."""
        return [task for task in tasks if not task.completed]

    def tasks_for_pet(self, pet_name: str) -> list:
        """Return all tasks belonging to a pet with the given name."""
        return [
            task
            for pet in self.pets
            if pet.name == pet_name
            for task in pet.tasks
        ]

    def detect_conflicts(self, tasks: list) -> list[str]:
        """Return warning messages for any tasks sharing the same date and time.

        Algorithm:
        1. Group tasks by (due_date, time) using a dict of lists.
        2. Any slot with more than one task is a conflict.
        3. Return one warning string per conflicting slot.
        """
        slots = defaultdict(list)
        for task in tasks:
            slots[(task.due_date, task.time)].append(task)

        warnings = []
        for (due_date, time), conflicting in slots.items():
            if len(conflicting) > 1:
                titles = ", ".join(t.title for t in conflicting)
                warnings.append(f"Conflict on {due_date} at {time}: {titles}")
        return warnings

    def tasks_by_frequency(self, frequency: str):
        """Return all tasks across all pets matching a given frequency."""
        return [
            task
            for pet in self.pets
            for task in pet.tasks
            if task.frequency == frequency
        ]
