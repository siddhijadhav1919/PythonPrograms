import importlib.util
import os

folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
name = os.path.basename(__file__)[5:]
spec = importlib.util.spec_from_file_location("module", os.path.join(folder, "Code", name))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


assert module.largest_of_three(1, 2, 3) == 3
assert module.largest_of_three(9, 2, 3) == 9
assert module.largest_of_three(1, 8, 3) == 8
assert module.largest_of_three(5, 5, 5) == 5
assert module.largest_of_three(-1, -2, -3) == -1
assert module.largest_of_three(3, 3, 1) == 3

print("All test cases passed.")
