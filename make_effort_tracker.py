from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from pathlib import Path

wb = Workbook()

header_fill = PatternFill("solid", fgColor="0F2C59")
header_font = Font(bold=True, color="FFFFFF", size=11, name="Calibri")
title_font = Font(bold=True, size=14, color="0F2C59", name="Calibri")
must_fill = PatternFill("solid", fgColor="FCE4D6")
lite_fill = PatternFill("solid", fgColor="FFF2CC")
blue_fill = PatternFill("solid", fgColor="DDEBF7")
thin = Border(
    left=Side(style="thin", color="B0B0B0"),
    right=Side(style="thin", color="B0B0B0"),
    top=Side(style="thin", color="B0B0B0"),
    bottom=Side(style="thin", color="B0B0B0"),
)
wrap = Alignment(wrap_text=True, vertical="center")
center = Alignment(wrap_text=True, vertical="center", horizontal="center")


def autosize(ws, widths):
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w


def add_status_dv(ws, col, max_row, options='"Not Started,In Progress,Done"'):
    dv = DataValidation(type="list", formula1=options, allow_blank=True)
    ws.add_data_validation(dv)
    dv.add(f"{col}2:{col}{max_row}")


# -------------------- 00 Read me --------------------
ws0 = wb.active
ws0.title = "00_Read_Me_First"
ws0["A1"] = "HOW TO USE THIS SHEET — NARENDRA INTERVIEW EFFORT TRACKER"
ws0["A1"].font = title_font
lines = [
    "",
    "Interview Date: 16 Aug 2026",
    "This Excel is your ONLY checklist for the next 3 days. Do not invent new syllabus.",
    "",
    "SHEETS:",
    "1) 01_Master_Plan_13to16  -> main day-wise tasks. Change Status dropdown to Done.",
    "2) 02_DSA_Must_Problems   -> 12 key problems. Write brute + optimal. Mark coded/explain.",
    "3) 03_Resume_HR_Speak     -> speak out loud. Mark Yes when you can do without notes.",
    "4) 04_CS_Core_Flash       -> short CS answers with examples.",
    "5) 05_Interview_Day_16    -> use only on interview morning.",
    "",
    "EFFORT RULES:",
    "- Mark Done only if you can explain out loud (not if you only read).",
    "- For every DSA problem: Brute idea + Optimal code + Time/Space.",
    "- Target before 16 Aug morning: finish almost all MUST rows.",
    "",
    "LOCAL FOLDER:",
    r"E:\sems\sem 7\Python DSA",
    "Intro PDF: Resume_Prep\\Narendra_Interview_Intro.pdf",
    "HR PDF: Resume_Prep\\Narendra_Interview_Behavioural.pdf",
    "GitHub: https://github.com/knarendrakumar187/Python-DSA-Interview-Prep",
    "",
    "START NOW: open sheet 01_Master_Plan_13to16 and do Task #1 (Two Sum).",
    "Mindset: You do not need perfection. You need calm clarity + honest effort.",
]
for i, line in enumerate(lines, 2):
    ws0.cell(i, 1, line)
ws0.column_dimensions["A"].width = 115

# -------------------- 01 Master plan --------------------
ws1 = wb.create_sheet("01_Master_Plan_13to16")
ws1["A1"] = "NARENDRA — INTERVIEW EMERGENCY PLAN (13 Aug night → 16 Aug)"
ws1["A1"].font = title_font
ws1.merge_cells("A1:I1")
ws1["A2"] = "Goal: Perform better (not perfect) | Formula: Clarify → Example → Brute → Better → Code → Time/Space"
ws1["A2"].font = Font(italic=True, size=10, color="333333")
ws1.merge_cells("A2:I2")

headers1 = ["#", "Date", "Time Block", "Task", "Category", "Priority", "Est. Min", "Status", "Notes / Proof"]
for c, h in enumerate(headers1, 1):
    cell = ws1.cell(3, c, h)
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = center
    cell.border = thin

