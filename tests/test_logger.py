import logging, datetime
import logging.handlers
from time import sleep
from custom_logger import CustomLog as CL

log = CL("custom_log")
log.stream_handler("INFO")
log = log.timeRotate_handler(filename="./time_log.txt",
                       when="M",
                       interval=2 ,
                       backupCount= 3 ,
                       level = "DEBUG"
                      )

## run
idx = 0
while True :
    log.debug('debug {}'.format(idx))
    log.info('info {}'.format(idx))
    log.warning('warning {}'.format(idx))
    log.error('error {}'.format(idx))
    log.critical('critical {}'.format(idx))
    idx += 1
    sleep(0.5)
    if idx ==1000 :
        break
