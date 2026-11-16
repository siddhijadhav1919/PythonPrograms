import importlib.util
import os

folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
name = os.path.basename(__file__)[5:]
spec = importlib.util.spec_from_file_location("module", os.path.join(folder, "Code", name))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


assert module.remove_duplicates([1, 2, 2, 3, 1]) == [1, 2, 3]
assert module.remove_duplicates([]) == []
assert module.remove_duplicates(["a", "b", "a"]) == ["a", "b"]
assert module.remove_duplicates([1, 1, 1]) == [1]

print("All test cases passed.")
