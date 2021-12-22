
users_and_bits = {}
user_name = 'andre'
user_bid = 12
users_and_bits[user_name] = user_bid
users_and_bits['max'] = 231
value = []

for keys, values in users_and_bits.items():
    value.append(values)

def get_key(users_and_bits, value):
    for k, v in users_and_bits.items():
        if v == value:
            return k