# Software Requirements Specification (SRS)

## Project Name
RAUS – Radiology Ultrasound Reporting System

## Version
1.0 (MVP)

## Date
2026-02-09

---

## 1. Introduction

### 1.1 Purpose
This document specifies the software requirements for the MVP version of RAUS.  
It serves as a technical reference for developers, testers, and stakeholders.

### 1.2 Scope
RAUS is a local software system that generates structured ultrasound reports using predefined templates and rule-based logic from structured input data.

### 1.3 Definitions & Acronyms
- **SRS:** Software Requirements Specification
- **PRD:** Product Requirements Document
- **MVP:** Minimum Viable Product
- **Template:** JSON-based report structure
- **Rule Engine:** Conditional logic for text inclusion

---

## 2. Overall Description

### 2.1 Product Perspective
RAUS is a standalone system operating locally without external integrations in MVP.

Architecture layers:
- Input Layer (JSON Data)
- Template Engine
- Rule Engine
- Output Renderer (Text)

### 2.2 User Classes
| User | Description |
|----|------------|
| Radiologist | Final reviewer of reports |
| Sonographer | Data input provider |
| Developer | Maintains templates & rules |

### 2.3 Operating Environment
- OS: Windows (MVP)
- Language: Python 3.11+
- Execution: CLI-based

### 2.4 Constraints
- No UI in MVP
- No PACS / HIS integration
- No patient identifiers

---

## 3. System Features

### 3.1 Template-Based Report Generation
**Description:**  
System generates reports using JSON templates.

**Inputs:**
- Template JSON
- Data JSON

**Outputs:**
- Plain text report

---

### 3.2 Rule Engine
**Description:**  
Rules define conditional inclusion of text.

**Supported Conditions (MVP):**
- `==`, `!=`, `>`, `<`
- Boolean evaluation
- Missing fields handled safely

---

### 3.3 Golden Test Validation
**Description:**  
System output must exactly match expected reports for predefined scenarios.

---

## 4. Functional Requirements

| ID | Requirement |
|----|------------|
| FR-1 | System shall load templates from JSON files |
| FR-2 | System shall replace placeholders with data |
| FR-3 | System shall evaluate conditional rules |
| FR-4 | System shall ignore irrelevant rules safely |
| FR-5 | System shall generate deterministic output |
| FR-6 | System shall support Abdomen & Pregnancy reports |

---

## 5. Non-Functional Requirements

### 5.1 Performance
- Report generation < 1 second

### 5.2 Reliability
- Same input → same output (100%)

### 5.3 Testability
- Unit tests for rule evaluation
- Golden tests for full reports

### 5.4 Maintainability
- Modular code
- Clear separation of template & logic

---

## 6. Use Cases

### UC-1: Generate Abdomen Ultrasound Report
**Actor:** Sonographer  
**Precondition:** Template and data available  
**Main Flow:**
1. Load template
2. Load data
3. Evaluate rules
4. Render report

---

### UC-2: Generate Pregnancy Ultrasound Report
Same as UC-1 with pregnancy-specific fields.

---

## 7. Data Requirements

### 7.1 Template Structure
```json
{
  "lines": [
    {
      "text": "The liver has normal size.",
      "condition": "fatty_liver == false"
    }
  ]
}
