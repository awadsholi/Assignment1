import time

def log_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Took time : {time.time() - start:.6f}s")
        return result
    return wrapper