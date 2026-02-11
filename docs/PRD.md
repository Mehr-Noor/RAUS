# Product Requirements Document (PRD)

## Project Overview
**Project Name:** RAUS – Radiology Ultrasound Reporting System  
**Version:** 1.0 (MVP)  
**Owner:** Radiology Software Team  
**Last Updated:** 2026-02-09  

---

## 1. Purpose
The purpose of this document is to define the product requirements for the MVP version of RAUS, a structured ultrasound reporting system designed to help radiologists and sonographers generate accurate, consistent, and fast ultrasound reports.

---

## 2. Problem Statement
Current ultrasound reporting workflows rely heavily on free-text typing, leading to:
- Inconsistent terminology
- Increased reporting time
- Higher risk of missing critical findings
- Difficulty in standardization and auditing

---

## 3. Goals & Objectives
- Reduce report writing time by at least 30%
- Improve report consistency and structure
- Enable template-based and rule-driven report generation
- Support common ultrasound studies (Abdomen, Pregnancy) in MVP

---

## 4. Target Users
| User Type        | Description |
|------------------|-------------|
| Radiologist      | Reviews and finalizes ultrasound reports |
| Sonographer      | Performs scan and inputs findings |
| Clinic Admin     | Manages templates and system settings |

---

## 5. Scope (MVP)
### In Scope
- Template-based ultrasound report generation
- JSON-driven templates
- Rule engine for conditional text
- Abdomen & Pregnancy ultrasound templates
- Export report as plain text

### Out of Scope
- PACS integration
- Voice recognition
- Billing & insurance
- Multi-language support

---

## 6. Functional Requirements
| ID | Requirement |
|----|------------|
| FR-1 | System shall generate reports from structured JSON input |
| FR-2 | System shall support conditional rules in templates |
| FR-3 | Users can edit generated text before finalizing |
| FR-4 | Templates shall be reusable and versionable |

---

## 7. Non-Functional Requirements
| Category | Requirement |
|--------|-------------|
| Performance | Report generation < 1 second |
| Reliability | Deterministic output for same input |
| Maintainability | Modular and testable codebase |
| Security | Local data processing only (MVP) |

---

## 8. Constraints & Assumptions
- Initial version runs locally (Desktop / CLI)
- No real patient identifiers in MVP
- Python is the primary implementation language

---

## 9. MVP Definition
**MVP includes:**
- Working TemplateEngine
- Rule Engine with unit & golden tests
- Sample Abdomen & Pregnancy templates
- CLI-based execution

---

## 10. Success Metrics
- Golden tests passing for all supported templates
- Radiologist feedback on clarity & usefulness
- Reduction in report writing time (qualitative)

---

## 11. Open Questions
- Should templates be user-editable via UI in future?
- What level of clinical customization is required per center?

---
