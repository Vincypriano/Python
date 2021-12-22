import logging
import logging.config

logging.config.fileConfig('PRINCIPAL\DuduMendes\simple_loggin.ini')

logger = logging.getLogger('Vinicius')

logger.info('Teste Append')
