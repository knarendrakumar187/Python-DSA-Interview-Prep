# CS Core — Simple Interview Answers

Don’t give only definitions. Give **one small example**.

---

## DBMS / SQL

**Primary Key:** unique id of a row (student_id).  
**Foreign Key:** link to another table (student_id in enrollments).

**Index:** makes SELECT faster, INSERT a bit slower.  
Example: index on email for login lookup.

**JOIN example**
```sql
SELECT s.name, c.title
FROM students s
JOIN enrollments e ON s.id = e.student_id
JOIN courses c ON c.id = e.course_id;
```

**ACID (bank transfer):** all steps succeed, or none.

---

## OOP (Python)

1. **Encapsulation:** hide data with methods  
2. **Abstraction:** show only needed details  
3. **Inheritance:** Child gets Parent features  
4. **Polymorphism:** same method name, different behavior

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "bark"
```

---

## OS

**Process vs Thread:**  
Process = separate program memory.  
Thread = lighter workers sharing memory inside a process.

**Deadlock:** 4 conditions (mutual exclusion, hold&wait, no preemption, circular wait).  
Simple example: 2 people each hold one key and wait for the other.

---

## CN

**TCP:** reliable (files, web)  
**UDP:** fast, less reliable (live video calls often)

**HTTP vs HTTPS:** HTTPS = HTTP + TLS encryption  
**DNS:** converts google.com → IP address

---

## Practice style
For every answer: **definition + tiny example + why companies care**
