# Parallel Programming Exercises

## 🔴 Basic Concepts I

### 1. What do you call a command-line interpreter which lets you interact with your OS and execute Python commands and scripts?

- An editor
- Jython
- A console
- A compiler

### 2. What is the expected output of the following code?

```python
prin("Goodbye!")
```

- The program will generate an error message to the screen
- The program will output **("Goodbye!")** to the screen
- The program will output **"Goodbye!"** to the screen
- The program will output **Goodbye!** to the screen

### 3. What is the expected output of the following code?

```python
print("Hello!")
```

- The program will output **Hello!** to the screen
- The program will generate an error message to the screen
- The program will output **"Hello!"** to the screen
- The program will output **("Hello!")** to the screen

### 4. What is CPython?

- It's a programming language that is a superset of the C language, designed to produce Python-like performance with code written in C
- It's the default, reference implementation of the C language, written in Python
- It's a programming language that is a superset of Python, designed to produce C-like performance with code written in Python
- It's the default, reference implementation of Python, written in the C language

### 5. What is true about compilation?

**I.** The code is converted directly into machine code executable by the processor
**II.** It tends to be slower that interpretation
**III.** Both you and the end user must have the compiler to run your code
**IV.** It tends to be faster that interpretation

- I and II
- I and III
- II and III
- I and IV

## 🔴 Basic Concepts II

### 1. The print() function can output values of

- any number of arguments (including zero)
- just one argument
- any number of arguments (excluding zero)
- not more than five arguments

### 2. What is the output of the following snippet if the user enters two lines containing 2 and 4 respectively?

```python
x = input()
y = input()
print(x + y)
```

- 24
- 2
- 4
- 6

### 3. What is the output of the following snippet?

```python
y = 2 + 3 * 5.
print(Y)
```

- 25
- the program will generate an error message to the screen
- 17
- 17.0

### 4. The ** operator

- does not exist
- performs duplicated multiplication
- performs floating-point multiplication
- performs exponentiation

### 5. The meaning of the keyword parameter is determined by

- its position within the argument list
- its value
- the argument's name specified along with its value
- its connection with existing variables

## 🔴 Loops and Sequences

### 1. What is the output of the following code?

```python
my_list = [1, 2, 3]
for v in range(len(my_list)):
    my_list.insert(1, my_list[v])
print(my_list)
```

- [1, 2, 3, 1, 2, 3]
- [1, 2, 3, 3, 2, 1]
- [3, 2, 1, 1, 2, 3]
- [1, 1, 1, 1, 2, 3]

### 2. How many stars will the following code snippet print?

```python
i = 0
while i <= 5:
    i += 1
    if i % 2 == 0:
        break
    print("*")
```

- three
- one
- two
- zero

### 3. How many elements does the my_list contain after the following code is executed?

```python
my_list = [i for i in range(-1, 2)]
```

- four
- one
- two
- three

### 4. What is the output of the following code?

```python
my_list = [3, 1, -2]
print(my_list[my_list[-1]])
```

- -2
- 3
- 1
- -1

### 5. The value eventually assigned to the variable x is

```python
x = 1
x = x == x
```

- False
- 1
- True
- 0

## 🔴 Functions and Decorators

### 1. What is the output of the following code?

```python
def func(a, b):
    return a ** a

print(func(2))
```

- 4
- 2
- None
- error

### 2. What is the output of the following code?

```python
def func(inp=2, out=3):
    return inp * out

print(func(out=2))
```

- 2
- 4
- 6
- error

### 3. What is the output of the following code?

```python
def decorator(func):
    def wrapper():
        print("Before function call", end=" >> ")
        result = func()
        print("After function call", end=" >> ")
        return result
    return wrapper


@decorator
def say_hello():
    print("Hello!", end=" >> ")

say_hello()
```

- Before function call >> Hello!
- Hello! >> Before function call
- Before function call >> Hello! >> After function call >>
- The program will generate an error message to the screen

### 4. What is the output of the following code?

```python
def func(x):
    global y
    y = x * x
    return y


func(2)
print(y)
```

- 2
- None
- 4
- error

### 5. What is the output of the following code?

```python
def func(x, y, z):
    return x + 2 * y + 3 * z


print(func(0, z=1, y=3))
```

- 3
- error
- 0
- 9

## 🔴 Asynchronous Programming

### 1. Which method starts an event loop in asyncio module?

- asyncio.start()
- asyncio.run()
- asyncio.loop()
- asyncio.call()

### 2. How does asynchronous programming handle multiple tasks?

- By running them on different threads
- By switching between tasks using the event loop
- By running them on multiple CPU cores
- By starting a new event loop for each task

### 3. What will happen if you forget to await a coroutine?

- The coroutine will run twice
- The coroutine will throw a runtime error
- The coroutine will return a coroutine object instead of running
- The coroutine will block the event loop

### 4. Which of the following correctly declares an asynchronous function?

- def async_function():
- async def async_function():
- def async async_function():
- def async_function async():

### 5. What is the function of asyncio.gather()?

- It creates a new event loop for each coroutine
- It ensures coroutines run sequentially
- It schedules multiple coroutines to run concurrently
- It waits for each coroutine to finish before starting the next one