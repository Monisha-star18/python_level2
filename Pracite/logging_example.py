import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("FoodInventory application started")
logging.warning("Low stock detected")
logging.error("Unable to read inventory file")