tasks = [
    [1, "Thu 13 Aug", "Night 1", "Solve Two Sum (brute + hash map)", "DSA", "MUST", 25, "Not Started", "Day01_02_Arrays/Day01_problems.py"],
    [2, "Thu 13 Aug", "Night 1", "Solve Contains Duplicate", "DSA", "MUST", 15, "Not Started", ""],
    [3, "Thu 13 Aug", "Night 1", "Solve Best Time to Buy/Sell Stock", "DSA", "MUST", 20, "Not Started", ""],
    [4, "Thu 13 Aug", "Night 1", "Solve Valid Parentheses", "DSA", "MUST", 20, "Not Started", "Day07_Stack_Queue/Day07_problems.py"],
    [5, "Thu 13 Aug", "Night 2", "Speak Intro Version B 3 times (timer)", "Resume", "MUST", 15, "Not Started", "Resume_Prep/INTRO.md or PDF"],
    [6, "Thu 13 Aug", "Night 2", "Speak Nyay Sahayak: What + RAG + 1 difficulty", "Resume", "MUST", 20, "Not Started", "PROJECT_DEPTH.md"],
    [7, "Thu 13 Aug", "Night 2", "CS: PK vs FK + INNER vs LEFT JOIN (speak)", "CS Core", "MUST", 20, "Not Started", "CS_Core/DBMS_SQL"],
    [8, "Thu 13 Aug", "Night 2", "CS: Process vs Thread (speak with example)", "CS Core", "MUST", 10, "Not Started", "CS_Core/OS"],
    [9, "Fri 14 Aug", "Morning", "Move Zeroes (in-place idea)", "DSA", "MUST", 20, "Not Started", ""],
    [10, "Fri 14 Aug", "Morning", "Valid Palindrome (two pointers)", "DSA", "MUST", 20, "Not Started", "Day04_Two_Pointers"],
    [11, "Fri 14 Aug", "Morning", "Longest Substring Without Repeating (try)", "DSA", "MUST", 35, "Not Started", "Day05 - explain if stuck"],
    [12, "Fri 14 Aug", "Morning", "Reverse Linked List + explain pointers", "DSA", "MUST", 30, "Not Started", "Day08_LinkedList"],
    [13, "Fri 14 Aug", "Morning", "Binary Search template from memory", "DSA", "MUST", 25, "Not Started", "Day10"],
    [14, "Fri 14 Aug", "Afternoon", "Max Depth of Binary Tree", "DSA", "MUST", 25, "Not Started", "Day11_Trees"],
    [15, "Fri 14 Aug", "Afternoon", "Timed drill: 2 Easy problems in 40 min", "DSA Mock", "MUST", 40, "Not Started", "Use phone timer"],
    [16, "Fri 14 Aug", "Afternoon", "Review fails + rewrite once", "DSA", "MUST", 40, "Not Started", "Write fails in Notes"],
    [17, "Fri 14 Aug", "Evening", "Intro Version A full (under 2 min)", "Resume", "MUST", 15, "Not Started", ""],
    [18, "Fri 14 Aug", "Evening", "GeoVerse 1-min pitch + 1 difficulty", "Resume", "SHOULD", 15, "Not Started", ""],
    [19, "Fri 14 Aug", "Evening", "AWS pipeline 1-min pitch + 1 difficulty", "Resume", "SHOULD", 15, "Not Started", ""],
    [20, "Fri 14 Aug", "Evening", "HR: Strength + Weakness + Why hire you", "HR", "MUST", 20, "Not Started", "BEHAVIOURAL.md / PDF"],
    [21, "Fri 14 Aug", "Evening", "CS: ACID (UPI example)", "CS Core", "MUST", 15, "Not Started", ""],
    [22, "Fri 14 Aug", "Evening", "CS: Deadlock 4 conditions + example", "CS Core", "MUST", 15, "Not Started", ""],
    [23, "Fri 14 Aug", "Evening", "CS: TCP vs UDP + HTTP vs HTTPS + DNS", "CS Core", "MUST", 20, "Not Started", ""],
    [24, "Fri 14 Aug", "Evening", "OOP 4 pillars with tiny Python example", "CS Core", "SHOULD", 15, "Not Started", "CS_Core/OOP.md"],
    [25, "Sat 15 Aug", "Morning", "Re-solve ONLY failed DSA problems", "DSA", "MUST", 90, "Not Started", "No new topics"],
    [26, "Sat 15 Aug", "Afternoon", "FULL MOCK: Intro -> 2 DSA -> Nyay -> CS -> HR", "Mock", "MUST", 75, "Not Started", "Day14_FULL_MOCK_SCRIPT.md"],
    [27, "Sat 15 Aug", "Afternoon", "Write top 5 weak answers + fix same day", "Mock", "MUST", 45, "Not Started", ""],
    [28, "Sat 15 Aug", "Evening", "Flash: CHEATSHEET + CS QUICK_REVISE", "Revise", "MUST", 30, "Not Started", ""],
    [29, "Sat 15 Aug", "Evening", "Final speak: Intro + Nyay + Why hire you", "Resume", "MUST", 20, "Not Started", ""],
    [30, "Sat 15 Aug", "Night", "Sleep early (before 11). No new coding.", "Health", "MUST", 0, "Not Started", "Critical"],
    [31, "Sun 16 Aug", "Morning", "15 min only: Intro + Nyay Sahayak", "Interview Day", "MUST", 15, "Not Started", "No new DSA"],
    [32, "Sun 16 Aug", "Morning", "Keep water, resume PDF, calm breath", "Interview Day", "MUST", 10, "Not Started", ""],
    [33, "Sun 16 Aug", "Interview", "Use: Clarify->Example->Brute->Better->Code->Complexity", "Interview Day", "MUST", 0, "Not Started", "Keep in mind"],
]

