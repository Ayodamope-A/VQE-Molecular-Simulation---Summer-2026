# VQE-Molecular-Simulation---Summer-2026

## Overview

This project explores how the number of quantum-circuit measurements, known as shots, affects the accuracy of the Variational Quantum Eigensolver (VQE).

We will use VQE to estimate the ground-state energy of a hydrogen molecule (H₂) and compare the result with an exact classical calculation.

## Research Question

> How does the number of circuit measurements affect the accuracy of VQE’s estimation of a molecule’s ground-state energy?

## Project Approach

Our experiment will:

1. Create a simplified Hamiltonian for H₂.
2. Convert the Hamiltonian into a qubit representation.
3. Calculate the exact ground-state energy.
4. Build and simulate a VQE circuit.
5. Test VQE using different numbers of shots.
6. Compare the estimated energies with the exact result.

## Tools

The project may use:

- Python
- Cirq
- OpenFermion
- NumPy
- SciPy
- Matplotlib

## Repository Contents

- `methodology.md` — Explanation of the experimental method
- `README.md` — General project overview
- `notebooks/` — VQE experiments and demonstrations
- `src/` — Main Python code
- `data/` — Experimental results
- `results/` — Tables, graphs, and circuit diagrams

## Project Status

This project is currently under development as part of our beginner-level study of quantum computing and VQE.

- `references.md` — Research papers and resources used in the project.
