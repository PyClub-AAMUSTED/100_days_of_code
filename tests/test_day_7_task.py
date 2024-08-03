import sys
from pathlib import Path

# Add the root directory of the project to the PYTHONPATH
project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))

from beginner.new.day_7_task import task_solution as run_test


def test():
    assert run_test("madam") == True
    assert run_test("racecar") == True
    assert run_test("hello") == False
    assert run_test("world") == False
