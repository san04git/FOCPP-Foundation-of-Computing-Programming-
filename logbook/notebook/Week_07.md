# Introduction to Programming – Week 7  
**Lab Logbook Summary: Sets and Dictionaries**

---

## Introducing Sets  
- Sets are unordered collections of unique, immutable elements.  
- Sets themselves are mutable (regular `set`), but elements must be immutable (e.g., no lists inside sets).  
- Sets do not support indexing or slicing because they are unordered.  
- Sets excel at fast membership testing (`in` and `not in`).  
- Create sets with curly braces `{}` or the `set()` constructor:  
  ```python
  vowels = {"a", "e", "i", "o", "u"}
  names = set(["John", "Eric", "Terry", "Michael", "Graham", "Terry"])