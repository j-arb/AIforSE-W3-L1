import random
import re

def generate_uuid():
    def get_random_byte():
        return random.randint(0, 255)
    
    def replace(match):
        c = int(match.group(0))
        r = get_random_byte() & (15 >> (c // 4))
        return hex(c ^ r)[2:]

    uuid_pattern = '10000000-1000-4000-8000-100000000000'
    uuid = re.sub(r'[018]', replace, uuid_pattern)
    return uuid

# Example usage:
print(generate_uuid())
