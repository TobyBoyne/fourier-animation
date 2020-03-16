"""
Calculates the Fourier coefficients for a given set of data points
"""

import matplotlib.pyplot as plt
import numpy as np


class Fourier:
	def __init__(self, points, N):
		# self.c stores all coefficients of the fourier series
		# self.n stores the value of n that each coefficient corresponds to
		#   self.n == [0, 1, -1, 2, -2, 3, -3, ...]
		self.c = np.zeros(2 * N + 1)
		self.n = np.array([(n // 2) * (-1) ** (n % 2) for n in range(1, 2 * N + 2)])

		self.L = points[-1, 0] - points[0, 0]

		values = self.get_points_for_trapz(points, N)
		self.integrate_coefficients(values, N)

	def get_points_for_trapz(self, points, N):
		"""Convert an array of [t, x] points to be ready for integration
		Output is a 2D array with rows [t, c_0],
		   where each row corresponds to the value of the integrand at point t
		These rows can then be integrated across via the trapezium rule

		This will create rows up to the Nth coefficient of the Fourier series"""

		ts = points[:, 0]
		xs = points[:, 1]

		c_n = np.array([xs * np.exp(-1j * n * ts * 2 * np.pi / self.L) for n in self.n])


		integrand_values = np.array([ts, *c_n])

		return integrand_values


	def integrate_coefficients(self, integrand_values, N):
		ts, values = integrand_values[0, :], integrand_values[1:, 0:]

		coeffs = np.trapz(values, x=ts, axis=1)
		coeffs *= (1 / self.L)

		self.c = coeffs


	def __call__(self, ts):
		"""Takes an array, and evaluate the fourier series f(t) for each t in ts
		Returns an array of f(t)
		If the input is an float, return an array of length 1"""
		if type(ts) != np.ndarray:
			ts = np.array([ts])

		fs = np.zeros_like(ts)
		for i, t in enumerate(ts):
			f = sum(self.c * np.exp(-1j * self.n * t * 2 * np.pi / self.L))
			fs[i] = f
		return fs


if __name__ == "__main__":
	xs = np.linspace(0, 4, 100)

	points = np.array([xs, [np.heaviside(x - 2, 1) for x in xs]]).T

	fourier = Fourier(points, 50)
	plt.plot(xs, fourier(xs))
	plt.show()