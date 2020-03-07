"""
Calculates the Fourier coefficients for a given set of data points
"""

import numpy as np


class Fourier:
	def __init__(self, points, N):
		self.d = 0
		self.a_n = np.zeros(N)
		self.b_n = np.zeros(N)

		L = points[-1, 0] - points[0, 0]

		self.get_poitns_for_trapz(points, L)

	def get_points_for_trapz(self, points, N, L):
		"""Convert an array of [t, x] points to be ready for integration
		Output is a 2D array with rows [t, d, a_1, ..., a_n, b_1, ..., b_n],
		   where each row corresponds to the value of the integrand at point t
		These rows can then be integrated across via the trapezium rule

		This will create rows up to the Nth coefficient of the Fourier series"""

		ts = points[:, 0]
		xs = points[:, 1]

		d = xs * 0.5

		a_n = np.array([xs * np.cos(n * ts * np.pi / L) for n in range(1, N+1)])

		b_n = np.array([xs * np.sin(n * ts * np.pi / L) for n in range(1, N+1)])

		integrand_values = np.array([ts, d, *a_n, *b_n])

		return integrand_values

	def integrate_coefficients(self, integrand_values, N):
		ts, values = integrand_values[0, :], integrand_values[1:, 0:]

		coeffs = np.trapz(values, x=ts, axis=1)

		d = coeffs[0]
		a_n = coeffs[1:1+N]
		b_n = coeffs[1+N:]

		return d, a_n, b_n


if __name__ == "__main__":
	points = np.array([
		[1, 2],
		[4, 3]
	])

	L = points[-1, 0] - points[0, 0]
	get_points_for_trapz(points, 5, L)