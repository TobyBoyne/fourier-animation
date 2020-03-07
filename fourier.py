"""
Calculates the Fourier coefficients for a given set of data points
"""

import numpy as np

def get_points_for_trapz(points, N, L):
	"""Convert an array of [t, x] points to be ready for integration
	Output is a 2D array with columns [t, d, a_1, ..., a_n, b_1, ..., b_n],
	   where each column corresponds to the value of the integrand at point t
	These columns can then be integrated down via the trapezium rule

	This will create columns up to the Nth coefficient of the Fourier series"""

	ts = points[:, 0]
	xs = points[:, 1]

	d = xs * 0.5

	a_n = np.array([xs * np.cos(n * xs * np.pi / L) for n in range(1, N+1)])

	b_n = np.array([xs * np.sin(n * xs * np.pi / L) for n in range(1, N+1)])

	integrand_values = np.array([ts, d, *a_n, *b_n])
	print(integrand_values.T)
	return integrand_values.T

if __name__ == "__main__":
	points = np.array([
		[1, 2],
		[4, 3]
	])

	L = 5
	get_points_for_trapz(points, 5, L)