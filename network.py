import logging
import requests                                 # Retrieve the response
from urllib.parse import urlencode              # Parse the response

import globals
import constants
import parameters

def create_request():
    # Start with the base URL
    globals.request = parameters.BASE_REQUEST_URL

    # Define query parameters as a dictionary
    query_params = {}

    if parameters.SEARCH_QUERY != '':
        query_params['q'] = parameters.SEARCH_QUERY
    if parameters.ASSET_ID != '':
        query_params['id'] = parameters.ASSET_ID
    if parameters.SORT != '':
        query_params['sort'] = parameters.SORT
    if parameters.METHOD != '':
        query_params['method'] = parameters.METHOD
    if parameters.TYPE != '':
        query_params['type'] = parameters.TYPE

    # Append query parameters to the base URL
    if query_params:
        globals.request += "?" + urlencode(query_params)

def send_request():
    print("")
    logging.info(f"Sent request : {globals.request}")

    # Make the GET request and store the response
    globals.response = requests.get(globals.request)

    # Raise an exception if the request failed
    globals.response.raise_for_status()  # This ensures HTTP errors are catched early

def filter_response():
    # Exclude the header line
    globals.filtered_response = globals.response.text.split("\n")[1:]

    # Exclude the footer newline caracter line
    globals.filtered_response = globals.filtered_response[:len(globals.filtered_response)-1]

    if constants.DEBUG:
        globals.display_mutex.acquire()

        globals.filtered_response = globals.filtered_response[:5] # Study only the first lines of the response
        print("")
        logging.debug("Raw response :")
        for line in globals.filtered_response:
            logging.debug(f" [Unfiltered] {line}")
        print("")

        globals.display_mutex.release()
    
    # Temporary list to store valid lines
    valid_lines = []

    lineNum = 0

    globals.display_mutex.acquire()

    # Filter lines with passed parameters
    for line in globals.filtered_response:
        # Initialise variables
        colNum = 0
        is_line_valid = True
        
        segmentedLine = line.split(",")

        # Loops through the column parameters to filter the lines
        for parameter in parameters.REQUEST_PARAMETERS:
            # If parameter is set
            if parameter != "":
                # Extract the parameter from the line
                lineParameter = segmentedLine[colNum]

                # If the parameter is 'downloadAttribute', separate the image resolution and type
                if colNum == constants.DOWNLOAD_ATTRIBUTE_COL:
                    # If our image resolution and type parameter is specified
                    if parameters.IMAGE_RESOLUTION != "" or parameters.IMAGE_EXTENSION != "":
                        # Get the line's download attribute 
                        line_download_attribute = lineParameter.split("-")

                        # Check if the split has both resolution and extension
                        if len(line_download_attribute) < 2:
                            is_line_valid = False
                            break
                        
                        else:
                            line_image_resolution = line_download_attribute[0]
                            line_image_extension = line_download_attribute[1]

                            # If our image resolution parameter is set
                            # and the line's image resolution is validated
                            if parameters.IMAGE_RESOLUTION != "" and (parameters.IMAGE_RESOLUTION != line_image_resolution):
                                is_line_valid = False
                                break   
                            
                            # If our image type parameter is set
                            # and the line's image type is validated
                            if parameters.IMAGE_EXTENSION != "" and (parameters.IMAGE_EXTENSION != line_image_extension):
                                is_line_valid = False
                                break
                        
                # Check if the line's parameter correspond to our parameter
                elif parameter != lineParameter:
                    is_line_valid = False

            colNum += 1
        
        # Keep the line if it corresponds to our parameters
        if is_line_valid == True:
            valid_lines.append(line)
            logging.info(f" [Asset kept] {line}")
        
    lineNum += 1

    globals.display_mutex.release()
    return valid_lines