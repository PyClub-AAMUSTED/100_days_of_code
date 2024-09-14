import sys
from pathlib import Path

# Add the root directory of the project to the PYTHONPATH
project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))

from beginner.new.day_3_task import task_solution as run_test


def test():
    assert run_test(2) == "Even"
    assert run_test(-1) == "Odd"
    assert run_test(1.4) == "Odd"
    assert run_test(-2) == "Even"
    assert run_test(3) == "Odd"
