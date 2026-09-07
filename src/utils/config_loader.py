"""Configuration Loader Module"""

import os
from pathlib import Path
from dotenv import load_dotenv
import yaml
import json


class ConfigLoader:
    """Load and manage application configuration from multiple sources"""
    
    def __init__(self, env_file='.env', config_dir='./config'):
        """
        Initialize configuration loader
        
        Args:
            env_file (str): Path to .env file
            config_dir (str): Directory containing YAML config files
        """
        self.env_file = env_file
        self.config_dir = Path(config_dir)
        self.config = {}
        
        # Load configurations in order of priority
        self._load_env_file()
        self._load_yaml_configs()
    
    def _load_env_file(self):
        """
        Load environment variables from .env file
        Priority: .env file > system environment variables
        """
        if Path(self.env_file).exists():
            load_dotenv(self.env_file)
        
        # Common configuration keys
        env_keys = [
            'APP_NAME', 'APP_LANGUAGE', 'DEBUG', 'LOG_LEVEL', 'TIMEZONE',
            'CURRENT_AFFAIRS_LANGUAGE', 'GENERATE_BILINGUAL',
            'DATABASE_URL', 'PDF_OUTPUT_DIR', 'RAW_DATA_DIR', 'PROCESSED_DATA_DIR',
            'LOG_DIR', 'CACHE_DIR', 'REQUEST_TIMEOUT', 'RETRY_ATTEMPTS',
            'RETRY_DELAY', 'USER_AGENT', 'RATE_LIMIT_DELAY', 'ENABLE_SCHEDULER',
            'SCHEDULER_TIME', 'SCHEDULER_TIMEZONE', 'ENABLE_EMAIL_NOTIFICATION',
            'SMTP_SERVER', 'SMTP_PORT', 'EMAIL_SENDER', 'EMAIL_PASSWORD',
            'EMAIL_RECIPIENTS', 'PDF_PAPER_SIZE', 'PDF_MARGIN_TOP',
            'PDF_MARGIN_BOTTOM', 'PDF_MARGIN_LEFT', 'PDF_MARGIN_RIGHT',
            'PDF_FONT_SIZE', 'PDF_LINE_HEIGHT', 'MIN_CONTENT_LENGTH',
            'MAX_CONTENT_LENGTH', 'DEDUPLICATION_THRESHOLD', 'SUMMARY_LENGTH',
            'ENABLE_PROXY', 'PROXY_URL', 'MAX_WORKERS', 'CACHE_EXPIRY_HOURS',
            'DATABASE_POOL_SIZE', 'FEATURE_NLP_ANALYSIS', 'FEATURE_TREND_DETECTION',
            'FEATURE_HISTORICAL_TRACKING', 'FEATURE_EMAIL_DELIVERY',
            'FEATURE_WEB_DASHBOARD', 'LOG_FORMAT', 'LOG_FILE'
        ]
        
        for key in env_keys:
            value = os.getenv(key)
            if value:
                self.config[key] = self._parse_value(value)
    
    def _load_yaml_configs(self):
        """
        Load YAML configuration files from config directory
        """
        if not self.config_dir.exists():
            return
        
        for yaml_file in self.config_dir.glob('*.yaml'):
            try:
                with open(yaml_file, 'r', encoding='utf-8') as f:
                    yaml_config = yaml.safe_load(f)
                    if yaml_config:
                        # Use filename (without .yaml) as section key
                        section_key = yaml_file.stem.upper()
                        self.config[section_key] = yaml_config
            except Exception as e:
                print(f"Error loading YAML config {yaml_file}: {str(e)}")
    
    def _parse_value(self, value):
        """
        Parse environment variable values to appropriate Python types
        
        Args:
            value (str): Environment variable value
        
        Returns:
            Parsed value (bool, int, list, str)
        """
        # Boolean values
        if value.lower() in ('true', 'yes', '1'):
            return True
        if value.lower() in ('false', 'no', '0'):
            return False
        
        # Integer values
        if value.isdigit():
            return int(value)
        
        # List values (comma-separated)
        if ',' in value:
            return [item.strip() for item in value.split(',')]
        
        # String values
        return value
    
    def get(self, key, default=None):
        """
        Get configuration value
        
        Args:
            key (str): Configuration key (supports dot notation for nested keys)
            default: Default value if key not found
        
        Returns:
            Configuration value or default
        """
        if '.' in key:
            # Support nested key access (e.g., 'SOURCES.COACHING_INSTITUTES')
            keys = key.split('.')
            value = self.config
            for k in keys:
                if isinstance(value, dict):
                    value = value.get(k.upper())
                else:
                    return default
            return value if value is not None else default
        else:
            return self.config.get(key.upper(), default)
    
    def get_all(self):
        """
        Get all configuration values
        
        Returns:
            dict: Complete configuration dictionary
        """
        return self.config.copy()
    
    def set(self, key, value):
        """
        Set configuration value at runtime
        
        Args:
            key (str): Configuration key
            value: Configuration value
        """
        self.config[key.upper()] = value
    
    def update(self, config_dict):
        """
        Update multiple configuration values
        
        Args:
            config_dict (dict): Dictionary of configuration key-value pairs
        """
        for key, value in config_dict.items():
            self.set(key, value)
    
    def save_to_env(self, output_file='.env'):
        """
        Save current configuration to .env file
        
        Args:
            output_file (str): Path to output .env file
        """
        with open(output_file, 'w', encoding='utf-8') as f:
            for key, value in sorted(self.config.items()):
                if not isinstance(value, dict):
                    f.write(f"{key}={value}\n")
    
    def validate_required_keys(self, required_keys):
        """
        Validate that required configuration keys are present
        
        Args:
            required_keys (list): List of required configuration keys
        
        Returns:
            tuple: (is_valid, missing_keys)
        """
        missing_keys = []
        for key in required_keys:
            if not self.get(key):
                missing_keys.append(key)
        
        return len(missing_keys) == 0, missing_keys
    
    def get_database_url(self):
        """
        Get database URL from configuration
        
        Returns:
            str: Database URL
        """
        return self.get('DATABASE_URL', 'sqlite:///./sutra.db')
    
    def get_api_key(self, service_name):
        """
        Get API key for a specific service
        
        Args:
            service_name (str): Service name (e.g., 'GOOGLE', 'NEWS_API')
        
        Returns:
            str: API key for the service
        """
        key = f"{service_name}_API_KEY"
        return self.get(key)
    
    def get_base_url(self, service_name):
        """
        Get base URL for a specific service
        
        Args:
            service_name (str): Service name
        
        Returns:
            str: Base URL for the service
        """
        key = f"{service_name}_BASE_URL"
        return self.get(key)
    
    def __repr__(self):
        """String representation"""
        return f"ConfigLoader(app={self.get('APP_NAME')}, language={self.get('APP_LANGUAGE')})"
