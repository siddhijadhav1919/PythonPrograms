import importlib.util
import os

folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
name = os.path.basename(__file__)[5:]
spec = importlib.util.spec_from_file_location("module", os.path.join(folder, "Code", name))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


assert module.common_elements([1, 2, 3, 4], [3, 4, 5]) == [3, 4]
assert module.common_elements([1, 2], [3, 4]) == []
assert module.common_elements([1, 1, 2], [1]) == [1]
assert module.common_elements([], [1]) == []
assert module.common_elements(["a", "b"], ["b", "a"]) == ["a", "b"]

print("All test cases passed.")
