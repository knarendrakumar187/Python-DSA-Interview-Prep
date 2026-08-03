# DBMS 03 — Normalization + ACID + Transactions

## Normalization (why?)
Remove duplicate data → less inconsistency.

### Forms (interview level)
- **1NF:** atomic values (no lists in one cell)
- **2NF:** 1NF + no partial dependency on part of composite key
- **3NF:** 2NF + no transitive dependency (non-key → non-key)

Simple talk:
> We split big messy tables into smaller linked tables so updates don’t break data.

## Denormalization
Sometimes we add controlled redundancy for **read speed**.  
Tradeoff: faster reads, harder updates.

## ACID (must)
| Letter | Meaning | Bank example |
|--------|---------|--------------|
| A Atomicity | all or nothing | debit+credit both happen or none |
| C Consistency | rules stay valid | total money conserved |
| I Isolation | concurrent txns don’t mess each other | two transfers safe |
| D Durability | committed data survives crash | after commit, data stays |

## Schedule / concurrency (short)
Many transactions run together.  
Need locking / isolation so results stay correct.  
**Conflict serializability** = concurrent schedule equal to some serial order.

## Deadlock in DBMS
Two transactions wait for each other’s locks forever.  
Handle by detection + rollback, or prevention.

## Index (extra must)
Speeds SELECT/WHERE/JOIN. Slightly slows INSERT/UPDATE.  
Like book index.

## Speak answer
> ACID makes transactions reliable. Atomicity means transfer fully succeeds or fully fails. Normalization reduces duplication; indexing speeds reads.

## Practice
60-sec speech: ACID with UPI payment example.
