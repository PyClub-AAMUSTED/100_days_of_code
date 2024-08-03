import sys
from pathlib import Path

# Add the root directory of the project to the PYTHONPATH
project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))

from beginner.new.day_5_task import task_solution as run_test

assert run_test(1) == 1
assert run_test(0) == 0
assert run_test(5) == [0, 1, 1, 2, 3, 5]
assert run_test(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
