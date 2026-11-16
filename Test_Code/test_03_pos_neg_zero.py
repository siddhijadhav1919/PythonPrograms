import importlib.util
import os

folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
name = os.path.basename(__file__)[5:]
spec = importlib.util.spec_from_file_location("module", os.path.join(folder, "Code", name))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


assert module.check_number(5) == "Positive"
assert module.check_number(-3) == "Negative"
assert module.check_number(0) == "Zero"
assert module.check_number(0.5) == "Positive"
assert module.check_number(-0.5) == "Negative"

print("All test cases passed.")
