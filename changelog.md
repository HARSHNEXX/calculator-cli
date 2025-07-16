incrementally

🧾 Full Update Log – Python Calculator v1.0 → v1.4
📅 Timeline: 14 July – 16 July 2025
📁 File: calculator_v1_4.py
✅ v1.0 – Initial Release
Basic calculator CLI with functions for add, subtract, multiply, divide

Input validation limited, no modularity

No main() function

✅ v1.1 – User Prompts & Improved UI
Added name input + friendly greeting

Introduced ASCII banner for professional look

Improved messages and calculation summaries

✅ v1.2 – Expanded Feature Set
Added power and check odd/even operations

Used if/else + while blocks for flow control

Started early input checking on division and power

Cleaner outputs and consistent formatting

✅ v1.3 – Input Validation with try/except
Wrapped all input requests with try/except blocks

Added loops to retry on invalid inputs

Improved input range checks (e.g., >= 0)

Introduced match/case for early logic handling (experimental)

✅ v1.4 – Modular Architecture + Utilities Integration
🔧 Codebase Refactor:

All input logic moved to utilities.py:

two_num_in(prompt1, prompt2)

one_num_in(prompt)

multi_num_in(prompt)

pos_num_in(prompt)

calculator_v1_4.py imports and uses these functions cleanly

Full separation of concerns: UI vs logic vs input

🧮 Features Added:

m: Calculate mean of user-supplied list (using statistics.mean())

Enhanced error handling for division by zero and empty lists

🛡️ Resilience Added:

Defensive programming across all math functions

Recursive retry on failed inputs

CLI ready for future argparse expansion

