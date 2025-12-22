import unittest
from src.controller import PIDController

class TestPIDController(unittest.TestCase):
    def setUp(self):
        self.controller = PIDController(kp=1.0, ki=0.1, kd=0.05)
    
    def test_initialization(self):
        self.assertEqual(self.controller.kp, 1.0)
        self.assertEqual(self.controller.ki, 0.1)
        self.assertEqual(self.controller.kd, 0.05)
        self.assertEqual(self.controller.previous_error, 0)
        self.assertEqual(self.controller.integral, 0)

    def test_compute_output(self):
        output = self.controller.compute_output(setpoint=10, measured_value=5)
        self.assertIsInstance(output, float)

    def test_integral_limit(self):
        self.controller.integral = 1000  # Simulate integral windup
        output = self.controller.compute_output(setpoint=10, measured_value=0)
        self.assertLessEqual(self.controller.integral, 100)  # Assuming integral limit is set to 100

if __name__ == '__main__':
    unittest.main()