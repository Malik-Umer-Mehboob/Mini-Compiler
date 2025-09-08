

```markdown
 🖥️ Mini Compiler for a Custom Language

A simple **mini compiler** built in Python that demonstrates the full compilation pipeline:

- **Lexer (Lexical Analysis)** → Breaks input into tokens  
- **Parser (Syntax Analysis)** → Builds an Abstract Syntax Tree (AST)  
- **Evaluator (Code Generation/Execution)** → Evaluates expressions and maintains a symbol table  

This project is educational and suitable for learning the basics of compiler design.

---

 📂 Project Structure

```

mini\_compiler/
│
├── lexer.py       # Token and Lexer implementation
├── parser.py      # AST Nodes and Parser
├── evaluator.py   # Symbol Table and Evaluator
└── main.py        # Entry point, connects the pipeline

````

---

 🚀 Features
- Supports **arithmetic expressions**: `+`, `-`, `*`, `/`
- **Variable assignment** with `=`
- **Parentheses** for precedence handling
- **Symbol Table** to store variable values
- Tabular display of tokens (using `tabulate`)

---

 🛠️ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/mini-compiler.git
cd mini-compiler
pip install tabulate
````

---

 ▶️ Usage

Run the compiler:

```bash
python main.py
```

Enter your custom code (end with an empty line):

```
x = 5 + 3;
y = x * 2;
z = (y - 4) / 2;
```

---

 📊 Example Output

```
Tokens (Lexical Analysis):
+-------------+--------------+
| Token Type  | Token Value  |
+-------------+--------------+
| ID          | x            |
| ASSIGN      | =            |
| NUMBER      | 5            |
| PLUS        | +            |
| NUMBER      | 3            |
| SEMICOLON   | ;            |
| ID          | y            |
| ASSIGN      | =            |
| ID          | x            |
| MULT        | *            |
| NUMBER      | 2            |
| SEMICOLON   | ;            |
| ID          | z            |
| ASSIGN      | =            |
| LPAREN      | (            |
| ID          | y            |
| MINUS       | -            |
| NUMBER      | 4            |
| RPAREN      | )            |
| DIV         | /            |
| NUMBER      | 2            |
| SEMICOLON   | ;            |
+-------------+--------------+

Evaluation Results:
x = 8
y = 16
z = 6.0

Symbol Table: {'x': 8, 'y': 16, 'z': 6.0}





