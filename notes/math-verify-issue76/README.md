# Math-Verify #76 — Markdown-bold final answers

**Upstream:** https://github.com/huggingface/Math-Verify/issues/76  
**Stage:** independent root-cause analysis and candidate patch; **not an upstream PR or accepted fix**.

## Problem and why it matters

For responses ending in `Final Answer: **73**`, the expression branch of `lazy_expr_regex` may capture `73**` because its arithmetic pattern permits operators as the final characters. That can fail the math parser and allow an incorrect answer to be selected instead of the final answer. This matters to LLM evaluation and verifiable-reward experiments.

## Candidate minimal fix

In `src/math_verify/parser.py`, change only the terminal condition for `expr_re`:

```diff
-        rf"(?P<expr>-?\\(?-?\\d{all_expr_chars}*[{operators_re}]{all_expr_chars}+\\)?)"
+        rf"(?P<expr>-?\\(?-?\\d{all_expr_chars}*[{operators_re}]{all_expr_chars}*[\\d\\)])"
```

This requires an arithmetic expression to finish in a digit or closing parenthesis, leaving Markdown bold closers to the suffix matcher. The standalone reproduction confirmed the original expression match captures `73**`, whereas the modified version prioritizes the final numeric answer `73`. It also tested `**2 + 3**`, `**2 * 3**.`, `**2**3**`, and legitimate unformatted exponent `2**3`.

## Evidence and limitations

- [Candidate patch](mathverify-issue76.patch)
- [Proposed upstream pytest regression cases](test_markdown_bold_answers.py)
- Local isolated regex reproduction (Python + SymPy) passed 8 cases; the patch also passed `git apply --check` against a matching source-context fixture.
- **Upstream package tests were not executed**, as the environment has no GitHub download access or the requisite installed upstream dependencies.
- On 2026-10-14, Issue #76 was open; no competing open PR matching the issue was found. Recheck before submitting.
- The GitHub integration cannot create a fork or post an issue comment to this upstream repository; attempting to comment was rejected with HTTP 403.

## Proposed next steps

1. Create an actual fork of `huggingface/Math-Verify`, bring this candidate change and tests into a working branch.
2. Run `pip install -e '.[dev,antlr4_13_2]'`, targeted pytest, full pytest, and ruff locally or in CI.
3. Revise the patch if broader parsing regressions appear; only then open an upstream PR referencing #76.

Not a claim of affiliation with Hugging Face, an accepted PR, or production-tested correctness.
