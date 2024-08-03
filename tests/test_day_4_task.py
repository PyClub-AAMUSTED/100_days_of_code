import sys
from pathlib import Path

# Add the root directory of the project to the PYTHONPATH
project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))

from beginner.new.day_4_task import task_solution as run_test

def test():
    assert run_test(1) == 1
    assert run_test(0) == 1
    assert run_test(5) == 120
    assert run_test(10) == 3628800
    assert run_test(20) == 2432902008176640000
