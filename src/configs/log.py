import logging


def configure_logging():
    logging.basicConfig(
        datefmt="%d.%m.%Y %H:%M:%S",
        format="%(asctime)s - [%(levelname)s] - %(message)s",
        level=logging.INFO,
        handlers=(logging.StreamHandler(), )
    )
