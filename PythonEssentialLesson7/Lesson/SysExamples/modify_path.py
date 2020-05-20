import os.path
import sys

# print(__file__)
# print(os.path.join('a', 'b'))

current_path = os.path.dirname(os.path.abspath(__file__))
parent_path = os.path.dirname(current_path)
module_path = os.path.join(parent_path, 'SampleModule')
sys.path.append(module_path)

import my_fibonacci

print(my_fibonacci.nth_fibonacci(10))
