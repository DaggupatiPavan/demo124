import sys
import logging
import requests
import os

# Get environment variables and inputs
version = sys.argv[1]  # Action Version
log_level = sys.argv[2]  # Logging Level (Info, Error, Debug)
api_url = sys.argv[3]  # API URL to send logs

# Configure the logging module
log_levels = {
    'INFO': logging.INFO,
    'ERROR': logging.ERROR,
    'DEBUG': logging.DEBUG
}

# Set default log level
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=log_levels.get(log_level.upper(), logging.INFO)
)
logger = logging.getLogger()

# Function to capture stdout and stderr
def capture_output():
    stdout = sys.stdout
    stderr = sys.stderr
    sys.stdout = open("stdout.log", "w")
    sys.stderr = open("stderr.log", "w")
    return stdout, stderr

def publish_log(message, api_url):
    try:
        response = requests.post(api_url, json={'message': message})
        if response.status_code == 200:
            logger.info(f"Log successfully sent to {api_url}")
        else:
            logger.error(f"Failed to send log to {api_url} with status code {response.status_code}")
    except Exception as e:
        logger.error(f"Error sending log to API: {str(e)}")

# Capture stdout and stderr
stdout, stderr = capture_output()

# Log version and input parameters
logger.info(f"Action Version: {version}")
logger.info(f"Input Parameters: Version={version}, Log Level={log_level}, API URL={api_url}")

# Send logs to the REST API
publish_log(f"Action started with version: {version} and log level: {log_level}", api_url)

# Simulate the script processing (For example, you can replace this with your actual processing)
try:
    logger.info("Action processing started...")
    # Simulate work being done
    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    # Simulate an error
    raise ValueError("Simulated Error for logging purposes")
except Exception as e:
    logger.error(f"Error: {str(e)}")
    publish_log(f"Error encountered: {str(e)}", api_url)
finally:
    sys.stdout = stdout
    sys.stderr = stderr

    # Publish final log
    logger.info("Action completed.")
    publish_log("Action completed.", api_url)
