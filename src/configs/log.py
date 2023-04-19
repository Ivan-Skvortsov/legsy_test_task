import logging
#  TODO: перенсти в инициализацию приложения, не нужно этого делать здесь


def configure_logging():
    logging.basicConfig(
        datefmt="%d.%m.%Y %H:%M:%S",
        format="%(asctime)s - [%(levelname)s] - %(message)s",
        level=logging.INFO,  # TODO
        handlers=(logging.StreamHandler())
    )
