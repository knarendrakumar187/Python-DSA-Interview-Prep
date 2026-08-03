# DBMS 02 — SQL Joins (Interview Gold)

## JOIN meaning
Combine rows from 2 tables using matching column.

## Types (say with example)
Tables:
- students(id, name)
- enrollments(student_id, course)

**INNER JOIN** — only matching rows  
**LEFT JOIN** — all left rows + matches (NULL if no match)  
**RIGHT JOIN** — all right rows + matches  
**FULL OUTER** — all from both (MySQL support varies)

## Must-write query
```sql
SELECT s.name, e.course
FROM students s
INNER JOIN enrollments e
  ON s.id = e.student_id;
```

## Students with NO enrollment
```sql
SELECT s.name
FROM students s
LEFT JOIN enrollments e ON s.id = e.student_id
WHERE e.student_id IS NULL;
```

## Nested query vs JOIN
Both can solve many problems.  
JOIN is often clearer for combining tables.  
Subquery is useful for “value compared to a computed set”.

```sql
SELECT name FROM students
WHERE id IN (SELECT student_id FROM enrollments WHERE course = 'DBMS');
```

## Aggregate + GROUP BY
```sql
SELECT course, COUNT(*) AS cnt
FROM enrollments
GROUP BY course
HAVING COUNT(*) >= 2;
```

## Speak answer
> INNER JOIN returns only matches. LEFT JOIN keeps all left rows even if right side has no match. I use JOIN to connect students and enrollments on student_id.

## Practice
Write on paper (no peek):
1. Inner join student-course
2. Count students per course
3. Students with zero courses