for i, row in enumerate(tasks):
    r = 4 + i
    for c, val in enumerate(row, 1):
        cell = ws1.cell(r, c, val)
        cell.border = thin
        cell.alignment = wrap if c in (4, 9) else center
        if row[5] == "MUST":
            ws1.cell(r, 6).fill = must_fill
        if "16 Aug" in str(row[1]):
            ws1.cell(r, 2).fill = blue_fill
        if row[1] == "Sat 15 Aug" and row[2] == "Night":
            ws1.cell(r, 2).fill = lite_fill
    ws1.row_dimensions[r].height = 30

add_status_dv(ws1, "H", 3 + len(tasks))
# fix range - status starts at row 4
ws1.data_validations.dataValidation[-1].sqref = f"H4:H{3+len(tasks)}"

autosize(ws1, [5, 14, 12, 58, 12, 10, 10, 14, 34])
ws1.freeze_panes = "A4"
ws1.auto_filter.ref = f"A3:I{3+len(tasks)}"

sum_row = 4 + len(tasks) + 1
ws1.cell(sum_row, 1, "PROGRESS").font = Font(bold=True, color="0F2C59")
ws1.cell(sum_row, 2, "Count Done")
ws1.cell(sum_row, 3, f'=COUNTIF(H4:H{3+len(tasks)},"Done")')
ws1.cell(sum_row + 1, 2, "Total Tasks")
ws1.cell(sum_row + 1, 3, len(tasks))
ws1.cell(sum_row + 2, 2, "Target")
ws1.cell(sum_row + 2, 3, "At least 25 Done (all MUST preferred)")

# -------------------- 02 DSA --------------------
ws2 = wb.create_sheet("02_DSA_Must_Problems")
ws2["A1"] = "DSA MUST LIST — For each: Brute idea + Optimal code + Time/Space"
ws2["A1"].font = title_font
ws2.merge_cells("A1:H1")

h2 = ["#", "Problem", "Pattern", "Brute Idea (write)", "Optimal Idea (write)", "Coded?", "Can Explain T/S?", "Status"]
for c, h in enumerate(h2, 1):
    cell = ws2.cell(2, c, h)
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = center
    cell.border = thin

dsa = [
    [1, "Two Sum", "Hash Map", "All pairs O(n^2)", "Dict value->index O(n)", "No", "No", "Not Started"],
    [2, "Contains Duplicate", "Hash Set", "Nested loop", "set / len compare", "No", "No", "Not Started"],
    [3, "Best Time Buy/Sell Stock", "One pass", "All pairs", "Track min price", "No", "No", "Not Started"],
    [4, "Move Zeroes", "Two pointers", "Extra array", "Write pointer in-place", "No", "No", "Not Started"],
    [5, "Valid Parentheses", "Stack", "Wrong count-only", "Stack match pairs", "No", "No", "Not Started"],
    [6, "Valid Palindrome", "Two pointers", "Clean + reverse", "L/R ignore non-alnum", "No", "No", "Not Started"],
    [7, "Longest Substring No Repeat", "Sliding Window", "All substrings", "Window + last seen", "No", "No", "Not Started"],
    [8, "Reverse Linked List", "Pointers", "Copy values", "prev/curr/next", "No", "No", "Not Started"],
    [9, "Binary Search", "Divide & conquer", "Linear scan", "mid cut half O(log n)", "No", "No", "Not Started"],
    [10, "Max Depth Binary Tree", "DFS recursion", "BFS levels also ok", "1+max(left,right)", "No", "No", "Not Started"],
    [11, "Majority Element (bonus)", "Hashing", "Count dict", "Counter", "No", "No", "Not Started"],
    [12, "First Unique Char (bonus)", "Hashing", "Nested scan", "Counter then scan", "No", "No", "Not Started"],
]

