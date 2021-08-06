from src import plugin
from src.example_reporter import ExampleReporter
from src.example_tool import ExampleTool


class TestPlugin:
    def test_get_reporters(self):
        """Test that the reporters are listed"""
        reporters_snapshot = {
            "example-reporter": ExampleReporter,
        }
        assert plugin.get_reporters() == reporters_snapshot

    def test_get_tools(self):
        """Test that the tools are listed"""
        tools_snapshot = {"example-tool": ExampleTool}
        assert plugin.get_tools() == tools_snapshot
