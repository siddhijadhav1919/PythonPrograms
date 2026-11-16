import importlib.util
import os

folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
name = os.path.basename(__file__)[5:]
spec = importlib.util.spec_from_file_location("module", os.path.join(folder, "Code", name))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


assert module.check_even_odd(4) == "Even"
assert module.check_even_odd(7) == "Odd"
assert module.check_even_odd(0) == "Even"
assert module.check_even_odd(-3) == "Odd"

print("All test cases passed.")
