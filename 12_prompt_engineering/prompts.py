from pathlib import Path
from jinja2 import Environment, FileSystemLoader

env = Environment(
    loader=FileSystemLoader("12_prompt_engineering/prompt_templates"),
    autoescape=False
)


def load_prompt(version: str, context: str, question: str):

    filename = f"college_{version}.txt"

    template = env.get_template(filename)

    return template.render(
        context=context,
        question=question
    )


# Few-shot examples
FEW_SHOT_EXAMPLES = """
Example 1:
Input: When is the admission process?
Output: admission

Example 2:
Input: What is my examination timetable?
Output: examination

Example 3:
Input: How can I pay my college fees?
Output: fees
"""