# DBMS 04 — SQL Practice (do on paper / any SQL editor)

## Tables to imagine
```text
students(id, name, city)
courses(id, title)
enrollments(student_id, course_id, marks)
```

## Write these (then check answers below)

1. All student names from Hyderabad  
2. Student name + course title  
3. Average marks per course  
4. Courses with average marks > 70  
5. Students not enrolled in any course  
6. Top marks in each course (student name + marks) — attempt ide

---

## Answers

```sql
-- 1
SELECT name FROM students WHERE city = 'Hyderabad';

-- 2
SELECT s.name, c.title
FROM students s
JOIN enrollments e ON s.id = e.student_id
JOIN courses c ON c.id = e.course_id;

-- 3
SELECT c.title, AVG(e.marks) AS avg_marks
FROM courses c
JOIN enrollments e ON c.id = e.course_id
GROUP BY c.title;

-- 4
SELECT c.title, AVG(e.marks) AS avg_marks
FROM courses c
JOIN enrollments e ON c.id = e.course_id
GROUP BY c.title
HAVING AVG(e.marks) > 70;

-- 5
SELECT s.name
FROM students s
LEFT JOIN enrollments e ON s.id = e.student_id
WHERE e.student_id IS NULL;
```

## Interview tip
If stuck, say:
1. which tables  
2. join key  
3. filter (WHERE)  
4. group (GROUP BY/HAVING)
