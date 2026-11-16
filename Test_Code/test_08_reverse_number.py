import importlib.util
import os

folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
name = os.path.basename(__file__)[5:]
spec = importlib.util.spec_from_file_location("module", os.path.join(folder, "Code", name))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


assert module.reverse_number(123456) == 654321
assert module.reverse_number(100) == 1
assert module.reverse_number(0) == 0
assert module.reverse_number(-123) == -321
assert module.reverse_number(7) == 7

print("All test cases passed.")
