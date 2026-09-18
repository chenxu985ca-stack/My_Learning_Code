import pathlib
import json

username = input("What's your name?: ")

path = pathlib.Path(
    "/Users/lee/Workspace/My_Learning_Code/python_projects/username.json")

contents = json.dumps(username)

path.write_text(contents)
print(f"I will always remember your name {username}!")
