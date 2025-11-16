import sys


class CustomException(Exception):
    """Base class for pipeline exceptions."""
    
    def __init__(self, error_message,error_details:sys):
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()

        self.line_no = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        

        format = (
            f"\n--- CustomException Trace ---\n"
            f"File       : {self.file_name}\n"
            f"Line       : {self.line_no}\n"
            f"Error      : {self.error_message}\n"
            f"------------------------------\n"
        )
        return format


