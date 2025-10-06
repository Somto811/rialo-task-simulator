# Rialo Task Simulator

A simple Python-based simulator for submitting AI tasks on Rialo.  
This tool lets you log tasks, rate AI performance, and keeps a record of all submissions in a CSV file. Perfect for beginners joining the Rialo Builder Program.

---

## Features

- Submit AI tasks with:
  - Task description
  - Category (drawing, text, analysis, etc.)
  - Priority (high, medium, low)
  - Deadline
  - Optional notes
- Rate AI performance as **good** or **bad**
- Automatic task status:
  - ✅ Task completed successfully! Payment released.
  - ⚠️ Task pending review
- Logs all submissions in `rialo_task_log.csv`
- Display tasks in a clean table format using **prettytable**
- Beginner-friendly and easy to run

---

## Requirements

- Python 3.10 or higher
- Pip (Python package manager)
- `prettytable` library

---

## Installation & Setup

1. Clone the repository:

```bash
git clone https://github.com/somto811/rialo-task-simulator.git
cd rialo-task-simulator


---

## Install Dependencies

```bash
pip install prettytable


---

## Run the Simulator

```bash
python3 rialo_task.py


## How to Use

1. Enter a task description.  
2. Select a category, priority, and deadline.  
3. Add optional notes for the AI task.  
4. Rate AI performance as **good** or **bad**.  
5. The task is logged in `rialo_task_log.csv` and shows task status.  
6. Repeat for multiple tasks. You can track all submissions in the CSV file.
