import re

class TemplateEngine:

    def __init__(self, template: dict, data: dict):
        self.template = template
        self.data = data

    def generate(self) -> str:
        output_lines = []

        template_type = self.template.get("type")
        data_type = self.data.get("type")

        # 🚫 mismatch → empty report
        if template_type and data_type and template_type != data_type:
            return ""

        for section in self.template.get("sections", []):
            for line in section.get("report_text", []):
                rendered = self._render_line(line)
                if rendered:
                    output_lines.append(rendered)

        return "\n".join(output_lines)

    def _render_line(self, line: str) -> str:
        # IF condition
        if "{{#if" in line:
            condition, text = self._extract_if(line)
            if self._evaluate_condition(condition):
                return self._replace_vars(text)
            return ""

        # Plain text
        return self._replace_vars(line)

    def _extract_if(self, line: str):
        match = re.search(r"\{\{#if (.*?)\}\}(.*?)\{\{\/if\}\}", line)
        return match.group(1).strip(), match.group(2).strip()

    def _evaluate_condition(self, condition: str) -> bool:
        # supports: ==, !=, >, <, true, false
        tokens = re.split(r"(==|!=|>|<)", condition)

        if len(tokens) == 3:
            field, op, value = tokens
            field = field.strip()
            value = value.strip().strip("'")

            field_value = self.data.get(field)
            if field_value is None:
                 return False

            if value.lower() == "true":
                value = True
            elif value.lower() == "false":
                value = False
            elif value.isdigit():
                value = int(value)

            if op == "==":
                return field_value == value
            if op == "!=":
                return field_value != value
            if op == ">":
                return field_value > value
            if op == "<":
                return field_value < value

        return False

    def _replace_vars(self, text: str) -> str:
        def replacer(match):
            key = match.group(1)
            return str(self.data.get(key, ""))

        return re.sub(r"\{\{(.*?)\}\}", replacer, text)
