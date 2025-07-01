
from utils.model_loader import ModelLoader
from prompt_library.prompt import SYSTEM_PROMPT
from langgraph.graph import StateGraph, MessagesState, END, START
from langgraph.prebuilt import ToolNode, tools_condition
from tools.weather_info_tool import WeatherInfoTool
from tools.place_search_tool import PlaceSearchTool
from tools.expense_calculator_tool import CalculatorTool
from tools.currency_conversion_tool import CurrencyConverterTool


# Loads the LLM (e.g., Groq or OpenAI) using the ModelLoader.
# Instantiates each tool class and collects their tool lists.
# Combines all tools into a single list and binds them to the LLM.
# Stores the system prompt for consistent agent behavior.

class GraphBuilder():
    
    # Initializes the GraphBuilder with a specified model provider.
    # Loads the LLM and initializes various tools.
    # Combines all tools into a single list and binds them to the LLM.
    # Initializes the system prompt for the agent.
    # This setup allows the agent to use multiple tools for different tasks 
    # like weather information, place search, calculations, and currency conversion.
    
    def __init__(self,model_provider: str = "groq"):
        self.model_loader = ModelLoader(model_provider=model_provider)
        self.llm = self.model_loader.load_llm()
        
        self.tools = []
        
        self.weather_tools = WeatherInfoTool()
        self.place_search_tools = PlaceSearchTool()
        self.calculator_tools = CalculatorTool()
        self.currency_converter_tools = CurrencyConverterTool()
        
       
        # Each tool class (e.g., WeatherInfoTool) has an attribute like weather_tool_list that contains one or more tool objects.
        # The * operator unpacks each list, so all the tools are added individually (not as sublists).
        # self.tools.extend([...]) adds all these tool objects to the self.tools list.

        # This line combines all the tool lists into a single list.
        self.tools.extend([* self.weather_tools.weather_tool_list, 
                           * self.place_search_tools.place_search_tool_list,
                           * self.calculator_tools.calculator_tool_list,
                           * self.currency_converter_tools.currency_converter_tool_list])
        
        self.llm_with_tools = self.llm.bind_tools(tools=self.tools)
        
        self.graph = None
        
        self.system_prompt = SYSTEM_PROMPT
    
    
    # Receives the current state (messages).
    # Prepends the system prompt to the user’s messages.
    # Invokes the LLM (with tools) to get a response.
    # Returns the response in the expected format.
    
    def agent_function(self,state: MessagesState):
        """Main agent function"""
        user_question = state["messages"]
        input_question = [self.system_prompt] + user_question
        response = self.llm_with_tools.invoke(input_question)
        return {"messages": [response]}
    
    # Builds a stateful workflow graph:
    # Nodes: agent (the LLM) and tools (all tools).
    # Edges: Defines the flow: start → agent → (tools if needed) → agent → end.
    # Conditional Edges: If the agent decides a tool is needed,the workflow routes to the tool node.
    # Compiles and returns the graph.
    def build_graph(self):
        graph_builder=StateGraph(MessagesState)
        graph_builder.add_node("agent", self.agent_function)
        graph_builder.add_node("tools", ToolNode(tools=self.tools))
        graph_builder.add_edge(START,"agent")
        graph_builder.add_conditional_edges("agent",tools_condition)
        graph_builder.add_edge("tools","agent")
        graph_builder.add_edge("agent",END)
        self.graph = graph_builder.compile()
        return self.graph
        
    # This method allows the GraphBuilder instance to be called like a function,
    # which will build and return the graph.
    # This is useful for integrating with frameworks that expect callable objects.
    # When you call an instance of GraphBuilder (e.g., graph = GraphBuilder();), it internally calls the build_graph() method.

    def __call__(self):
        return self.build_graph()