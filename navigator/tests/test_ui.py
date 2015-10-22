import mock
import sys
import unittest

from navigator import ui


#-----------------------------------------------------------------------------#
# Test Cases
#-----------------------------------------------------------------------------#
class UIPromptTestCase(unittest.TestCase):
    def test_prompt(self):
        with mock.patch("six.moves.input", return_value="Test"):
            res = ui.prompt("Test Message")
            self.assertEqual(res, "Test")

    def test_prompt_empty(self):
        with mock.patch("six.moves.input", side_effect=["", "Test"]):
            res = ui.prompt("Test Message")
            self.assertEqual(res, "Test")

    def test_prompt_int(self):
        with mock.patch("six.moves.input", return_value="1"):
            res = ui.prompt("Test Message", "int")
            self.assertEqual(res, 1)

        with mock.patch("six.moves.input", return_value="0"):
            res = ui.prompt("Test Message", "int")
            self.assertEqual(res, 0)

    def test_prompt_str_as_int(self):
        with mock.patch("six.moves.input", side_effect=["one", "1"]):
            res = ui.prompt("Test Message", "int")
            self.assertEqual(res, 1)


class UIConfirmTestCase(unittest.TestCase):
    def test_confirm(self):
        with mock.patch("six.moves.input", return_value='yes'):
            res = ui.confirm("Test Message")
            self.assertTrue(res)

    def test_confirm_false(self):
        with mock.patch("six.moves.input", return_value='n'):
            res = ui.confirm("Test Message")
            self.assertFalse(res)

    def test_confirm_default_as_false(self):
        with mock.patch("six.moves.input", return_value=''):
            res = ui.confirm("Test Message")
            self.assertFalse(res)

    def test_confirm_with_default_as_true(self):
        with mock.patch("six.moves.input", return_value=''):
            res = ui.confirm("Test Message", default=True)
            self.assertTrue(res)


class UIChoicesTestCase(unittest.TestCase):
    def test_choice(self):
        choices = [("Male", "M"), ("Female", "F")]
        with mock.patch("six.moves.input", return_value='1'):
            res = ui.choice("Test Message", choices)
            self.assertEqual(res, "F")

    def test_choice_invalid_selection(self):
        choices = [("Male", "M"), ("Female", "F")]
        with mock.patch("six.moves.input", side_effect=['100', '0']):
            res = ui.choice("Test Message", choices)
            self.assertEqual(res, "M")

        with mock.patch("six.moves.input", side_effect=["-1", '0']):
            res = ui.choice("Test Message", choices)
            self.assertEqual(res, "M")


class UITextTestCase(unittest.TestCase):
    def _run_text_test(self, function, expected_output, *args):
        function(*args)
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("Need to run in buffered mode")

        # stdout is an StringIO instance
        actual_output = sys.stdout.getvalue()
        self.assertEqual(actual_output, expected_output)

    def test_text_prompt_no_end(self):
        self._run_text_test(ui.text_prompt, "\x1b[33mTest\x1b[0m\n", "Test")

    def test_text_success_no_end(self):
        self._run_text_test(ui.text_success, "\x1b[32mTest\x1b[0m\n", "Test")

    def test_text_error_no_end(self):
        self._run_text_test(ui.text_error, "\x1b[31mTest\x1b[0m\n", "Test")

    def test_text_info_no_end(self):
        self._run_text_test(ui.text_info, "\x1b[37mTest\x1b[0m\n", "Test")

    def test_text_prompt_with_end(self):
        self._run_text_test(ui.text_prompt, "\x1b[33mTest\x1b[0m", "Test", "")

    def test_text_success_with_end(self):
        self._run_text_test(ui.text_success, "\x1b[32mTest\x1b[0m", "Test", "")

    def test_text_error_with_end(self):
        self._run_text_test(ui.text_error, "\x1b[31mTest\x1b[0m", "Test", "")

    def test_text_info_with_end(self):
        self._run_text_test(ui.text_info, "\x1b[37mTest\x1b[0m", "Test", "")


#-----------------------------------------------------------------------------#
if __name__ == "__main__":
    unittest.main(module=__name__, buffer=True)
