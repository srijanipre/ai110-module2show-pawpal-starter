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

    # Create tasks (intentionally out of order to test sorting)
    task1 = Task("Breakfast", "Feed breakfast", "08:00", "daily")
    task2 = Task("Morning Walk", "Take Milo for a walk", "09:00", "daily")
    task3 = Task("Medication", "Give Luna medication", "18:00", "daily")

    # Create conflict tasks (same time)
    conflict1 = Task("Brush Fur", "Brush Milo's fur", "08:00", "once")
    conflict2 = Task("Vet Call", "Call the vet", "08:00", "once")

    # Assign tasks to pets
    dog.add_task(task2)
    dog.add_task(conflict1)

    cat.add_task(task1)
    cat.add_task(task3)
    cat.add_task(conflict2)

    # Create scheduler
    scheduler = Scheduler()

    # Add pets to scheduler
    scheduler.add_pet(dog)
    scheduler.add_pet(cat)

    print("\n=== ALL TASKS (UNSORTED) ===")
    for pet in scheduler.pets:
        for task in pet.tasks:
            print(f"{pet.name} - {task.title} at {task.due_date}")

    # ------------------------------------------------
    # TEST SORTING
    # ------------------------------------------------

    print("\n=== SORTED TASKS BY TIME ===")

    all_tasks = owner.all_tasks()
    sorted_tasks = scheduler.sort_by_time(all_tasks)

    for task in sorted_tasks:
        print(f"{task.title} at {task.due_date}")

    # ------------------------------------------------
    # TEST FILTERING
    # ------------------------------------------------

    print("\n=== PENDING TASKS ===")

    pending = scheduler.get_pending_tasks(cat)

    for task in pending:
        print(task)

    # ------------------------------------------------
    # TEST CONFLICT DETECTION
    # ------------------------------------------------

    print("\n=== CONFLICT CHECK ===")

    conflicts = scheduler.detect_conflicts(owner.all_tasks())

    if conflicts:
        for warning in conflicts:
            print("⚠️", warning)
    else:
        print("No conflicts detected.")

    # ------------------------------------------------
    # TEST RECURRING TASK LOGIC
    # ------------------------------------------------

    print("\n=== TEST RECURRING TASK ===")

    print("Completing task:", task1.title)
    scheduler.complete_task(task1)

    print("Task status:", task1.completed)

    print("\nTasks after completion:")
    for task in owner.all_tasks():
        print(task)


if __name__ == "__main__":
    main()