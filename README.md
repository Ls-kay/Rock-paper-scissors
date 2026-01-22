# Rock Paper Scissors Lizard Spock (Python)

## 📌 Project Overview

This project is a simple Python implementation of the classic **Rock–Paper–Scissors–Lizard–Spock** game. It allows two players to input their choices and determines the winner based on predefined rules.

The project is designed to demonstrate:

* Clean Python function design
* Dictionary-based game logic
* Input validation
* Conditional decision-making

It is ideal for beginners learning Python fundamentals or for use as a coding exercise, interview question, or teaching example.

---

## 🎯 Purpose

The purpose of this project is to:

* Show how game rules can be modeled using Python dictionaries
* Practice writing readable and maintainable Python code
* Demonstrate logical problem-solving and control flow
* Provide a correct and extensible solution to the Rock–Paper–Scissors–Lizard–Spock problem

---

## 🕹️ Game Rules

Each option defeats two others and loses to two others:

* **Rock** crushes Scissors and Lizard
* **Paper** covers Rock and disproves Spock
* **Scissors** cuts Paper and decapitates Lizard
* **Lizard** eats Paper and poisons Spock
* **Spock** smashes Scissors and vaporizes Rock

If both players choose the same option, the result is a tie.

---

## ⚙️ How It Works

The game logic is stored in a dictionary where each key represents a move, and its value is a list of moves that defeat it.

Example:

```python
"rock": ["paper", "spock"]
```

This means that **rock loses** to paper and spock.

The program:

1. Validates both player inputs
2. Checks for a tie
3. Determines the winner using dictionary lookup
