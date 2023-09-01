from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

llm = Ollama(base_url="http://localhost:11434",
             model="llama2",
             callback_manager = CallbackManager([StreamingStdOutCallbackHandler()]))
llm("Tell me about the history of AI")
tools = load_tools(["serpapi", "llm-math"],
                   llm=llm,
                   serpapi_api_key='6271283bfbd5df35b44961ef156de6717f35655db800fd50eab08152ec33f78e')
