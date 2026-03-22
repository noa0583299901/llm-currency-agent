# LLM Currency Agent 🤖💱

An AI-powered agent that performs multi-step reasoning and uses external tools to solve real-world financial tasks.

The system demonstrates how Large Language Models (LLMs) can interact with tools such as web search, date retrieval, and calculations to complete complex workflows.

------------------------------------------------------------

## Features

• Multi-step reasoning using LLM agents  
• Tool-calling architecture  
• Real-time web search for exchange rates  
• Currency conversion with fee calculation  
• Modular tool-based design  

------------------------------------------------------------

## Technologies

- Python  
- OpenAI Models  
- smolagents  
- DuckDuckGo Search API  

------------------------------------------------------------

## How It Works

The agent follows a structured reasoning process:

1. Retrieves today's date  
2. Searches for the current exchange rate (USD → ILS)  
3. Extracts relevant numeric data  
4. Calculates final conversion including fees  

The system uses multiple tools:

- Date tool  
- Web search tool  
- Calculation tool  

------------------------------------------------------------

## Example Task

Convert 500 USD to ILS using the latest exchange rate, including a 2.5% fee.

------------------------------------------------------------

## Architecture

The system includes:

- Tool definitions (functions)  
- LLM model integration  
- Agent orchestration layer  
- Multi-step execution logic  

------------------------------------------------------------

## Installation

Install dependencies:

pip install smolagents python-dotenv

------------------------------------------------------------

## Run the Project

python main.py

------------------------------------------------------------

## Project Structure

llm-currency-agent

main.py  
README.md  
.env  
.gitignore  

------------------------------------------------------------

## Why This Project Stands Out

- Demonstrates LLM tool usage (advanced AI concept)  
- Shows real-world problem solving with AI  
- Combines reasoning + external data  
- Implements agent-based architecture  

------------------------------------------------------------

## Future Improvements

- Add UI (web interface)  
- Support multiple currencies  
- Improve data extraction accuracy  
- Add API endpoint  
