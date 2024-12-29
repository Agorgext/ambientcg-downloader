DEBUG = 0
MAX_OUTPUT_FOLDERS = 20     # Number of maximum output folders that can be created

######### Predefined constant arrays ###########################################################
IMAGE_RESOLUTIONS = [
    "1K",
    "2K",
    "4K",
    "8K",
    "12K",
    "16K",
    "HQ",  # for .sbsar (Substance Painter)
    "LQ"   # for .sbsar (Substance Painter)
]

IMAGE_EXTENSIONS = ["JPG", "PNG"]

TYPES = [
    "3DModel",
    "Atlas",
    "Brush",
    "Decal",
    "HDRI",
    "Material",
    "PlainTexture",
    "Substance",
    "Terrain"
]

METHODS = [
    "PBRApproximated",
    "PBRPhotogrammetry",
    "PBRProcedural",
    "PBRMultiAngle",
    "3DPhotogrammetry",
    "HDRIStitched",
    "HDRIStitchedEdited",
    "PlainPhoto",
    "UnknownOrOther"
]

SORTS = ["Latest", "Popular", "Alphabet", "Downloads"]

FILE_TYPES = ["zip", "sbsar"]
################################################################################################

######### Other constants ######################################################################
# Order of the response : assetId,downloadAttribute,filetype,size,downloadLink,rawLink
ASSET_ID_COL = 0
DOWNLOAD_ATTRIBUTE_COL = 1
FILETYPE_COL = 2
SIZE_COL = 3
DOWNLOAD_LINK_COL = 4
RAW_LINK_COL = 5
################################################################################################
