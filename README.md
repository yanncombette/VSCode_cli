# Project Name

## Introduction

This project is a command-line interface (CLI) tool designed to simplify the process of opening projects in Visual Studio Code (VSCode). Instead of manually navigating to project folders, users can use this tool to quickly open their desired project from a list of pre-defined project directories.

## Installation

To install the project, follow these steps:

1. **Install Dependencies**: Ensure that all necessary dependencies for the project are installed on your computer.

2. **Setup Database**: Run the `install.py` script to set up the database. This script will initialize any required databases or configurations needed for the project to function properly.

    ```bash
    python3 install.py
    ```

3. **Add Projects Root**: After setting up the database, use the `-a` or `--add` command to add the root directory of your projects. This step is necessary to populate the list of available projects in the CLI tool.

    ```bash
    python3 cli.py -a
    ```

4. **Optional: Add Alias for Visual Studio Code**: For optimal use, you can add an alias for the CLI tool to simplify running commands. *See configuration below for details.*

## Configuration

After installation, to enhance your workflow, consider adding an alias to simplify running commands.

### Adding Alias for Visual Studio Code

To conveniently access the CLI tool from the terminal using the alias `vscode`, follow these steps:

1. Open your terminal.
2. Navigate to your home directory if you're not already there:
    ```bash
    cd ~
    ```

3. Open your shell configuration file. If you're using Bash, it's usually `.bashrc` or `.bash_profile`. If you're using Zsh, it's usually `.zshrc` or `.zprofile`:
    ```bash
    nano ~/.bashrc
    ```

4. Add the following line to the end of the file:
    ```bash
    alias vscode='python3 ~/path/to/cli.py'
    ```

    Replace `~/path/to/cli.py` with the actual path to your `cli.py` script.

5. Save and close the file by pressing `Ctrl + X`, then `Y`, and finally `Enter`.
6. Source the updated configuration file to apply the changes:
    ```bash
    source ~/.bashrc
    ```

Now, you can simply type `vscode` in your terminal to run the CLI tool.

## Usage

To use the CLI tool, follow these steps:

1. Open your terminal.
2. Run the `vscode` command to access the tool.
3. Use the following commands to perform actions:

    - `-c` or `--create`: Create a new project.
    - `-o` or `--open`: Open an existing project.
    - `-a` or `--add`: Add new projects directory.
    - `-h` or `--help`: Show usage instructions.

For example:
```bash
vscode -o