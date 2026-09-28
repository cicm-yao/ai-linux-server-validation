# AI-Augmented Linux Server System Validation & Failure Diagnosis Platform


## Overview

This project implements an automated Linux server validation framework
with evidence collection and AI-assisted failure diagnosis capability.

The primary goal is to build a realistic server validation workflow:

Requirement
→ Test Plan
→ Test Execution
→ Evidence Collection
→ Deterministic PASS/FAIL
→ Failure Analysis
→ RCA Assistance
→ Regression


AI is used only for failure analysis assistance.
PASS/FAIL decisions are determined by test results and validation rules.


---

## Current Status

Phase 0 - Environment Setup

Completed:

- Project repository initialization
- Python validation framework skeleton
- Configuration-driven test execution
- Evidence mapping
- RCA analyzer prototype
- Regression test framework
- Failure knowledge base structure


---

## Environment

Controller:

- Ubuntu 20.04 VM

Hypervisor:

- VMware Workstation


DUT:

- Not connected yet
- Planned: Physical Linux system for hardware validation


---

## Architecture

 	        Test Configuration
                   YAML / JSON
                        |
                        v

              Validation Runner
                        |
    +-------------------+-------------------+
    |                   |                   |
    v                   v                   v

Functional Tests Stress Tests Fault Injection

    \                   |                   /
     \                  |                  /
      +-----------------+----------------+
                        |
                        v

             Evidence Collection
                        |
                        v

          Deterministic Validation Judge

                +---------------+
                |               |
                v               v

              PASS             FAIL

                               |
                               v

                      Failure Analysis

                               |
                               v

                     RCA Report Generation

                               |
                               v

                     Fix Verification

                               |
                               v

                     Regression Testing

---

## Project Structure


server-validation/

├── config/
│   ├── test_plan.yaml
│   └── evidence_map.yaml

├── tests/
│   ├── cpu/
│   ├── memory/
│   ├── storage/
│   └── network/

├── evidence/
│   Runtime test evidence

├── experiments/
│   └── fault_injection/

├── rca/
│   ├── rules.yaml
│   ├── failure_cases.yaml
│   └── templates/

├── regression/

├── reports/

├── scripts/

└── runner.py


---

## Implemented Features

### Validation Framework

- YAML based test configuration
- pytest integration
- Automated test execution
- JSON report generation


### Evidence Management

- Test evidence mapping
- Failure evidence association
- Structured validation report


### Failure Analysis

- Rule based RCA analyzer
- Failure knowledge base
- RCA report generation


### Regression

- Regression test plan
- Automated regression execution
- Regression report generation


---

## Future Work

Planned:

- Linux hardware inventory
- CPU / Memory / Storage / Network validation
- Stress and stability testing
- Fault injection scenarios
- Kernel log analysis
- AI-assisted RCA
- Failure knowledge base with RAG


---

## How to Run

Current status:

Validation workflow is under development.

Planned workflow:

```bash
python runner.py
