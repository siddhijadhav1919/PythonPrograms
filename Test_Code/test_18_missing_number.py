import importlib.util
import os

folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
name = os.path.basename(__file__)[5:]
spec = importlib.util.spec_from_file_location("module", os.path.join(folder, "Code", name))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


assert module.missing_number([1, 2, 4, 5]) == 3
assert module.missing_number([2, 3, 4]) == 1
assert module.missing_number([1, 2, 3]) == 4
assert module.missing_number([1]) == 2
assert module.missing_number([3, 1, 2, 5]) == 4
assert module.missing_number([]) == 1

print("All test cases passed.")
