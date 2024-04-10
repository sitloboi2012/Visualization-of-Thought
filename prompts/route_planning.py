from openai import OpenAI
import base64
import requests

client = OpenAI()

# OpenAI API Key
api_key = ""


# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


# Path to your image
route = "prompts/route_planning_img.png"

# Getting the base64 string
encode_route = encode_image(route)


headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}

vot_method = {
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
                    "text": "Now given the image of the map, tarting from the Home position, provide the steps to navigate to Office position. Visualize the state after each reasoning step.",
                },
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{encode_route}"},
                },
            ],
        },
    ],
}

cot_method = {
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
                    Let's think this step by step
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

gpt_4_cot = client.chat.completions.create(
    model = "gpt-4-0125-preview",
    messages = [
        {"role": "system", "content": """
        You are a helpful assistant. You have been given a 3 by 3 square grid. 
        Starting from a vertex, you will move along the edges of the grid. 
        Initially, you are positioned at the bottom-left corner of the grid, where
        you will find a Path, then you go right, where you will find a Path, then you go right, where
        you will find the Office. Then you go up, where you will find a Blocker, then you go left, where
        you will find a Blocker, then you go left, where you will find a Blocker. Then you go up,
        where you will find the House, then you go right, where you will find a Blocker, then you
        go right, where you will find a Blocker.
        """},
        {"role": "user", "content": """
        Now you have all the information on the map. 
        You start at the House position, provide the steps to navigate to Office position without blocking by the Blocker.
        Please visualize the state after each reasoning step.
        """}
    ]
)

#response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=cot_method)

#print(response.json()["choices"][0]["message"]["content"])

print(gpt_4_cot.choices[0].message.content)
