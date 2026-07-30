"""Generate printable PDFs for Intro + Behavioural interview scripts."""

from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    ListFlowable,
    ListItem,
    HRFlowable,
)

OUT_DIR = Path(__file__).resolve().parent
NAVY = HexColor("#0F2C59")
TEAL = HexColor("#1F6F5B")
GRAY = HexColor("#333333")
LIGHT = HexColor("#F4F7FA")


def styles():
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "title",
            parent=base["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=18,
            textColor=NAVY,
            spaceAfter=6,
            leading=22,
        ),
        "subtitle": ParagraphStyle(
            "subtitle",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=10,
            textColor=TEAL,
            spaceAfter=14,
            leading=14,
        ),
        "h2": ParagraphStyle(
            "h2",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=13,
            textColor=NAVY,
            spaceBefore=12,
            spaceAfter=6,
            leading=16,
        ),
        "h3": ParagraphStyle(
            "h3",
            parent=base["Heading3"],
            fontName="Helvetica-Bold",
            fontSize=11,
            textColor=TEAL,
            spaceBefore=8,
            spaceAfter=4,
            leading=14,
        ),
        "body": ParagraphStyle(
            "body",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=10.5,
            textColor=GRAY,
            leading=15,
            spaceAfter=6,
        ),
        "script": ParagraphStyle(
            "script",
            parent=base["Normal"],
            fontName="Helvetica-Oblique",
            fontSize=10.5,
            textColor=GRAY,
            leading=16,
            leftIndent=8,
            rightIndent=8,
            spaceBefore=4,
            spaceAfter=8,
            backColor=LIGHT,
            borderPadding=8,
        ),
        "tip": ParagraphStyle(
            "tip",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=10,
            textColor=GRAY,
            leading=14,
            leftIndent=10,
            spaceAfter=3,
        ),
        "footer": ParagraphStyle(
            "footer",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8,
            textColor=HexColor("#666666"),
            alignment=1,
        ),
    }


def line():
    return HRFlowable(width="100%", thickness=1, color=HexColor("#D0D7E2"), spaceBefore=4, spaceAfter=8)


def bullets(items, st):
    return ListFlowable(
        [ListItem(Paragraph(i, st["tip"]), leftIndent=12, bulletColor=TEAL) for i in items],
        bulletType="bullet",
        start="•",
    )


