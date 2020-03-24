import pandas as pd


import os
from os.path import dirname
from os.path import join


CVM_URL = "http://dados.cvm.gov.br"
FI_CAD_SUFIX = "/dados/FI/CAD/DADOS/"
FI_DIA_SUFIX = '/dados/FI/DOC/INF_DIARIO/DADOS/'
FI_DOC_EXTRATO_SUFIX = '/dados/FI/DOC/EXTRATO/DADOS/'

RAW_DATA_DIR = join(dirname("__file__"), 'fundos_cvm', 'database', 'raw_files')

FI_CAD_DIR = join(RAW_DATA_DIR, 'FI', 'FI_CAD')
FI_DIA_DIR = join(RAW_DATA_DIR, 'FI', 'FI_DIARIO')
FI_EXTRATO_DIR = join(RAW_DATA_DIR, 'FI', 'FI_EXTRATO')

dir_files = os.listdir(FI_EXTRATO_DIR)

info = pd.read_csv(
    join(FI_EXTRATO_DIR, dir_files[-1]),
    sep=';',
    engine='python'
    )

info[['TAXA_PERFM',
      'PARAM_TAXA_PERFM',
      'PR_INDICE_REFER_TAXA_PERFM',
      'VL_CUPOM',
      'INF_TAXA_PERFM']][info["CNPJ_FUNDO"] == "18.471.807/0001-78"]
