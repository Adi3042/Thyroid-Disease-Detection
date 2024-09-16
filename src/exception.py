import sys
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(message)s",
)

def error_message_detail(error: Exception, error_detail: sys) -> str:
    """
    Generates a detailed error message including file name, line number, and error message.

    :param error: The caught exception.
    :param error_detail: sys module to extract traceback details.
    :return: A formatted string with error details.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    error_message = (
        f"Error occurred in script [{file_name}] "
        f"at line [{line_number}] with message [{str(error)}]"
    )

    return error_message

class CustomException(Exception):
    """
    Custom exception class that provides detailed error information.
    """
    def __init__(self, error: Exception, error_detail: sys):
        error_message = error_message_detail(error, error_detail)
        super().__init__(error_message)
        self.error_message = error_message

    def __str__(self) -> str:
        return self.error_message

if __name__=="__main__":
    logging.info("Logging has started")