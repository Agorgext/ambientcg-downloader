import logging
import os.path                                  # Create a folder
import zipfile                                  # Unzip assets
import mimetypes                                # Extract file extension from the HTTP Content-Type header 
from urllib.request import Request, urlopen     # Download the asset from an url

import globals
import constants
import parameters

"""
return_mode (int): Mode for the return value:
    0 - Return a boolean indicating success or failure.
    1 - Return the created folder's path or None if already exists.
"""
def create_new_folder(directory, folder_name, return_mode, display_info):
    # Create the folder's path
    newpath = os.path.join(directory, folder_name)

    # Check if the path doesn't already exist
    if not os.path.exists(newpath):
        try:
            # Create folder
            os.makedirs(newpath)
            logging.info(f"New folder created: {newpath}")
            
            # Return based on return_mode
            return newpath if return_mode == 1 else True
        except OSError as e:
            logging.error(f"Failed to create folder: {e}")
            return None if return_mode == 1 else False

    # If the folder already exists
    if display_info:
        logging.info(f"Folder already exists: {newpath}")

    return None if return_mode == 1 else False


def create_new_output_folder():
    folder_id = 0

    # Increment folder_id until a folder with this Id can be created
    for folder_id in range(0, constants.MAX_OUTPUT_FOLDERS):
        new_path = create_new_folder(parameters.OUTPUT_PATH, f"output{folder_id}", 1, False)

        if new_path != None:
            globals.output_path = new_path
            globals.absolute_output_path = os.path.abspath(globals.output_path)
            return True
    
    logging.error("Max output folder reached")
    return False

def save_asset_locally(file_data, file_extension, asset_id, save_directory):
    # Ensure the save directory exists
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # Define the file name and full path
    file_name = f"{asset_id}.{file_extension}"
    file_path = os.path.join(save_directory, file_name)

    # Write the binary data to the file
    with open(file_path, "wb") as file:
        file.write(file_data)
    
     # If the file is a zip
    if file_extension == "zip":

        # Unzip the file ?
        if parameters.UNZIP_ASSET_FILES:
            # Unzip the file
            zip_file_path = os.path.join(save_directory, f"{asset_id}")
            with zipfile.ZipFile(file_path,"r") as zip_ref:
                zip_ref.extractall(zip_file_path)
                logging.debug(f"File unzipped : {zip_file_path}")
            
            # Keep the zip files ?
            if not parameters.KEEP_ZIP_FILES:
                # Delete the zip file
                os.remove(file_path)
                
                logging.debug(f"File deleted : {file_path}")

    return file_path
    

def download_assets():
    asset_download_num = 1

    # Get the total number of assets to download
    globals.total_assets_to_download = len(globals.filtered_response)

    # Ask the user if he wants the download to proceed
    print(f"\n{globals.total_assets_to_download} assets are going to be downloaded and placed inside {os.path.abspath(parameters.OUTPUT_PATH)}")
    user_input = input("Do you want to proceed (Y/n) ? ").lower()
    if user_input in ["yes", "y", ""]:
        # Create an output folder to store the downloaded assets
        if create_new_output_folder():
            print("Download starting...")
        else:
            return 1
    else:
        print("Exiting...")
        return 1
    
    for line in globals.filtered_response:
        # Get the name of the asset and the downloadLink URL
        segmented_line = line.split(",")
        asset_id = segmented_line[constants.ASSET_ID_COL]
        download_link = segmented_line[constants.DOWNLOAD_LINK_COL]

        # Create the request
        req = Request(
            url=download_link, 
            headers={'User-Agent': 'Mozilla/6.0'}, # This mimics a regular browser user-agent to avoid 403 errors
        )

        # Download the asset
        response = urlopen(req)
        file_data = response.read()

        # Get the file extension from the Content-Type header
        content_type = response.headers.get('Content-Type', '')
        file_extension = mimetypes.guess_extension(content_type)[1:] or ''
        
        # Save the file locally
        saved_path = save_asset_locally(file_data, file_extension, asset_id, globals.output_path)
        print(f"{asset_download_num}/{globals.total_assets_to_download} Asset downloaded: {saved_path}")

        # Increment the number of downloaded assets
        asset_download_num += 1
    
    print(f"Download successfully finished. {globals.total_assets_to_download} assets were saved to {globals.absolute_output_path}.")
