"""
Testing the qubit_register module
"""
import numpy as np

from two_qubit_simulator.qubit_register import QubitRegister

def check_register(register):
	'''
	Checks properties of density matrices.
	'''	
	# Trace should be 1
	assert np.trace(register) == 1

    # Diagonal elements must be positive
    assert np.all(register.diagonal()) >= 0

    # shape must be 4x4
    assert register.shape == (4,4)

def test_qubit_register():

	# |0>
	zero = np.array([[1,0], [0,0]])
	one = np.array([[0,0], [0,1]])

	# Test 1 : |00>
	initial_state = np.kron(zero, zero)
	qubit_register = QubitRegister(initial_state)
	check_register(qubit_register.state)
	initial_state = initial_state/np.trace(initial_state)

	assert np.allclose(qubit_register.state.flatten(), initial_state.flatten())

	assert np.allclose(np.array(qubit_register.measure(5000)).average(axis=0), [1, 0, 0, 0])

	# Test 2 : |01>
	initial_state = np.kron(zero, one)
	qubit_register = QubitRegister(initial_state)
	check_register(qubit_register.state)
	initial_state = initial_state/np.trace(initial_state)

	assert np.allclose(qubit_register.state.flatten(), initial_state.flatten())

	assert np.allclose(np.array(qubit_register.measure(5000)).average(axis=0), [0, 1, 0, 0])

	# Test 3 : |11>
	initial_state = np.kron(one, one)
	qubit_register = QubitRegister(initial_state)
	check_register(qubit_register.state)
	initial_state = initial_state/np.trace(initial_state)

	assert np.allclose(qubit_register.state.flatten(), initial_state.flatten())

	assert np.allclose(np.array(qubit_register.measure(5000)).average(axis=0), [0, 0, 0, 1])

	# Test 4 : (|00> + |11>)/sqrt(2)
	initial_state = np.kron(zero, zero) + np.kron(one, one)
	qubit_register = QubitRegister(initial_state)
	check_register(qubit_register.state)
	initial_state = initial_state/np.trace(initial_state)

	assert np.allclose(qubit_register.state.flatten(), initial_state.flatten())

	assert np.allclose(np.array(qubit_register.measure(5000)).average(axis=0), [0.5, 0, 0, 0.5])

	# Test 5 : (|01> + |10>)/sqrt(2)
	initial_state = np.kron(zero, one) + np.kron(one, zero)
	qubit_register = QubitRegister(initial_state)
	check_register(qubit_register.state)
	initial_state = initial_state/np.trace(initial_state)

	assert np.allclose(qubit_register.state.flatten(), initial_state.flatten())

	assert np.allclose(np.array(qubit_register.measure(5000)).average(axis=0), [0, 0.5, 0.5, 0])

	# Test 6 : mixed
	initial_state = np.kron(zero, one) + np.kron(one, zero) + np.kron(zero, zero) + np.kron(one, one)
	qubit_register = QubitRegister(initial_state)
	check_register(qubit_register.state)
	initial_state = initial_state/np.trace(initial_state)

	assert np.allclose(qubit_register.state.flatten(), initial_state.flatten())

	assert np.allclose(np.array(qubit_register.measure(5000)).average(axis=0), [0.25, 0.25, 0.25, 0.25])

	# Test 7 : should work with list
	initial_state = list(np.kron(zero, zero))
	qubit_register = QubitRegister(initial_state)
	check_register(qubit_register.state)
	initial_state = initial_state/np.trace(initial_state)

	assert np.allclose(qubit_register.state.flatten(), np.array(initial_state).flatten())

	assert np.allclose(np.array(qubit_register.measure(5000)).average(axis=0), [1, 0, 0, 0])

	# Test 8 : some random ones
	for _ in range(10):
		initial_state = np.random.rand(4, 4)
		qubit_register = QubitRegister(initial_state)
		check_register(qubit_register.state)
		initial_state = initial_state/np.trace(initial_state)

		assert np.allclose(qubit_register.state.flatten(), np.array(initial_state).flatten())

