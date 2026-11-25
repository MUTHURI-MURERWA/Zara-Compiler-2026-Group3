\# Contributing to Zara Programming Language Compiler



\## 1. Introduction



This document provides guidelines for all team members contributing to the Zara Programming Language Compiler project.



All members are expected to collaborate, communicate, test their work, and maintain proper documentation throughout the project.



\## 2. Project Repository



GitHub Repository: https://github.com/MUTHURI-MURERWA/Zara-Compiler-2026-Group3



The `main` branch contains the stable, integrated version of the project.



\## 3. Branch Management



Each member should work on their assigned feature branch.



| Responsibility | Branch |

|---|---|

| Symbol Table and Lexer | feature/symbol-table-lexer |

| Top-Down and Bottom-Up Parsers | feature/parsers |

| Semantic Analysis and Syntax-Directed Translation | feature/semantic-analysis |

| Intermediate Code and Optimization | feature/intermediate-code |

| OOP and Code Generation | feature/oop-code-generation |



Members should not commit directly to `main`.



\## 4. Development Workflow



1\. Clone the repository.

2\. Switch to the assigned feature branch.

3\. Pull the latest changes before starting work.

4\. Implement and test assigned features.

5\. Commit changes using meaningful messages.

6\. Push changes to the remote feature branch.

7\. Create a Pull Request when the work is ready for review.

8\. Wait for review and approval before merging into `main`.



\## 5. Commit Message Guidelines



Commit messages should briefly describe the changes made.



Examples:



\- Add symbol table implementation

\- Implement lexical error detection

\- Add recursive descent parser

\- Implement semantic type checking

\- Add three-address code generation

\- Fix parser expression handling



\## 6. Coding Guidelines



\- Write readable and properly organized code.

\- Use meaningful variable and function names.

\- Add comments where necessary.

\- Test features before submitting changes.

\- Avoid modifying another member's assigned files without communication.

\- Report bugs and technical challenges to the group.



\## 7. Testing



Test cases should be organized into:



\- `tests/valid` – programs expected to compile successfully.

\- `tests/invalid` – programs expected to produce errors.



Both successful and unsuccessful test cases should be documented.



\## 8. Documentation



Members should document their implementation, testing procedures, challenges, and results.



Weekly progress reports and technical documentation should be maintained in the `docs` directory.



\## 9. Team Participation



All five members are expected to contribute to implementation, testing, documentation, and the final project demonstration.



Each member's contributions should be traceable through GitHub commits and Pull Requests.



\## 10. Integration



The group leader coordinates integration and reviews submitted contributions.



Only tested and reviewed changes should be merged into the `main` branch.

