"""
Logger module for agent logging functionality.
"""

import logging
import sys
from datetime import datetime


class Logger:
    """
    Custom logger for the agent system.
    """
    
    def __init__(self, name="Agent", level=logging.INFO):
        """
        Initialize the logger.
        
        Args:
            name: Name of the logger
            level: Logging level (default: INFO)
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        # Create console handler
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(level)
        
        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        
        # Add handler to logger
        if not self.logger.handlers:
            self.logger.addHandler(handler)
    
    def info(self, message):
        """
        Log an info message.
        
        Args:
            message: Message to log
        """
        self.logger.info(message)
    
    def error(self, message):
        """
        Log an error message.
        
        Args:
            message: Message to log
        """
        self.logger.error(message)
    
    def warning(self, message):
        """
        Log a warning message.
        
        Args:
            message: Message to log
        """
        self.logger.warning(message)
    
    def debug(self, message):
        """
        Log a debug message.
        
        Args:
            message: Message to log
        """
        self.logger.debug(message)
