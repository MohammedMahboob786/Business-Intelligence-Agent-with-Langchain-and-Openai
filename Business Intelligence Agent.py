import streamlit as st
import pandas as pd
import json
import openai
import os
import re
import matplotlib.pyplot as plt
from langchain.agents import create_csv_agent
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType

# Define a function to run the CSV agent
def csv_agent_func(file_path, user_message):
    # Create a CSV agent using ChatOpenAI
    agent = create_csv_agent(
        ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613", openai_api_key="apikey"),
        file_path,
        verbose=True,
        handle_parsing_errors=True,  # Handle parsing errors
        agent_type=AgentType.OPENAI_FUNCTIONS,
    )

    try:
        # Properly format the user's input and wrap it with the required "input" key
        tool_input = {
            "input": {
                "name": "python",
                "arguments": user_message
            }
        }
        
        response = agent.run(tool_input)
        return response
    except Exception as e:
        st.write(f"Error: {e}")
        return None

def display_content_from_json(json_response):
    """
    Display content to Streamlit based on the structure of the provided JSON.
    """
    
    # Check if the response has plain text.
    if "answer" in json_response:
        st.write(json_response["answer"])

    # Check if the response has a bar chart.
    if "bar" in json_response:
        data = json_response["bar"]
        df = pd.DataFrame(data)
        df.set_index("columns", inplace=True)
        st.bar_chart(df)

    # Check if the response has a scatterplot.
    if "scatterplot" in json_response:
        data = json_response["scatterplot"]
        df = pd.DataFrame(data["data"], columns=data["columns"])
        st.write("Scatterplot:")
        st.write(df)  # Display the scatterplot data

    # Check if the response has a KDE plot.
    if "kde" in json_response:
        data = json_response["kde"]
        df = pd.DataFrame(data["data"], columns=data["columns"])
        st.write("KDE Plot:")
        st.write(df)

    # Check if the response has a pie chart.
    if "pie" in json_response:
        data = json_response["pie"]
        df = pd.DataFrame(data["data"], columns=data["columns"])
        st.write("Pie Chart:")
        st.write(df)

    # Check if the response has a bar plot.
    if "barplot" in json_response:
        data = json_response["barplot"]
        df = pd.DataFrame(data["data"], columns=data["columns"])
        st.write("Bar Plot:")
        st.write(df)

    # Check if the response has a table.
    if "table" in json_response:
        data = json_response["table"]
        df = pd.DataFrame(data["data"], columns=data["columns"])
        st.table(df)

def extract_code_from_response(response):
    """Extracts Python code from a string response."""
    # Use a regex pattern to match content between triple backticks
    code_pattern = r"```python(.*?)```"
    match = re.search(code_pattern, response, re.DOTALL)
    
    if match:
        # Extract the matched code and strip any leading/trailing whitespaces
        return match.group(1).strip()
    return None

def csv_analyzer_app():
    """Main Streamlit application for CSV analysis."""

    st.title('Business Intelligence Agent')
    st.write('Please upload your CSV file and enter your query below:')
    
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        # file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type, "FileSize": uploaded_file.size}
        # st.write(file_details)
        
        # Save the uploaded file to disk
        file_path = os.path.join(uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        df = pd.read_csv(file_path)
        st.dataframe(df)
        
        user_input = st.text_input("Your query")
        if st.button('Run'):
            response = csv_agent_func(file_path, user_input)
            
            # Extracting code from the response
            code_to_execute = extract_code_from_response(response)
            
            if code_to_execute:
                try:
                    # Making df available for execution in the context
                    exec(code_to_execute, globals(), {"df": df, "plt": plt})
                    fig = plt.gcf()  # Get current figure
                    st.pyplot(fig)  # Display using Streamlit
                except Exception as e:
                    st.write(f"Error executing code: {e}")
            else:
                st.write(response)

    st.divider()

if __name__ == "__main__":
    csv_analyzer_app()