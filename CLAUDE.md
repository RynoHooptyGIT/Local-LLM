# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python-based Local LLM project. The codebase is currently in early stages with minimal implementation.

## Development Setup

### Initial Setup

```bash
# Create virtual environment (already created)
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On macOS/Linux
# venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt
```

### Running the Application

```bash
# Ensure virtual environment is activated first
python main.py
```

## Project Structure

- [main.py](main.py) - Entry point for the application
- [requirements.txt](requirements.txt) - Python dependencies
- [.gitignore](.gitignore) - Git ignore rules for Python projects
- `venv/` - Virtual environment (ignored by git)

## Architecture Notes

This project appears to be focused on local LLM integration. As the codebase develops, consider documenting:
- Which LLM models/frameworks are being used (e.g., llama.cpp, Ollama, Transformers)
- Model loading and inference patterns
- API endpoints or CLI interface design
- Configuration management approach
