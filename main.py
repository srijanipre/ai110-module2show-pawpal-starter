from pawpal_system import Owner, Pet, Task, Scheduler


def main():
    # Create owner
    owner = Owner("Alex", "alex@email.com")

    # Create pets
    dog = Pet("Milo", "Dog", 3)
    cat = Pet("Luna", "Cat", 5)

    # Add pets to owner
    owner.add_pet(dog)
    owner.add_pet(cat)

    # Create tasks (title, description, due_date, frequency)
    task1 = Task("Breakfast", "Feed breakfast", "08:00", "daily")
    task2 = Task("Morning Walk", "Take Milo for a walk", "09:00", "daily")
    task3 = Task("Medication", "Give Luna medication", "18:00", "daily")

    # Assign tasks to pets
    dog.add_task(task2)
    cat.add_task(task1)
    cat.add_task(task3)

    # Create scheduler
    scheduler = Scheduler()

    # Add pets to scheduler so it can track them
    scheduler.add_pet(dog)
    scheduler.add_pet(cat)

    # Print schedule
    print("\nToday's Schedule")
    print("----------------")

    for pet in scheduler.pets:
        for task in pet.tasks:
            print(f"{pet.name} - {task.description} at {task.due_date}")


if __name__ == "__main__":
    main()