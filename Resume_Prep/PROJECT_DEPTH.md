# Project Depth (Simple Interview Answers)

Your mock said: **needs more depth**.  
So answer with: **What → How → Why → Problem → Result**.

---

## 1) Nyay Sahayak (main project)

### Simple explanation
Nyay Sahayak is an AI legal helper for Indian law (BNS).  
User asks a question → we **search related law text** → then AI answers using that text.  
This is called **RAG** (Retrieval Augmented Generation).

### Why RAG? (say this)
If we only use LLM, it can invent wrong law.  
With RAG, answer is based on retrieved legal chunks, so it is safer.

### Flow (memorize)
1. User asks question (text/voice)
2. Login + role check (Firebase)
3. FastAPI backend searches ChromaDB
4. Top matching law pieces + question go to Groq LLM
5. Stream answer to UI

### Likely questions
**Q: What did YOU do?**  
A: Be honest and specific (RAG pipeline / auth roles / IPC-BNS mapping / deploy). Pick your real parts.

**Q: Hardest part?**  
A: Use STAR. Example: chunking legal text / role permissions / streaming latency.

**Q: What will you improve?**  
A: Better retrieval testing, show citations in UI, cache common queries.

---

## 2) GeoVerse AI

### Simple explanation
A world exploration website.  
Shows countries, weather, earthquakes, ISS data.  
Also gives AI travel plans. If AI key is missing, app still works with fallback.

### Good line
"I designed for reliability: API + CDN fallback, lazy routes, cached fetching."

---

## 3) AWS Intelligence Loop

### Simple explanation
Serverless pipeline:
API/S3 → Lambda → Amazon Comprehend (sentiment) → DynamoDB → QuickSight dashboard.

### Good line
"It processes 10k+ records/day. I focused on event-driven flow and monitoring."

### Be careful
If asked exact 200ms measurement, explain your test honestly. Don’t bluff.

---

## Extra depth phrases (use often)
- "The tradeoff was ..."
- "I chose X because ..."
- "A failure case is ..."
- "I would measure success by ..."
