# Introduction to Programming – Week 3  
**Lab Logbook Summary**

## Overview
This lab focused on **decision making and repetition** in Python programs. The main topics included Boolean expressions, relational and logical operators, selection using `if`, `elif`, and `else`, and iteration using `while` and `for` loops. The lab also introduced membership testing, ternary operators, and loop control statements such as `break` and `continue`. These concepts allow programs to make decisions and repeat actions efficiently.

---

## Boolean Expressions
Boolean expressions evaluate to either `True` or `False` and are commonly used in control structures like `if` and `while`.

- Relational operators include:  
  `<`, `>`, `<=`, `>=`, `==`, `!=`
- Boolean expressions usually involve variables rather than fixed values.

Examples include comparing numeric values, strings (alphabetical order), and even lists. Python allows comparisons only between compatible data types; otherwise, a runtime error occurs.

A common logical error occurs when comparing values of different data types, especially when using `input()` which always returns a string.

---

## Logical Operators
Logical operators are used to combine multiple Boolean expressions:

- `and` – True if both conditions are True  
- `or` – True if at least one condition is True  
- `not` – Reverses the Boolean value  

Parentheses are often used to make evaluation order clearer and to avoid logical mistakes. Python also allows **operator chaining**, which provides a cleaner way to write multiple comparisons.

---

## Membership Testing
Membership testing checks whether a value exists within a sequence such as a list or string.

- `in` checks if a value exists
- `not in` checks if a value does not exist

Membership tests can be applied to lists and strings and are often used as alternatives to relational expressions.

---

## The `if` Statement
The `if` statement enables **selection**, allowing code to run only when a condition is met.

- Code blocks are defined using indentation.
- Conditions typically use Boolean expressions.
- Only the indented block runs if the condition evaluates to `True`.

### `else` and `elif`
- `else` executes when the `if` condition is False.
- `elif` allows multiple conditions to be tested in sequence.
- Only one block in an `if-elif-else` chain executes.

Python also allows non-Boolean conditions, where:
- `0`, empty strings, and empty lists evaluate to `False`
- Non-zero values and non-empty sequences evaluate to `True`

However, using explicit Boolean expressions improves code clarity.

---

## Ternary Operator
The ternary operator is a concise, single-line alternative to an `if-else` statement.

Syntax:
```python
value_if_true if condition else value_if_false