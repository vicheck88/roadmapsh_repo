## TASK TRACKER

Solution of [Task Tracker](https://roadmap.sh/projects/task-tracker)

## Process

1. Clone the repository and move to the directory

```sh
git clone https://github.com/vicheck88/roadmapsh_repo.git
cd task_cli
```

2. install setup.py. You may need sudo command

```sh
sudo python3 setup.py install
```

3. Run the following commands. Instead of task-cli, I use task_cli

```sh
# Adding a new task
task_cli add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
task_cli update 1 "Buy groceries and cook dinner"
task_cli delete 1

# Marking a task as in progress or done
task_cli mark-in-progress 1
task_cli mark-done 1

# Listing all tasks
task_cli list

# Listing tasks by status
task_cli list done
task_cli list todo
task_cli list in-progress
```
