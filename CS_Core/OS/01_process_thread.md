# OS 01 — Process, Thread, Scheduling

## Process vs Thread (top question)
| | Process | Thread |
|--|---------|--------|
| Memory | separate | share process memory |
| Creation cost | heavier | lighter |
| Crash effect | usually isolated | can affect siblings |

Example: Chrome tabs ~ processes/isolation; one tab’s workers ~ threads.

## Process states (simple)
New → Ready → Running → Waiting → Terminated

**PCB:** Process Control Block stores process info (id, state, registers…).

**Context switch:** CPU saves one process state, loads another. Has overhead.

## Scheduling
**Preemptive:** can interrupt running process (Round Robin, modern OS)  
**Non-preemptive:** runs until waits/finishes (FCFS basic idea)

### Common algorithms
- **FCFS:** first come first serve — simple, convoy effect
- **SJF:** shortest job first — good average wait, hard to know burst time
- **Round Robin:** time quantum — fair for interactive
- **Priority:** higher priority first — starvation risk

## Speak answer
> Process has own memory; threads share memory inside a process. Round Robin gives each process a time slice so UI apps stay responsive.

## Practice
Explain: Why context switch has cost?
