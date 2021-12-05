import hashlib

def compute_lowest_md5_hash(input: str):
    i = 1
    while True:
        
        digest = hashlib.md5(input + str(i)).hexdigest()
        if digest.startswith('00000'):
            return digest, i
        i += 1
