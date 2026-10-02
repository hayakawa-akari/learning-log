import sys

todos = []

command = sys.argv[1]

if command == "add":
    task = sys.argv[2]
    todos.append(task)
    print("追加しました:", task)
elif command == "list":
    for i, task in enumerate(todos, 1):
        print(i, task)