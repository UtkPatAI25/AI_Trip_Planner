import logging
import os

# Ensure the logs directory exists
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler("logs/ai_trip_planner.log"),  # Log to logs folder
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("ai_trip_planner")