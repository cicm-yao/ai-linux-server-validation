# AI-Augmented Linux Server System Validation & Failure Diagnosis Platform

## Overview

This project implements an automated Linux server validation framework with evidence collection and rule-based failure diagnosis capability.

The goal is to build a lightweight server validation workflow:

```
Test Plan
    |
    v
Automated Test Execution
    |
    v
Evidence Collection
    |
    v
PASS / FAIL Judgment
    |
    v
Failure Analysis
    |
    v
RCA Report
    |
    v
Regression Validation
```
The project focuses on:

- Linux system validation
- Test automation
- Failure injection
- Evidence-driven debugging
- Rule-based RCA
- Failure-triggered regression validation
- AI-assisted failure analysis extension

AI is used as an assistant for failure analysis rather than replacing deterministic validation logic.

---

# Features

## Validation Framework

Implemented a configuration-driven validation framework based on Python and pytest.

Features:

- YAML-based test plan
- Automated test execution
- Test case management
- JSON validation report generation
- Evidence path tracking

Workflow:

```
test_plan.yaml
        |
        v
    runner.py
        |
        v
     pytest
        |
        v
validation_report.json
```

---

## Test Coverage

Current implemented validation modules:

### CPU Validation

- Basic CPU validation
- CPU stress testing

Example:

```
TC_CPU_001
TC_CPU_STRESS_001
```

---

### Memory Validation

- Memory stress testing

Example:

```
TC_MEMORY_STRESS_001
```

---

### Storage Validation

- Storage I/O validation
- fio based testing

Example:

```
TC_STORAGE_FIO_001
```

---

### Network Validation

- Network connectivity validation

Example:

```
TC_NETWORK_001
```

---

### Fault Injection

Implemented software-level fault injection examples:

```
TC_FAULT_CPU_001

TC_FAULT_NETWORK_001
```

Current fault workflow:

```
Fault Injection
        |
        v
Evidence Collection
        |
        v
Failure Classification
        |
        v
RCA Analysis
```

---

# Architecture

```
                Test Configuration
                  YAML / JSON
                       |
                       v
                  Python Runner
                       |
        +--------------+--------------+
        |              |              |
        v              v              v

    Test Engine    Evidence      Reports
        |
        |
 +------+-------+
 |      |       |
CPU Memory Network
 |
Storage
 |
Fault Injection


                       |
                       v

                Failure Analysis

                       |
                       v

                RCA Report

                       |
                       v

                Regression Test
```

---

# Project Structure

```
server-validation/

├── analyzer/
│   ├── log_parser.py
│   └── ai/
│       └── rca_assistant.py
│
├── config/
│   ├── test_plan.yaml
│   ├── evidence_map.yaml
│   └── failure_regression_map.yaml
│
├── docs/
│   ├── architecture.md
│   ├── current_architecture.md
│   ├── failure_case_network.md
│   ├── project_progress.md
│   └── test_inventory.md
│
├── evidence/
│   ├── cpu/
│   ├── memory/
│   ├── storage/
│   ├── network/
│   └── fault/
│
├── experiments/
│   └── fault_injection/
│       ├── cpu/
│       ├── memory/
│       ├── network/
│       └── storage/
│
├── inventory/
│   ├── baseline.md
│   └── reports/
│       └── inventory_report.json
│
├── knowledge/
│   ├── cpu.yaml
│   ├── memory.yaml
│   ├── network.yaml
│   ├── network_fault.yaml
│   └── storage.yaml
│
├── rca/
│   ├── rules.yaml
│   ├── failure_cases.yaml
│   └── templates/
│
├── regression/
│   ├── regression_plan.yaml
│   └── regression_runner.py
│
├── reports/
│   ├── validation_report.json
│   ├── rca_report.json
│   ├── regression_report.json
│   ├── ai_rca_report.json
│   ├── failure_context.json
│   └── structured_evidence.json
│
├── runs/
│   └── YYYYMMDD_HHMMSS/
│
├── scripts/
│   ├── collect_inventory.py
│   ├── evidence_collector.py
│   ├── history_store.py
│   ├── knowledge_loader.py
│   └── rca_analyzer.py
│
├── tests/
│   ├── cpu/
│   ├── memory/
│   ├── storage/
│   ├── network/
│   └── fault/
│
├── runner.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Example Workflow

## Normal Validation

Run:

```bash
python runner.py
```

Example output:

```
Running TC_CPU_001
Running TC_CPU_STRESS_001
Running TC_MEMORY_STRESS_001
Running TC_STORAGE_FIO_001
Running TC_NETWORK_001

