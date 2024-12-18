import os

def load_dotenv(dotenv_path=".env"):
    """Load environment variables from a .env file."""
    with open(dotenv_path) as f:
        for line in f:
            # Remove leading/trailing whitespace and ignore empty lines or comments
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            # Split the line into key-value pairs at the first '='
            key, value = line.split('=', 1)
            
            # Strip any extra whitespace
            key = key.strip()
            value = value.strip()
            
            # Set the environment variable
            os.environ[key] = value