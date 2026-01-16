# Introduction to Programming – Week 6  
**Lab Logbook Summary: Lists, List Comprehensions & Tuples**

---

## Using List Methods  
- Lists are mutable sequences supporting indexing, slicing, concatenation, and iteration.  
- Common mutator methods:  
  - `append(value)`: Adds a single element to the end.  
  - `extend(iterable)`: Adds multiple elements from an iterable.  
  - `insert(index, value)`: Inserts a value at a specific position.  
  - `remove(value)`: Removes first occurrence of value; raises error if not found.  
  - `pop([index])`: Removes and returns last element by default or element at index.  
  - `clear()`: Removes all elements, leaving an empty list.  
  - `sort([key=func, reverse=bool])`: Sorts list in place; can sort by custom key or reverse order.  
  - `reverse()`: Reverses elements in place.  
- Accessor methods:  
  - `index(value, [start, end])`: Returns  index of value, optional search range.  
  - `count(value)`: Returns count of how many times value appears.  
  - `copy()`: Returns a shallow copy of the list.  
- The `del` statement can delete elements by index, slice, or delete entire variables.

---

## List Comprehensions  
- Provide a concise syntax to create lists programmatically:  
  ```python
  squares = [x*x for x in range(10)]