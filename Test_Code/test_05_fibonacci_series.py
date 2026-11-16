import importlib.util
import os

folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
name = os.path.basename(__file__)[5:]
spec = importlib.util.spec_from_file_location("module", os.path.join(folder, "Code", name))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


assert module.fibonacci_series(0) == []
assert module.fibonacci_series(-3) == []
assert module.fibonacci_series(1) == [0]
assert module.fibonacci_series(2) == [0, 1]
assert module.fibonacci_series(7) == [0, 1, 1, 2, 3, 5, 8]
assert module.fibonacci_series(10)[-1] == 34

print("All test cases passed.")
