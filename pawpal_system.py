from dataclasses import dataclass, field


@dataclass
class Task:
    title: str
    description: str
    due_date: str
    completed: bool = False

    def complete(self):
        pass

    def reset(self):
        pass


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: list = field(default_factory=list)

    def add_task(self, task):
        pass

    def remove_task(self, task):
        pass

    def list_tasks(self):
        pass


class Owner:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.pets = []

    def add_pet(self, pet):
        pass

    def remove_pet(self, pet):
        pass

    def list_pets(self):
        pass


class Scheduler:
    def __init__(self):
        self.pets = []

    def add_pet(self, pet):
        pass

    def get_pending_tasks(self, pet):
        pass

    def complete_task(self, task):
        pass

    def daily_summary(self):
        pass
