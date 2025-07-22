# ==============================================================================
# File: tests/unit/test_structure.py
# A simple test to ensure the unit test environment is set up correctly.
# ==============================================================================

import unittest


class TestUnitStructure(unittest.TestCase):
    def test_can_import_main_class(self):
        """
        Tests that the main application class can be imported from a unit test.
        This verifies that the Python path is configured correctly for tests.
        """
        try:
            from glmpynet.logistic_regression import LogisticRegression
        except ImportError as e:
            self.fail(f"Failed to import LogisticRegression from a unit test: {e}")

        # A simple assertion to make sure the test does something.
        self.assertTrue(True, "Import successful.")