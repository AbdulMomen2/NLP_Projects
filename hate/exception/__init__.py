import os
import sys

def error_message_detail(error, error_detail: sys):
    # Extract traceback information
    _, _, exc_tb = error_detail.exc_info()
    
    # Get file name where the error occurred
    file_name = os.path.basename(exc_tb.tb_frame.f_code.co_filename)
    
    # Format the error message
    error_message = "Error occurred in script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        """
        :param error_message: Error message in string format
        :param error_detail: sys module to extract traceback details
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
