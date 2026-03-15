# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

1) A user should be able to add a pet to their account.
2) A user should be able to schedule a care task such as feeding, walking, medication, or an appointment.
3) A user should be able to view upcoming or current tasks for each pet.

I structured the system around four main classes: Owner, Pet, Task, and Scheduler. The Owner class represents the user and keeps track of their pets. Each Pet stores basic information and a list of care tasks. The Task class represents things like feeding, walks, medication, or appointments. The Scheduler class manages the logic for organizing and retrieving tasks, and later will handle things like sorting and conflict detection. I chose this structure because it follows the real-world relationship where an owner has pets, pets have tasks, and the scheduler helps organize those tasks. 

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
I didn’t make any major structural changes after reviewing the design with AI. However, during prompting the AI initially generated regular Python classes. After I clarified that I wanted to use Python dataclasses for objects like Task and Pet, the skeleton was updated to use dataclasses instead, which made the structure cleaner and more concise.
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
