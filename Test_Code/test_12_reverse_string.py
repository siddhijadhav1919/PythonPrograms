import importlib.util
import os

folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
name = os.path.basename(__file__)[5:]
spec = importlib.util.spec_from_file_location("module", os.path.join(folder, "Code", name))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


assert module.reverse_string("hello") == "olleh"
assert module.reverse_string("") == ""
assert module.reverse_string("a") == "a"
assert module.reverse_string("Python 3") == "3 nohtyP"

print("All test cases passed.")
