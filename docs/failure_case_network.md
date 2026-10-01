# Failure Case: Network Link Failure Injection


## 1. Overview

Failure ID:


NET_LINK_DOWN_001


Component:


Network



Purpose:

Validate that the system can detect network unavailable
conditions, collect failure evidence, perform RCA analysis,
and execute regression validation.


---

# 2. Test Scenario


Test Case:


TC_FAULT_NETWORK_001



Scenario:

Simulate a network unavailable condition.


Workflow:


Fault Injection

↓

Failure Detection

↓

Evidence Collection

↓

RCA Analysis

↓

Regression Validation



---

# 3. Fault Injection


Input:


network_fault.log



Example:



Network Fault Injection Test

Fault:
simulate network unavailable

Detection Result:
True



The purpose is to validate the failure detection workflow.

---

# 4. Evidence Collection


Generated evidence:


evidence/fault/network_fault.log



Collected information:

- Network state
- Interface information
- Fault injection information
- Detection result


Evidence is used as input for RCA.


---

# 5. Failure Knowledge Base


Knowledge file:


knowledge/network_fault.yaml



Failure definition:



Failure ID:
NET_LINK_DOWN_001



Symptoms:

- network unavailable
- connectivity failure


Possible causes:

- Network interface unavailable
- NIC link issue
- Driver or configuration issue


Recommended checks:

- ip link show
- ethtool
- dmesg


---

# 6. RCA Analysis


Tool:


scripts/rca_analyzer.py



Process:



network_fault.log

↓

Keyword Matching

↓

Failure Classification

↓

RCA Report



Generated report:


reports/rca_report.json



Example:


```json
{
    "failure_id": "NET_LINK_DOWN_001",
    "component": "Network",
    "root_cause":
    "Network interface unavailable",
    "confidence": 21
}

Note:

The RCA result represents a possible diagnosis
based on available evidence.

It is not a replacement for engineer verification.

7. Regression Validation

Regression test:

TC_NETWORK_001

Purpose:

Verify network validation after recovery.

Workflow:

Failure

↓

RCA

↓

Recovery Action

↓

TC_NETWORK_001

↓

Regression PASS
8. Complete Failure Loop

Final workflow:

TC_FAULT_NETWORK_001

        |

        v

network_fault.log

        |

        v

Failure Knowledge Base

        |

        v

Rule-based RCA

        |

        v

NET_LINK_DOWN_001

        |

        v

Regression Test

        |

        v

PASS
9. Lessons Learned

During development, keyword conflict appeared between:

NET_LINK_DOWN_001

and

NETWORK_001

Reason:

Generic network state information:

UNKNOWN
LOWER_UP
ens33

could match normal network configuration rules.

Solution:

Increase fault-specific evidence weight:

simulate network unavailable

to improve failure classification accuracy.

This demonstrates the importance of evidence quality
in failure diagnosis systems.


---