def make_intro_pdf():
    path = OUT_DIR / "Narendra_Interview_Intro.pdf"
    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=0.7 * inch,
        rightMargin=0.7 * inch,
        topMargin=0.65 * inch,
        bottomMargin=0.65 * inch,
    )
    st = styles()
    story = []

    story.append(Paragraph("Tell Me About Yourself — Interview Scripts", st["title"]))
    story.append(Paragraph("Narendra Kumar · Placement Prep · Practice daily out loud", st["subtitle"]))
    story.append(line())

    story.append(Paragraph("Version A — Full Intro (90–110 seconds)", st["h2"]))
    story.append(Paragraph("Best for: HR / first round — “Tell me about yourself”", st["body"]))
    story.append(
        Paragraph(
            "Good morning, sir/ma’am. "
            "I’m <b>Narendra Kumar</b>, from Andhra Pradesh. I’m pursuing <b>B.Tech CSE at SRM University AP</b> "
            "with a CGPA of <b>8.51</b>, and I’m an <b>AWS Certified Cloud Practitioner</b>.",
            st["script"],
        )
    )
    story.append(
        Paragraph(
            "I come from a simple family — my father is a farmer, my mother is a homemaker, and I have one elder brother. "
            "Their support is a big reason I keep pushing myself.",
            st["script"],
        )
    )
    story.append(
        Paragraph(
            "In college, I focused on building real products, not only theory. My main project is <b>Nyay Sahayak</b>, "
            "an AI legal assistant that uses <b>RAG</b> to answer questions from the <b>Bharatiya Nyaya Sanhita</b>, "
            "with role-based access and IPC–BNS mapping for <b>550+ sections</b>. I also built <b>GeoVerse AI</b>, "
            "a world-exploration app with live APIs and AI itineraries, and <b>AWS Intelligence Loop</b>, "
            "a serverless sentiment pipeline on AWS that processes <b>10,000+ records a day</b>.",
            st["script"],
        )
    )
    story.append(
        Paragraph(
            "Outside academics, I have done <b>six national hackathons</b>, which improved my teamwork and speed under pressure. "
            "My hobby is <b>nature photography</b> — I run an Instagram page for my photos. It trains my eye for detail, "
            "and I bring that same detail-check habit into debugging and UI work.",
            st["script"],
        )
    )
    story.append(
        Paragraph(
            "I’m looking for a role where I can learn from strong engineers, grow in backend/full-stack or AI-backed products, "
            "and contribute from day one. Thank you.",
            st["script"],
        )
    )

    story.append(Paragraph("Why this intro works", st["h3"]))
    story.append(
        bullets(
            [
                "Personal, but family part is short",
                "Each project has one clear point",
                "Hobby linked to a work skill (attention to detail)",
                "Ends with what you want + what you give",
            ],
            st,
        )
    )

    story.append(Spacer(1, 8))
    story.append(Paragraph("Version B — Short Tech Intro (60–75 seconds)", st["h2"]))
    story.append(Paragraph("Best for: technical / coding rounds", st["body"]))
    story.append(
        Paragraph(
            "Hi, I’m <b>Narendra Kumar</b>, final-year CSE at SRM University AP, CGPA <b>8.51</b>, AWS Cloud Practitioner. "
            "I build with <b>Python, FastAPI, React, and AWS</b>. "
            "My strongest project is <b>Nyay Sahayak</b> — a production RAG legal assistant using ChromaDB and Groq, "
            "with role-based workflows and IPC↔BNS mapping. "
            "I’ve also shipped <b>GeoVerse AI</b> and an <b>AWS serverless sentiment pipeline</b> for 10k+ records/day. "
            "I enjoy turning ideas into working products, and I’m looking for an SDE / backend / full-stack role "
            "where I can keep learning and contribute.",
            st["script"],
        )
    )

    story.append(Paragraph("Delivery tips", st["h2"]))
    story.append(
        bullets(
            [
                "Smile once at the start",
                "Pause after each project name — don’t rush",
                "Don’t memorize like a robot — keep meaning, change small words",
                "If time is short, use Version B only",
            ],
            st,
        )
    )

    story.append(Paragraph("Practice checklist", st["h2"]))
    story.append(
        bullets(
            [
                "Version A under 2 minutes",
                "Version B under 75 seconds",
                "Can continue into Nyay Sahayak when they ask “tell me more”",
            ],
            st,
        )
    )

    story.append(Spacer(1, 16))
    story.append(Paragraph("Narendra Kumar · Interview Prep · Practice out loud daily", st["footer"]))
    doc.build(story)
    return path


