# Introduction to Programming – Week 4  
**Lab Logbook Summary**

## Overview
This lab focused on **functions** in Python and how they help structure programs through code reuse and abstraction. Topics included importing functions from modules, defining and documenting custom functions, handling arguments in flexible ways, and using lambda expressions. These concepts are essential for writing clean, modular, and maintainable programs.

---

## Importing and Using Functions
Python provides many **built-in functions** such as `print()`, `input()`, and `range()`. Additional functions are organised into **modules**, which must be imported before use.

Common ways to import functions include:
- Importing an entire module using `import module_name`
- Importing specific functions using `from module_name import function`
- Importing all contents using `from module_name import *` (not recommended in large programs)

The **math** module from the Python Standard Library was used to access mathematical functions such as `sqrt()` and `log2()`. Constants like `pi` can also be imported from modules.

---

## Defining Functions
Functions are defined using the `def` keyword, followed by:
- The function name
- A list of formal parameters
- An indented block of code

Functions allow repeated logic to be written once and reused multiple times. Parameters passed into functions act as **local variables**, meaning they are only accessible within the function’s scope.

---

## Docstrings and Documentation
Functions should be documented using **docstrings**, which are triple-quoted strings placed as the first line of the function body.

- Docstrings describe the purpose and behaviour of a function
- They are accessible using Python’s `help()` system
- Proper documentation improves readability and maintainability

---

## Returning Values
Functions can return values to the caller using the `return` statement.

- When `return` is executed, the function exits immediately
- If no return statement is provided, the function returns `None`
- Returned values can be stored in variables or used in expressions

---

## Default Arguments
Default argument values can be assigned to parameters in function definitions.

- Default arguments allow functions to be called with fewer parameters
- They must be placed after parameters without default values
- If an argument is omitted during a call, the default value is used

This makes functions more flexible and easier to use in common cases.

---

## Keyword Arguments
Functions can be called using **keyword arguments**, where parameter names are explicitly specified.

- Argument order does not matter when using keywords
- Required (non-default) parameters must still be provided
- Positional arguments must appear before keyword arguments

Keyword arguments improve clarity, especially when functions have many parameters.

---

## Arbitrary Length Argument Lists
Python allows functions to accept a variable number of arguments using `*args`.

- Arguments are collected into a tuple
- Useful when the number of inputs is unknown
- Commonly used for mathematical calculations and aggregation functions

Such parameters usually appear at the end of the function’s parameter list.

---

## Lambda Expressions
Lambda expressions define **small anonymous functions** using a single expression.

Syntax:
```python
lambda parameters : expression