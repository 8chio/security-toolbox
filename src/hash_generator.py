import hashlib

def generate_sha256_hash(input_string):

    return hashlib.sha256(input_string.encode()).hexdigest()