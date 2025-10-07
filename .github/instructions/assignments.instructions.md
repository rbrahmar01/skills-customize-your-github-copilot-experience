---
applyTo: "assignments/**/*.md"
---

# Assignment Markdown Structure Guidelines

Author every assignment `README.md` so it is clear, consistent, and student-friendly. This document defines the ONLY acceptable structure and style.

## ✅ 1. Use the Official Template

All assignment markdown files MUST follow the exact structure in [`templates/assignment-template.md`](../../templates/assignment-template.md).

Required top-level sections (with the exact icons and capitalization):

1. `# 📘 Assignment: <Title>`
2. `## 🎯 Objective`
3. `## 📝 Tasks` (contains one or more task subsections)

Each task subsection MUST follow this nesting:
```
### 🛠️ <Task Title>
#### Description
...text...
#### Requirements
Completed program should:

- Requirement 1
- Requirement 2
```

DO NOT add, rename, or remove required headings or icons. Do not introduce extra sections (e.g., "Background", "Hints", "Resources") unless explicitly requested for a specific assignment.

## 🗂️ 2. File & Folder Expectations

Each assignment folder under `assignments/<assignment-id>/` must contain:

- `README.md` (the assignment document – required)
- `starter-code.py` (if starter is helpful; name exactly this unless language differs)
- Additional data files (e.g., `data.csv`) only if directly used in tasks

Avoid dumping unrelated assets. If a dataset or image is optional enrichment, omit it.

## ✍️ 3. Writing Guidance by Section

### Title (`# 📘 Assignment: ...`)
- Replace placeholder with a concise, descriptive noun phrase (e.g., `Python Basics`, `Data Analysis Intro`).
- Avoid punctuation at the end; no emojis beyond the provided icon.

### Objective (`## 🎯 Objective`)
- 1–2 sentences only.
- State the learning outcome using action verbs (e.g., "Practice using loops to process collections"; "Build a simple class to model game objects").
- Focus on skills, not instructions (avoid step lists here).

### Tasks (`## 📝 Tasks`)
- Provide 1–4 tasks. Split logically if the work has milestones.
- Each task must be independently testable by a teacher.
- Avoid tasks that are just restatements of requirements (make them purposeful: "Implement Input Validation", not "Validation").

#### Task Title (`### 🛠️ <Title>`)
- Use active or descriptive phrasing: "Build the Data Loader", "Implement Player Movement".
- Keep under 5 words when possible.

#### Description
- Explain WHAT the student is building and WHY it matters.
- Keep it to a short paragraph (3–5 lines max). Use plain language.

#### Requirements
- Start with the fixed line: `Completed program should:` (exact wording).
- Use bullet points; each bullet must be:
   - Observable (teacher can verify by running code / reading output)
   - Singular (avoid combining multiple requirements with "and")
   - Written in present tense ("prints a summary", "validates input", "handles empty file")
- Avoid vague verbs: NOT "understand", "learn". Prefer concrete: "reads", "saves", "counts", "raises", "logs".

Example requirement set:
```
Completed program should:

- Load `data.csv` and ignore blank lines
- Compute the average value of the `score` column
- Print the result rounded to 2 decimal places
- Exit with an error message if the file is missing
```

## 🧪 4. Examples & Code Blocks

Provide example input/output ONLY when it clarifies expectations (especially for formatting). Keep them minimal:
```
Input: 3 5 9
Output: Average: 5.67
```
Do NOT reveal the full solution or algorithm.

## 🧩 5. Scope & Difficulty

Align difficulty with course progression:
- Early: basics (variables, loops, conditionals)
- Mid: functions, modularization, simple classes
- Later: data handling, problem decomposition, basic OOP

If a task depends on advanced concepts not yet covered, revise or defer.

## 🛑 6. Common Mistakes to Avoid
- Adding extra headings not in the template
- Long narrative intros – keep it actionable
- Mixing multiple expectations in one requirement
- Writing requirements as questions
- Using future tense ("will load") instead of present

## 🗃️ 7. Attachments / Starter Code
- If starter code is provided, reference it in the Description of the FIRST task only (e.g., "Use the provided `starter-code.py` as a starting point").
- Do NOT list files in the Objective.
- Keep starter code minimal: scaffolding, function signatures, docstrings – no core logic.

## ♿ 8. Accessibility & Tone
- Use inclusive, encouraging language (e.g., "You will build...", "Try experimenting by...").
- Avoid sarcasm, negative framing, or assumptions about prior background beyond syllabus coverage.
- Keep reading level approachable (upper middle school / early high school).

## 🔍 9. Quick Author Checklist (Before Commit)
- [ ] Uses exact required headings & icons
- [ ] Objective is 1–2 sentences, outcome-focused
- [ ] Each task has Description + Requirements
- [ ] All requirements are measurable & singular
- [ ] No extra sections added
- [ ] Examples (if any) are concise and non-solution revealing
- [ ] Starter code (if present) matches references
- [ ] No spelling / formatting inconsistencies

## ✅ 10. Acceptance Criteria (Automated / Review)
A `README.md` failing any of these is considered non-compliant:
- Missing or altered required headings
- Omits "Completed program should:" phrasing
- Any requirement longer than two lines (rephrase or split)
- Task list empty or tasks without requirements

## 🛠 11. Updating Existing Assignments
When revising an assignment:
- Preserve student-facing intent unless pedagogy changes
- If restructuring tasks, ensure continuity with previously distributed materials (note changes in commit message)
- Keep backward-compatible filenames unless absolutely necessary

## 🧾 12. Example (Annotated Fragment)
```
# 📘 Assignment: Data Analysis Intro

## 🎯 Objective
Load a small CSV file, compute simple statistics, and practice reading structured data from disk.

## 📝 Tasks

### 🛠️ Load the Dataset
#### Description
Read the provided `data.csv` file and prepare the records for analysis by filtering invalid rows.
#### Requirements
Completed program should:

- Read `data.csv` from the current directory
- Skip rows missing the `score` column
- Convert `score` values to integers
```

---
Author with clarity. Keep students focused on outcomes, not filler. Consistency accelerates learning.