1. logger.py文件内容
    ```python
    import logging
    from logging.handlers import TimedRotatingFileHandler

    def get_logger(name, log_file=None, log_level='INFO'):
        """
        logger
        :param name: 模块名称
        :param log_file: 日志文件，如无则输出到标准输出
        :param log_level: 日志级别
        :return:
        """
        logger = logging.getLogger(name)
        logger.setLevel(log_level.upper())
        ch = TimedRotatingFileHandler(log_file, when='W0', encoding="utf-8")
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('[%(levelname)7s %(asctime)s %(module)s:%(lineno)4d] %(message)s',
                                    datefmt='%Y%m%d %I:%M:%S')
        ch.setFormatter(formatter)
        logger.addHandler(ch)

        handle = logging.StreamHandler()
        handle.setFormatter(formatter)
        logger.addHandler(handle)
        return logger


    # if __name__ == '__main__':
    #     logger = get_logger(__name__, log_file='log/test.log', log_level='DEBUG')
    #     logger.debug('hi')
    #     logger.info('hi')
    #     logger.error('hi')
    #     logger.warning('hi')

    ```

2. 代码文件内容
   ```python
    from logger import get_logger
    logger = get_logger(__name__, log_file = '/home/code/log/file.log', log_level = 'DEBUG')
    logger.info('xxx')
   ```