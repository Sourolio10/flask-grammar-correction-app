import logging

def get_logger(name, level=logging.DEBUG):
    """
    Create and return a logger with the specified name and level.
    Logs will be output to the console.

    :param name: Name of the logger.
    :param level: Logging level, e.g., logging.DEBUG, logging.INFO.
    :return: Configured logger.
    """
    # Create a logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(level)

    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Add formatter to ch
    ch.setFormatter(formatter)

    # Add ch to logger
    logger.addHandler(ch)

    # IMPORTANT: Avoid adding handlers repeatedly if running this function multiple times.
    # This checks if the handler is already added to the logger.
    if not logger.hasHandlers():
        logger.addHandler(ch)

    return logger

logger = get_logger(__name__)

