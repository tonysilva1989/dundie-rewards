import os
import logging
from logging import handlers

LOG_LEVEL = os.getenv("LOG_LEVEL","WARNING").upper()

# getLogger gets an existing instance of Logger, if does exist. This is more useful since this
# module will be called in other parts of the project
# calling only Logger will return a new object
log = logging.getLogger("dundie")
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s'
    'l:%(lineno)d f:%(filename)s: %(message)s'
)

def get_logger(logfile='dundie.log'):
    """Returns a configured logger."""

    fh = handlers.RotatingFileHandler(
        "mylog.log",
        maxBytes=300,
        backupCount=10,
    )

    fh.setLevel(LOG_LEVEL)
    fh.setFormatter(fmt)
    log.addHandler(fh)
    return log
