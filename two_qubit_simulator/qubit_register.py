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

    def __init__(self, initial_state=np.kron(np.array([[0.5, 0.5], [0.5, 0.5]]), np.array([[0.5, 0.5], [0.5, 0.5]]))):
        """ Create a QubitRegister object """
        self.state=initial_state


    def apply_unitary(self, unitary=np.kron(np.array([[1.0, 0.0], [0.0, 1.0]]), np.array([[1.0, 0.0], [0.0, 1.0]]))):
        """ Apply a unitary state transformation on the qubit register """
        #Updates qubit state by applying unitary gate 'unitary'

        if len(unitary) is not 4:
            raise 'Wrong dimensions. Matrix dimensions should be 4', len(unitary)
        self.state=unitary.dot(self.state)

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
