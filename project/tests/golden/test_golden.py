import sys
import os
import json

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)
sys.path.insert(0, PROJECT_ROOT)

from template_engine import TemplateEngine


BASE_DIR = os.path.dirname(__file__)
TEMPLATE_PATH = os.path.join(PROJECT_ROOT, "template.json")


def normalize(text: str) -> str:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return "\n".join(lines)


def run_golden_test(test_folder: str):
    template_path = os.path.join(test_folder, "template_pregnancy.json")
    
    if os.path.exists(template_path):
     with open(template_path, encoding="utf-8") as f:
         template = json.load(f)
    else:
     with open(TEMPLATE_PATH, encoding="utf-8") as f:
        template = json.load(f)
   
    
    with open(os.path.join(test_folder, "data.json"), encoding="utf-8") as f:
        data = json.load(f)

    with open(os.path.join(test_folder, "expected.txt"), encoding="utf-8") as f:
        expected = f.read()

    engine = TemplateEngine(template, data)
    result = engine.generate()

    assert normalize(result) == normalize(expected)


def test_abdomen_normal():
    run_golden_test(os.path.join(BASE_DIR, "abdomen_normal"))


def test_abdomen_fatty_liver():
    run_golden_test(os.path.join(BASE_DIR, "abdomen_fatty_liver"))


def test_pregnancy_normal():
    run_golden_test(os.path.join(BASE_DIR, "pregnancy_normal"))