for i, row in enumerate(dsa):
    r = 3 + i
    for c, val in enumerate(row, 1):
        cell = ws2.cell(r, c, val)
        cell.border = thin
        cell.alignment = wrap
    ws2.row_dimensions[r].height = 36

for col, opts in [("F", '"No,Yes"'), ("G", '"No,Yes"'), ("H", '"Not Started,In Progress,Done"')]:
    dv = DataValidation(type="list", formula1=opts, allow_blank=True)
    ws2.add_data_validation(dv)
    dv.add(f"{col}3:{col}{2+len(dsa)}")

autosize(ws2, [5, 30, 16, 26, 26, 10, 16, 14])
ws2.freeze_panes = "A3"
ws2.cell(16, 1, "INTERVIEW SPEAK TEMPLATE").font = Font(bold=True, color="0F2C59")
ws2.cell(17, 1, "1 Clarify   2 Example   3 Brute + complexity   4 Optimal + complexity   5 Code   6 Edge cases")
ws2.merge_cells("A17:H17")

# -------------------- 03 Resume HR --------------------
ws3 = wb.create_sheet("03_Resume_HR_Speak")
ws3["A1"] = "RESUME + HR — Speak out loud (mark Yes only if without notes)"
ws3["A1"].font = title_font
ws3.merge_cells("A1:F1")

h3 = ["#", "Item", "What to cover", "Target Time", "Spoken without notes?", "Status"]
for c, h in enumerate(h3, 1):
    cell = ws3.cell(2, c, h)
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = center
    cell.border = thin

resume = [
    [1, "Intro Version B (short)", "Name, college, CGPA, AWS cert, 3 projects short, role", "60-75 sec", "No", "Not Started"],
    [2, "Intro Version A (full)", "Family short + projects + hackathons + photography + close", "90-110 sec", "No", "Not Started"],
    [3, "Nyay Sahayak depth", "RAG flow, ChromaDB+Groq, roles, IPC-BNS, 1 difficulty, next improve", "3 min", "No", "Not Started"],
    [4, "What is RAG?", "Retrieve then generate; safer than pure LLM", "45 sec", "No", "Not Started"],
    [5, "GeoVerse pitch", "4 APIs, LLM itinerary, fallback, lazy load", "60 sec", "No", "Not Started"],
    [6, "AWS Intelligence Loop", "Lambda+Comprehend+DynamoDB+QuickSight + 1 difficulty", "60 sec", "No", "Not Started"],
    [7, "Strength", "Ship usable products + calm under hackathon pressure", "45 sec", "No", "Not Started"],
    [8, "Weakness", "Was surface-level; now practice depth (DSA+project followups)", "45 sec", "No", "Not Started"],
    [9, "Why hire you?", "Learn fast + shipped projects + AWS cert + ownership", "45 sec", "No", "Not Started"],
    [10, "STAR hardest bug", "Nyay ungrounded answers -> RAG fix -> learning", "60-90 sec", "No", "Not Started"],
    [11, "Where in 3-5 years?", "Own features end-to-end; later mentor; now fundamentals", "40 sec", "No", "Not Started"],
]

for i, row in enumerate(resume):
    r = 3 + i
    for c, val in enumerate(row, 1):
        cell = ws3.cell(r, c, val)
        cell.border = thin
        cell.alignment = wrap
    ws3.row_dimensions[r].height = 40

for col, opts in [("E", '"No,Yes"'), ("F", '"Not Started,In Progress,Done"')]:
    dv = DataValidation(type="list", formula1=opts, allow_blank=True)
    ws3.add_data_validation(dv)
    dv.add(f"{col}3:{col}{2+len(resume)}")

autosize(ws3, [5, 28, 72, 12, 22, 14])

# -------------------- 04 CS --------------------
ws4 = wb.create_sheet("04_CS_Core_Flash")
ws4["A1"] = "CS CORE — Answer format: Definition + Example + Why companies care"
ws4["A1"].font = title_font
ws4.merge_cells("A1:F1")

h4 = ["#", "Subject", "Question", "Keywords for your answer", "Can speak?", "Status"]
for c, h in enumerate(h4, 1):
    cell = ws4.cell(2, c, h)
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = center
    cell.border = thin

