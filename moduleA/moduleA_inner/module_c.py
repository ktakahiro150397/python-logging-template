
import logging

from logger_factory import LoggerFactory

module_logger = LoggerFactory.getLogger(__name__)

class moduleC:
    def __init__(self):
        # self.logger = logging.getLogger(__name__)

        module_logger.info("moduleC is initialized")
        module_logger.warn("moduleC warning")
