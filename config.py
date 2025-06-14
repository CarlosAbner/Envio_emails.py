# config.py
import logging


try:
    from variaveis_ambiente import *
except Exception as e:
    logging.error(f"Erro ao encontrar a variavel: {str(e)}")
