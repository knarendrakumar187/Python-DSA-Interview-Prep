# Project Depth + Difficulties (Interview Ready)

Answer pattern every time:  
**What I built → How it works → Difficulty I faced → What I did → Result / learning**

---

## 1) Nyay Sahayak — AI Legal Assistant (MAIN)

### 30-second pitch
> Nyay Sahayak is an AI legal assistant for Bharatiya Nyaya Sanhita.  
> User asks a question → we retrieve relevant law chunks from ChromaDB → Groq LLM answers using that context.  
> I also built role-based access for different users and IPC↔BNS mapping for 550+ sections.

### Why RAG?
> Pure LLM can invent law. RAG forces the answer to use retrieved legal text, so it is safer and more useful.

### Architecture (say in order)
1. React UI + Firebase Auth  
2. Role check (5 user types; Police-only FIR)  
3. FastAPI backend  
4. ChromaDB retrieval  
5. Groq generation (streamed response)  
6. Deploy: Vercel (frontend) + Render (backend)

### Difficulties faced (prepare 2–3)

**Difficulty 1 — Wrong / vague legal answers**  
- Problem: First version answered like ChatGPT, not always linked to correct BNS sections.  
- What I did: Switched to RAG, improved chunking of law text, and used retrieved context in the prompt.  
- Result: Answers became more grounded and section-aware.  
- Learning: For serious domains (law), retrieval quality matters more than fancy UI.

**Difficulty 2 — Role permissions getting mixed**  
- Problem: Different users needed different actions. FIR filing should be Police-only.  
- What I did: Designed role-based access and protected sensitive routes/features.  
- Result: Clear workflows for each user type.  
- Learning: Auth is not only login — it is also authorization.

**Difficulty 3 — IPC to BNS confusion**  
- Problem: People still search with old IPC numbers.  
- What I did: Built bidirectional IPC↔BNS mapping across 550+ official sections.  
- Result: Better section lookup accuracy.  
- Learning: Real users don’t speak in your data model; you must bridge old and new.

**Difficulty 4 — Voice + streaming complexity**  
- Problem: Voice input/output and streaming answers made debugging harder.  
- What I did: Separated concerns (STT/TTS vs RAG vs auth), tested each part alone, then connected.  
- Result: Feature worked without breaking core Q&A.  
- Learning: Complex features should be integrated step-by-step.

### Improve next
- Show citations in UI  
- Add retrieval quality tests  
- Cache common questions

---

## 2) GeoVerse AI — World Exploration App

### 30-second pitch
> GeoVerse is a React app for exploring the world with live data — countries, weather, earthquakes, ISS — plus AI travel itineraries.  
> I focused on speed and reliability with lazy loading, caching, and fallbacks.

### Difficulties faced

**Difficulty 1 — External APIs fail**  
- Problem: Public APIs sometimes go down or rate-limit.  
- What I did: Added CDN/local fallback paths so the app doesn’t fully break.  
- Result: Better uptime experience during outages.  
- Learning: Never trust one external API as a single point of failure.

**Difficulty 2 — AI feature blocked without API key**  
- Problem: Groq features failed for users without a key.  
- What I did: Built a local fallback so core AI-like experience still works.  
- Result: App remains usable in more situations.  
- Learning: Good products degrade gracefully.

**Difficulty 3 — App felt slow as pages grew**  
- Problem: Too much loading at once.  
- What I did: Lazy-loaded routes and cached fetches.  
- Result: Faster navigation.  
- Learning: Performance is a feature.

**Difficulty 4 — Too many features, risk of mess**  
- Problem: Rankings, quizzes, compare, dashboard — easy to make UI confusing.  
- What I did: Kept mobile-first layout and clear page separation.  
- Result: Feature-rich but still usable.  
- Learning: More features need more structure.

### Improve next
- Better offline handling  
- Stronger API error messages  
- Usage analytics

---

## 3) AWS Intelligence Loop — Serverless Sentiment Pipeline

### 30-second pitch
> It’s a serverless AWS pipeline: data comes in through API/S3, Lambda processes it, Amazon Comprehend finds sentiment, results go to DynamoDB, and QuickSight shows dashboards.  
> It was designed for high volume — 10,000+ records/day.

### Difficulties faced

**Difficulty 1 — Understanding service connections**  
- Problem: First time wiring Lambda + API Gateway + DynamoDB + Comprehend together was confusing.  
- What I did: Built one stage at a time, tested each with sample payloads, then connected the pipeline.  
- Result: End-to-end flow worked reliably.  
- Learning: In cloud, test each service boundary.

**Difficulty 2 — Cold starts / latency**  
- Problem: Serverless functions can be slow on first request.  
- What I did: Reduced unnecessary work in Lambda, kept payloads clean, monitored with CloudWatch.  
- Result: Improved response path toward our latency goal.  
- Learning: Measure before optimizing. Be honest about how you measured p99.

**Difficulty 3 — Manual analysis was slow**  
- Problem: Reading sentiment by hand across categories took too long.  
- What I did: Automated classification with Comprehend into 5 categories and visualized in QuickSight.  
- Result: Reporting dropped from days-style effort to minutes.  
- Learning: Automation has value only if dashboard/output is usable by humans.

**Difficulty 4 — Failure handling**  
- Problem: What if one record fails mid-pipeline?  
- What I did: Thought in terms of retries, logging, and not losing track of failed events.  
- Result: More trustworthy pipeline behavior.  
- Learning: In data pipelines, failure handling is part of the feature.

### Improve next
- Dead-letter queue for failed events  
- Better alerting  
- Cost dashboard

---

## Quick “hardest bug” answer (use in HR/tech)

> In Nyay Sahayak, the hardest issue was answers sounding confident but not always tied to the right legal section.  
> I fixed it by improving retrieval and forcing the model to use retrieved BNS context.  
> That taught me that in AI products, grounding is more important than fluent language.

---

## Phrases that impress (use naturally)
- “The tradeoff was …”
- “I chose X because …”
- “A failure case is …”
- “I measured success by …”
- “If I rebuild it, I would …”
