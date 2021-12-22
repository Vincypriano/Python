# Criando Logs de aplicações
'''Level |                  Quando usar isso
---------------------------------------------------------------------------------
   Debug | informações mais detalhadas, quando estamos buscando problemas
   Info  | Confirmar que as coisas estão funcionando como esperado
  Warning| informação de que algo inesperado aconteceu(mas tudo funcionabem)
    Error| Quando algo inesperado ocorre e o programa não consegue executar algo
 Critical| Um erro grave que impediu o sistema de executar algo'''
import logging

log_format = '%(asctime)s:%(levelname)s:%(filename)s:%(lineno)d:%(message)s'
logging.basicConfig(filename='exemplo.log',
                    filemode='w', # 'a' de append (logs são escritos em sequencia no arquivo) 'w' write (subscreve o arquivo de log)
                    level=logging.DEBUG, #
                    format=log_format)

logging.debug("DEBUG")
logging.info("INFO") 
logging.warning("WARNING") 
logging.error("ERROR")
logging.critical("CRITICAL")
'''
    Atributo |           formato           |            Descrição
    ----------------------------------------------------------------------------
    asctime  |          %(asctime)s        | Mostra a hora do log (d/m/a-h:m:s)
    filename |          %(filename)s       | O arquivo em que a chamada foi feita
    levelname|          %(levelname)s      | Nivel do log
    message  |          %(message)s        | Mensagem logada'''

# Personalização do Log
log_format = '%(asctime)s:%(levelname)s:%(filename)s:%(lineno)d:%(message)s'

logging.basicConfig(filename='exemplo_3.log',
                    filemode='w',
                    level=logging.DEBUG,
                    format=log_format)

logger = logging.getLogger('root')

def add(x:int,y:int) -> int:
    """Função que efetua a soma de dois números inteiros."""
    if isinstance(x, int) and isinstance (y, int):
        logger.info(f'x: {x} - y: {y}')
        return x + y
    else:
        logger.warning(
            f'x: {x} type: {type(x)}- y: {y} type: {type(y)}'
        )
print(add(7, 7))
print(add(7, 7.5))