# OS 03 — Memory, Paging, Virtual Memory

## Why memory management?
Programs need memory; RAM is limited; OS shares it safely.

## Paging (simple)
Split memory into fixed-size **pages/frames**.  
Easy allocation, less external fragmentation.

## Segmentation
Split by logical parts (code, stack, heap). Variable size.

## Virtual memory
Program can use more memory than physical RAM.  
OS keeps some pages on disk.

## Page fault
Needed page not in RAM → OS loads from disk (slow).

## Page replacement (know names)
- FIFO
- LRU (Least Recently Used)
- Optimal (theoretical best)

**Belady’s anomaly:** more frames can sometimes increase faults in FIFO.

## Speak answer
> Virtual memory lets processes run even if not fully in RAM. Page fault means required page is on disk and must be loaded. LRU replaces the page unused for longest time.

## Practice
60-sec: Paging vs Segmentation.