def make_behavioural_pdf():
    path = OUT_DIR / "Narendra_Interview_Behavioural.pdf"
    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=0.7 * inch,
        rightMargin=0.7 * inch,
        topMargin=0.65 * inch,
        bottomMargin=0.65 * inch,
    )
    st = styles()
    story = []

    story.append(Paragraph("HR / Behavioural Answers — Interview Scripts", st["title"]))
    story.append(
        Paragraph(
            "Narendra Kumar · Unique answers in simple English · Speak naturally, not like a textbook",
            st["subtitle"],
        )
    )
    story.append(line())

    story.append(Paragraph("1) What is your strength?", st["h2"]))
    story.append(Paragraph("Say this", st["h3"]))
    story.append(
        Paragraph(
            "My strength is that I don’t stop at “it works on my laptop.” "
            "When I build something, I try to make it usable for real users — auth, fallback, deployment, and edge cases. "
            "For example, in <b>GeoVerse</b>, if the AI key is missing, the app still works with a local fallback. "
            "In <b>Nyay Sahayak</b>, I didn’t only connect an LLM — I added retrieval so answers stay grounded in law text. "
            "Hackathons also trained me to stay calm and ship under time pressure.",
            st["script"],
        )
    )
    story.append(Paragraph("Extra strength options", st["h3"]))
    story.append(
        bullets(
            [
                "Attention to detail → from photography + debugging",
                "Ownership → I take a feature from idea to deploy",
                "Learning speed → AWS cert + RAG stack learned by building",
            ],
            st,
        )
    )

    story.append(Paragraph("2) What is your weakness?", st["h2"]))
    story.append(Paragraph("Avoid: “I am a perfectionist” / “I work too hard”", st["body"]))
    story.append(Paragraph("Say this", st["h3"]))
    story.append(
        Paragraph(
            "Earlier, I used to understand topics only at the surface — I could explain the idea, "
            "but I struggled when interviewers went one level deeper. "
            "I saw this clearly in my mock interview feedback: “good understanding, needs more depth.” "
            "So now I changed my method. For DSA, I don’t just solve — I explain time/space and edge cases out loud. "
            "For projects, I prepare follow-up questions like tradeoffs and failure cases. "
            "I’m still improving, but my answers are more solid than before.",
            st["script"],
        )
    )

    story.append(Paragraph("3) Why should we hire you?", st["h2"]))
    story.append(Paragraph("Say this", st["h3"]))
    story.append(
        Paragraph(
            "You should hire me if you want someone who can learn fast and also deliver working software. "
            "I already have proof: a live RAG product, a multi-API React app, and an AWS serverless pipeline — "
            "plus an AWS Cloud Practitioner cert. "
            "I’m not coming only with theory. I’m coming with shipped projects, hackathon experience, "
            "and the hunger to go deeper every day. "
            "If you give me a chance, I’ll take ownership of tasks, ask clear questions, and improve quickly with feedback.",
            st["script"],
        )
    )
    story.append(Paragraph("Short version (30 sec)", st["h3"]))
    story.append(
        Paragraph(
            "I build and ship. I have live projects, cloud fundamentals, and strong willingness to go deep. "
            "I’ll contribute early and grow with the team.",
            st["script"],
        )
    )

    story.append(Paragraph("4) Why this company / this role?", st["h2"]))
    story.append(
        Paragraph(
            "I want to work on real users and real systems, not only college demos. "
            "Your company’s work in ________ interests me because ________. "
            "I can contribute with my Python/React/AWS base, and I want to learn production-quality engineering from your team.",
            st["script"],
        )
    )

    story.append(Paragraph("5) Where do you see yourself in 3–5 years?", st["h2"]))
    story.append(
        Paragraph(
            "In 3 years, I want to be a reliable engineer who can own a feature end-to-end — backend, quality, "
            "and basic design decisions. "
            "In 5 years, I want to mentor juniors and help design systems that stay simple, reliable, and measurable. "
            "Right now my focus is becoming strong in fundamentals and clean delivery.",
            st["script"],
        )
    )

    story.append(Paragraph("6) Tell me about a failure / challenge", st["h2"]))
    story.append(
        Paragraph(
            "Use one project difficulty (Nyay Sahayak RAG grounding / GeoVerse API fallback / AWS pipeline wiring). "
            "Then end with: <i>What I learned is: measure first, then fix. Don’t guess in production.</i>",
            st["body"],
        )
    )

    story.append(Paragraph("STAR reminder", st["h2"]))
    story.append(
        Paragraph(
            "<b>Situation → Task → Action (your action) → Result</b>",
            st["body"],
        )
    )

    story.append(Spacer(1, 16))
    story.append(Paragraph("Narendra Kumar · Interview Prep · Practice out loud daily", st["footer"]))
    doc.build(story)
    return path


if __name__ == "__main__":
    p1 = make_intro_pdf()
    p2 = make_behavioural_pdf()
    print("Created:")
    print(p1)
    print(p2)
