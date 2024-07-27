# Diff-Cult-Equations
## Differential Equations with Checkmarks and Crosses

This project contains Python code for solving basic differential equations using SciPy. The user can input the coefficients and initial conditions for the differential equations from the keyboard. The script also provides visual plots of the solutions.

## Operations Included

1. Solving a first-order linear differential equation <code>\( \frac{dy}{dt} = a \cdot y + b \)</code>
2. Solving a second-order linear differential equation <code>\( \frac{d^2y}{dt^2} = a \cdot y + b \cdot \frac{dy}{dt} + c \)</code>

## How to Use

1. Clone the repository:
    ```
    git clone https://github.com/yourusername/Diff-Cult-Equations.git
    ```

2. Navigate to the project directory:
    ```
    cd Diff-Cult-Equations
    ```

3. Install the dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Run the Python script:
    ```
    python differential_equations.py
    ```

5. Follow the prompts to input the coefficients and initial conditions for the differential equations. The script will then display a plot of the solution.

## Example

After running the script, you will be prompted to enter the coefficients and initial conditions for the differential equations. The script will then display a plot of the solution.

### Sample Input for First-order ODE
```
Choose the type of differential equation to solve:
1. First-order linear ODE (dy/dt = a*y + b)
2. Second-order linear ODE (d2y/dt2 = a*y + b*dy + c)
Enter 1 or 2: 1
Enter the coefficient a: 1
Enter the coefficient b: 2
Enter the initial condition y(0): 0
```

### Sample Output for First-order ODE
For the input coefficients <code>a = 1</code>, <code>b = 2</code>, and the initial condition <code>y(0) = 0</code>, the solution of the first-order differential equation <code>\( \frac{dy}{dt} = y + 2 \)</code> is:
```
y(t) = 2(e^t - 1)
```
The plot of this solution over time will show an exponential growth starting from <code>y(0) = 0</code>. Here are some sample values:
- At <code>t = 0</code>, <code>y(0) = 0</code>
- At <code>t = 1</code>, <code>y(1) \approx 4.4366</code>
- At <code>t = 2</code>, <code>y(2) \approx 12.7781</code>
- At <code>t = 3</code>, <code>y(3) \approx 38.8906</code>

### Sample Input for Second-order ODE
```
Choose the type of differential equation to solve:
1. First-order linear ODE (dy/dt = a*y + b)
2. Second-order linear ODE (d2y/dt2 = a*y + b*dy + c)
Enter 1 or 2: 2
Enter the coefficient a: 1
Enter the coefficient b: -2
Enter the coefficient c: 1
Enter the initial condition y(0): 0
Enter the initial condition dy/dt(0): 1
```

### Sample Output for Second-order ODE
For the input coefficients <code>a = 1</code>, <code>b = -2</code>, <code>c = 1</code>, and the initial conditions <code>y(0) = 0</code> and <code>\( \frac{dy}{dt}(0) = 1 \)</code>, the solution of the second-order differential equation <code>\( \frac{d^2y}{dt^2} = y - 2\frac{dy}{dt} + 1 \)</code> is:
```
y(t) = e^t - t - 1
```
The plot of this solution over time will show a curve that starts from <code>y(0) = 0</code> and initially rises due to the positive initial derivative. Here are some sample values:
- At <code>t = 0</code>, <code>y(0) = 0</code>
- At <code>t = 1</code>, <code>y(1) \approx 0.7183</code>
- At <code>t = 2</code>, <code>y(2) \approx 4.3891</code>
- At <code>t = 3</code>, <code>y(3) \approx 16.0855</code>

## Dependencies

- Python 3.x
- NumPy 1.21.0
- SciPy 1.7.1
- Matplotlib 3.4.3

Install the dependencies using pip:
```
pip install numpy==1.21.0 scipy==1.7.1 matplotlib==3.4.3
```

## License

This project is licensed under the MIT License.
