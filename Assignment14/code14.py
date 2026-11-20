import logging

logger = logging.getLogger("MyLogger")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()

file_handler = logging.FileHandler(
    "experiment14.log",
    mode="a",
    encoding="utf-8"
)

console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.debug("This is a DEBUG message")

logger.info("This is an INFO message")

logger.warning("This is a WARNING message")

logger.error("This is an ERROR message")

logger.critical("This is a CRITICAL message")

print("Logging completed successfully!")