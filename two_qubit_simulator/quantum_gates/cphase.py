"""
Contains the CPHASE gate
"""

from .quantum_gate import QuantumGate
import numpy as np

class CPHASE(QuantumGate):
    """ Implements the CPHASE gate """
    
    def __init__(self, target = 0):
        my_unitary = np.diag([1,1,1,-1])
        QuantumGate.__init__(self, my_unitary)
