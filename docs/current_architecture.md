# Current Architecture


## Execution Flow

runner.py

↓

pytest test cases

↓

Evidence Collection

↓

validation_report.json

↓

RCA Analyzer

↓

rca_report.json

↓

History Storage

↓

Regression Runner

↓

regression_report.json


## Current Configuration

config/test_plan.yaml

- Test case description


config/evidence_map.yaml

- Test evidence mapping


regression/regression_plan.yaml

- Regression execution list
