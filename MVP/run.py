import json
from template_engine import TemplateEngine

with open("template.json", "r", encoding="utf-8") as f:
    template = json.load(f)

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

engine = TemplateEngine(template, data)
result = engine.generate()

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(result)

print("Report generated successfully!")
print("---------")
print(result)
