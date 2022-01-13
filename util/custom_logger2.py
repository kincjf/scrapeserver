import logging
import logging.config
import json
from logging.handlers import RotatingFileHandler
from logging.handlers import TimedRotatingFileHandler


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG) # 모든 레벨의 로그를 Handler들에게 전달해야 합니다.

formatter = logging.Formatter('%(asctime)s:%(module)s:%(levelname)s:%(message)s', '%Y-%m-%d %H:%M:%S')

# INFO 레벨 이상의 로그를 콘솔에 출력하는 Handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# DEBUG 레벨 이상의 로그를 `debug.log`에 출력하는 Handler
file_debug_handler = logging.FileHandler('debug.log')
file_debug_handler.setLevel(logging.DEBUG)
file_debug_handler.setFormatter(formatter)
logger.addHandler(file_debug_handler)

# ERROR 레벨 이상의 로그를 `error.log`에 출력하는 Handler
file_error_handler = logging.FileHandler('error.log')
file_error_handler.setLevel(logging.ERROR)
file_error_handler.setFormatter(formatter)
logger.addHandler(file_error_handler)

# 100MB 파일을 10개까지 남기겠다라는 의미입니다.
fileMaxByte = 1024 * 1024 * 100
fileHandler = logging.handlers.RotatingFileHandler(filename, maxBytes=fileMaxByte, backupCount=10)
logger.addHandler(fileHandler)

# 매 분마다 로그 파일이 나누어지며 최대 5개의 백업파일을 생성할 것입니다.
# 만약 한 시간 마다 rotating하고 싶다면 interval 을 60으로 설정하거나, when=”h” 와 같이 설정하면 됩니다.
timeRotatingFileHandler = TimedRotatingFileHandler(path, when="m", interval=1, backupCount=5)
logger.addHandler(timeRotatingFileHandler)

# config = json.load(open('./logger.json'))
# logging.config.dictConfig(config)


# example1: https://googleapis.dev/python/logging/2.6.0/handlers.html
# import logging
# import google.cloud.logging
# from google.cloud.logging_v2.handlers import CloudLoggingHandler

# client = google.cloud.logging.Client()
# handler = CloudLoggingHandler(client)

# cloud_logger = logging.getLogger('cloudLogger')
# cloud_logger.setLevel(logging.INFO)
# cloud_logger.addHandler(handler)

# cloud_logger.error('bad news')  # API call

# example2: https://googleapis.dev/python/logging/2.6.0/handlers.html
# import logging
# import google.cloud.logging
# from google.cloud.logging_v2.handlers import CloudLoggingHandler

# client = google.cloud.logging.Client()
# handler = CloudLoggingHandler(client)
# google.cloud.logging.handlers.setup_logging(handler)
# logging.getLogger().setLevel(logging.DEBUG)

# logging.error('bad news')  # API call
