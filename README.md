# Business Intelligence Agent with Langchain and Openai

This project showcases the development of a Business Intelligence Agent using LangChain, OpenAI's GPT-3.5 Turbo model, and the Streamlit framework. The assistant enables users to interact with CSV files and perform various data analysis tasks. This README provides an overview of the project's structure and key components.

## Table of Contents
- [Description](#description)
- [Setup and Dependencies](#setup-and-dependencies)
- [Project Components](#project-components)
  - [Imports](#imports)
  - [API Key](#api-key)
  - [CSV Agent Function](#csv-agent-function)
  - [Display Functions](#display-functions)
  - [Extract Code Function](#extract-code-function)
  - [CSV Analyzer App](#csv-analyzer-app)
  - [Running the Agent](#running-the-agent)
  - [Displaying Results](#displaying-results)

## Description

The Business Intelligence Agent project is designed to simplify data analysis tasks by providing an interactive interface for working with CSV files. Users can upload a CSV file, ask questions about the data, and receive responses that include textual information and visualizations.

## Setup and Dependencies

Before using the CSV Assistant, you need to set up the required dependencies. Make sure you have the following installed:

- Python
- Streamlit
- pandas
- json
- openai
- os
- re (for regular expressions)
- matplotlib.pyplot

Additionally, you need to obtain an API key from OpenAI, which should be saved in an external file named `apikey.py`. The key is stored in a variable named `OPENAI_API_KEY`.


## Project Components

### Imports

You've imported the necessary libraries and modules, including Streamlit, pandas, json, openai, os, re (for regular expressions), and matplotlib.pyplot.

### API Key

You've set up your OpenAI API key using a variable named OPENAI_API_KEY, which is imported from an external file named apikey.py.

### CSV Agent Function

The `csv_agent_func` function is defined to run the CSV agent from LangChain with a given CSV file and user message. It uses the LangChain framework to interact with OpenAI's GPT-3.5 Turbo model for processing user queries related to the CSV file.

### Display Functions

You have defined functions like `display_content_from_json` to display content in Streamlit based on the structure of the JSON response received from the LangChain agent.

### Extract Code Function

The `extract_code_from_response` function extracts Python code from a string response received from the agent. This code can be executed to generate visualizations or perform other actions.

### CSV Analyzer App

The `csv_analyzer_app` function is the main Streamlit application. It displays a title and allows users to upload a CSV file. Once a file is uploaded, it reads and displays the file's content using pandas and provides a text input box for user queries.

### Running the Agent

When the user clicks the "Run" button, the `csv_agent_func` function is called to process the user's query using LangChain and GPT-3.5 Turbo. The response may contain code, which is extracted and executed in a safe environment.

### Displaying Results

Depending on the response, the application may display textual information, tables, or plots (e.g., bar charts) generated from the extracted code.

