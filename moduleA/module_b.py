
import logging

from logger_factory import LoggerFactory
from moduleA.module_a import moduleA

module_logger = LoggerFactory.getLogger(__name__)

class moduleB(moduleA):
    def __init__(self):
        module_logger.info("moduleB is initialized")
