import logging

from logger_factory import LoggerFactory

module_logger = LoggerFactory.getLogger(__name__)

def module_function():
    module_logger.info("TestModule is initialized / module logger")

class TestModule:
    def __init__(self) -> None:
        module_function()

        self.logger = LoggerFactory.getLogger(f"{__name__}.{self.__class__.__name__}")
        
        self.logger.info("TestModule is initialized / instance logger")
