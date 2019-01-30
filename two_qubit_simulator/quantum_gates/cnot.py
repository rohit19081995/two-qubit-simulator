"""
Contains the CNOT gate
"""

from .quantum_gate import QuantumGate
import numpy as np

class CNOT(QuantumGate):
    """ Implements the CNOT gate 
        Parameters
        ------------
            target : 0 or 1, optional
                Specifies the target qubit, default is 0.
    
    """
    
    def __init__(self, target = 0):
        X = np.array([[0,1],[1,0]])
        ground = np.diag([1,0])
        excited = np.diag([0,1])
        qeye = np.diag([1,1])
        if (target is 0):
            my_unitary = np.kron(qeye, ground) + np.kron(X, excited)
        else:
            my_unitary = np.kron(ground, qeye) + np.kron(excited, X)
        QuantumGate.__init__(self, my_unitary)
