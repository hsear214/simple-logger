import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    count = 0
    while True:
        count += 1
        logging.info(f"Heartbeat log #{count}")
<<<<<<< HEAD
        time.sleep(0.5)
=======
        time.sleep(5)
>>>>>>> 7b10a5df1ac9723f5a3ff41ef706216a0a0d8a90

if __name__ == "__main__":
    main()
