import importlib.util
import os

folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
name = os.path.basename(__file__)[5:]
spec = importlib.util.spec_from_file_location("module", os.path.join(folder, "Code", name))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


assert module.char_frequency("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}
assert module.char_frequency("") == {}
assert module.char_frequency("aab") == {"a": 2, "b": 1}
assert module.char_frequency("a a") == {"a": 2, " ": 1}

print("All test cases passed.")
