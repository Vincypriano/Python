from functools import wraps
import logging

log_format = '%(asctime)s:%(levelname)s:\n%(filename)s:%(lineno)d:%(message)s'

logging.basicConfig(filename='PRINCIPAL\DuduMendes\Live48#exemplo2.log',
                    filemode='w',
                    level=logging.DEBUG,
                    format=log_format
                    )

logger = logging.getLogger('root')

def log(func):
    @wraps(func)
    def inner(*args,**kwargs):
        result = func(*args, **kwargs)
        l_sms = f'\nfunc:{func.__name__}:\nargs:{args}:\nkwargs:{kwargs}:\nresult:{result}'
        logger.debug(l_sms)
        return result
    return inner

@log
def add(x,y):
    return x + y


add(7,7)