import logging
import constants
import parameters

def validate_value(value, category):
    # If the value is empty, the value is validated
    if value == '':
        return

    """Validate if the given value is in the predefined category."""
    allowed_values = {
        "image_resolution": constants.IMAGE_RESOLUTIONS,
        "image_extension": constants.IMAGE_EXTENSIONS,
        "type": constants.TYPES,
        "sort": constants.SORTS,
        "method": constants.METHODS,
        "file_type": constants.FILE_TYPES
    }

    if category not in allowed_values:
        raise ValueError(f"Invalid category: {category}. Allowed categories are: {', '.join(allowed_values.keys())}")

    if value not in allowed_values[category]:
        raise ValueError(f"Invalid {category}: {value}. Allowed {category} values are: {', '.join(allowed_values[category])}")

    return '%-20s %-20s %-20s' % (category.capitalize(), value, "valid")

def validate_values():
    print("")
    logging.info("################################################")
    logging.info(validate_value(parameters.IMAGE_RESOLUTION, "image_resolution"))
    logging.info(validate_value(parameters.IMAGE_EXTENSION, "image_extension"))
    logging.info(validate_value(parameters.METHOD, "method"))
    logging.info(validate_value(parameters.TYPE, "type"))
    logging.info(validate_value(parameters.SORT, "sort"))
    logging.info(validate_value(parameters.FILE_TYPE, "file_type"))
    logging.info("################################################")
    print("")

    # Ask the user if request parameters are what he wants
    user_input = input("Do you want to proceed with these parameters (Y/n) ? ").lower()
    if user_input in ["yes", "y", ""]:
        return 0
    else:
        print("Exiting...")
        return 1