"""Regression tests for huggingface/Math-Verify#76 (candidate upstream tests)."""

import pytest

from math_verify import ExprExtractionConfig, parse, verify


@pytest.mark.parametrize(
    "prediction,gold,expected_text",
    [
        ("Final Answer: **73**", "73", "73"),
        ("✅ Final Answer: **73**", "73", "73"),
        ("The answer is **73**.", "73", "73"),
        ("Answer: **-5**", "-5", "-5"),
        ("Final Answer: **2 + 3**", "5", "2 + 3"),
        ("Final Answer: **2 * 3**.", "6", "2 * 3"),
        ("Final Answer: **2**3**", "8", "2**3"),
        ("Final Answer: 2**3", "8", "2**3"),
    ],
)
def test_bold_final_answer_does_not_consume_markdown_as_operator(
    prediction, gold, expected_text
):
    config = [ExprExtractionConfig()]
    parsed = parse(prediction, extraction_config=config)
    assert parsed, prediction
    assert verify(parse(gold, extraction_config=config), parsed)
    assert parsed[-1] == expected_text


def test_issue_76_long_answer_prioritizes_bold_final_answer():
    prediction = """
    ... - 73 = 489 ...(iii)
    Now sum (i)+(ii)+(iii):
    Left: (x_D + x_G + x_S) + 2(y_DG + y_DS + y_GS) = 437 + 2*234 = 437 + 468 = 905
    Right: 122 + 294 + 489 = 905
    ✅ Consistent!
    So answer is consistent.
    Thus, the number of residents who own all four of the things is **73**.
    ---
    ✅ Final Answer: **73**
    """
    config = [ExprExtractionConfig()]
    parsed = parse(prediction, extraction_config=config)
    assert verify(parse("73", extraction_config=config), parsed)
    assert parsed[-1] == "73"
