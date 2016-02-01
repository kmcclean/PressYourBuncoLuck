from src.ErrorHandling import ErrorHandling as eh
import unittest


# This runs against each of the true cases presented in error handling. It can be used to quickly check and make sure
# that the correct information is being provided.
class ValidatorTests(unittest.TestCase):

    # makes sure that is_nonblank_string_truth_check is returning "True" when presented with text.
    def test_is_nonblank_string_is_true(self):
        self.assertTrue(eh.is_nonblank_string_truth_check(eh(), "test"), "test_is_nonblank_string_is_true failed")

    # makes sure that is_nonblank_string_truth_check is returning "False" when presented with nothing.
    def test_is_nonblank_string_is_false(self):
        self.assertFalse(eh.is_nonblank_string_truth_check(eh(), ""), "test_is_nonblank_string_is_false failed")

    # makes sure that range_provided_truth_check returns "True" when a number is within the range provided.
    def test_range_provided_truth_check_is_true(self):
        self.assertTrue(eh.range_provided_truth_check(eh(), 1, 0, 2), "test_range_provided_truth_check_is_true failed")

    # makes sure that range_provided_truth_check returns "False" when a number is outside the range provided.
    def test_range_provided_truth_check_is_false(self):
        self.assertFalse(eh.range_provided_truth_check(eh(), 3, 0, 2), "test_range_provided_truth_check_is_true failed")