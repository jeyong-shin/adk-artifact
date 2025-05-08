import matplotlib.pyplot as plt
import google.genai.types as types
from google.adk.tools import ToolContext


def make_image_artifact_tool(values: list[float], tool_context: ToolContext) -> None:
    """
    Create an image artifact tool.

    Args:
        values (list[float]): A list of float values representing the image artifact.

    Returns:
        None
    """
    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the values
    ax.plot(values)

    # Set the title and labels
    ax.set_title("Image Artifact")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")

    # Save the figure to a file
    plt.savefig("image_artifact.png")

    # Create an image artifact
    image_artifact = types.Part(
        inline_data=types.Blob(
            mime_type="image/png",
            data=open("image_artifact.png", "rb").read()
        )
    )

    tool_context.save_artifact(
        filename="image_artifact.png",
        artifact=image_artifact
    )
