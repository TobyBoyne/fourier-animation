"""
Calculates the Fourier coefficients for a given set of data points
"""

import numpy as np


class Fourier:
	def __init__(self, points, N):
		self.d = 0
		self.a_n = np.zeros(N)
		self.b_n = np.zeros(N)

		self.L = points[-1, 0] - points[0, 0]

		values = self.get_points_for_trapz(points, N)
		self.integrate_coefficients(values, N)

	def get_points_for_trapz(self, points, N):
		"""Convert an array of [t, x] points to be ready for integration
		Output is a 2D array with rows [t, d, a_1, ..., a_n, b_1, ..., b_n],
		   where each row corresponds to the value of the integrand at point t
		These rows can then be integrated across via the trapezium rule

		This will create rows up to the Nth coefficient of the Fourier series"""

		ts = points[:, 0]
		xs = points[:, 1]

		d = xs * 0.5

		a_n = np.array([xs * np.cos(2 * n * ts * np.pi / self.L) for n in range(1, N+1)])

		b_n = np.array([xs * np.sin(2 * n * ts * np.pi / self.L) for n in range(1, N+1)])

		integrand_values = np.array([ts, d, *a_n, *b_n])

		return integrand_values


	def integrate_coefficients(self, integrand_values, N):
		ts, values = integrand_values[0, :], integrand_values[1:, 0:]

		coeffs = np.trapz(values, x=ts, axis=1)
		coeffs *= (2 / self.L)

		self.d = coeffs[0]
		self.a_n = coeffs[1:1+N]
		self.b_n = coeffs[1+N:]


	def __call__(self, t):
		"""Evaluate the fourier series f(t) at a time t"""
		f = 0
		f += self.d

		n = np.arange(1, len(self.a_n)+1)
		f += self.a_n * np.cos(2 * n * t * np.pi / self.L)
		f += self.b_n * np.sin(2 * n * t * np.pi / self.L)

		return f


if __name__ == "__main__":
	points = np.array([
		[1, 2],
		[4, 3]
	])
