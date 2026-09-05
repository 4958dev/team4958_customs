# Portfolio cleanup notes

This overlay intentionally does **not** rewrite the historical source code.

Changes prepared for the public portfolio presentation:

- rewrote the README to explain the original motivation, scope and historical status;
- made the pre-AI / independently written provenance explicit;
- replaced the old joke-style package description with a professional one;
- removed `asyncio` from package dependencies because it is part of Python's standard library;
- removed `disnake` from the library's direct dependencies because it is referenced by a generated project preset rather than imported by the package runtime itself; generated Disnake projects already declare their own dependency;
- corrected the MIT license copyright line from the Python Packaging Authority template attribution to the project author;
- simplified `.gitignore` for the actual repository.

No source module is included in this overlay because the portfolio strategy is to preserve the existing implementation and Git history as evidence of early independent Python work.
