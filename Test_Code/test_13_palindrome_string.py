import importlib.util
import os

folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
name = os.path.basename(__file__)[5:]
spec = importlib.util.spec_from_file_location("module", os.path.join(folder, "Code", name))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


assert module.is_palindrome_string("madam") is True
assert module.is_palindrome_string("Racecar") is True
assert module.is_palindrome_string("hello") is False
assert module.is_palindrome_string("A man, a plan, a canal: Panama") is True
assert module.is_palindrome_string("") is True
assert module.is_palindrome_string("ab") is False

print("All test cases passed.")
