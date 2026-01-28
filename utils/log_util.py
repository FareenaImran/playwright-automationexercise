import logging
import os.path
import time
from charset_normalizer.md import getLogger


class Logger:
    def __init__(self,logger,file_level=logging.INFO):
        self.logger=getLogger(logger)
        self.logger.setLevel(logging.INFO)


        fmt=logging.Formatter('%(asctime)s %(filename)s - %(levelname)s - [ Line# %(lineno)s : %(message)s]',datefmt='%d/%m/%Y %H:%M:%S')
        curr_time=time.strftime("%d-%m-%Y")

        BASE_DIR=os.path.dirname(os.path.abspath(__file__))
        LOG_PATH=os.path.join(BASE_DIR,"..","logs","log")
        self.log_file_name=LOG_PATH +"_"+ curr_time + ".txt"

        #File handle
        fh=logging.FileHandler(self.log_file_name,mode="a")
        fh.setFormatter(fmt)
        fh.setLevel(file_level)
        self.logger.addHandler(fh)

        #Console handler
        ch=logging.StreamHandler()
        ch.setFormatter(logging.Formatter("\n[%(levelname)s]: %(message)s"))
        self.logger.addHandler(ch)
