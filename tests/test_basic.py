import sys
import os
import pytest
import json
from datetime import datetime
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from tasks import (
    load_tasks,
    save_tasks,
    generate_unique_id,
    filter_tasks_by_priority,
    filter_tasks_by_category,
    filter_tasks_by_completion,
    search_tasks,
    get_overdue_tasks,
    DEFAULT_TASKS_FILE
)

# Mocking file system for testing purposes
@pytest.fixture
def mock_tasks():
    return [
        {"id": 1, "title": "Task 1", "priority": "High", "category": "Work", "completed": False, "due_date": "2025-05-01", "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
        {"id": 2, "title": "Task 2", "priority": "Medium", "category": "School", "completed": True, "due_date": "2025-04-01", "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
        {"id": 3, "title": "Task 3", "priority": "Low", "category": "Personal", "completed": False, "due_date": "2025-04-10", "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    ]

# ----- Test load_tasks ----- 
def test_load_tasks(mock_tasks):
    file_path = "mock_tasks.json"
    save_tasks(mock_tasks, file_path)
    loaded_tasks = load_tasks(file_path)
    assert len(loaded_tasks) == len(mock_tasks)
    assert loaded_tasks[0]["title"] == "Task 1"
    assert loaded_tasks[1]["completed"] is True
    assert loaded_tasks[2]["priority"] == "Low"

# ----- Test save_tasks -----
def test_save_tasks(mock_tasks):
    file_path = "mock_save_tasks.json"
    save_tasks(mock_tasks, file_path)
    with open(file_path, "r") as f:
        saved_tasks = json.load(f)
    assert len(saved_tasks) == len(mock_tasks)
    assert saved_tasks[0]["id"] == 1

# ----- Test generate_unique_id -----
def test_generate_unique_id(mock_tasks):
    task_id = generate_unique_id(mock_tasks)
    assert task_id == 4  # Since the existing tasks have ids 1, 2, 3, the next should be 4

# ----- Test filter_tasks_by_priority -----
def test_filter_tasks_by_priority(mock_tasks):
    high_priority_tasks = filter_tasks_by_priority(mock_tasks, "High")
    assert len(high_priority_tasks) == 1
    assert high_priority_tasks[0]["priority"] == "High"

# ----- Test filter_tasks_by_category -----
def test_filter_tasks_by_category(mock_tasks):
    school_tasks = filter_tasks_by_category(mock_tasks, "School")
    assert len(school_tasks) == 1
    assert school_tasks[0]["category"] == "School"

# ----- Test filter_tasks_by_completion -----
def test_filter_tasks_by_completion(mock_tasks):
    completed_tasks = filter_tasks_by_completion(mock_tasks, True)
    assert len(completed_tasks) == 1
    assert completed_tasks[0]["completed"] is True

    incomplete_tasks = filter_tasks_by_completion(mock_tasks, False)
    assert len(incomplete_tasks) == 2
    assert incomplete_tasks[0]["completed"] is False

# ----- Test search_tasks -----
def test_search_tasks(mock_tasks):
    searched_tasks = search_tasks(mock_tasks, "Task 1")
    assert len(searched_tasks) == 1
    assert searched_tasks[0]["title"] == "Task 1"

    searched_tasks = search_tasks(mock_tasks, "nonexistent")
    assert len(searched_tasks) == 0

# ----- Test get_overdue_tasks -----
def test_get_overdue_tasks(mock_tasks):
    overdue_tasks = get_overdue_tasks(mock_tasks)
    assert len(overdue_tasks) == 1
    assert overdue_tasks[0]["due_date"] == "2025-04-10"

# ----- Test that the tasks file is handled properly -----
def test_file_operations(mock_tasks):
    file_path = "test_tasks.json"
    
    # Save tasks to file
    save_tasks(mock_tasks, file_path)
    
