# Import 

import numpy as np
import matplotlib.pyplot as plt


from models.test_functions import ThreeHumpCamel
from optimizers.momentum import Momentum
from optimizers.SGD import SGD
from optimizers.NesterovMomentum import NesterovMomentum

# Main

if __name__ == '__main__':
    
    np.random.seed(1)

    ## Initialize function and optimizer
    x0, y0 = 1.8, -1.8
    function = ThreeHumpCamel(x0, y0)

    sgd = SGD(learning_rate=0.5)
    momentum = Momentum(learning_rate=0.3, gamma=0.9)
    nesterov = NesterovMomentum(learning_rate=0.3, gamma=0.9)

    n_steps = 35

    xs_sgd, ys_sgd = np.zeros(n_steps + 1), np.zeros(n_steps + 1)
    xs_sgd[0], ys_sgd[0] = x0, y0
    

    for i in range(n_steps):
        print(f'Step {i+1} : {function.forward()}')
        grads = function.backward()
        new_params = sgd.step(function.params, grads)
        function.update(new_params)
        xs_sgd[i+1], ys_sgd[i+1] = new_params['x'], new_params['y']

    function.update({'x': x0, 'y': y0})

    xs_momentum, ys_momentum = np.zeros(n_steps + 1), np.zeros(n_steps + 1)
    xs_momentum[0], ys_momentum[0] = x0, y0

    for i in range(n_steps):
        print(f'Step {i+1} : {function.forward()}')
        grads = function.backward()
        new_params = momentum.step(function.params, grads)
        function.update(new_params)
        xs_momentum[i+1], ys_momentum[i+1] = new_params['x'], new_params['y']


    function.update({'x': x0, 'y': y0})

    xs_nesterov, ys_nesterov = np.zeros(n_steps + 1), np.zeros(n_steps + 1)
    xs_nesterov[0], ys_nesterov[0] = x0, y0

    for i in range(n_steps):
        print(f'Step {i+1} : {function.forward()}')
        grads = function.backward()
        new_params = nesterov.step(function.params, grads)
        function.update(new_params)
        xs_nesterov[i+1], ys_nesterov[i+1] = new_params['x'], new_params['y']


    # Plotting
    x_vals = np.linspace(-2.01, 2.01, 100)
    y_vals = np.linspace(-2.01, 2.01, 100)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = function.evaluate(X, Y)

    plt.figure(figsize=(8, 6))
    contours = plt.contour(X, Y, Z, levels=50, cmap='viridis')
    plt.clabel(contours, inline=True, fontsize=8)
    plt.plot(xs_sgd, ys_sgd, marker='o', color='red', label='SGD')
    plt.plot(xs_momentum, ys_momentum, marker='o', color='green', label='Momentum')
    plt.plot(xs_nesterov, ys_nesterov, marker='o', color='blue', label='Nesterov')
    plt.title("Optimizer Trajectory")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.show()