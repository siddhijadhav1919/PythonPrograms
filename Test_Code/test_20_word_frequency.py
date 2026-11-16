import importlib.util
import os

folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
name = os.path.basename(__file__)[5:]
spec = importlib.util.spec_from_file_location("module", os.path.join(folder, "Code", name))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


assert module.word_frequency("the cat and the hat") == {"the": 2, "cat": 1, "and": 1, "hat": 1}
assert module.word_frequency("Hello, hello!") == {"hello": 2}
assert module.word_frequency("") == {}
assert module.word_frequency("a b a") == {"a": 2, "b": 1}

print("All test cases passed.")
