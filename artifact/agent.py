from google.adk.agents import Agent
from .tools.tools import make_image_artifact_tool


root_agent = Agent(
    name="root_agent",
    model="gemini-2.0-flash",
    description="This is the agent that will be used to create image artifacts.",
    instruction="Given a prompt, create an image artifact.",
    tools=[make_image_artifact_tool],
)
