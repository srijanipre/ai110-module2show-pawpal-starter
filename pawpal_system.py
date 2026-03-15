from dataclasses import dataclass, field


@dataclass
class Task:
    title: str
    description: str
    due_date: str
    frequency: str        # e.g. "daily", "weekly", "once"
    completed: bool = False

    def complete(self):
        """Mark the task as completed."""
        self.completed = True

    def reset(self):
        """Reset the task completion status."""
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

    def tasks_by_frequency(self, frequency: str):
        """Return all tasks across all pets matching a given frequency."""
        return [
            task
            for pet in self.pets
            for task in pet.tasks
            if task.frequency == frequency
        ]
