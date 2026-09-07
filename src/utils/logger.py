"""Logger Configuration Module"""

import logging
import logging.handlers
from pathlib import Path
import sys


def setup_logger(name, log_level='INFO', log_dir='./logs'):
    """
    Setup logger with file and console handlers
    
    Args:
        name (str): Logger name
        log_level (str): Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_dir (str): Directory for log files
    
    Returns:
        logging.Logger: Configured logger instance
    """
    
    # Create logs directory if not exists
    log_path = Path(log_dir)
    log_path.mkdir(parents=True, exist_ok=True)
    
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, log_level.upper()))
    
    # Prevent duplicate handlers
    if logger.hasHandlers():
        return logger
    
    # Log format
    log_format = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(getattr(logging, log_level.upper()))
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)
    
    # File handler with rotation
    log_file = log_path / f'{name}.log'
    file_handler = logging.handlers.RotatingFileHandler(
        log_file,
        maxBytes=10485760,  # 10MB
        backupCount=5
    )
    file_handler.setLevel(getattr(logging, log_level.upper()))
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)
    
    return logger
