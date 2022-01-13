import logging
import logging.config
import json

config = json.load(open('./logger.json'))
logging.config.dictConfig(config)

logger = logging.getLogger(__name__)
