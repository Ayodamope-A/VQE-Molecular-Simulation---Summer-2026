<h1>Methodology</h1>

<h2>Project Approach</h2>

<p>
  This project will use the Variational Quantum Eigensolver (VQE) to estimate
  the ground-state energy of a hydrogen molecule (H₂). The ground-state energy
  is the lowest possible energy that the molecule can have.
</p>

<p>Our main research question is:</p>

<h4>
  How does the number of circuit measurements, or shots, affect the accuracy
  of VQE’s estimation of a molecule’s ground-state energy?
</h4>

<p>
  We selected H₂ because it is one of the simplest molecules that can be
  studied with VQE. This makes it appropriate for our current beginner-level
  experience with quantum computing.
</p>

<h2>Software and Tools</h2>

<p>
  We plan to complete the project using Python in a Jupyter Notebook or a
  similar Python environment. The main libraries may include:
</p>

<ul>
  <li>Cirq for creating and simulating quantum circuits</li>
  <li>OpenFermion for representing the molecular Hamiltonian</li>
  <li>NumPy for mathematical calculations</li>
  <li>SciPy for the classical optimization process</li>
  <li>Matplotlib for creating graphs</li>
</ul>

<p>
  The exact libraries may change slightly as we develop and test the program.
</p>

<h2>Molecular Setup</h2>

<p>
  The molecule used in this project will be hydrogen, or H₂. It contains two
  hydrogen atoms and two electrons.
</p>

<p>
  We plan to use a standard H₂ bond length of approximately 0.74 angstroms. We
  will also use the STO-3G basis set, which is a basic basis set commonly used
  in beginner quantum-chemistry simulations.
</p>

<p>
  The molecular information will be used to create a Hamiltonian. The
  Hamiltonian is a mathematical representation of the total energy of the
  molecule.
</p>

<h2>Converting the Hamiltonian</h2>

<p>
  The molecular Hamiltonian is originally written using information about
  electrons. A quantum computer, however, performs calculations using qubits.
</p>

<p>
  We will use a mapping method, such as the Jordan–Wigner transformation, to
  convert the molecular Hamiltonian into a qubit Hamiltonian. The resulting
  Hamiltonian will be represented as a collection of Pauli terms that can be
  measured using a quantum circuit.
</p>

<p>
  Our initial project design will use a four-qubit representation of H₂ unless
  the software or project requirements lead us to use a reduced two-qubit
  version. Any reduction made during the project will be explained in the
  final report.
</p>

<h2>Exact Energy Calculation</h2>

<p>
  Before running VQE, we will calculate the ground-state energy of the
  Hamiltonian using an exact classical method. This result will be used as the
  reference value for our experiment.
</p>

<p>
  In this project, “exact energy” means the exact result for the simplified H₂
  model and basis set used in our simulation. It does not represent the
  perfectly exact energy of an H₂ molecule in the real world.
</p>

<h2>VQE Circuit</h2>

<p>
  We will create a parameterized quantum circuit called an ansatz. The ansatz
  will prepare a trial quantum state that represents a possible state of the
  H₂ molecule.
</p>

<p>
  The circuit will begin with an initial state representing the electrons in
  the molecule. It will then use parameterized rotation gates and entangling
  gates, such as CNOT gates. The rotation angles will act as the adjustable
  parameters of the circuit.
</p>

<p>
  A quantum simulator will run the circuit and estimate the energy of the
  prepared state. A classical optimizer will then adjust the circuit
  parameters to search for a lower energy.
</p>

<p>
  This process will repeat until the optimizer reaches its stopping condition
  or cannot find a meaningfully lower energy.
</p>

<h2>Shot-Count Experiment</h2>

<p>
  A shot is one execution and measurement of a quantum circuit. Since quantum
  measurements are probabilistic, a small number of shots may produce an
  energy estimate that varies more from one trial to another. Increasing the
  number of shots should generally produce a more stable estimate, although it
  also requires more circuit executions.
</p>

<p>We plan to test several shot counts, such as:</p>

<ul>
  <li>100 shots</li>
  <li>500 shots</li>
  <li>1,000 shots</li>
  <li>5,000 shots</li>
  <li>10,000 shots</li>
</ul>