cs = [
    [1, "DBMS", "Primary key vs Foreign key", "PK unique row; FK links tables (student_id)", "No", "Not Started"],
    [2, "DBMS", "INNER JOIN vs LEFT JOIN", "INNER = matches only; LEFT = all left + matches", "No", "Not Started"],
    [3, "DBMS", "ACID with UPI example", "Atomic Consistency Isolation Durability", "No", "Not Started"],
    [4, "DBMS", "Index upside/downside", "Faster SELECT; slower writes", "No", "Not Started"],
    [5, "DBMS", "Normalization simple meaning", "Reduce duplicate/inconsistent data", "No", "Not Started"],
    [6, "OS", "Process vs Thread", "Process own memory; threads share memory", "No", "Not Started"],
    [7, "OS", "Deadlock 4 conditions", "ME, hold&wait, no preempt, circular wait", "No", "Not Started"],
    [8, "OS", "Virtual memory / page fault", "Disk as extra mem; fault loads page", "No", "Not Started"],
    [9, "CN", "TCP vs UDP", "TCP reliable; UDP fast", "No", "Not Started"],
    [10, "CN", "HTTP vs HTTPS", "HTTPS = HTTP + TLS", "No", "Not Started"],
    [11, "CN", "DNS role", "Domain -> IP", "No", "Not Started"],
    [12, "OOP", "4 pillars + example", "Encapsulation Abstraction Inheritance Polymorphism", "No", "Not Started"],
    [13, "SE", "Agile vs Waterfall", "Sprints+feedback vs fixed stages", "No", "Not Started"],
    [14, "SQL", "Write one JOIN + GROUP BY", "Practice from CS_Core/DBMS_SQL/04_sql_practice.md", "No", "Not Started"],
]

for i, row in enumerate(cs):
    r = 3 + i
    for c, val in enumerate(row, 1):
        cell = ws4.cell(r, c, val)
        cell.border = thin
        cell.alignment = wrap
    ws4.row_dimensions[r].height = 34

for col, opts in [("E", '"No,Yes"'), ("F", '"Not Started,In Progress,Done"')]:
    dv = DataValidation(type="list", formula1=opts, allow_blank=True)
    ws4.add_data_validation(dv)
    dv.add(f"{col}3:{col}{2+len(cs)}")

autosize(ws4, [5, 10, 36, 58, 12, 14])

# -------------------- 05 Interview day --------------------
ws5 = wb.create_sheet("05_Interview_Day_16")
ws5["A1"] = "16 AUG INTERVIEW DAY CHECKLIST"
ws5["A1"].font = title_font
ws5.merge_cells("A1:D1")

h5 = ["#", "Checklist", "Status", "Notes"]
for c, h in enumerate(h5, 1):
    cell = ws5.cell(2, c, h)
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = center
    cell.border = thin

day = [
    [1, "Sleep well night before", "Not Started", ""],
    [2, "Light breakfast + water", "Not Started", ""],
    [3, "Resume PDF/print ready", "Not Started", ""],
    [4, "Laptop/network ready if online", "Not Started", ""],
    [5, "15 min revise: Intro + Nyay only (no new coding)", "Not Started", ""],
    [6, "Reach early / join link 10 min early", "Not Started", ""],
    [7, "Greet calmly and smile once", "Not Started", ""],
    [8, "DSA formula: Clarify -> Example -> Brute -> Better -> Code -> T/S", "Not Started", ""],
    [9, "If stuck: say brute force first, then optimize", "Not Started", ""],
    [10, "Be honest on any resume metric you are unsure about", "Not Started", ""],
    [11, "Ask 1 good question at end (team stack / mentorship)", "Not Started", ""],
]

for i, row in enumerate(day):
    r = 3 + i
    for c, val in enumerate(row, 1):
        cell = ws5.cell(r, c, val)
        cell.border = thin
        cell.alignment = wrap
    ws5.row_dimensions[r].height = 28

dv5 = DataValidation(type="list", formula1='"Not Started,Done"', allow_blank=True)
ws5.add_data_validation(dv5)
dv5.add(f"C3:C{2+len(day)}")
autosize(ws5, [5, 75, 14, 28])
ws5.cell(16, 1, "AFTER INTERVIEW").font = Font(bold=True, color="0F2C59")
ws5.cell(17, 1, "Write questions asked + mistakes. One interview is not your whole future. Continue next day.")
ws5.merge_cells("A17:D17")

out = Path(r"E:\sems\sem 7\Python DSA\Narendra_Interview_Effort_Tracker_13to16Aug.xlsx")
wb.save(out)
print("Saved:", out)
print("Sheets:", wb.sheetnames)
print("Master tasks:", len(tasks))
