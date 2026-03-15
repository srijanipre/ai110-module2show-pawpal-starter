import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from pawpal_system import Task, Pet, Scheduler


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


# --- Sorting ---

def test_sort_by_time_orders_tasks():
    """Tasks should come back in ascending HH:MM order."""
    scheduler = Scheduler()
    tasks = [
        Task(title="Evening Meds",  description="", due_date="2026-03-16", frequency="daily", time="18:00"),
        Task(title="Morning Walk",  description="", due_date="2026-03-16", frequency="daily", time="07:30"),
        Task(title="Afternoon Play",description="", due_date="2026-03-16", frequency="daily", time="13:00"),
    ]
    sorted_tasks = scheduler.sort_by_time(tasks)
    assert [t.time for t in sorted_tasks] == ["07:30", "13:00", "18:00"]


def test_sort_by_time_empty_list():
    """Sorting an empty list should return an empty list."""
    scheduler = Scheduler()
    assert scheduler.sort_by_time([]) == []


def test_sort_by_time_single_task():
    """A single-element list should be returned as-is."""
    scheduler = Scheduler()
    task = Task(title="Walk", description="", due_date="2026-03-16", frequency="once", time="09:00")
    assert scheduler.sort_by_time([task]) == [task]


def test_sort_by_time_preserves_equal_times():
    """Tasks with identical times should all appear in the result (stable sort)."""
    scheduler = Scheduler()
    t1 = Task(title="Feed",  description="", due_date="2026-03-16", frequency="daily", time="08:00")
    t2 = Task(title="Brush", description="", due_date="2026-03-16", frequency="daily", time="08:00")
    result = scheduler.sort_by_time([t1, t2])
    assert len(result) == 2
    assert result[0].time == result[1].time == "08:00"


# --- Recurring task logic ---

def test_advance_daily_increments_date():
    """advance() on a daily task should move due_date forward by 1 day."""
    task = Task(title="Walk", description="", due_date="2026-03-16", frequency="daily")
    task.advance()
    assert task.due_date == "2026-03-17"


def test_advance_daily_resets_completion():
    """After advance(), a daily task should be pending again."""
    task = Task(title="Walk", description="", due_date="2026-03-16", frequency="daily")
    task.advance()
    assert task.completed is False


def test_advance_weekly_increments_by_seven_days():
    """advance() on a weekly task should move due_date forward by 7 days."""
    task = Task(title="Bath", description="", due_date="2026-03-16", frequency="weekly")
    task.advance()
    assert task.due_date == "2026-03-23"


def test_advance_once_stays_completed():
    """advance() on a 'once' task should leave it completed with no date change."""
    task = Task(title="Vet Visit", description="", due_date="2026-03-16", frequency="once")
    task.advance()
    assert task.completed is True
    assert task.due_date == "2026-03-16"


def test_advance_daily_crosses_month_boundary():
    """advance() should correctly roll over to the next month."""
    task = Task(title="Walk", description="", due_date="2026-03-31", frequency="daily")
    task.advance()
    assert task.due_date == "2026-04-01"


def test_advance_daily_crosses_year_boundary():
    """advance() should correctly roll over to the next year."""
    task = Task(title="Walk", description="", due_date="2026-12-31", frequency="daily")
    task.advance()
    assert task.due_date == "2027-01-01"


# --- Conflict detection ---

def test_detect_conflicts_same_date_and_time():
    """Two tasks with the same date and time should produce one conflict warning."""
    scheduler = Scheduler()
    tasks = [
        Task(title="Morning Walk",  description="", due_date="2026-03-16", frequency="daily", time="08:00"),
        Task(title="Morning Feed",  description="", due_date="2026-03-16", frequency="daily", time="08:00"),
    ]
    warnings = scheduler.detect_conflicts(tasks)
    assert len(warnings) == 1
    assert "Morning Walk" in warnings[0]
    assert "Morning Feed" in warnings[0]
    assert "2026-03-16" in warnings[0]
    assert "08:00" in warnings[0]


def test_detect_conflicts_different_times_no_conflict():
    """Tasks on the same date but different times should not conflict."""
    scheduler = Scheduler()
    tasks = [
        Task(title="Walk", description="", due_date="2026-03-16", frequency="daily", time="08:00"),
        Task(title="Feed", description="", due_date="2026-03-16", frequency="daily", time="09:00"),
    ]
    assert scheduler.detect_conflicts(tasks) == []


def test_detect_conflicts_three_way():
    """Three tasks at the same slot should produce one warning listing all three titles."""
    scheduler = Scheduler()
    tasks = [
        Task(title="Walk",  description="", due_date="2026-03-16", frequency="daily", time="08:00"),
        Task(title="Feed",  description="", due_date="2026-03-16", frequency="daily", time="08:00"),
        Task(title="Brush", description="", due_date="2026-03-16", frequency="daily", time="08:00"),
    ]
    warnings = scheduler.detect_conflicts(tasks)
    assert len(warnings) == 1
    assert "Walk" in warnings[0]
    assert "Feed" in warnings[0]
    assert "Brush" in warnings[0]


def test_detect_conflicts_default_time_triggers_conflict():
    """Two tasks with no explicit time both default to 00:00 and should conflict."""
    scheduler = Scheduler()
    tasks = [
        Task(title="Meds",  description="", due_date="2026-03-16", frequency="daily"),
        Task(title="Weigh", description="", due_date="2026-03-16", frequency="daily"),
    ]
    warnings = scheduler.detect_conflicts(tasks)
    assert len(warnings) == 1


def test_detect_conflicts_empty_list():
    """No tasks should produce no warnings."""
    scheduler = Scheduler()
    assert scheduler.detect_conflicts([]) == []
