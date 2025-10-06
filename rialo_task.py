import csv
from datetime import datetime

# File to save task submissions
log_file = "rialo_task_log.csv"

def save_task(task_data):
    """Save task to CSV"""
    fieldnames = ["Timestamp", "Task", "Category", "Priority", "Deadline", "Notes", "AI_Performance", "Status"]
    
    try:
        with open(log_file, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # Write header if file is empty
            if csvfile.tell() == 0:
                writer.writeheader()
            writer.writerow(task_data)
    except Exception as e:
        print(f"Error saving task: {e}")

def main():
    print("Welcome to Rialo Task Simulator!")
    print("You are submitting an AI task to Rialo...\n")
    
    # Task inputs
    task_desc = input("Enter the task description: ").strip()
    category = input("Enter task category (drawing/text/analysis/etc.): ").strip()
    priority = input("Enter priority (high/medium/low): ").strip()
    deadline = input("Enter deadline (e.g., 2 hours, 1 day): ").strip()
    notes = input("Any extra notes for AI (optional): ").strip()
    
    # AI performance input
    while True:
        ai_perf = input("Rate AI performance (good/bad): ").strip().lower()
        if ai_perf in ["good", "bad"]:
            break
        print("⚠️ Invalid input. Please type 'good' or 'bad'.")
    
    status = "✅ Task completed successfully! Payment released." if ai_perf == "good" else "⚠️ Task pending review."
    
    # Save task
    task_data = {
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Task": task_desc,
        "Category": category,
        "Priority": priority,
        "Deadline": deadline,
        "Notes": notes,
        "AI_Performance": ai_perf,
        "Status": status
    }
    
    save_task(task_data)
    print(f"\n{status}\n")
    print("Task details saved to rialo_task_log.csv")

if __name__ == "__main__":
    main()
