import logging
from time import sleep

import utils

logging.getLogger("requests").setLevel(logging.WARNING)
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(filename)s:%(lineno)d %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


def sync_orders():
    while True:
        logger.info("Processing orders...")
        try:
            utils.process_orders()
        except Exception as e:
            logger.error(
                "The application crashed due to the following exception: %s", e
            )
        sleep(60)


if __name__ == "__main__":
    sync_orders()
