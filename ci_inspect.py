#!/usr/bin/env python


"""
Runtime environment inspection for Kaizen PoC.
Shows whether vllm & Neuron libs are visible, and from where.
"""

import importlib, sys

print("=== pip list (neuron|vllm) ===")
try:
    import pkg_resources
    for dist in pkg_resources.working_set:
        n = dist.project_name.lower()
        if "neuron" in n or "vllm" in n:
            print(f"{dist.project_name} {dist.version}")
except Exception as e:
    print(f"(pkg_resources error: {e})")

print("\n=== import locations ===")
for m in ["vllm", "torch_neuronx", "neuronx_distributed", "torch"]:
    try:
        mod = importlib.import_module(m)
        print(f"{m}: OK @ {getattr(mod, '__file__', None)}")
    except Exception as exc:
        print(f"{m}: FAIL -> {exc}")

print("\n=== Top sys.path ===")
for p in sys.path[:20]:
    print("  ", p)
