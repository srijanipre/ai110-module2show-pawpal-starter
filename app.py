import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

if "owner" not in st.session_state:
    st.session_state.owner = Owner("Alex", "alex@email.com")

owner = st.session_state.owner

st.title("🐾 PawPal+")

st.header("Add a Pet")

new_pet_name = st.text_input("Pet Name")
new_species = st.text_input("Species")
new_age = st.number_input("Age", min_value=0)

if st.button("Add Pet"):
    if new_pet_name and new_species:
        new_pet = Pet(new_pet_name, new_species, new_age)
        owner.add_pet(new_pet)
        st.success(f"{new_pet_name} added!")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

st.markdown("### Tasks")

if not owner.pets:
    st.info("Add a pet first before adding tasks.")
else:
    pet_names = [pet.name for pet in owner.pets]
    selected_pet_name = st.selectbox("Assign to pet", pet_names)

    col1, col2 = st.columns(2)
    with col1:
        task_title = st.text_input("Task title", value="Morning walk")
        task_description = st.text_input("Description", value="")
        task_time = st.text_input("Time (HH:MM)", value="08:00")
    with col2:
        task_due_date = st.date_input("Due date")
        task_frequency = st.selectbox("Frequency", ["once", "daily", "weekly"])

    if st.button("Add task"):
        selected_pet = next(p for p in owner.pets if p.name == selected_pet_name)
        new_task = Task(
            title=task_title,
            description=task_description,
            due_date=task_due_date.isoformat(),
            frequency=task_frequency,
            time=task_time,
        )
        selected_pet.add_task(new_task)
        st.success(f"Task '{task_title}' added to {selected_pet_name}.")

    all_tasks = owner.all_tasks()
    if all_tasks:
        st.write("Current tasks:")
        st.table([
            {"Pet": p.name, "Task": t.title, "Time": t.time, "Due": t.due_date, "Frequency": t.frequency}
            for p in owner.pets
            for t in p.tasks
        ])
    else:
        st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")

if st.button("Generate schedule"):
    scheduler = Scheduler()
    for pet in owner.pets:
        scheduler.add_pet(pet)

    all_tasks = owner.all_tasks()
    sorted_tasks = scheduler.sort_by_time(all_tasks)

    if not sorted_tasks:
        st.info("No tasks found. Add a pet and tasks above.")
    else:
        rows = [
            {
                "Time": t.time,
                "Task": t.title,
                "Due": t.due_date,
                "Frequency": t.frequency,
                "Status": "Done" if t.completed else "Pending",
            }
            for t in sorted_tasks
        ]
        st.table(rows)

        conflicts = scheduler.detect_conflicts(sorted_tasks)
        if conflicts:
            for msg in conflicts:
                st.warning(msg)
        else:
            st.success("No conflicts detected — your schedule is clear!")

st.header("Your Pets")

for pet in owner.pets:
    st.write(f"{pet.name} ({pet.species}, age {pet.age})")