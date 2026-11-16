import importlib.util
import os

folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
name = os.path.basename(__file__)[5:]
spec = importlib.util.spec_from_file_location("module", os.path.join(folder, "Code", name))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


assert module.is_palindrome_number(121) is True
assert module.is_palindrome_number(123) is False
assert module.is_palindrome_number(0) is True
assert module.is_palindrome_number(-121) is False
assert module.is_palindrome_number(1221) is True
assert module.is_palindrome_number(10) is False

print("All test cases passed.")
