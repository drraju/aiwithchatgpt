# Agentic AI - Week 1

This project implements a basic agentic AI system with modular components.

## Project Structure

```
agentic_ai_week1/
├── agent/
│   ├── agent.py      # Main agent implementation
│   ├── tools.py      # Tool definitions and utilities
│   ├── llm.py        # Language model integration
│   ├── memory.py     # Memory management system
│   └── logger.py     # Logging functionality
├── main.py           # Entry point of the application
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

## Components

### Agent (`agent/agent.py`)
The core agent class that orchestrates the AI agent behavior using LLM, tools, memory, and logging.

### Tools (`agent/tools.py`)
Defines tools that the agent can use to perform various tasks. Includes a base `Tool` class and default tool implementations.

### LLM (`agent/llm.py`)
Language model wrapper for integrating with various LLM providers like OpenAI.

### Memory (`agent/memory.py`)
Memory system for storing and retrieving information during agent execution.

### Logger (`agent/logger.py`)
Custom logging system for tracking agent operations and debugging.

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Set up your environment variables (create a `.env` file):
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

Run the main application:
```bash
python main.py
```

## Features

- Modular architecture for easy extension
- Tool-based system for agent capabilities
- Memory management for context retention
- Comprehensive logging
- LLM integration ready

## Future Enhancements

- Add more sophisticated tools
- Implement semantic memory search
- Add support for multiple LLM providers
- Implement agent reasoning and planning
- Add conversation history management
