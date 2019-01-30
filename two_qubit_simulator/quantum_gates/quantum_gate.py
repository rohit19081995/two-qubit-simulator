"""
Contains the base class for one and two qubit quantum gates
"""
import numpy as np

class QuantumGate(object): # pylint: disable=useless-object-inheritance
    """
        Base class for a quantum gate

        Parameters
        ------------
            symbol : str, optional
                The symbol representing the gate. This is used when producing string
                representations of circuits.
            unitary_operator : numpy array
                The (unitary) operator that implements the desired gate
    
        - - - CONTINUE DOUMENTATION FROM HERE - - -

    """
    def __init__(self, unitary_operator, symbol=None):
        """ Create a QuantumGate object """
        self.symbol = symbol
        self.unitary_operator = unitary_operator.astype(np.complex128)
        self.EPSILON = 1e-3

        self.assert_operation_is_unitary()

    def assert_operation_is_unitary(self):
        """ Checks that the input unitary operator is unitary """
        #for line in self.unitary_operator:
        #    assert((abs(line).sum() - 1.0) < self.EPSILON)
        U = np.matrix(self.unitary_operator)
        assert abs(np.dot(U, U.H) - np.diag(np.ones(4))).max() < self.EPSILON
        assert abs(np.dot(U.H, U) - np.diag(np.ones(4))).max() < self.EPSILON
        

    def __call__(self, register):
        """ Apply the gate to a given qubit register. See apply_register method """
        self.apply_gate(register)


    def apply_gate(self, register):
        """ Apply the gate to a given qubit register. See apply_register method.

            Parameters
            ------------
                register : .qubit_register.QubitRegister
                    The register of qubits to which the gate is applied
        """
        register.apply_unitary(self.unitary_operator)

    def __repr__(self):
        """
            Print a representation of the gate using the class name and the symbol and
            unitary_operator attribute
        """
        return 'QuantumGate {} ({}):,\n'.format(
            self.__class__.__name__, self.symbol) + repr(self.unitary_operator)
