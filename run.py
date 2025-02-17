import unittest
from HtmlTestRunner import HTMLTestRunner

if __name__ == "__main__":
    test_dir = "tests"
    suite = unittest.defaultTestLoader.discover(test_dir)
    runner = HTMLTestRunner(output="reports")
    runner.run(suite)