<p>
  We may adjust these values depending on the simulator’s performance and the
  time available to complete the project.
</p>

<p>
  The molecule, Hamiltonian, ansatz, and other main settings will remain the
  same during the experiment. The number of shots will be the main value that
  changes.
</p>

<h2>Experimental Procedure</h2>

<p>The experiment will follow these basic steps:</p>

<ol>
  <li>Define the structure and basic properties of the H₂ molecule.</li>
  <li>Generate the molecular Hamiltonian.</li>
  <li>Convert the molecular Hamiltonian into a qubit Hamiltonian.</li>
  <li>
    Calculate the exact ground-state energy using a classical method.
  </li>
  <li>Create the parameterized VQE circuit.</li>
  <li>Select a starting value for the circuit parameters.</li>
  <li>Use the quantum simulator to estimate the energy.</li>
  <li>Use a classical optimizer to adjust the circuit parameters.</li>
  <li>Record the final VQE energy.</li>
  <li>
    Calculate the difference between the VQE result and the exact energy.
  </li>
  <li>Repeat the process using different numbers of shots.</li>
  <li>Compare the results from the different shot counts.</li>
</ol>

<p>
  Because measurements include randomness, we plan to run each shot-count
  setting more than once. If time allows, each setting will be tested
  approximately five times. This will help us determine whether the results
  are consistent instead of depending on only one trial.
</p>

<h2>Data Collection</h2>

<p>For each experiment, we plan to record:</p>

<ul>
  <li>Number of shots</li>
  <li>Trial number</li>
  <li>Exact ground-state energy</li>
  <li>VQE-estimated energy</li>
  <li>Difference between the VQE and exact energies</li>
  <li>Number of optimization steps</li>
  <li>Whether the optimizer completed successfully</li>
</ul>

<p>
  The results will be stored in a table or CSV file so they can be reviewed
  and used to create graphs.
</p>

<h2>Measuring Accuracy</h2>

<p>
  The main measurement of accuracy will be the absolute energy error:
</p>

<p>
  <strong>
    Absolute error = |VQE-estimated energy − exact energy|
  </strong>
</p>

<p>
  A smaller error will mean that the VQE result is closer to the exact result
  and is therefore more accurate.
</p>

<p>
  We will also calculate the average VQE energy and average error for each shot
  count. If possible, we will record how much the results vary between
  repeated trials.
</p>

<h2>Presenting the Results</h2>

<p>The final results may be presented using:</p>

<ul>
  <li>A table comparing the exact and VQE energies</li>
  <li>
    A graph showing the number of shots compared with the energy error
  </li>
  <li>
    A graph showing how the estimated energy changes during optimization
  </li>
  <li>A circuit diagram showing the VQE ansatz</li>
</ul>

<p>
  These results will help us determine whether increasing the number of shots
  improves the accuracy and consistency of the VQE energy estimate.
</p>

<h2>Controlled Variables</h2>

<p>
  To make the comparison fair, we will try to keep the following settings the
  same:
</p>

<ul>
  <li>H₂ molecular geometry</li>
  <li>Bond length</li>
  <li>Basis set</li>
  <li>Qubit Hamiltonian</li>
  <li>Qubit-mapping method</li>
  <li>VQE circuit</li>
  <li>Classical optimizer</li>
  <li>Initial circuit parameters</li>
  <li>Maximum number of optimization steps</li>
</ul>

<p>
  Keeping these settings constant will allow us to focus mainly on the effect
  of changing the shot count.
</p>

<h2>Limitations</h2>

<p>
  This project has several limitations. First, the experiment will be
  performed using a quantum simulator instead of a real quantum computer.
  Therefore, it may not include hardware problems such as gate errors,
  environmental noise, or loss of quantum information.
</p>

<p>
  H₂ is also a very small and simple molecule, so the results may not apply
  directly to larger molecules. The accuracy of VQE can also be affected by
  the selected circuit, optimizer, basis set, and starting parameters—not only
  by the number of shots.
</p>

<p>
  Finally, our project is intended as a beginner-level demonstration of VQE.
  Its purpose is to understand the basic VQE workflow and observe how quantum
  measurement affects the estimated energy, rather than to develop a new or
  advanced VQE method.
</p>


