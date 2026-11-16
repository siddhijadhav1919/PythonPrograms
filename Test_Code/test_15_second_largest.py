import importlib.util
import os

folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
name = os.path.basename(__file__)[5:]
spec = importlib.util.spec_from_file_location("module", os.path.join(folder, "Code", name))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


assert module.second_largest([1, 2, 3, 4]) == 3
assert module.second_largest([5, 5, 4]) == 4
assert module.second_largest([10, 10]) is None
assert module.second_largest([7]) is None
assert module.second_largest([]) is None
assert module.second_largest([-1, -2, -3]) == -2
assert module.second_largest([3, 1, 2]) == 2

print("All test cases passed.")
