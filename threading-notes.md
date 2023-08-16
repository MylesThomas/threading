# Threading

## Project Setup

Open VSCode terminal or a command prompt in Windows.

Setup the local project directory:

```sh
mkdir threading
cd threading
```

Head to github.com and create a new repository named threading.

After completing that, create a new repository on the command line:

```sh
echo "# threading" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/MylesThomas/threading.git
git push -u origin main
```

Save this markdown file into directory `threading` as `threading-notes.md`, then open up a new VSCode instance and Open folder > `threading`.

Setup a virtual Python environment:

```sh
cd threading
py -m venv env
```

You should now see a folder 'env' with a python.exe program in the /Scripts directory.

Create a .gitignore file for the Python project and save it in the root directory `threading`:

```sh
cd threading
echo > .gitignore
```

Code for .gitignore: [Link to file](https://github.com/github/gitignore/blob/main/Python.gitignore)

Activate the virtual environment in the terminal:

```sh
where python
.\env\Scripts\activate

python.exe -m pip install --upgrade pip
pip list
```

Note: You can leave the virtual environment with this call:

```sh
deactivate
```

Save these files and update git before beginning the project:

```sh
cd threading
git status
git add .
git commit -m "Completed project setup"
git push -u origin main
git status
git log --oneline
q
```

## Tech With Tim - Threading Explained

[Link to video series](https://www.youtube.com/watch?v=olYdb0DdGtM&list=PLzMcBGfZo4-lTUl-4m1-9Jk27Eulyrmkx)

### Threading Tutorial #1 - Concurrency, Threading and Parallelism Explained

#### Intro

We won't be doing coding to start, just learning about what the heck threading actually is. More specifically:
- What is a thread
- What is threading
- Why do we use threading?

#### What is Threading?

A classic multi-core processor in 2020:
- 1 CPU (Central Processing Unit)
- 4 Cores

Notes:
- In old days, you'd have 1 CPU with 1 core
    - Nowadays, there will be 1 CPU with 4/8/16/32 cores

- Idea: Amount of cores on your process = # of things that can occur at once
    - 4 cores = 4 operations can occur at the same time
        - Low level operations that take nanoseconds

Parallelism: Multiple things happening at the same exact time
- Example of Parallel Operations: 4 cars driving on road at the same time

Note: Think of the opposite of parallel for 4 cars, where the 3 in the back have to wait for car #1 to go first

Clock speed of processor: 2.6ghz
- Meaning: Each of your 4 cores can run at 2.6gpz
    - The entire computer can do 4*2.6million operations per second

Now, we are going to do way more than 4 operations, so how do we schedule when those happen? This is where threads and multi-processing comes in!

Thread: 1 set of operations that needs to occur
- Each thread gets assigned to 1 core

Threading: How we determine when to run different things on the same CPU core
- Different things can run on the same core
    - Threading does not involve running on multiple cores

- Example: 1 core with 2 threads
    - 
    - 

Look at Threads in Action:
- Head to Task Manager > Performance
    - Under speed in GHz, you should see the number of threads currently running (Mine says 3527 threads and 285 processes)

What this means - Between the 4 cores on my computer, we can run 4 threads at once, and we are doing that by switching between the 3527 threads
- All the operations take milliseconds
- All the operations are being switched between

We are NOT doing things in parallel, we are changing the order in which we are doing things.

What is the point of this if we can't do things at the same time?
- Sometimes, a thread hangs/stops. When a thread hangs/stops, it can work on something else!
    - We don't need to actually be executing at the current time, so our processor's core can turn around and work on a different thread
        - No need to be stuck on a thread that is idle

Concurrent Programming: Multiple sequences of operations are run in overlapping periods of time
- YES: Multiple threads running at the same time, and the CPU core switches between the different threads
- NOT: Doing things in parallel at the same time

#### One Core Model

Let's take an old 1 core to explain how a single core processor works.

Now, let's look at the difference between running in 1 thread vs. multiple threads:

1 thread:

```py
# thread 1
print(1)
time.sleep(10)
print(2)
```

Time elapsed: ~10 seconds
- 1 is printed
- 10 second sleep
- 2 is printed

Multiple threads:

```py
# thread 1
print(1)
time.sleep(10)
print(3)
# thread 2
print(2)
```

Time elapsed: ~10 seconds
- 1 is printed
    - we skip over the 10 second sleep (no need to wait/stall at thread 1 while it hangs)
    - we are now working on thread 2
- 2 is printed
    - thread 2 is finished, so back to thread 1
    - we continue to wait for the 10 seconds sleep to finish...
- 3 is printed

Threads are very useful for web applications and online games!
- You don't want to pause the screen while you wait for a few mb of data
- What you want:
    - All server related commands running in a thread
        - While you wait for the server to return a response to you, your whole game does not freeze
        - The other thread that updates/displays the screen does not get slowed down, this way

Notes:
- A lot of applications are multi-processed, which makes it more complicated
    - Their threads run at different CPU cores at the same time (This is beyond scope of this video)

Ending notes:
- If we are waiting for something to happen in 1 thread, we will switch to another thread/threads and execute as much as we can, and then go back to thread #1 when it is ready/stops hanging

#### Git

```sh
cd threading

git status
git add .
git commit -m "Completed Video #1 - Concurrency, Threading and Parallelism Explained"
git push -u origin main
git status
git log --oneline
q
```

### Threading Tutorial #2 - Implementing Threading in Python 3 (Examples)

This video will have examples to give a clear image of how threading works.

#### Setup

```sh
echo > basics.py
```

```py
# basics.py
import threading
import time
```

Notes:
- Import thread is the depracated way
    - old ones may have _thread - still fine to use, but best to use newer stuff

How to make a thread:
- Make a function that will act as your thread
- Make a thread with threading.Thread()
    - target: function to call
        - do not use brackets
    - args: a tuple of arguments
        - make sure to use a tuple with a comma at the end (None automatically gets infered afterwards, it keeps it in the correct tuple form)
- Start the thread with x.start()

```py
import threading
import time

def func():
    print('ran')
    time.sleep(1)
    print('done')
    
# x = threading.Thread(target=func, args=(4, ))
print(threading.active_count()) # 1
x = threading.Thread(target=func)
print(threading.active_count()) # 1
x.start()

print(threading.active_count()) # 2
```

Notes:
- You can use lambda function if you'd like for target

Good to remember: Before importing threading or making new threads, our program is running from 1 thread.
- If you create a new thread: You now have 2 active threads!
    - Active thread
    - x
        - look at number of active threads with threading.active_count()

Let's look at a little more complex of an example:

```py
import threading
import time

def func():
    print('ran')
    time.sleep(1)
    print('done')
    time.sleep(0.85)
    print('now done')
    
x = threading.Thread(target=func)
x.start()
print(threading.active_count()) # 2
time.sleep(0.90)
print("finally")
```

Run the code with Ctrl-Shift-N.

What happens here/order of operations:
- start on the main thread, the python program
    - A new thread is created
    - Once we get down to x.start(), we switch to that thread
- thread x, we begin running the function `func`
    - print 'ran'
    - Now that we have to sleep for 1 second, we switch back to the main thread
- main thread, we continue down the program
    - print '2' (for the active thread count)
    - Now that we have to sleep for 0.90 seconds, we switch back to the x thread
- thread x, we continue down the function
    - print 'done'
    - Now that we have to sleep for 0.85 seconds, we switch back to the main thread
- main thread, we continue on down
    - print 'finally'
    - This thread is done, so we switch back to the x thread
- thread x, we continue to finish the function
    - print 'now done'


Let's make an example of more than 1 thread:

```py
import threading
import time

def count(n):
    for i in range(1, n+1):
        print(i)
        time.sleep(0.01)
        
for _ in range(2):
    x = threading.Thread(target=count, args=(10, ))
    x.start()
    
print("Done!")
```

What happens here/order of operations:
- 1 is printed by thread x1
- 1 is printed by thread x2
- Done is printed
    - Both threads have to pause and sleep, so in the meantime, we go back to the main thread and finish running the program
- 2/2, 3/3, 4/4, etc. by threads x1/x2 until we hit 10


Watch what happens if you pass in an argument for sleep:

```py
import threading
import time

def count(n):
    for i in range(1, n+1):
        print(i)
        time.sleep(0.01)
        
def count2(n):
    for i in range(1, n+1):
        print(i)
        time.sleep(0.02)
        
x = threading.Thread(target=count, args=(10, ))
x.start()

y = threading.Thread(target=count2, args=(10, ))
y.start()
    
print("Done!")
```

What happens here:
- Count2 takes longer to sleep, so sometimes Count gets to print twice


Now, let's look at using a global variable with different threads:

```py
import threading
import time

ls = []

def count(n):
    for i in range(1, n+1):
        ls.append(i)
        time.sleep(0.5)
        
def count2(n):
    for i in range(1, n+1):
        ls.append(i)
        time.sleep(0.5)
        
x = threading.Thread(target=count, args=(5, ))
y = threading.Thread(target=count2, args=(5, ))

x.start()
y.start()

print(ls)
    
print("Done!")
```

Notes:
- Threads are NOT safe when it comes to accessing global memory (Can fix that with locks ie. threading.Lock())

What happens here:
- We get [1, 1] ie. not the full list...
    - This is because while count/count2 are sleeping, the program continues onto the main thread to print ls.

We want the ls to get filled all the way up, how do we get our code to do that?

Using "Thread Synchronization" with the .join() method!

What does thread.join() do?
- "Wait for this thread to stop running"
- "Do not move past this line of code until the thread is done"
    - In most examples: The main Python program's thread is halted
        - Allows you to have multiple threads run AND finish before moving on

```py
import threading
import time

ls = []

def count(n):
    for i in range(1, n+1):
        ls.append(i)
        time.sleep(0.5)
        
def count2(n):
    for i in range(1, n+1):
        ls.append(i)
        time.sleep(0.5)
        
x = threading.Thread(target=count, args=(5, ))
y = threading.Thread(target=count2, args=(5, ))

x.start()
y.start()

x.join()
x.join()

print(ls)
    
print("Done!")
```

What happens here:
- Main thread starts
- X starts
    - Adds 1 to ls
    - Gets halted by time.sleep
- Y starts
    - Adds 1 to ls
    - Gets halted by time.sleep
- We alternate between threads x/y until they complete
- Main thread picks up and ls is printed
- Done!

#### Git

```sh
cd threading

git status
git add .
git commit -m "Completed Video #2 - Implementing Threading in Python 3 (Examples)"
git push -u origin main
git status
git log --oneline
q
```