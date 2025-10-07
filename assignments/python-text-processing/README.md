# 📘 Assignment: Python Text Processing

## 🎯 Objective
Process and analyze raw text from a file using Python string operations, loops, and basic data structures to extract useful statistics and cleaned output.

## 📝 Tasks

### 🛠️ Load & Clean Text
#### Description
Read a provided text file, normalize its contents, and prepare it for further analysis by removing noise and standardizing formatting.
#### Requirements
Completed program should:

- Read `sample.txt` from the current directory
- Convert all characters to lowercase
- Replace punctuation (.,!?:;"') with spaces
- Collapse multiple spaces into a single space
- Strip leading and trailing whitespace from the final string

### 🛠️ Compute Statistics
#### Description
Generate core metrics that summarize the content and structure of the cleaned text.
#### Requirements
Completed program should:

- Count total number of words
- Count unique words (case-insensitive)
- Identify the top 5 most frequent words (break ties alphabetically)
- Display average word length rounded to 2 decimals
- Print results in a readable, labeled format

### 🛠️ Word Frequency Report
#### Description
Produce a frequency report file that lists each unique word alongside its occurrence count, sorted for easy inspection.
#### Requirements
Completed program should:

- Build a dictionary mapping each word to its count
- Sort words primarily by descending frequency, then alphabetically
- Write results to `word_frequencies.txt` (one `word,count` per line)
- Exclude empty tokens created by spacing operations
- Confirm creation of the output file with a console message

### 🛠️ Optional Enhancements
#### Description
Add advanced processing features to extend analysis accuracy or depth. These are optional.
#### Requirements
Completed program should (if enhancements added):

- Ignore a list of common stop words (e.g., `the`, `and`, `to`)
- Track and display the longest sentence length (in words)
- Provide a command-line argument for input filename

---
Example (partial) output format:
```
Total words: 523
Unique words: 287
Average word length: 4.62
Top 5 words:
1. data (23)
2. analysis (18)
3. file (17)
4. python (15)
5. text (14)
```

Keep code modular: separate loading, cleaning, counting, and reporting into functions.
