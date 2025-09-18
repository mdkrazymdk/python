from src.string_utils import print_string, check_case
from src.even_odd_gen import even_odd_generator

print_string("Привіт, світе!")
check_case("ПРИВІТ")
check_case("світ")
print_string(123)

gen = even_odd_generator()
print(next(gen))
print(next(gen))
