import csv


def read_task_list(filename="tasks.txt"):
    """Read tasks from a text file and return a list of task lines."""
    tasks = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            tasks.append(line.strip())
    return tasks


def add_task_to_csv(task, priority, status, filename="tasks.csv"):
    """Append a new task row to a CSV file."""
    with open(filename, "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([task, priority, status])
    return True


def generate_report(text_filename="tasks.txt", csv_filename="tasks.csv"):
    """Generate a simple report from the text and CSV files."""
    task_list = read_task_list(text_filename)
    status_counts = {}

    with open(csv_filename, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            status = row.get("status", "unknown").strip().lower()
            status_counts[status] = status_counts.get(status, 0) + 1

    report_parts = [f"Total tasks: {len(task_list)}"]
    report_parts.append(", ".join(f"{status}={count}" for status, count in status_counts.items()))
    return "\n".join(report_parts)


if __name__ == "__main__":
    print("Task list:", read_task_list())
    print("Add task result:", add_task_to_csv("Review pull requests", "high", "pending"))
    print(generate_report())
