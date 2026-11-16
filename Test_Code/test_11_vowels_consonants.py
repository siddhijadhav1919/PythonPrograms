import importlib.util
import os

folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
name = os.path.basename(__file__)[5:]
spec = importlib.util.spec_from_file_location("module", os.path.join(folder, "Code", name))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


assert module.count_vowels_consonants("Hello World") == (3, 7)
assert module.count_vowels_consonants("") == (0, 0)
assert module.count_vowels_consonants("aeiou") == (5, 0)
assert module.count_vowels_consonants("bcd") == (0, 3)
assert module.count_vowels_consonants("AEx 12!") == (2, 1)

print("All test cases passed.")
