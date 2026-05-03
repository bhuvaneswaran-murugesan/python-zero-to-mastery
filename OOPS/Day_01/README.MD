✅ 1. What is OOP?

Object-Oriented Programming (OOP) is a programming paradigm that organizes code using objects and classes to model real-world entities.

It focuses on:

Encapsulation
Abstraction
Inheritance
Polymorphism

👉 It helps in building systems that are:

Reusable
Maintainable
Scalable

✅ 2. Difference between Class and Object

A class is a blueprint or template used to create objects. It defines properties (variables) and behaviors (methods).
An object is an instance of a class — a real-world entity created using that blueprint.

“Class defines structure, object represents actual data.”

✅ 3. Why use private variables?

Private variables are used to restrict direct access to internal data and ensure it is modified only through controlled methods.

👉 This helps:

Protect data integrity
Prevent accidental misuse
Enforce validation logic

✅ 4. What happens if we don’t use encapsulation?

Without encapsulation:

Internal data is exposed directly
No control over how data is modified
Leads to bugs, inconsistent state, and security issues

👉 Example:
Anyone can do:
```python
acc.balance = -100000
```

No validation → system breaks.

“Without encapsulation, the system becomes fragile and hard to maintain.”

Without encapsulation, data is exposed directly, leading to lack of control, potential bugs, and poor maintainability.