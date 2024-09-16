import sys
from src.logger import logger

def error_message_detail(error: Exception, error_detail: sys) -> str:

    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    error_message = (
        f"Error occurred in script [{file_name}] "
        f"at line [{line_number}] with message [{str(error)}]"
    )

    return error_message

class CustomException(Exception):
    
    def __init__(self, error: Exception, error_detail: sys):
        error_message = error_message_detail(error, error_detail)
        super().__init__(error_message)
        self.error_message = error_message

    def __str__(self) -> str:
        return self.error_message

if __name__=="__main__":
    logger.info("Logging has started")