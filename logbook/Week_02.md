# Introduction to Programming – Week 2  
**Lab Logbook Summary**

## Overview
This lab built upon the foundational concepts introduced in Week 1 by focusing on how Python stores and manipulates data. The session covered working with variables, understanding data types, using built-in functions, handling strings with different types of quotes, performing indexing and slicing operations, and introducing lists. These concepts are essential for managing data and writing meaningful Python programs.

---

## Working with Variables
Variables are used to store values so they can be reused later in a program. Each variable is identified by a name chosen by the programmer, which should be meaningful and descriptive.

Key rules for variable names:
- Must begin with a letter or underscore
- Can contain letters, digits, and underscores
- Are case-sensitive (`age`, `Age`, and `AGE` are different variables)
- Should be descriptive to improve code readability

Variables are created using the **assignment operator (`=`)**, which assigns the value on the right-hand side to the variable  on the left-hand side. Variables must be assigned a value before they can be used.

---

## Assignment and Augmented Assignment
The assignment operator has low precedence, meaning expressions on the right-hand side are evaluated before assignment.

Python supports **augmented assignment operators**, which provide a shorter way to update a variable using its current value:
- `+=`, `-=`, `*=`, `/=`

These operators improve clarity and reduce repetition when modifying variables.

---

## Data Types
All values in Python have a data type, which determines how operations are applied to them.

Common primitive data types include:
- `int` – whole numbers
- `float` – decimal numbers
- `bool` – Boolean values (`True` or `False`)
- `str` – text data

Python uses **dynamic typing**, meaning a variable’s data type is determined by the value it currently holds and can change during execution. The `type()` function was used to identify the data type of values, variables, and expressions.

The importance of data types was demonstrated through operator behaviour, such as:
- Numeric addition with `+`
- String concatenation when `+` is applied to strings
- String repetition using the `*` operator

---

## Built-in Functions
Python provides many built-in functions that perform common tasks.

Functions are called using their name followed by parentheses, which may contain arguments.

Examples used in this lab include:
- `print()` – displays output to the screen
- `len()` – returns the length of a string or list
- `type()` – returns the data type of a value
- `input()` – reads input from the user as a string

Some functions return values, which can be stored in variables or used within expressions. Nested function calls were also demonstrated.

---

## User Input and Type Conversion
The `input()` function always returns a string, even when numeric input is entered. This can cause errors when performing arithmetic operations.

To resolve this, type conversion functions such as `int()` were used to convert string input into numeric values. This allowed correct mathematical operations to be performed on user input.

---

## Strings and Quotes
Strings can be defined using:
- Single quotes (`' '`)
- Double quotes (`" "`)
- Triple quotes (`""" """`)

Using different quote types allows quotes to appear inside strings without errors.

### Escape Sequences
Escape sequences were used to represent special characters within strings, including:
- `\n` for new lines
- `\t` for tabs
- `\\` for backslashes
- `\"` and `\'` for quotes

### Triple-Quoted Strings
Triple-quoted strings allow multi-line text and the inclusion of quotes without using escape sequences. These are commonly used for multi-line output and documentation.

---

## Indexing and Slicing
Strings are sequences of characters and support indexing and slicing operations.

### Indexing
- Uses zero-based indexing
- Allows access to individual characters
- Supports negative indices to count from the end of the string

### Slicing
- Extracts a range of characters
- Uses the format `[start:end]`
- Start index is inclusive, end index is exclusive
- Supports omitted indices and negative values
- Out-of-range indices do not cause errors

---

## Introduction to Lists
Lists are ordered collections of values enclosed in square brackets.

Key characteristics of lists:
- Can store multiple values
- Can contain duplicate elements
- Support indexing and slicing
- Support concatenation (`+`) and repetition (`*`)

Lists can store values of any data type, although they typically contain values of the same type.

---

## Mutable and Immutable Types
A key difference between strings and lists is mutability.

- **Strings are immutable**: they cannot be changed after creation
- **Lists are mutable**: their contents can be modified

List elements can be updated using indexing, slicing, or the `append()` method. Slicing can also be used to insert or remove multiple elements. Augmented assignment (`+=`) mutates lists, while standard concatenation creates a new list.

---

## Key Terminology
This lab reinforced understanding of important programming terms, including:
- Assignment
- Data type
- Argument
- Indexing
- Slicing
- Mutable
- Immutable

---

## Conclusion
This lab developed essential skills for handling data in Python. By learning how to work with variables, data types, strings, and lists, and understanding mutability and built-in functions, a strong foundation was established for more advanced programming concepts in later lab sessions.