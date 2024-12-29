import os.path

######### Global parameters ###################################################################
# API URL
BASE_REQUEST_URL = 'https://ambientCG.com/api/v2/downloads_csv'

# Editable parameters
UNZIP_ASSET_FILES = True    # Unzip the assets after download ?
KEEP_ZIP_FILES = False      # Keep zip files after download or delete them ?

DEFAULT_OUTPUT_FILENAME = "output"
OUTPUT_PATH = os.path.join(os.path.curdir, f"{DEFAULT_OUTPUT_FILENAME}")

################################################################################################

######### Your request parameters ##############################################################
# NOTE: Leave the parameter empty to exclude it from the request.

# Main
IMAGE_RESOLUTION = '2K'     # Resolution of downloaded images
IMAGE_EXTENSION = 'JPG'     # Extension type of downloaded images
TYPE = 'Material'

# Secondary
ASSET_ID = ''               # Select a specific asset by their id. Ex: "Bricks097"
SORT = 'Alphabet'           # Defines the order of the results
METHOD = ''                 # Method used by the creator of the asset to make the asset
SEARCH_QUERY = 'glass facade'           # A list of keywords, separated by commas or spaces.

# Others
FILE_TYPE = 'zip'           # Type of the downloaded package : .zip, .sbsar (Subtance Painter)
MAX_FILE_SIZE = ''          # Not used
################################################################################################

# Parameters added to the string request
IMAGE_DOWNLOAD_ATTRIBUTE = IMAGE_RESOLUTION + '-' + IMAGE_EXTENSION
REQUEST_PARAMETERS = [
    ASSET_ID,
    IMAGE_DOWNLOAD_ATTRIBUTE
]