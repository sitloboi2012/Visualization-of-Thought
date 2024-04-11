import base64
import requests

OPENAI_API_KEY = ""
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPENAI_API_KEY}",
}
ROUTE_IMAGE = "prompts/route_planning_img.png"


# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


# Getting the base64 string
encode_route = encode_image(ROUTE_IMAGE)

COT_VISION_PAYLOAD = {
    "model": "gpt-4-turbo",
    "messages": [
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": """
                    You are a helpful assistant. You have been given a map that contains the route from Home to the Office.
                    Your task is to plan the route from the Home position to the Office position. 
                    The tile that contains letter H represents the Home position, and the tile that contains letter O represents the Office position.
                    The tile that contains letter B represents obstacles like walls that you cannot pass through.
                    You can only move up, down, left, or right. You cannot move diagonally.
                    There exists one and only one viable route for this map.
                    Each step you choose a direction and move to the end of the continuous road or the destination.
                    """,
                }
            ],
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Now given the image of the map, starting from the Home position, provide the steps to navigate to Office position. Let's think this step by step",
                },
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{encode_route}"},
                },
            ],
        },
    ],
}

VOT_NONVISION_PAYLOAD = {
    "model": "gpt-4-turbo",
    "messages": [
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": """
                    You are a helpful assistant. You have been given a 3 by 3 square grid map that contains the route from Home to the Office.
                    Your task is to plan the route from the Home position to the Office position. 
                    The tile that contains letter H represents the Home position, and the tile that contains letter O represents the Office position.
                    The tile that contains letter B represents obstacles like walls that you cannot pass through.
                    You can only move up, down, left, or right. You cannot move diagonally.
                    On the first row, you will find the H next to a B and then the B.
                    On the second row, you will find the X next to the B and then B.
                    On the third row, you will find the X next to another X and then the O.
                    There exists one and only one viable route for this map.
                    Each step you choose a direction and move to the end of the continuous road or the destination.
                    """,
                }
            ],
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": """Now you have all the information on the map.
                    You start at the position where the H which is the Home is located.
                    Provide the steps to navigate to the O which is the Office position. Please visualize the state after each reasoning step.""",
                },
            ],
        },
    ],
}

COT_NONVISION_PAYLOAD = {
    "model": "gpt-4-turbo",
    "messages": [
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": """
                    You are a helpful assistant. You have been given a 3 by 3 square grid map that contains the route from Home to the Office.
                    Your task is to plan the route from the Home position to the Office position. 
                    The tile that contains letter H represents the Home position, and the tile that contains letter O represents the Office position.
                    The tile that contains letter B represents obstacles like walls that you cannot pass through.
                    You can only move up, down, left, or right. You cannot move diagonally.
                    On the first row, you will find the H next to a B and then the B.
                    On the second row, you will find the X next to the B and then B.
                    On the third row, you will find the X next to another X and then the O.
                    There exists one and only one viable route for this map.
                    Each step you choose a direction and move to the end of the continuous road or the destination.
                    """,
                }
            ],
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": """Now you have all the information on the map.
                    You start at the position where the H which is the Home is located.
                    Provide the steps to navigate to the O which is the Office position. Let's think this step by step.""",
                },
            ],
        },
    ],
}

NOVIZ_COT_NONVISION_PAYLOAD = {
    "model": "gpt-4-turbo",
    "messages": [
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": """
                    You are a helpful assistant. You have been given a 3 by 3 square grid map that contains the route from Home to the Office.
                    Your task is to plan the route from the Home position to the Office position. 
                    The tile that contains letter H represents the Home position, and the tile that contains letter O represents the Office position.
                    The tile that contains letter B represents obstacles like walls that you cannot pass through.
                    You can only move up, down, left, or right. You cannot move diagonally.
                    On the first row, you will find the H next to a B and then the B.
                    On the second row, you will find the X next to the B and then B.
                    On the third row, you will find the X next to another X and then the O.
                    There exists one and only one viable route for this map.
                    Each step you choose a direction and move to the end of the continuous road or the destination.
                    """,
                }
            ],
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": """Now you have all the information on the map.
                    You start at the position where the H which is the Home is located.
                    Provide the steps to navigate to the O which is the Office position. : Don't use visualization. Let's think step by step""",
                },
            ],
        },
    ],
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=HEADERS, json=VOT_NONVISION_PAYLOAD)
print(response.json()["choices"][0]["message"]["content"])