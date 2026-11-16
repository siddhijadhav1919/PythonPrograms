import importlib.util
import os

folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
name = os.path.basename(__file__)[5:]
spec = importlib.util.spec_from_file_location("module", os.path.join(folder, "Code", name))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


assert module.sum_of_digits(123) == 6
assert module.sum_of_digits(0) == 0
assert module.sum_of_digits(9999) == 36
assert module.sum_of_digits(-45) == 9
assert module.sum_of_digits(5) == 5

print("All test cases passed.")
