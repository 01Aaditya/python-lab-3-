# Simple To-Do Manager Using Functional Programming

# Function to add a task
def add_task(task_list, task_name):
    return task_list + [{"name": task_name, "completed": False}]

# Function to list only pending tasks
def list_pending(task_list):
    return list(filter(lambda t: not t["completed"], task_list))

# Function to mark all tasks as complete
def complete_all(task_list):
    return list(map(lambda t: {**t, "completed": True}, task_list))

# Function to search tasks by keyword (case-insensitive)
def search_tasks(task_list, keyword):
    kw = keyword.lower()
    return list(filter(lambda t: kw in t["name"].lower(), task_list))

# Function to format tasks for display
def fmt(task):
    return f"{task['name']} - {'Done' if task['completed'] else 'Pending'}"

# ----------- Sample Workflow -----------
tasks = []
tasks = add_task(tasks, "Buy groceries")
tasks = add_task(tasks, "Finish assignment")
tasks = add_task(tasks, "Call friend")

# List incomplete tasks
print("Pending Tasks:", [fmt(t) for t in list_pending(tasks)])

# Mark all tasks as complete
tasks = complete_all(tasks)
print("After complete_all:", [fmt(t) for t in tasks])

# Search tasks with keyword "call"
print("Search Result:", [fmt(t) for t in search_tasks(tasks, "call")])
