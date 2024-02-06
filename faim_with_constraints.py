import numpy as np
from scipy.optimize import minimize

def functional_additive_index_model(params, X, y):
    """
    Functional additive-index model with constraints.

    Parameters:
    params (array): Parameters to be optimized.
    X (array): Independent variables.
    y (array): Dependent variable.

    Returns:
    float: Negative log-likelihood of the model.
    """
    # Extracting parameters
    beta = params[:-1]  # Coefficients
    alpha = params[-1]  # Intercept
    
    # Linear combination of predictors
    linear_pred = np.dot(X, beta) + alpha
    
    # Calculate the negative log-likelihood (assuming Gaussian errors)
    neg_log_likelihood = np.sum((y - linear_pred)**2)
    
    return neg_log_likelihood

# Example data
X = np.array([[1, 2],
              [3, 4],
              [5, 6]])
y = np.array([10, 20, 30])

# Example constraints
constraints = ({'type': 'eq', 'fun': lambda x: x[-1] - 5})  # Constraint: Intercept = 5

# Initial guess for parameters
initial_params = np.zeros(X.shape[1] + 1)

# Optimize the model
result = minimize(functional_additive_index_model, initial_params, args=(X, y), constraints=constraints)

# Extract the optimized parameters
optimal_params = result.x

print("Optimized parameters:", optimal_params)
