"""
Contains the Hadamard gate
"""

from .quantum_gate import QuantumGate
import numpy as np

class Hadamard(QuantumGate):
    """ 
    Implements the Hadamard gate 
    
        Parameters
        ------------
            target : 0 or 1, optional
                Specifies the target qubit, default is 0.
    
    """
    
    def __init__(self, target = 0):
        my_unitary = 1/np.sqrt(2)*np.array([[1,1], [1,-1]])
        qeye = np.diag([1,1])
        my_unitary = np.kron(my_unitary, qeye) if target is 0 else np.kron(qeye, my_unitary)
        QuantumGate.__init__(self, my_unitary)
