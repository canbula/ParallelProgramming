import time
import logging




class Timer:
    """
    Timer class that measures the time taken by the block of code it manages. 
    It is a context manager class that can be used with the 'with' statement.
    It logs the start time, end time and the elapsed time of the block of code it manages.

    
    :param start_time: The time when the timer is started
    :type start_time: float
    :param end_time: The time when the timer is ended
    :type end_time: float 
    
    """
    def __init__(self):
        """ Initializes the start_time and end_time of the Timer class """
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        """ Logs the start time of the Timer class and caller module """
        self.start_time=time.time()
        logging.info("--------------------Timer started-------------------")
        logging.info(f"Timer called by {__name__} module")
        return self
    
    def __exit__(self,execution_type = None, execution_value=None, traceback=None)-> float:
        """ Logs the end time of the Timer class and calculates the elapsed time of the block of code it manages """
        self.end_time=time.time()  

        if execution_type or execution_value or traceback:
            logging.error(Exception(f"An error occured during the exiting of the {__name__} module"))
            logging.info("--------------------Timer stopped-------------------")
            return False

        time_taken  = self.end_time-self.start_time
        logging.info(f"Elapsed time of {__name__} module is {time_taken} seconds")
        logging.info("--------------------Timer stopped-------------------")
        return time_taken
    


