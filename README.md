
## Project Purpose

**AI_Trip_Planner** is an agentic application that helps users plan trips anywhere in the world. It leverages real-time data from various APIs and LLMs (Large Language Models) to generate detailed, personalized travel itineraries, including cost breakdowns, weather, attractions, restaurants, activities, and transportation.

---

## Main Components

### 1. **Backend API (main.py)**
- Built with FastAPI.
- Exposes a `/query` endpoint that receives user questions (e.g., "Plan a trip to Goa for 5 days").
- Uses the `GraphBuilder` agent to process the query, generate a plan, and return the result as JSON.

### 2. **Agentic Workflow (agent/agentic_workflow.py)**
- Orchestrates the interaction between the LLM and various tools (weather, place search, expense calculation, currency conversion).
- Uses LangGraph to build a stateful graph for tool invocation and response generation.
- The agent receives the user’s question, invokes tools as needed, and compiles a comprehensive Markdown response.

### 3. **Tools**
- **Weather Info** (tools/weather_info_tool.py): Fetches current and forecast weather using OpenWeatherMap.
- **Place Search** (tools/place_search_tool.py): Finds attractions, restaurants, activities, and transportation using Google Places and Tavily.
- **Expense Calculator** (tools/expense_calculator_tool.py): Calculates hotel costs, total expenses, and daily budgets.
- **Currency Converter** (tools/currency_conversion_tool.py): Converts currencies using ExchangeRate-API.

### 4. **LLM Model Loader (utils/model_loader.py)**
- Loads and configures the LLM (Groq or OpenAI) based on settings in config.yaml.
- Binds the tools to the LLM for tool-augmented reasoning.

### 5. **Frontend (streamlit_app.py)**
- Built with Streamlit.
- Provides a chat-like interface for users to input travel queries.
- Displays the AI-generated travel plan in Markdown.

### 6. **Utilities**
- **Config Loader** (utils/config_loader.py): Loads YAML configuration.
- **Save to Document** (utils/save_to_document.py): Exports travel plans to Markdown files.
- **Weather, Place Info, Currency, Expense Calculation**: Utility modules for API calls and calculations.

---

## Workflow

1. **User Input**: User enters a travel query in the Streamlit app.
2. **API Call**: The frontend sends the query to the FastAPI backend.
3. **Agentic Processing**: The backend agent uses the LLM and tools to gather real-time data and generate a detailed plan.
4. **Response**: The backend returns the plan, which is displayed in the frontend.
5. **Optional**: The plan can be saved as a Markdown document.

---

## Key Features

- **Real-time Data**: Integrates with external APIs for up-to-date information.
- **Comprehensive Plans**: Provides detailed itineraries, cost breakdowns, and recommendations.
- **Tool-Augmented LLM**: Uses LangChain and LangGraph to enable the LLM to call external tools.
- **Extensible**: Modular design allows easy addition of new tools or data sources.

---

## Configuration

- API keys and model settings are managed via environment variables and config.yaml.
- Requirements are listed in requirements.txt.

---

## How to Run

1. Install dependencies (see README.md).
2. Set up environment variables for API keys.
3. Start the backend:  
   `uvicorn main:app --reload --port 8000`
4. Start the frontend:  
   `streamlit run streamlit_app.py`

---

## Summary

This project is a modern, modular AI-powered travel planner that combines LLMs with real-world data sources and utility tools to deliver rich, actionable travel plans to users via a web interface.




======================================================================
```uv --version
```


```import shutil
print(shutil.which("uv"))```

```pip install uv```

```uv init AI_Travel_Planner```

```uv pip list```

```uv python list```

```uv python install ypy-3.10.16-windows-x86_64-none```

```uv python list```

```uv venv env --python cpython-3.10.18-windows-x86_64-none```

```uv add pandas```

#if you have conda then first deactivate that
```conda deactivate```

```uv venv env --python cpython-3.10.18-windows-x86_64-none```

## use this command from your virtual env
```C:\Users\sunny\AI_Trip_Planner\env\Scripts\activate.bat```


```
streamlit run streamlit_app.py
```

```
uvicorn main:app --reload --port 8000
```