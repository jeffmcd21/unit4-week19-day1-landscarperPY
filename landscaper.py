
# ~ # ----- OPENING STATEMENT ----- # ~ #
print("Welcome to Grasslandia, Let's begin!")

# ~ # ----- PLAYER DICTIONARY ----- # ~ #
workers = {
    "money": 0,
    "tool": 0,
    "expense": 0,
    "is_trimmed": False
}

# ~ # ----- TOOLS DICTIONARY ----- # ~ #
tools = [
    { "name": "teeth", "price": 0, "revenue": 1 },
    {"name": "rusty scissors", "price": 5, "revenue": 5},
    {"name": "old-timey push mower", "price": 25, "revenue": 50},
]

# ~ # ----- CUTTING FUNCTION ----- # ~ #
def cut_grass():
    tool = tools[workers['tool']]
    print(f"That property is done! Using {tool['name']} you earned ${tool['revenue']}")
    workers['money'] += tool['revenue']

# ~ # ----- UPGRAGE FUNCTION ----- # ~ #
def updrade():
    if workers['tool'] < len(tools) - 1:
        next_tool_index = workers['tool'] + 1
        next_tool = tools[next_tool_index]
        if workers['money'] >= next_tool['price']:
            workers['money'] -= next_tool['price']
            workers['tool'] = next_tool_index
        else:
            print('You cannot afford that yet')
    else:
        print('You have the best available tool')

# ~ # ----- USER INPUT LOOP ----- # ~ #
while not workers["is_trimmed"]:
    response = input(
        f"You currently have ${workers['money']}.00 ,"
        f"do you want to [c]ut grass or [u]pgrade equipment?\n"
    )

    if response.lower() == 'c':
        cut_grass()
    elif response.lower() == 'u':
        updrade()
    else:
        print("Input error, please try again")