Report generated:
reports/validation_report.json
```

Generated report:

```json
{
    "test_case_id": "TC_NETWORK_001",
    "status": "PASS",
    "evidence": [
        "evidence/network/network_check.log"
    ]
}
```

---

# Failure Analysis Example

## Network Fault Injection

Fault injection test cases are expected to generate controlled failures.
A FAIL result indicates that the fault condition was successfully reproduced,
not that the validation framework failed.

Scenario:

```
Network unavailable condition
```

Workflow:

```
TC_FAULT_NETWORK_001

        |
        v

network_fault.log

        |
        v

Failure Knowledge Base

        |
        v

RCA Analyzer

        |
        v
Failure Classification

        |

        v

RCA Analysis

        |

        v

Regression Trigger

        |

        v


NET_LINK_DOWN_001

        |
        v

rca_report.json

        |
        v

failure_regression_map.yaml

        |
        v

Regression Runner

        |
        v

regression_report.json
```

Example RCA output:

```json
{
    "failure_id": "NET_LINK_DOWN_001",
    "component": "Network",
    "root_cause": "Network interface unavailable",
    "suggestion": "Check interface state and NIC link status",
    "confidence": 21,
    "matched_keywords": [
        "simulate network unavailable",
        "network",
        "unavailable"
    ]
}
```

---

# Regression Validation

Regression framework automatically selects and re-runs validation cases based on detected failure IDs.

The mapping between failure cases and regression tests is defined in:


config/failure_regression_map.yaml

Workflow:

```
Failure
   |
   v
RCA
   |
   v
Recovery
   |
   v
Regression Test
   |
   v
PASS / FAIL
```

Example:

```
NET_LINK_DOWN_001

        |
        v

Recovery Action

        |
        v

TC_NETWORK_001

        |
        v

PASS
```
Generated report:

reports/regression_report.json


Example:

```json
{
    "trigger_failure": "NET_LINK_DOWN_001",

    "recovery_action":
    "Check interface state and NIC link status",

    "results":
    [
        {
            "test_id":
            "TC_NETWORK_001",

            "result":
            "PASS"
        }
    ]
}
---

# Technology Stack

## Programming

- Python
- Shell / Bash

## Testing

- pytest

## Configuration

- YAML
- JSON

## Linux Tools

- ip
- lspci
- lsblk
- dmesg
- journalctl
- fio
- stress-ng

---

# AI-Assisted RCA (Future Work)

AI is designed to assist failure analysis.

Pipeline:

```
Raw Logs

    |

Log Parsing

    |

Structured Evidence

    |

AI Analysis

    |

RCA Suggestions
```

Expected AI output:

```
Observed Facts:

- Network connectivity failure detected


Possible Causes:

- Interface configuration issue
- NIC link problem


Recommended Checks:

- Check ethtool status
- Check kernel messages
```

AI will not determine PASS/FAIL.

Validation decisions remain based on:

- Test results
- Expected results
- Actual results
- Validation rules

---

# Current Status

## Completed

- Configuration-driven validation framework
- Automated test execution
- CPU validation
- Memory validation
- Storage validation
- Network validation
- Stress testing
- Fault injection framework
- Evidence collection
- Failure Knowledge Base
- Rule-based RCA
- Regression framework
- Failure-triggered regression execution
- Recovery action reporting

## In Progress

- AI-assisted log analysis
- Advanced failure report generation
- More realistic hardware validation


## Future Work

- Physical Linux DUT validation
- PCIe validation
- NVMe validation
- Kernel log analysis
- RAG-based failure retrieval
- AI evaluation

---

# How to Run

Complete workflow:

```bash
# 1. Run validation

python runner.py


# 2. Generate RCA

python scripts/rca_analyzer.py \
evidence/fault/network_fault.log


# 3. Run failure-triggered regression

python regression/regression_runner.py NET_LINK_DOWN_001

---


# Project Goal

This project aims to demonstrate:

- Understanding of Linux server validation workflow
- Ability to build automated testing infrastructure
- Experience with failure reproduction and diagnosis
- Evidence-driven debugging methodology
- AI-assisted system troubleshooting concepts

The final goal is to build a practical validation framework for Linux server and AI infrastructure testing scenarios.
