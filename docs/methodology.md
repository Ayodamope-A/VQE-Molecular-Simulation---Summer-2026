# VQE Molecular Simulation Project

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
methodology.md
# Methodology

## Project Approach

This project will use the Variational Quantum Eigensolver (VQE) to estimate the ground-state energy of a hydrogen molecule (H₂). The ground-state energy is the lowest possible energy that the molecule can have.

Our main research question is:

> How does the number of circuit measurements, or shots, affect the accuracy of VQE’s estimation of a molecule’s ground-state energy?

We selected H₂ because it is one of the simplest molecules that can be studied with VQE. This makes it appropriate for our current beginner-level experience with quantum computing.

## Software and Tools

We plan to complete the project using Python in a Jupyter Notebook or a similar Python environment. The main libraries may include:

- Cirq for creating and simulating quantum circuits
- OpenFermion for representing the molecular Hamiltonian
- NumPy for mathematical calculations
- SciPy for the classical optimization process
- Matplotlib for creating graphs

The exact libraries may change slightly as we develop and test the program.

## Molecular Setup

The molecule used in this project will be hydrogen, or H₂. It contains two hydrogen atoms and two electrons.

We plan to use a standard H₂ bond length of approximately 0.74 angstroms. We will also use the STO-3G basis set, which is a basic basis set commonly used in beginner quantum-chemistry simulations.

The molecular information will be used to create a Hamiltonian. The Hamiltonian is a mathematical representation of the total energy of the molecule.

## Converting the Hamiltonian

The molecular Hamiltonian is originally written using information about electrons. A quantum computer, however, performs calculations using qubits.

We will use a mapping method, such as the Jordan–Wigner transformation, to convert the molecular Hamiltonian into a qubit Hamiltonian. The resulting Hamiltonian will be represented as a collection of Pauli terms that can be measured using a quantum circuit.

Our initial project design will use a four-qubit representation of H₂ unless the software or project requirements lead us to use a reduced two-qubit version. Any reduction made during the project will be explained in the final report.

## Exact Energy Calculation

Before running VQE, we will calculate the ground-state energy of the Hamiltonian using an exact classical method. This result will be used as the reference value for our experiment.

In this project, “exact energy” means the exact result for the simplified H₂ model and basis set used in our simulation. It does not represent the perfectly exact energy of an H₂ molecule in the real world.

## VQE Circuit

We will create a parameterized quantum circuit called an ansatz. The ansatz will prepare a trial quantum state that represents a possible state of the H₂ molecule.

The circuit will begin with an initial state representing the electrons in the molecule. It will then use parameterized rotation gates and entangling gates, such as CNOT gates. The rotation angles will act as the adjustable parameters of the circuit.

A quantum simulator will run the circuit and estimate the energy of the prepared state. A classical optimizer will then adjust the circuit parameters to search for a lower energy.

This process will repeat until the optimizer reaches its stopping condition or cannot find a meaningfully lower energy.

## Shot-Count Experiment

A shot is one execution and measurement of a quantum circuit. Since quantum measurements are probabilistic, a small number of shots may produce an energy estimate that varies more from one trial to another. Increasing the number of shots should generally produce a more stable estimate, although it also requires more circuit executions.

We plan to test several shot counts, such as:

- 100 shots
- 500 shots
- 1,000 shots
- 5,000 shots
- 10,000 shots

We may adjust these values depending on the simulator’s performance and the time available to complete the project.

The molecule, Hamiltonian, ansatz, and other main settings will remain the same during the experiment. The number of shots will be the main value that changes.

## Experimental Procedure

The experiment will follow these basic steps:

1. Define the structure and basic properties of the H₂ molecule.
2. Generate the molecular Hamiltonian.
3. Convert the molecular Hamiltonian into a qubit Hamiltonian.
4. Calculate the exact ground-state energy using a classical method.
5. Create the parameterized VQE circuit.
6. Select a starting value for the circuit parameters.
7. Use the quantum simulator to estimate the energy.
8. Use a classical optimizer to adjust the circuit parameters.
9. Record the final VQE energy.
10. Calculate the difference between the VQE result and the exact energy.
11. Repeat the process using different numbers of shots.
12. Compare the results from the different shot counts.

Because measurements include randomness, we plan to run each shot-count setting more than once. If time allows, each setting will be tested approximately five times. This will help us determine whether the results are consistent instead of depending on only one trial.

## Data Collection

For each experiment, we plan to record:

- Number of shots
- Trial number
- Exact ground-state energy
- VQE-estimated energy
- Difference between the VQE and exact energies
- Number of optimization steps
- Whether the optimizer completed successfully

The results will be stored in a table or CSV file so they can be reviewed and used to create graphs.

## Measuring Accuracy

The main measurement of accuracy will be the absolute energy error:

\[
\text{Absolute error} = |E_{\text{VQE}} - E_{\text{exact}}|
\]

A smaller error will mean that the VQE result is closer to the exact result and is therefore more accurate.

We will also calculate the average VQE energy and average error for each shot count. If possible, we will record how much the results vary between repeated trials.

## Presenting the Results

The final results may be presented using:

- A table comparing the exact and VQE energies
- A graph showing the number of shots compared with the energy error
- A graph showing how the estimated energy changes during optimization
- A circuit diagram showing the VQE ansatz

These results will help us determine whether increasing the number of shots improves the accuracy and consistency of the VQE energy estimate.

## Controlled Variables

To make the comparison fair, we will try to keep the following settings the same:

- H₂ molecular geometry
- Bond length
- Basis set
- Qubit Hamiltonian
- Qubit-mapping method
- VQE circuit
- Classical optimizer
- Initial circuit parameters
- Maximum number of optimization steps

Keeping these settings constant will allow us to focus mainly on the effect of changing the shot count.

## Limitations

This project has several limitations. First, the experiment will be performed using a quantum simulator instead of a real quantum computer. Therefore, it may not include hardware problems such as gate errors, environmental noise, or loss of quantum information.

H₂ is also a very small and simple molecule, so the results may not apply directly to larger molecules. The accuracy of VQE can also be affected by the selected circuit, optimizer, basis set, and starting parameters—not only by the number of shots.

Finally, our project is intended as a beginner-level demonstration of VQE. Its purpose is to understand the basic VQE workflow and observe how quantum measurement affects the estimated energy, rather than to develop a new or advanced VQE method.



