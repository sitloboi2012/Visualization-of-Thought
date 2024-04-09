from openai import OpenAI
from prompts.natural_language_navigation import VISUALIZATION_OF_THOUGHT_PROMPT

client = OpenAI()

response_1 = client.chat.completions.create(
    model = "gpt-4-0125-preview",
    messages = [
        {"role": "system", "content": """
        You are a helpful assistant. You have been given a 3 by 3 square grid. Starting from a vertex, you will move
        along the edges of the grid. Initially, you are positioned at the bottom-left corner of the grid, where
        you will find a Cassette player, then you go right, where you will find a Wool, then you go right, where
        you will find an Conch. Then you go up, where you will find a Moving Van, then you go left, where
        you will find a Confectionary Store, then you go left, where you will find a Pot Pie. Then you go up,
        where you will find a Siamang, then you go right, where you will find a Black-and-white Colobus, then you
        go right, where you will find a Minivan.
        Please visualize the state after each reasoning step.
         """},
        {"role": "user", "content": """
         Now you have all the information on the map. You start at
        the position where the Cassette player is located, then you go right by one step, then you go right by one step,
        then you go up by one step, then you go up by one step, then you go left by one step, then you go
        down by one step, and then you go down by one step. What will you find?
        """}
    ]
)

response_2 = client.chat.completions.create(
    model = "gpt-4-0125-preview",
    messages = [
        {"role": "system", "content": "You are a helpful assistant.  Don't use any visualization. Let's think this step by step"},
        {"role": "user", "content": VISUALIZATION_OF_THOUGHT_PROMPT}
    ]
)

print(response_1.choices[0].message.content)