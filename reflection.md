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
My scheduler currently detects conflicts only when two tasks have the exact same scheduled time. It does not yet check for overlapping durations (for example, a 20-minute walk starting at 9:00 overlapping with a feeding at 9:10). I chose this simpler approach because it keeps the conflict detection algorithm easy to understand and sufficient for a basic scheduling demo.
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?
I used AI to help debug and draft my functions. By checking everything it was outputting, it was helpful for me to learn what functions were going wrong later. The prompts that were the most helpful was when I was very specific in my prompting as it wouldn't stray from what I was advising. 

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?
One example where I modified AI output was during conflict detection. The initial suggestion included a more complex approach for checking overlapping time ranges. Since my system only stores task times in a simple "HH:MM" format, I simplified the logic to detect only exact time matches. This made the code easier to read and sufficient for the scope of the project.---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?
I tested several core behaviors of the PawPal+ system. These included verifying that tasks can be added to a pet correctly, that marking a task as complete updates its status, and that tasks are sorted properly by time using the scheduler. I also tested conflict detection to make sure the scheduler flags tasks that are scheduled at the same time. These tests were important because they verify that the main features of the system—task management, scheduling, and conflict detection—work as expected.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?
I feel fairly confident that the scheduler works correctly for the basic scenarios the app supports. The automated tests confirm that sorting, task completion, and conflict detection behave as expected. If I had more time, I would test additional edge cases such as pets with no tasks, multiple pets with overlapping schedules, and more complex recurring task scenarios.
---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
The part of the project I’m most satisfied with is the overall system structure. Designing the classes for Owner, Pet, Task, and Scheduler made the project easier to organize and helped separate responsibilities clearly. Once the architecture was in place, implementing features like sorting tasks and detecting conflicts became much easier.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
If I had another iteration, I would improve how the UI interacts with the backend scheduler. Right now the UI is fairly simple, and I would expand it to allow users to manage tasks more directly through the interface. I would also improve the scheduling logic to handle more complex time conflicts or overlapping task durations.
**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
One key takeaway from this project is the importance of acting as the “lead architect” when working with AI tools. While Copilot helped generate useful ideas and code suggestions, it was still necessary to evaluate those suggestions and adapt them to fit the overall design of the system. This reinforced that AI can be a powerful assistant, but the developer still needs to guide the structure and decisions of the project.