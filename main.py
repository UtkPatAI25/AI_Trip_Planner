#Built with FastAPBuilt with FastAPI.
#Exposes a /query endpoint that receives user questions (e.g., "Plan a trip to Goa for 5 days").
#Uses the GraphBuilder agent to process the query, generate a plan, and return the result as JSON.

from logger.logger import logger
from fastapi import FastAPI, Request
from exception.global_exception_handler import global_exception_handler
from fastapi.middleware.cors import CORSMiddleware
from agent.agentic_workflow import GraphBuilder
from utils.save_to_document import save_document
from starlette.responses import JSONResponse
import os
import datetime
from dotenv import load_dotenv
from pydantic import BaseModel



load_dotenv()

app = FastAPI()

# Register global exception handler
app.add_exception_handler(Exception, global_exception_handler)


# Adds CORS support so API can be called from any frontend (e.g. Streamlit app).
# In production, restrict allow_origins.

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # set specific origins in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the request model for the /query endpoint
class QueryRequest(BaseModel):
    question: str

# Endpoint to handle user queries
# This endpoint receives a question, processes it using the GraphBuilder agent,
# and returns the generated travel plan as a JSON response.
@app.post("/query")
# Function to process the user query
async def query_travel_agent(query:QueryRequest):
    try:
        logger.info(f"Received query: {query}")
        print(query)
        graph = GraphBuilder(model_provider="groq")
        react_app=graph()
        #react_app = graph.build_graph()
        
        # Generate the graph and save it as a PNG file
        # This will create a visual representation of the agent's workflow.
        png_graph = react_app.get_graph().draw_mermaid_png()
        with open("my_graph.png", "wb") as f:
            f.write(png_graph)

        print(f"Graph saved as 'my_graph.png' in {os.getcwd()}")
        # Assuming request is a pydantic object like: {"question": "your text"}
        # Prepare the messages for the agent
        # The agent expects a dictionary with a "messages" key containing the user's question.
        messages={"messages": [query.question]}
        output = react_app.invoke(messages)
         
        # Save the output to a document
        # This function saves the output to a document with a timestamp in the filename.
        # extract the last message content as the final output.
        # This is the AI's response to the user's question.
        # If the output is a dictionary with a "messages" key, we take the last message's content.
        # Otherwise, we convert the output to a string.    
        if isinstance(output, dict) and "messages" in output:
            final_output = output["messages"][-1].content  # Last AI response
        else:
            final_output = str(output)
        
        # Ensure output directory exists
        os.makedirs("output", exist_ok=True)
        # Save the output as a Markdown file in the output folder
        filename = f"output/plan_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        save_document(final_output, filename)
        logger.info(f"Saved plan to {filename}")
        
        logger.info("Successfully processed query.")
        return {"answer": final_output}
    #If anything goes wrong, returns a 500 error with the exception message.
    except Exception as e:
        logger.error(f"Error in /query endpoint: {e}", exc_info=True)
        raise  # This will be caught by the global handler
        #return JSONResponse(status_code=500, content={"error": str(e)})