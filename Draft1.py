#Written by Rudra
#Roll Number - 240041031

from qiskit import QuantumCircuit

# Create quantum circuit with 4 qubits and 4 classical bits
q_circ = QuantumCircuit(4, 4)
q_circ.x([0,1])          # x gate on q0 & q1
q_circ.barrier()
q_circ.cx(1,2)           # control not gate  on q2 
q_circ.cx(0,2)           # control not gate  on q2
q_circ.ccx(0,1,3)        # control control not gate
q_circ.barrier()
q_circ.measure([0, 1, 2, 3], [0, 1, 2, 3])  # measurement  

# Drawing Circuit
print(q_circ)