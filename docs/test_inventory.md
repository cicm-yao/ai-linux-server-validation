# Test Inventory


| Test ID | Script | Component | Evidence | Status |
|---|---|---|---|---|
| TC_CPU_001 | tests/cpu/test_cpu.py | CPU Discovery | inventory/reports/inventory_report.json | Done |
| TC_CPU_STRESS_001 | tests/cpu/test_cpu_stress.py | CPU Stress | evidence/cpu/cpu_stress.log | Done |
| TC_MEMORY_STRESS_001 | tests/memory/test_memory_stress.py | Memory Stress | evidence/memory/memory_stress.log | Done |
| TC_STORAGE_FIO_001 | tests/storage/test_storage_fio.py | Storage/FIO | evidence/storage/storage_fio.log | Done |
| TC_NETWORK_001 | tests/network/test_network_check.py | Network | evidence/network/network_check.log | Done |
| TC_FAULT_CPU_001 | tests/fault/test_cpu_fault_injection.py | Fault Injection | evidence/fault/cpu_fault.log | Implemented |
