from PIL.ImageChops import screen

##### A new generate random colour function
Unlike the previous `generate_colour()` function I code,this function avoids generating same colours twice in a row.

```
def random_colour(last_colour):
    while True:
        new_colour = tuple(random.randint(0, 255) for _ in range(3))
        if new_colour == last_colour:
            last_colour = new_colour
            return new_colour
random_colour.last_colour = None
```

##### Make an Etch-A-Sketch App
This file named `day19_etch_a_sketch_app` I have has a game Etch-A-Sketch. I used a different python file,`day19_etch_a_sketch_app_movement_system`, to store the movement system.
It has a function name `clear_drawing` when u press 'c' it will clear the screen. I used the funtion `resetscreen()` but u can also use `clear() and to return turtle to center home()`
# 🐢 Understanding Key Programming Concepts

This guide explains important concepts like **instance**, **state**, and **lambda functions**, with simple analogies and examples from Turtle graphics in Python.

---

## 🧩 What is an **Instance**?

An **instance** is a specific individual object created from a class.  
You can think of a class like a blueprint, and an instance as the actual object built from it.

> 🧠 **Analogy:**  
> A `Turtle()` object is an instance of the `Turtle` class.  
> Just like you and I are instances of the `Human` class.

### ✅ Example:
```
from turtle import Turtle

timmy = Turtle()
tommy = Turtle()
```
Here, both timmy and tommy are separate instances of the Turtle class. They can move independently, have different shapes, colors, and behaviors.

## 🧠 What is **State**?
The state of an object refers to its current attributes or what it’s doing at a particular moment.

>🧠 Analogy:
>If timmy is green and moving forward, and tommy is purple and stationary, they are in different states.

### ✅ Example:
```
timmy.color("green")
timmy.forward(100)

tommy.color("purple")
# Tommy is not moving
```
- `timmy's state`: color is green, and it is moving.  

- `tommy's state`: color is purple, and it's not moving.

Each object (instance) can have its own state.

## ⚡ What is a Lambda Function?
A lambda is a small, anonymous function.
It's used when you need a function temporarily — often for callbacks or short expressions.

> ### 🧠 Analogy:
> A lambda is like a mini function written on a sticky note — small, quick, and meant to be used once.

### ✅ Syntax:

```python
lambda arguments: expression
```
#### ✅ Example (Turtle movement):

```python
    screen.onkey(lambda: timmy.forward(10), "W")
```  

Here, `lambda: timmy.forward(10)` creates a function on the fly.
It doesn’t run immediately, but will be executed when the "W" key is pressed.

#### 🔄 Related Concepts
### ✅ Function vs. Lambda:
```python
# Regular function
def say_hello():
    print("Hello!")

# Lambda version (anonymous)
say_hello = lambda: print("Hello!")
```
Both do the same thing — but lambda is shorter and useful when passing functions as arguments.

🧪 Summary Table

| Concept  | Meaning                                               | Example                      |
|----------|--------------------------------------------------------|------------------------------|
| Instance | An individual object created from a class              | `timmy = Turtle()`           |
| State    | The current attributes or behavior of an instance      | `timmy.color("green")`       |
| Lambda   | A small, anonymous function used for short callbacks   | `lambda: timmy.forward(10)`  |

