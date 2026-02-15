# 🧠 Python OOP (Object Oriented Programming) – Complete Guide

This document explains Python OOP concepts from the very beginning to advanced level with examples and diagrams.

---

### 📌 What is OOP?

OOP (Object Oriented Programming) is a programming style where we organize code using:

- Classes
- Objects

It helps to build real-world structured and scalable applications.

---

### 1️⃣ Class

A class is a blueprint or template.

Example:

```python
class Student:
    pass
```

##### Student is just a design. It does not hold data ye


### 2️⃣ Object

An object is a real instance of a class.

```python

class Student:
    pass

s1 = Student()
s2 = Student()


```

- Student → Blueprint  
- s1, s2 → Real objects

### 3️⃣ Constructor (__init__)

A constructor runs automatically when an object is created.

```python

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Lincoln", 23)

print(s1.name)
print(s1.age)

```

#### Explanation

self.name = name

Left side → Object variable

Right side → Value passed during object creation


### 4️⃣ Instance Variables

Variables created using self inside constructor.

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

```

Each object will have its own separate data.


### 5️⃣ Methods

Functions inside a class are called methods.

```python 
class Calculator:
    def add(self, a, b):
        return a + b

obj = Calculator()
print(obj.add(5, 3))

```

### 6️⃣ Encapsulation
📌 Definition

Encapsulation means:

Protecting data and allowing controlled access.

```bash
        Bank Account
        -----------------
        - balance (private)
        -----------------
        + deposit()
        + withdraw()
        + get_balance()

```

#### 🔹 Example

```python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount(5000)
account.deposit(1000)
print(account.get_balance())


```