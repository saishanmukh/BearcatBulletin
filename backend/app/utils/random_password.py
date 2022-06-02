# generate a random token

import random
import string

# generate a random token
def generate_token():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))