# Singleton Design Pattern in Python

## 1. Introduction

Singleton Design Pattern is a creational design pattern that ensures a class has only one instance throughout the entire application and provides a global point of access to that instance.

In simple words, it means only one object of a class will ever be created and reused everywhere in the program.

---

## 2. Core Idea of Singleton

The main idea of Singleton is to control object creation.

Normally, when we create a class, we can create multiple objects from it. But in Singleton, we restrict this behavior and allow only one object.

The same object is returned every time the class is called.

---

## 3. Characteristics of Singleton Pattern

The Singleton Pattern has the following characteristics:

Only one instance is created for the entire application  
The same instance is reused everywhere  
Object creation is controlled inside the class  
It provides a global access point to the object  
It helps in sharing state across the application

---

## 4. Where Singleton is Used

Singleton is commonly used in real-world applications where a single shared resource is required.

It is used in database connection management where only one connection object is maintained  
It is used in logging systems where all logs go through a single logger instance  
It is used in configuration management where application settings are shared globally  
It is used in caching systems to store and retrieve shared data  
It is used in API clients to reuse a single connection handler  
It is used in thread pools and resource managers

---

## 5. Basic Implementation in Python

A simple Singleton implementation using the **new** method is shown below.

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```
