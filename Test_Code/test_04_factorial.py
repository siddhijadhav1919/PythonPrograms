import importlib.util
import os

folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
name = os.path.basename(__file__)[5:]
spec = importlib.util.spec_from_file_location("module", os.path.join(folder, "Code", name))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


assert module.factorial(0) == 1
assert module.factorial(1) == 1
assert module.factorial(5) == 120
assert module.factorial(10) == 3628800

try:
    module.factorial(-1)
    assert False, "Expected ValueError for negative input"
except ValueError:
    pass

print("All test cases passed.")
