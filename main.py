import globals
import constants
import network
import validation
import file_management

import logging # Display info, debug and error logs

# Debug mode
if constants.DEBUG:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

def main():
    # Check correctness of the request parameters
    try:
        if validation.validate_values():
            return 1
    except ValueError as e:
        logging.error(e)
        return 1
    
    # Proceed with completing the request
    network.create_request()
    network.send_request()
    globals.filtered_response = network.filter_response()

    # Check if the filtered response is empty
    if not globals.filtered_response:
        logging.info("Filtered response is empty. Ending.")
        return 1

    # Download and save the assets
    if file_management.download_assets():
        return 1

if __name__ == "__main__":
    main()

