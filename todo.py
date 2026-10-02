import sys
import json
import os

FILE = "todos.json"

if os.path.exists(FILE):
    with open(FILE, "r", encoding="utf-8") as f:
        todos = json.load(f)
else:
    todos = []

command = sys.argv[1]

if command == "add":
    task = sys.argv[2]
    todos.append(task)
    print("追加しました:", task)
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False)
elif command == "list":
    for i, task in enumerate(todos, 1):
        print(i, task)