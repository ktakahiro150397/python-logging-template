import asyncio
import logging

from logger_factory import LoggerFactory
from moduleA.moduleA_inner.module_c import moduleC
from moduleA.module_a import moduleA
from moduleA.module_b import moduleB
from test_module import TestModule

# ロガーを取得し、出力
logger = LoggerFactory.getLogger(__name__)
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG) # ここのログレベル設定が必要(logger自身のログレベル)

# log_format = "%(asctime)s [%(levelname)-8s] [%(filename)s:%(lineno)d] %(name)s %(message)s"

# stream_handler = logging.StreamHandler()
# stream_handler.setLevel(logging.DEBUG)
# stream_handler.setFormatter(logging.Formatter(log_format))
# logger.addHandler(stream_handler)

# file_handler = logging.FileHandler("application.log")
# file_handler.setLevel(logging.DEBUG)
# file_handler.setFormatter(logging.Formatter(log_format))
# logger.addHandler(file_handler)

# logging.basicConfig(
#     filename="application.log",
#     level=logging.DEBUG,
#     format="%(asctime)s [%(levelname)-8s] %(name)s %(message)s",
#     datefmt="%Y-%m-%d %H:%M:%S",
#     encoding="utf-8",
# )

async def main():
    try:
        # logging.debug("root_debug_main")
        
        logger.debug("debug_main")
        logger.info("info_main")
        logger.warning("warning_main")
        logger.error("error_main")
        logger.critical("critical_main")

        var = "test_var"
        logger.info("var is \"%s\"",var)

        mod = TestModule()

        modA = moduleA()
        modB = moduleB()
        modC = moduleC()

        # エラーを起こす
        3/0

    except Exception as e:
        logger.exception(e)

if __name__ == "__main__":
    asyncio.run(main())
