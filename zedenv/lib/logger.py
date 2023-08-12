"""
Common functions
"""

import logging.config
import logging.handlers
import sys


class ZELogger:
    logger_config = {
        'version': 1,
        'formatters': {
            'console': {
                'class': 'logging.Formatter',
                'format': '%(message)s',
            },
            'error': {
                'class': 'logging.Formatter',
                'format': '%(message)s',
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': logging.INFO,
                'formatter': 'console',
                'stream': sys.stdout,
            },
            'error': {
                'class': 'logging.StreamHandler',
                'level': logging.DEBUG,
                'formatter': 'error',
            },
        },
        'root': {
            'level': logging.INFO,
            'handlers': ['console']
        },
    }

    logging.config.dictConfig(logger_config)
    logger = logging.getLogger(__name__)

    @classmethod
    def callback(cls, log, exit_on_error=False):
        """Helper to call the appropriate logging level"""

        if log['level'] == 'CRITICAL':
            cls.logger.critical(log['message'])

        elif log['level'] == 'ERROR':
            cls.logger.error(log['message'])

        elif log['level'] == 'WARNING':
            cls.logger.warning(log['message'])

        elif log['level'] == 'INFO':
            cls.logger.info(log['message'])

        elif log['level'] == 'DEBUG':
            cls.logger.debug(log['message'])

        elif log['level'] == 'EXCEPTION':
            if not exit_on_error:
                raise RuntimeError(log['message'])
            cls.logger.error(log['message'])
            raise SystemExit(1)

    @classmethod
    def log(cls, content, exit_on_error=False):
        level = content["level"]
        message = content["message"]

        cls.callback({
            "level": level,
            "message": message
        }, exit_on_error)

    @classmethod
    def verbose_log(cls, content, verbose_logs, exit_on_error=False):
        if verbose_logs:
            cls.log(content, exit_on_error=exit_on_error)
