import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from pawpal_system import Task, Pet


def test_task_completion():
    """Mark the task as completed."""
    task = Task(
        title="Morning Walk",
        description="Walk around the block",
        due_date="2026-03-16",
        frequency="daily"
    )
    assert task.completed is False
    task.complete()
    assert task.completed is True


def test_add_task_increases_count():
    pet = Pet(name="Buddy", species="Dog", age=3)
    task = Task(
        title="Feed Buddy",
        description="Half cup of kibble",
        due_date="2026-03-16",
        frequency="daily"
    )
    assert len(pet.tasks) == 0
    pet.add_task(task)
    assert len(pet.tasks) == 1
