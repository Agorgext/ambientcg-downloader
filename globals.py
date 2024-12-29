from threading import Lock # Create a display mutex

response = ''
request = ''
output_path = None
absolute_output_path = ''
total_assets_to_download = 0
filtered_response = []
display_mutex = Lock() # Mutex used to prevent concurrent display operations and avoid overlapping outputs.