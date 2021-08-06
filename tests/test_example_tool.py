from src.example_tool import ExampleTool
from eze.core.tool import (
    ScanResult,
    Vulnerability,
)

import pytest
import os
import json
from pathlib import Path
from unittest import mock
from io import StringIO
import sys


class TestExampleTool:
    def test_check_installed(self):
        """Test if the example tool is installed and which version is it"""
        expected_output = "0.8.0"
        output = ExampleTool.check_installed()
        assert output == expected_output

    @pytest.mark.asyncio
    async def test_run_scan(self, snapshot):
        """Test if the results from running the scan were successfully extracted and parsed"""
        testee = ExampleTool()
        report = await testee.run_scan()
        report_str = json.dumps(report, default=vars, indent=2, sort_keys=True)

        snapshot.snapshot_dir = "tests/__snapshots__"
        snapshot.assert_match(report_str, "example-tool-report-output.json")
