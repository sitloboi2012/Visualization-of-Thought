from openai import OpenAI

client = OpenAI()

gpt_4_vot = client.chat.completions.create(
    model = "gpt-4-turbo",
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
        down by one step, and then you go down by one step. What will you find? Please visualize the state after each reasoning step.
        """}
    ]
)

gpt_4_cot = client.chat.completions.create(
    model = "gpt-4-0125-preview",
    messages = [
        {"role": "system", "content": """
         You are a helpful assistant. You have been given a 3 by 3 square grid. Starting from a vertex, you will move
        along the edges of the grid. Initially, you are positioned at the bottom-left corner of the grid, where
        you will find a Cassette player, then you go right, where you will find a Wool, then you go right, where
        you will find an Conch. Then you go up, where you will find a Moving Van, then you go left, where
        you will find a Confectionary Store, then you go left, where you will find a Pot Pie. Then you go up,
        where you will find a Siamang, then you go right, where you will find a Black-and-white Colobus, then you
        go right, where you will find a Minivan. Let's think this step by step
        """},
        {"role": "user", "content": """
        Now you have all the information on the map. You start at
        the position where the Cassette player is located, then you go right by one step, then you go right by one step,
        then you go up by one step, then you go up by one step, then you go left by one step, then you go
        down by one step, and then you go down by one step. What will you find? Let's think this step by step
        """}
    ]
)

gpt_4_without_viz = client.chat.completions.create(
    model = "gpt-4-0125-preview",
    messages = [
        {"role": "system", "content": """
         You are a helpful assistant. You have been given a 3 by 3 square grid. Starting from a vertex, you will move
        along the edges of the grid. Initially, you are positioned at the bottom-left corner of the grid, where
        you will find a Cassette player, then you go right, where you will find a Wool, then you go right, where
        you will find an Conch. Then you go up, where you will find a Moving Van, then you go left, where
        you will find a Confectionary Store, then you go left, where you will find a Pot Pie. Then you go up,
        where you will find a Siamang, then you go right, where you will find a Black-and-white Colobus, then you
        go right, where you will find a Minivan. Don't use any visualization. Let's think this step by step
        """},
        {"role": "user", "content": """
        Now you have all the information on the map. You start at
        the position where the Cassette player is located, then you go right by one step, then you go right by one step,
        then you go up by one step, then you go up by one step, then you go left by one step, then you go
        down by one step, and then you go down by one step. What will you find? Don't use any visualization. Let's think this step by step
        """}
    ]
)

print(f"GPT_3.5: {gpt_4_vot.choices[0].message.content}")
print("-----------------")
print(f"GPT_4 COT: f{gpt_4_cot.choices[0].message.content}")
print("-----------------")
print(f"GPT_4 COT no Viz: {gpt_4_without_viz.choices[0].message.content}")