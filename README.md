# 🚀 GrammarGraph AST Generator

A Python-based project that reads formal grammar rules and generates **Abstract Syntax Trees (ASTs)** from given sentences. The project also supports **visualizing parse trees as PNG images**.

---

## 📌 Overview

This project implements a simple **grammar-driven parser** that:

* Reads grammar rules from `.txt` files
* Parses input sentences according to the grammar
* Builds a structured **AST (tree representation)**
* Outputs:

  * Console-based tree view 🌳
  * JSON-like structure 📦
  * PNG visualization 🖼️

It is designed for **educational purposes**, especially for understanding:

* Context-Free Grammars (CFG)
* Parsing logic
* Tree structures (AST)
* Syntax visualization

---

## 🧠 How It Works

1. **Grammar Input**

   * Grammar rules are defined in files like:

     * `grammar1.txt`
     * `grammar2.txt`
   * Format:

     ```
     <sentence> ::= <noun_phrase> <verb_phrase>
     <noun_phrase> ::= the cat | a dog
     ```

2. **Sentence Input**

   * Sentences are read from:

     * `sentences1.txt`
     * `sentences2.txt`

3. **Parsing**

   * `Parser` class processes tokens step-by-step
   * Builds a tree using custom `Node` structure

4. **Output Generation**

   * Tree printed in console
   * Converted to dictionary (JSON-like)
   * Visualized using `pydot` as PNG

---

## ✨ Features

* 📖 Grammar file reader (`grammar_reader.py`)
* 🧩 Recursive parsing logic (`parser_logic.py`)
* 🌳 Custom tree structure (`nodes.py`)
* 🖼️ AST visualization (`visualizer.py`)
* 🔄 Multiple grammar support (switchable via `main.py`)
* ⚠️ Error handling with meaningful messages

---

## 🏗️ Project Structure

```
grammargraph-ast-generator/
│
├── main.py                 # Entry point
├── grammar_reader.py       # Reads grammar rules
├── parser_logic.py         # Core parsing logic
├── nodes.py                # AST node structure
├── visualizer.py           # Tree visualization (PNG)
│
├── grammar1.txt            # Sample grammar (natural language)
├── grammar2.txt            # Sample grammar (epsilon rules)
├── sentences1.txt          # Input sentences
├── sentences2.txt          # Input sentences
│
├── document/               # Outputs & documentation
│   ├── ast_output.png
│   ├── tree_output_*.png
│   └── document.pdf
│
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/eylulkalfa/grammargraph-ast-generator.git
cd grammargraph-ast-generator
```

---

### 2. Install dependencies

```bash
pip install pydot
```

⚠️ Also make sure you have **Graphviz** installed:

* Mac:

```bash
brew install graphviz
```

* Ubuntu:

```bash
sudo apt install graphviz
```

---

### 3. Run the project

```bash
python main.py
```

---

## ⚙️ Configuration

Inside `main.py`:

```python
active_test = "1"
```

* `"1"` → Natural language grammar
* `"2"` → Epsilon-based grammar

---

## 🧪 Example

### Input

```
the cat eats fish
```

### Console Output

```
└── <sentence>
    ├── <noun_phrase>
    └── <verb_phrase>
```

---

### JSON-like Output

```json
{
  "sentence": {
    "noun_phrase": {...},
    "verb_phrase": {...}
  }
}
```

---

### Visualization

The system generates:

* ✅ `parse_tree_*.png`
* Tree structure rendered visually

---

## 🖼️ Example Output

(Project already includes generated visuals in `/document` folder)

* AST visualization
* Parse tree diagrams

---

## ⚠️ Error Handling

Parser provides meaningful errors:

* Missing noun phrase
* Missing verb phrase
* Unexpected token

Example:

```
Expected: a verb phrase
Reason: The sentence has a subject but lacks a predicate.
```

---

## 🧩 Use Cases

* 📚 Compiler design courses
* 🧠 NLP basics
* 🌳 AST learning
* 🏗️ Parser development practice
* 🎓 Academic projects (Teknofest / university)

---

## 🔧 Technologies

* Python
* Recursive Descent Parsing
* Graph Visualization (`pydot`, Graphviz)
