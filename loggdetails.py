import logging


def logzfile():
    return 'data.log'


def logg(filepath,code="",mess="",desc=""):

    scode=str(code)
    smess=str(mess)

    logger = logging.getLogger(__name__)#instantiating a logger
    logger.setLevel(logging.INFO)



    # create a file handler

    handler = logging.FileHandler(filepath)
    handler.setLevel(logging.INFO)

# create a logging format

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

# add the handlers to the logger

    logger.addHandler(handler)

    logger.info("\t*****{}*****\n{}=>{}\n".format(desc,scode,smess))

    #The handler is added each time you call from outside,hence it has to be removed after the job is finished your job:
    logger.handlers.pop()




def deleteContent(pfile):
    #note pfile is a fileobject
    pfile.seek(0)#Go to beginning of contents of file
    pfile.truncate() #delete contents