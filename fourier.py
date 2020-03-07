"""
Calculates the Fourier coefficients for a given set of data points
"""

import numpy as np

def get_points_for_trapz(points):
	"""Convert an array of [t, x] points to be ready for integration
	Output is a 2D array with columns [t, x, 0.5x, sin(x)x, cos(x)]
	These columns can then be integrated down via the trapezium rule"""

	xs = points[:, 1]
	print(xs)


if __name__ == "__main__":
	points = np.array([
		[1, 2],
		[2, 3]
	])

	get_points_for_trapz(points)