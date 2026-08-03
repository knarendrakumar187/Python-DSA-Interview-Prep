# OS 02 — Sync + Deadlock

## Why synchronization?
Multiple threads share data → race condition (wrong final value).

Example: two threads do `count++` without lock → lost updates.

## Critical section
Code part that touches shared data. Only one thread should be inside at a time.

## Semaphore / Mutex (simple)
- **Mutex:** lock for mutual exclusion
- **Semaphore:** counter to control access (can allow N)

Classic problems (know names + idea):
- Producer-Consumer
- Readers-Writers

## Deadlock
Set of processes waiting forever for each other’s resources.

### 4 necessary conditions
1. Mutual exclusion  
2. Hold and wait  
3. No preemption  
4. Circular wait  

### Handling
- Prevention / avoidance (Banker’s algorithm idea)
- Detection + recovery (kill/rollback one)

## Speak answer
> Deadlock happens when processes wait for each other in a circle. Four conditions must hold. We prevent by breaking one condition, or detect and recover.

## Practice
Give real-life deadlock example (2 people, 2 keys).
