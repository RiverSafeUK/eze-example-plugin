from src.example_reporter import ExampleReporter
from eze.core.tool import ScanResult

from unittest import mock
from io import StringIO
import pytest
import sys


class TestExampleReporter:
    def test_check_installed(self):
        """Test if the example reporter is installed and which version is it"""
        expected_output = "0.8.0"
        output = ExampleReporter.check_installed()
        assert output == expected_output

    @pytest.mark.asyncio
    async def test_run_report(self):
        """Test if the results from scanning was successfully converted to this reporter format"""
        testee = ExampleReporter()

        mocked_print_output = StringIO()
        sys.stdout = mocked_print_output
        await testee.run_report([ScanResult({"tool": "tool_1"})])
        sys.stdout = sys.__stdout__
        assert (
            mocked_print_output.getvalue()
            == "Running 'example-reporter' reporter\nExample scan result 'tool_1' report output\n"
        )
