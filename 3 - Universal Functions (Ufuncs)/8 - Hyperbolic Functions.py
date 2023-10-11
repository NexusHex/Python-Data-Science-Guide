import numpy as np

# Hyperbolic functions are an extension of trigonometric functions, and involve values like sinh, cosh and tanh

# PART I.I - USING HYPERBOLIC FUNCTIONS ON SINGLE VALUES:
# You can use the ufuncs np.sinh(), np.cosh() and np.tanh() to calculate radians using hyperbolic functions:

print(np.sinh(np.pi/2))
print(np.cosh(np.pi/2))
print(np.tanh(np.pi/2))

# PART I.II - USING HYPERBOLIC FUNCTIONS ON ARRAYS:
# Like trigonometric functions, you simply need to pass in the whole array of radians into the hyperbolic function, and it will return the result:

a = np.array([[np.pi/2, np.pi/3, np.pi/4, np.pi/5]])

print(np.sinh(a))

# PART II.I - FINDING ANGLES:
# You can find angles from values of hyperbolic sin, cos and tan (sinh, cos, tanh inverse - arcsinh, arccosh, arctanh)

print(np.arcsinh(1.0))

# PART II.II - FINDING ANGLES FROM AN ARRAY:
# Same thing, just pass the whole array of radians:

b = np.array([0.1, 0.2, 0.5])

print(np.arctanh(b))

# Now that you know how to calculate radians using hyperbolic functions, you can move onto learning about set operations. See you in Lesson 9!