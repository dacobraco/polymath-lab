import unittest
import numpy as np

from fourier_utils import calculate_fourier_coefficients, calculate_rmse, calculate_spectrum, reconstruct_signal, generate_ideal_signal


class TestFourierSeriesVisualizer(unittest.TestCase):

    def test_square_wave_coefficients(self):
        a0, an, bn = calculate_fourier_coefficients("square", 5)

        expected_an = np.zeros(5)
        expected_bn = np.array([
            4 / np.pi,
            0,
            4 / (3 * np.pi),
            0,
            4 / (5 * np.pi),
        ])

        self.assertEqual(a0, 0.0)
        np.testing.assert_allclose(an, expected_an)
        np.testing.assert_allclose(bn, expected_bn)


    def test_rmse_of_identical_signals(self):
        ideal = np.array([1.0, 2.0, 3.0])
        reconstructed = np.array([1.0, 2.0, 3.0])

        result = calculate_rmse(ideal, reconstructed)

        self.assertEqual(result, 0.0)


    def test_known_amplitude_and_phase(self):
        an = np.array([3.0])
        bn = np.array([4.0])

        amplitudes, phases = calculate_spectrum(an, bn)

        np.testing.assert_allclose(amplitudes, np.array([5.0]))
        np.testing.assert_allclose(phases, np.array([-53.13010235]))


    def test_single_sine_reconstruction(self):
        a0 = 0.0
        an = np.array([0.0])
        bn = np.array([1.0])
        theta = np.array([0.0, np.pi / 2, np.pi])

        expected = np.sin(theta)
        signal = reconstruct_signal(theta, a0, an, bn)

        np.testing.assert_allclose(signal, expected, atol=1e-12)


    def test_nonpositive_harmonic_count(self):
        with self.assertRaises(ValueError):
            calculate_fourier_coefficients("square", 0)


    def test_square_signal_generation(self):
        theta = np.array([-np.pi / 2, np.pi / 2])
        ideal_signal = generate_ideal_signal("square", theta)
        np.testing.assert_allclose(ideal_signal, np.array([-1.0, 1.0]))


    def test_sawtooth_signal_generation(self):
        theta = np.array([-np.pi / 2, 0.0, np.pi / 2,])
        ideal_signal = generate_ideal_signal("sawtooth", theta)
        np.testing.assert_allclose(ideal_signal, np.array([-0.5, 0.0, 0.5]))

    def test_sawtooth_coefficients(self):
        a0, an, bn = calculate_fourier_coefficients("sawtooth", 3)

        expected_an = np.zeros(3)
        expected_bn = np.array([
            2 / np.pi,
            -1 / np.pi,
            2 / (3 * np.pi),
        ])

        self.assertEqual(a0, 0.0)
        np.testing.assert_allclose(an, expected_an)
        np.testing.assert_allclose(bn, expected_bn)


    def test_known_nonzero_rmse(self):
        ideal = np.array([0.0, 0.0])
        reconstructed = np.array([1.0, -1.0])

        result = calculate_rmse(ideal, reconstructed)

        self.assertAlmostEqual(result, 1.0)


    def test_sawtooth_periodic_wrapping(self):
        theta = np.array([3 * np.pi / 2])

        result = generate_ideal_signal("sawtooth", theta)
        expected = np.array([-0.5])

        np.testing.assert_allclose(result, expected)


    def test_unsupported_signal_generation(self):
        theta = np.array([0.0])

        with self.assertRaises(ValueError):
            generate_ideal_signal("triangle", theta)


    def test_unsupported_signal_coefficients(self):
        with self.assertRaises(ValueError):
            calculate_fourier_coefficients("triangle", 5)


    def test_rmse_shape_mismatch(self):
        ideal = np.array([1.0, 2.0])
        reconstructed = np.array([1.0, 2.0, 3.0])

        with self.assertRaises(ValueError):
            calculate_rmse(ideal, reconstructed)


    def test_reconstruction_coefficient_length_mismatch(self):
        theta = np.array([0.0, np.pi / 2])
        an = np.array([1.0])
        bn = np.array([1.0, 2.0])

        with self.assertRaises(ValueError):
            reconstruct_signal(theta, 0.0, an, bn)


    def test_spectrum_coefficient_shape_mismatch(self):
        an = np.array([1.0])
        bn = np.array([1.0, 2.0])

        with self.assertRaises(ValueError):
            calculate_spectrum(an, bn)

if __name__ == "__main__":
    unittest.main()
