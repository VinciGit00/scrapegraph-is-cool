"""
Example of Search Graph
"""
import os
import json
from dotenv import load_dotenv
from scrapegraphai.graphs import SearchGraph

load_dotenv()

# ************************************************
# Define the configuration for the graph
# ************************************************

openai_key = os.getenv("OPENAI_APIKEY")

graph_config = {
    "llm": {
        "api_key": openai_key,
        "model": "openai/gpt-4o",
    },
    "max_results": 2,
    "verbose": True,
}

# ************************************************
# Create the SearchGraph instance and run it
# ************************************************

search_graph = SearchGraph(
    prompt="List me all the ceos of Microsoft?",
    config=graph_config
)

result = search_graph.run()
print(json.dumps(result, indent=4))
