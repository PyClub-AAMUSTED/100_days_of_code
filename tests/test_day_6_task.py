def run_test(string):
    return string[::-1]


print(run_test("man of the year"))

import sys
from pathlib import Path

# Add the root directory of the project to the PYTHONPATH
project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))

from beginner.new.day_6_task import task_solution as run_test

def test():
    assert run_test("man") == "nam"
    assert run_test("mom") == "mom"
    assert run_test("dad") == "dad"
    assert run_test("sister") == "retsis"
