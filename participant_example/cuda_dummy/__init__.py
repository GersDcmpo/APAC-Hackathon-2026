"""CUDA dummy example: synthetic training → checkpoint → fresh-worker CUDA inference (SPEC-16).

DEMO only (`example_only=true`, DEMO checklist). Not a TRL model or baseline. Importing this package
does not import torch; `model`, `train` and `adapter` import torch where they need it.
"""
