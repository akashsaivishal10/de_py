# # 8. Custom exceptions (Advanced)
# You can create your own exception classes.
import logging

class InvalidAgeErrorException(Exception) :
    pass

try :
    age=15
    if age<18:
        raise InvalidAgeErrorException("Age must be 18 or above")
    print("eligible")
except InvalidAgeErrorException as e:
    print(e)
    
logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")

try :
    result =10/0
except ZeroDivisionError :
    logging.exception("caluclation failed")
    
#Method	                 Purpose
# logging.debug()	     Detailed debugging
# logging.info()	     Normal execution information
# logging.warning()	     Something unexpected
# logging.error()	     An operation failed
# logging.exception()	 Error with traceback inside an exception handler