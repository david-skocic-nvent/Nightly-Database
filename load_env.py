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

# Load the .env file
load_dotenv()

# Access environment variables
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')

print(f"Connecting to database at {db_host} with user {db_user}")
