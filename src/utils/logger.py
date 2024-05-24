import logging
from config import config
from colorama import Fore, Style
import os, json

FORMAT = '[%(asctime).19s] [%(filename)s -> %(funcName)s():%(lineno)s] %(levelname)s - %(message)s'

class CustomFormatter(logging.Formatter):
    format = FORMAT
    FORMATS = {
        logging.DEBUG: Fore.WHITE + format + Fore.RESET,
        logging.INFO: Fore.WHITE + format + Fore.RESET,
        logging.WARNING: Fore.YELLOW + format + Fore.RESET,
        logging.ERROR: Fore.RED + format + Fore.RESET,
        logging.CRITICAL: Fore.RED + Style.BRIGHT + format + Fore.RESET
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

def setMyLevel():
    if config['LOGGING']['level'] == 'DEBUG':
        return logging.DEBUG
    if config['LOGGING']['level'] == 'INFO':
        return logging.INFO
    if config['LOGGING']['level'] == 'WARNING':
        return logging.WARNING
    if config['LOGGING']['level'] == 'CRITICAL':
        return logging.CRITICAL

def getMyLogger():
    logger = logging.getLogger('Contextual')
    level = setMyLevel()
    logger.setLevel(level)

    if not logger.handlers:
        ch = logging.StreamHandler()
        level = setMyLevel()
        ch.setLevel(level)
        ch.setFormatter(CustomFormatter())
        
        logger.addHandler(ch)

    if json.loads(config['LOGGING']['tofile']):
        fh = logging.FileHandler(config['LOGGING']['logfilename'])
        level = setMyLevel()
        fh.setLevel(level)
        fh.setFormatter(CustomFormatter())
        
        logger.addHandler(fh)
    
    logger.propagate = False
    
    return logger


logger = getMyLogger() 