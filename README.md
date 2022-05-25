# Finite-Automata
## This is my lab task 4 for Dyscrete math based on Finite Automata.
My program simulates one month of making any big project. Here I have to make 700 small tasks per month to finish the project. (Small tasks means anything from typing the text to creating an algorithm. It doesn't matter. 700 small tasks = one big project.) In the end of the simulation it will print whether project was finished or you failed it because some bad events.

### DAily routine is:
1. Sleeping (from 0 AM to 8 AM)
2. Wake up and eating (8 AM)
3. Studying (from 8 AM to 5 PM)
4. Going for a walk (5 PM to 7 PM)
5. Family gathering (from 7 PM to 8 PM)
6. Beer or Whiskey drinking (rest)

### There are also 3 more events which can interrupt daily routine:
1. Air alarm (happens randomly, I move to the shelter and hiding until the end )
2. Feedback (when you received a message about your grade from some test. If it is good, the mood is ok, else mood is bad and it makes delay in your tasks. YOu will made less of them)
3. The beer is over! (It also makes you sad, and creates delay in making your project.)

## How to run the program:
~~~bash
simulator_name = Simulator()
simulator_name.run()
~~~

## Output:
You will see message by message what is happening. (When it's night, nothing is happening and the guy is sleeping you will not receive a new message, but you will see the time changing) (\r)
~~~bash
It is 1st day. 2 AM and I'm in good mood. I'm sleeping right now. There is 0 tasks done and 700 tasks left.
It is 1st day. 3 AM and I'm in good mood. I'm sleeping right now. There is 0 tasks done and 700 tasks left.
~~~
You will see just changing of the time
