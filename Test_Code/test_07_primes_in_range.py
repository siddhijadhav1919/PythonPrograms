import importlib.util
import os

folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
name = os.path.basename(__file__)[5:]
spec = importlib.util.spec_from_file_location("module", os.path.join(folder, "Code", name))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


assert module.primes_in_range(1, 10) == [2, 3, 5, 7]
assert module.primes_in_range(10, 20) == [11, 13, 17, 19]
assert module.primes_in_range(20, 22) == []
assert module.primes_in_range(2, 2) == [2]
assert module.primes_in_range(-5, 5) == [2, 3, 5]
assert module.primes_in_range(10, 1) == []

print("All test cases passed.")
