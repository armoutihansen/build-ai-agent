# Build AI Agent

A powerful AI agent framework built with Google's Gemini API that enables intelligent code execution, file manipulation, and autonomous task completion through natural language prompts.

## Overview

This project implements an agentic AI system that can understand user requests and autonomously execute a series of operations to accomplish goals. The agent has the ability to:

- **List and explore** file structures and directories
- **Read file contents** for analysis and context
- **Execute Python scripts** with optional arguments
- **Create and write files** to implement solutions
- **Iterate intelligently** by analyzing results and making follow-up decisions

The agent uses Google's Gemini 2.5 Flash model with function calling capabilities, allowing it to reason about problems and execute tools in sequence to achieve objectives.

## Features

- **Tool-Based Architecture**: Built-in functions for safe file operations and code execution
- **Agentic Loops**: Supports up to 20 iterations of function calls, enabling complex multi-step reasoning
- **Sandboxed Execution**: Working directory restrictions ensure secure operation
- **Verbose Mode**: Detailed logging of token usage and function calls for debugging and monitoring
- **Simple CLI Interface**: Easy-to-use command-line API for sending prompts to the agent

## Quick Start

### Prerequisites

- Python 3.13+
- Google Gemini API key

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/build-ai-agent.git
cd build-ai-agent
```

2. Set up your environment:
```bash
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY
```

3. Install dependencies:
```bash
pip install -r requirements.txt
# or with uv
uv sync
```

### Usage

Run the agent with a natural language prompt:

```bash
python main.py "Create a calculator module that can add, subtract, multiply, and divide two numbers"
```

For verbose output showing token usage and function calls:

```bash
python main.py "Your prompt here" --verbose
```

## How It Works

1. **User Input**: Send a natural language prompt to the agent
2. **Reasoning**: The Gemini model analyzes the request and creates a function call plan
3. **Execution**: Available functions (list files, read content, run code, write files) are called as needed
4. **Iteration**: Results are fed back to the model, which either calls more functions or provides a final response
5. **Output**: The agent returns results or newly created files

## Project Structure

```
build-ai-agent/
├── main.py                 # Main entry point and agentic loop
├── call_function.py        # Function dispatcher and caller
├── prompts.py              # System prompts for the AI agent
├── functions/              # Available tool implementations
│   ├── get_files_info.py   # List directory contents
│   ├── get_file_content.py # Read file contents
│   ├── run_python_file.py  # Execute Python scripts
│   └── write_file.py       # Create/write files
├── calculator/             # Example project working directory
│   ├── main.py
│   ├── tests.py
│   └── pkg/
│       ├── calculator.py
│       └── render.py
└── tests/                  # Test files for individual functions
```

## Available Functions

### get_files_info
Lists files and directories in a specified directory with file sizes and type information.

### get_file_content
Reads the complete contents of a specified file.

### run_python_file
Executes a Python file with optional command-line arguments.

### write_file
Creates or overwrites files with specified content.

## Environment Setup

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_api_key_here
```

Get your API key from [Google's AI Studio](https://aistudio.google.com/apikey).

## Configuration

- **Model**: Gemini 2.5 Flash (configurable in `main.py`)
- **Max Iterations**: 20 function calls per prompt (configurable)
- **Working Directory**: Defaults to `./calculator` (can be modified)

## Example Workflows

### Create a New Python Module
```bash
python main.py "Create a file called utils.py with utility functions for string manipulation"
```

### Test and Debug Code
```bash
python main.py "Run tests.py and show me any errors, then fix them"
```

### Complex Multi-Step Tasks
```bash
python main.py "Analyze the files in this directory, create a summary document, and list all functions found"
```

## Security Considerations

- **Working Directory Sandboxing**: The agent can only access files within the specified working directory
- **Path Validation**: All file paths are validated to prevent directory traversal attacks
- **API Keys**: Keep your `.env` file private and never commit it to version control

## Dependencies

- `google-genai==1.12.1` - Google's Gemini API client
- `python-dotenv==1.1.0` - Environment variable management

## Future Enhancements

- Additional tools (git operations, web requests, database queries)
- Streaming responses for long-running tasks
- Advanced error recovery and retry logic
- Multi-turn conversation support
- Custom tool registration system

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Google Gemini API](https://ai.google.dev/)
- Inspired by modern AI agent architectures
