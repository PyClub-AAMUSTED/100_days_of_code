import sys
from pathlib import Path

# Add the root directory of the project to the PYTHONPATH
project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))

from beginner.new.day_2_task import task_solution as run_test


def test_run_test():
    assert run_test(2, 3) == 5
    assert run_test(-2, 3) == 1
    assert run_test(2, -3) == -1
    assert run_test(-2, -3) == -5
    assert run_test(0, 0) == 0
    assert run_test(2, 0) == 2
    assert run_test(-2, 0) == -2
    assert run_test(0, -3) == -3
    assert run_test(0, 3) == 3


if __name__ == "__main__":
    test_run_test()
