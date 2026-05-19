# 📘 Assignment: Python File Automation

## 🎯 Objective

Practice reading and writing files in Python by automating a small data workflow using text and CSV files.

## 📝 Tasks

### 🛠️ Read and summarize a text file

#### Description
Create a function named `read_task_list()` that reads a plain text file containing a list of tasks and returns the contents as a list of strings.

#### Requirements
Completed program should:

- Open the file named `tasks.txt` in read mode.
- Read each line from the file and strip any trailing whitespace.
- Return a list of task descriptions.
- Example output:
  ```python
  ["Prepare presentation", "Write unit tests", "Review code"]
  ```

### 🛠️ Update a CSV task tracker

#### Description
Create a function named `add_task_to_csv()` that appends a new task row to a CSV file.

#### Requirements
Completed program should:

- Open the file named `tasks.csv` in append mode.
- Add a new row with `task`, `priority`, and `status` values.
- Use the CSV header format: `task,priority,status`.
- Return `True` when the row is successfully written.

### 🛠️ Generate an automation report

#### Description
Create a function named `generate_report()` that reads both the text file and the CSV file, then returns a summary string.

#### Requirements
Completed program should:

- Call `read_task_list()` to load tasks from `tasks.txt`.
- Read `tasks.csv` and count how many tasks are in each status.
- Return a report string with the total number of tasks and a count for each status.
- Example output:
  ```text
  Total tasks: 5
  Status counts: pending=2, in progress=1, done=2
  ```
