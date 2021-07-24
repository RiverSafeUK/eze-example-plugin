# Overview
This is a how-to manual to guide anyone to implement a plugin class from Scratch. Also, how to use the plugin in Eze.


# Implementation

## Review plugin documentation
Read all the documentation about the plugin you want to include in the project. Useful info:

- Command/Actions to install plugin.
- Command to execute the plugin
- Useful arguments/flags to pass into the executable command.
- Structure of the response, type, info.
- Plugin's version

>**Note:** Make sure the plugin you choose is kept mantained, so the libraries are supported.

## Include plugin files

### I. Install the plugin
The installation may vary based on the plugin: 
 * If binary file: download it and save it on your home directory
 * If python package: install it by using "pip install ..."
 * If Node library: by using "npm install ..."
 * Other ways are via apt-get or docker.

>Step is finished when you are able to run the plugin locally. 
```[plugin] --version``` *Although this is not an unique command*.

### II. Add plugin code

1. Design your executable command, the arguments and the flags it may contain inside a Python file ```[plugin].py``` (See an example in example_tool.py TOOL_CLI_CONFIG). 

>In the EZE_CONFIG, we receive the arguments from .ezerc that will compound the command. Describing their type and default values.

```python
{
    "<PARAMETER_NAME>": {"type": <type>, "default": "<default_value>"}
    ...
}
```

>In the CMD_CONFIG, we organised the command in base, arguments and flags. This acts as a translator between the config file and the plugin. 

You will have to add SHORT_DESCRIPTION, CONFIG_HELP and INSTALL_HELP for display.

2. Define the following functions: 
- check_installed() -> str
- _parse_config(self, eze_config: dict) -> dict 
    - Optional, define if you want to customise the parsing.
- run_scan(self) -> ScanResult


## Installation
These are the steps for installing your new plugin in an external project.

### Register the plugin for external use

1. In the python project (our example Eze-sandpit)

#### setup.py
go to setup.py to set your entry point:

>entry_points={
    "eze.plugins": "example=src.plugin"
    },

>**_NOTE:_** Replace example=src.plugin, by `<PluginName>=<PluginsLocation>`

#### setup.cfg
go to setup.cfg to set your entry point:

>```
>[options.entry_points]
>eze.plugins =
>eze =
>    example=src.tools

>**_NOTE:_** Replace example=src.plugin, by `<PluginName>=<PluginsLocation>`

2. Build the plugin package, enter:
```bash
python setup.py sdist
```
3. Make sure you have the package on:
/dist/[plugin_name-version].tar.gz

### Install the plugin on your Python environment

1. After the *.tar file is generated, open the bash terminal on **Eze-core** project and enter:

```bash
pip install [tar_location]
```

2. Finally, you can check the list of the tools/reporters and verify the new plugin is listed:
```bash
eze tools list  
eze reporters list  
```
