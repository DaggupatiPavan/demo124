import argparse
import logging
import requests
import sys

# Set up argument parsing
def parse_args():
    parser = argparse.ArgumentParser(description="GitHub Action Logging Pre-op")

    # Define command-line arguments
    parser.add_argument('--version', type=str, default='v1.0.0', help='Version of the Action (default: v1.0.0)')
    parser.add_argument('--log_level', type=str, default='INFO', choices=['INFO', 'ERROR', 'DEBUG'], help='Logging Level (default: INFO)')
    parser.add_argument('--api_url', type=str, default='http://example.com/api/logs', help='API URL for live logging (default: http://example.com/api/logs)')
    
    # Parse the arguments
    return parser.parse_args()

# Set up logging based on the provided log level
def setup_logging(log_level):
    log_levels = {
        'INFO': logging.INFO,
        'ERROR': logging.ERROR,
        'DEBUG': logging.DEBUG
    }
    
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=log_levels.get(log_level.upper(), logging.INFO)
    )
    return logging.getLogger()

# Function to capture stdout and stderr
def capture_output():
    stdout = sys.stdout
    stderr = sys.stderr
    sys.stdout = open("stdout.log", "w")
    sys.stderr = open("stderr.log", "w")
    return stdout, stderr

# Function to publish logs to the REST API
def publish_log(message, api_url):
    try:
        response = requests.post(api_url, json={'message': message})
        if response.status_code == 200:
            logger.info(f"Log successfully sent to {api_url}")
        else:
            logger.error(f"Failed to send log to {api_url} with status code {response.status_code}")
    except Exception as e:
        logger.error(f"Error sending log to API: {str(e)}")

# Main execution
if __name__ == "__main__":
    # Parse command-line arguments
    args = parse_args()

    # Set up logging
    logger = setup_logging(args.log_level)

    # Capture stdout and stderr
    stdout, stderr = capture_output()

    # Log version and input parameters
    logger.info(f"Action Version: {args.version}")
    logger.info(f"Input Parameters: Version={args.version}, Log Level={args.log_level}, API URL={args.api_url}")

    # Send logs to the REST API
    publish_log(f"Action started with version: {args.version} and log level: {args.log_level}", args.api_url)

    # Simulate the script processing
    try:
        logger.info("Action processing started...")
        # Simulate some log messages
        logger.debug("This is a debug message.")
        logger.info("This is an info message.")
        # Simulate an error
        raise ValueError("Simulated Error for logging purposes")
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        publish_log(f"Error encountered: {str(e)}", args.api_url)
    finally:
        sys.stdout = stdout
        sys.stderr = stderr

        # Publish final log
        logger.info("Action completed.")
        publish_log("Action completed.", args.api_url)
