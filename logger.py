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
        time.sleep(5)

if __name__ == "__main__":
    main()
