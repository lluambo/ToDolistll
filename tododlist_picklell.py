import sys
import pickle

file_name = "todo_data.txt" #if you want to change the file name
todos = []

# Read File
try:
    file = open(file_name, "rb")
    todos = pickle.load(file)
    file.close()
except:
    pass   

# Add d
if len(sys.argv) >= 3 and sys.argv[1].lower() == "add":
    todos.append(f"{sys.argv[2]}\n")


# Remove d
if len(sys.argv) >= 3 and sys.argv[1].lower() == "remove":
    try:
        index_to_del= int(sys.argv[2])
    except ValueError:
        print("Wrong number")
        sys.exit(1)
    if index_to_del > 0:
        index_to_del -= 1
        del(todos[index_to_del])
    else:
        print("Wrong number")
        sys.exit(1)

# Save File
file = open(file_name, "wb")
pickle.dump(todos, file)
file.close()
# Print List
print("\n*******************************\n")
print(f"Your ToDos:\n")
if len(todos) == 0:
    print("No ToDos, add one!")
else:
    for index in range(len(todos)):
        print(f"{index+1}. {todos[index]}", end="")
    
# Print Commands
print("\n*******************************\n")
print(f"To view ToDos:\n{sys.argv[0]}")
print(f"\nTo add a ToDo:\n{sys.argv[0]} add \"Clean Room\"\n")
print(f"To remove or complete ToDo:\n{sys.argv[0]} remove 2\n")
