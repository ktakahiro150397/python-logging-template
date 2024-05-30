
import logging

from logger_factory import LoggerFactory

module_logger = LoggerFactory.getLogger(__name__)

class moduleA:
    def __init__(self):
        # self.logger = logging.getLogger(__name__)

        module_logger.info("moduleA is initialized")
