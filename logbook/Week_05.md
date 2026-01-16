# Introduction to Programming – Week 5  
**Scripts and Modules – Lab Logbook Summary**

## Overview
This lab introduced the use of Python scripts and modules, explaining how Python programs are stored in files and executed from the operating system. The session focused on the difference between interactive mode and script execution, the use of command-line arguments, importing modules, and understanding how Python locates and manages external code. These concepts are essential for structuring larger programs and enabling code reuse.

---

## Python Scripts
A Python script is a program stored in a text file with the `.py` file extension. Scripts are executed from a terminal or command prompt rather than entered line-by-line into the Python interpreter.

Unlike interactive mode, Python scripts do not automatically display the result of expressions. Output must be explicitly displayed using the `print()` function. This reinforces the importance of controlling program output within scripts.

Scripts can be written using any text editor; a specialised Integrated Development Environment (IDE) is not required, although IDEs can provide useful features such as syntax highlighting and debugging tools.

---

## Executing Scripts and Command-Line Arguments
Python scripts are executed from the terminal using the Python interpreter. Additional values can be passed to a script at runtime using command-line arguments.

Command-line arguments are accessed using the `sys` module. The `sys.argv` variable stores these arguments as a list of strings:
- The first element contains the script name
- Subsequent elements contain arguments provided by the user

Using command-line arguments allows programs to behave differently depending on user input without modifying the source code.

---

## Using the sys Module
The `sys` module provides access to system-specific variables and functions. Importing this module enables scripts to read command-line arguments and interact with the execution environment.

The length of `sys.argv` can be checked to ensure that required arguments have been provided. Conditional statements can then be used to handle missing input gracefully, improving program robustness.

---

## Importing Modules and Aliases
Python supports importing entire modules or specific components from a module. Modules can also be assigned aliases to shorten names or avoid conflicts with existing identifiers.

Selective imports improve code clarity and efficiency by importing only what is required. Using wildcard imports is discouraged because it can lead to naming conflicts and reduce readability.

---

## Symbol Tables and Name Management
Python uses symbol tables to keep track of names and the objects they reference. Each module has its own symbol table, which helps prevent conflicts and supports modular programming.

The `dir()` function can be used in interactive mode to list all names defined within a module, assisting with exploration and debugging.

---

## Module Search Path
The `sys.path` variable defines the list of directories that Python searches when importing modules. Understanding this search path is important when working with custom modules or resolving import errors.

---

## The __name__ Variable
The special variable `__name__` is automatically assigned by Python. When a program is run as a script, `__name__` is set to `"__main__"`. When the same file is imported as a module, `__name__` is set to the module’s name.

This feature allows programs to detect how they are being used and ensures that certain code executes only when intended.

---

## Conclusion
This lab strengthened understanding of how Python programs are structured and executed. By learning how to create scripts, use command-line arguments, import modules, and manage namespaces, important skills were developed for building scalable, reusable, and well-organised Python applications. These concepts are fundamental for progressing to more complex programming tasks.