# LIBRARIES
from django.core.exceptions import ValidationError

def validate_file_size(value):
    """A function which validates file sizes."""

    # Creating a variable called file_size from the input's size.
    file_size = value.size

    # Checking if the file size is over 30MB.
    if file_size > 30485760:
        # Raising validation error if the maximum file size is over 30MB
        raise ValidationError("The maximum file size that can be uploaded is 30MB")
    # Checking if the file is less than 30MB.
    else:
        # Returning the input.
        return value
