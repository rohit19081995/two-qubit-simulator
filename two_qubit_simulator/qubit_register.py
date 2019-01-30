"""
Contains the QubitRegister class
"""
import numpy as np

class QubitRegister(object): # pylint: disable=useless-object-inheritance
    """ Defines a qubit register with one or two qubits.
        
        Parameters
        ------------
        initial_state: numpy array
            The initial density matrix of the two qubit system.
        
        unitary: numpy array
            Unitary operation defined by the gate classes

    """

    def __init__(self, initial_state = None):
        """ Create a QubitRegister object """
        if (initial_state is None):
            initial_state = np.diag([1,0,0,0])
        self.state=initial_state/np.trace(initial_state)
        
    def apply_gate(self, gate):
        """ Apply a unitary state transformation on the qubit register """
        #Updates qubit state by applying unitary gate 'gate'
        if len(gate) is not 4:
            raise 'Wrong dimensions. Matrix dimensions should be 4', len(gate)
        self.state=gate.dot(self.state)

    def measure(self, number_of_samples=1):
        """ Perform a measurement of the qubit register by sampling from a uniform
            probability distribution.
        """
        #Defines number of qubits. In this version, it will be forced to be two qubits
        num_qubits = self.state.shape[0] // 2

        #Defines the projectors for both qubits
        projectors = [
        np.kron(
            pure_state_vector[:, np.newaxis],
            pure_state_vector[:, np.newaxis].T
        )
        for pure_state_vector in np.eye(num_qubits * 2)
        ]
        outcome_probabilities = [
            np.abs(np.trace(projector.dot(self.state))) for projector in projectors
        ]
        results = np.random.choice(
            [i for i in range(num_qubits * 2)],
            number_of_samples,
            p=outcome_probabilities)
        return [
            np.eye(num_qubits*2)[result, :] for result in results
        ]
