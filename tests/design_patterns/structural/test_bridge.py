import unittest
from unittest.mock import patch

from src.python_algorithms.design_patterns.structural.bridge import DrawingAPI1, DrawingAPI2, CircleShape


class BridgeTest(unittest.TestCase):
    def test_bridge_shall_draw_with_concrete_api_implementation(self):
        ci1 = DrawingAPI1()
        ci2 = DrawingAPI2()
        with patch.object(ci1, 'draw_circle') as mock_ci1_draw_circle, patch.object(
            ci2, 'draw_circle'
        ) as mock_ci2_draw_circle:
            sh1 = CircleShape(1, 2, 3, ci1)
            sh1.draw()
            self.assertEqual(mock_ci1_draw_circle.call_count, 1)
            sh2 = CircleShape(1, 2, 3, ci2)
            sh2.draw()
            self.assertEqual(mock_ci2_draw_circle.call_count, 1)

    def test_bridge_shall_scale_both_api_circles_with_own_implementation(self):
        scale_factor = 2
        circle1_radius = 3
        expected_circle1_radius = 6
        circle2_radius = circle1_radius * circle1_radius
        expected_circle2_radius = circle2_radius * scale_factor

        ci1 = DrawingAPI1()
        ci2 = DrawingAPI2()
        sh1 = CircleShape(1, 2, circle1_radius, ci1)
        sh2 = CircleShape(1, 2, circle2_radius, ci2)
        sh1.scale(scale_factor)
        sh2.scale(scale_factor)
        self.assertEqual(sh1._radius, expected_circle1_radius)
        self.assertEqual(sh2._radius, expected_circle2_radius)
        with patch.object(sh1, 'scale') as mock_sh1_scale_circle, patch.object(sh2, 'scale') as mock_sh2_scale_circle:
            sh1.scale(2)
            sh2.scale(2)
            self.assertEqual(mock_sh1_scale_circle.call_count, 1)
            self.assertEqual(mock_sh2_scale_circle.call_count, 1)
