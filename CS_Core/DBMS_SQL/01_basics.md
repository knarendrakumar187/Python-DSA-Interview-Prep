# DBMS 01 — Basics (Interview)

## What is DBMS?
Software to store, manage, and get data safely.  
Example: MySQL storing users, orders, products.

## Why not only files?
- Hard to search big data
- No multi-user safety
- No easy relationships
DBMS gives structure, query language (SQL), security, transactions.

## 3-tier idea (simple)
1. **Presentation** — UI/app
2. **Application** — backend logic
3. **Database** — MySQL/Postgres

Your Nyay Sahayak is similar: React → FastAPI → data/vector store.

## Keys (must know)
| Key | Meaning | Example |
|-----|---------|---------|
| Super key | any set that uniquely identifies row | (email), (email,phone) |
| Candidate key | minimal super key | email OR student_id |
| Primary key | chosen candidate key | student_id |
| Foreign key | link to another table PK | enrollments.student_id → students.id |
| Alternate key | candidate key not chosen as PK | email if id is PK |

## ER Model (1 line)
Entity = table idea (Student), Relationship = link (enrolls), Attribute = column (name).

## Speak answer
> DBMS manages data with tables, keys, and SQL. Primary key uniquely identifies a row. Foreign key connects tables and keeps links valid.

## Practice now
Explain out loud (60 sec): Primary key vs Foreign key with Students/Courses example.
