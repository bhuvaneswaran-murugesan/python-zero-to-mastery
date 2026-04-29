# 🍽️ Ratatouille OOP Mini Project (Python)

## 📌 Overview

This project is inspired by the movie *Ratatouille* and is designed to demonstrate the **four pillars of Object-Oriented Programming (OOP)** in Python:

* Encapsulation
* Inheritance
* Abstraction
* Polymorphism

It simulates a kitchen system where chefs prepare dishes, orders are managed, and payments are processed.

---

## 🎯 Objectives

* Practice real-world OOP design
* Understand how to structure Python projects
* Apply OOP concepts in a modular way
* Prepare for interview-level design questions

---

## 🧱 Project Structure

```
ratatouille_oops/
│
├── main.py
├── README.md
│
├── chefs/
│   ├── base_chef.py
│   ├── human_chef.py
│   └── rat_chef.py
│
├── kitchen/
│   └── kitchen.py
│
├── orders/
│   └── order.py
│
├── payments/
│   ├── base_payment.py
│   ├── card_payment.py
│   └── cash_payment.py
│
└── models/
    └── dish.py
```

---

## 🧠 OOP Concepts Used

### 🔐 Encapsulation

* Private variables in `Kitchen` class (e.g., `__orders`)
* Controlled access via methods

---

### 🧬 Inheritance

* `Chef` → `HumanChef`, `RatChef`
* `Payment` → `CardPayment`, `CashPayment`

---

### 🧩 Abstraction

* Abstract base classes using `ABC`
* Enforced method implementation (`cook()`, `pay()`)

---

### 🎭 Polymorphism

* Same method (`cook()`) behaves differently:

  * Human chef cooks normally
  * Rat chef (Remy) cooks secretly

---

## 🚀 How to Run

### 1. Clone or Download

```
git clone <your-repo-url>
cd ratatouille_oops
```

### 2. Run the program

```
python main.py
```

---

## 🔄 Example Flow

1. Create dishes
2. Place orders
3. Assign a chef
4. Process orders
5. Make payment

---

## 🧪 Sample Output

```
Remy cooks Ratatouille
Paid 300 using card
```

---

## 🔧 Features

* Modular folder structure
* Clean separation of concerns
* Extensible design
* Beginner-friendly but scalable

---

## 🚀 Future Improvements

* Add ingredient validation
* Support multiple chefs dynamically
* Add order status tracking (Pending → Completed)
* Introduce logging system
* Add unit tests

---

## 📚 Learning Outcomes

By completing this project, you will:

* Understand real-world application of OOP
* Learn Python project structuring
* Improve debugging and design skills
* Be better prepared for coding interviews

---

## 🙌 Acknowledgment

Inspired by the creativity and teamwork shown in *Ratatouille*—where even a rat can become a great chef!

---

## 📌 Author

**Bhuvaneswaran Murugesan**

---
