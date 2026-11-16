import importlib.util
import os

folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
name = os.path.basename(__file__)[5:]
spec = importlib.util.spec_from_file_location("module", os.path.join(folder, "Code", name))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


assert module.is_prime(2) is True
assert module.is_prime(3) is True
assert module.is_prime(17) is True
assert module.is_prime(97) is True
assert module.is_prime(0) is False
assert module.is_prime(1) is False
assert module.is_prime(-7) is False
assert module.is_prime(4) is False
assert module.is_prime(9) is False
assert module.is_prime(100) is False

print("All test cases passed.")
