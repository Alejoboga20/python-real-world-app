# Introduction

Object-oriented programming (OOP) is a programming paradigm you can use to model the real world in code. It's based on the idea of grouping related data and functions into "islands" of information. These islands are known as objects

## OOP modeling: Identify concepts

The first step is to identify actors. They're called actors because they act and perform an action. After you identify actors, you look at what they do, which is their behavior. Then you look at descriptions of the actors and any data that's needed to carry out the action

## What' an object?

An object is an actor. It's something that does something within a system. As a result of taking an action, it changes state within itself or other objects.

## What is a class?

A class is a data type that acts as a template definition for a particular kind of object. A class is a blueprint of an object. Where the class is the blueprint of a car, the object is the actual car you drive around.

# Create a Class

A class in python is created by using the keyword **_class_** and giving it a name

```python
class Car:
```

When you create an object from a class, you're said to instantiate it.

```python
car = Car()
```

You need to tell the class what attributes it should have at construction time, when an object is being instantiated. There's a special function that's being called at the moment of creation, called a constructor.

## Constructor

In Python, the constructor has the name **init**(). You also need to pass a special parameter, self, to the constructor. The parameter self refers to the object's instance. The parameter self will also need to be passed to any methods that need to refer to anything on the object instance. You don't call the **init**() method by name, but it's called when the object is created

```python
class Elevator:
  def __init__(self, starting_floor): # __init__() is called implicitly
    self.make = 'The Elevator Company'
    self.floor = starting_floor

# To Create an object
elevator = Elevator(1)
print(elevator.make, elevator.floor) # The Elevator Company, 1
```

```python
class Car:
    def __init__():
        self.color = "Red" # ends up on the object
        make = "Mercedes" # becomes a local variable in the constructor

car = Car()
print(car.color) # "Red"
print(car.make) # would result in an error, `make` does not exist on the object
```

## Rock, paper, scissors game.

Problem description: Rock, paper, scissors is a **game** played by two participants. The game consists of **rounds**. In each round, a **participant** chooses a symbol from rock, paper, or scissors, and the other participant does the same. Then a winner of the **round** is determined by comparing the chosen symbols. The rules of the game state that rock wins over scissors, scissors beats (cuts) paper, and paper beats (covers) rock. The winner of the round is awarded a point. The game goes on for as many rounds as the participants agree on. The winner is the participant with the most points.

| Phase      | Actor       | Behavior                            | Data                                          |
| ---------- | :---------- | :---------------------------------- | :-------------------------------------------- |
| Input      | Participant | Chooses symbol                      | Symbol saved as choice on Participant(choice) |
| Processing | GameRound   | Compares choices against game rules | Result inspected                              |
| Processing | GameRound   | Awards points based on result value | Points added to winning Participant(point)    |
| Processing | Game        | Check continue answer               | Answer is true, continue, else quit           |
| Output     | Game        | New game round or game end credit   |

## Encapsulation: Protect your data

The general idea of encapsulation is that the data on an object is internal, something that only concerns the object. To protect this data you can use access modifiers.
One leading underscore still allows for data to be modified, which Python refers to as protected. Can we do this better? Yes we can, by having two leading underscores, \_\_, which is referred to as private.

```python
class Square:
  def __init__(self):
    self.__height = 2
    self.__width = 2
  def new_side(self, new_side):
    self.__height = new_side
    self.__width = new_side

square = Square()

```

Have we protected our data? Well, not entirely. Python just changes the name of the underlying data.

## Getters and Setters (Accesors and Mutators)

Getters and setters, which are also known as accessors and mutators, are methods dedicated to reading or changing your data.

```python
class Square:
  def __init__(self):
    self.__height = 2
    self.__width = 2
  def new_side(self, new_side):
    self.__height = new_side
    self.__width = new_side
  def set_height(self, h):
    if h >= 0:
      self.__height = h
    else:
      raise Exception('Value needs to be 0 or larger')


square = Square()
square.__height = 3 # raises AttributeError

```

### Use decorators for getters and setters

In the context of OOP and getters and setters, a specific decorator @property can help you remove some boilerplate code when you add getters and setters.

```python
class Square:
  def __init__(self, w, h):
    self.height = h
    self.__width = w

  def set_side(self, new_side):
    self.__height = new_side
    self.__width = new_side

  @property
  def height(self):
    return self.__height

  @height.setter
  def height(self, new_value):
    if new_value >= 0:
      self.__height = new_value
    else:
      raise Exception("Value must be larger than 0")
```

# Build an AI web app by using Python and Flask

Create Virutal Environment:

```bash
# Windows
# Create the environment
python -m venv venv
# Activate the environment
.\venv\scripts\activate

# macOS or Linux
# Create the environment
python -m venv venv
# Activate the environment
source ./venv/bin/activate

```

## Flask Fundamentals

Typically, the entry point for Flask applications is a file named app.py

To Run Flask Server:

```bash
# Windows
set FLASK_ENV=development

# Linux/macOS
export FLASK_ENV=development

flask run
```
