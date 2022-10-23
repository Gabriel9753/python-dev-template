from tqdm import tqdm
import time

if __name__ == "__main__":
    with tqdm(total=100) as pbar:
        for i in range(10):
            time.sleep(0.1)
            pbar.update(10)