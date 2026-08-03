# OOP — 4 Pillars (always revise with CS)

## 1 Encapsulation
Hide data; access via methods.
```python
class BankAccount:
    def __init__(self):
        self.__balance = 0  # private-ish
    def deposit(self, x):
        self.__balance += x
```

## 2 Abstraction
Show only needed details; hide complex internals.
Example: `car.start()` — you don’t see engine chemistry.

## 3 Inheritance
Child gets parent features.
```python
class Animal:
    def eat(self): return "eating"
class Dog(Animal):
    def bark(self): return "bark"
```

## 4 Polymorphism
Same interface, different behavior.
```python
class Animal:
    def speak(self): pass
class Dog(Animal):
    def speak(self): return "bark"
class Cat(Animal):
    def speak(self): return "meow"
```

## Speak answer
> OOP pillars are encapsulation, abstraction, inheritance, and polymorphism. Polymorphism lets Dog and Cat both use speak() differently.
