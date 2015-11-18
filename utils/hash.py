import time
import hashlib

def generate_sha256():
    return hashlib.sha256(str(time.time())).hexdigest()
