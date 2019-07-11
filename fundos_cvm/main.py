# from fundos_cvm.cvm_scrapper import cvm_scrapper
from os.path import join
from os.path import dirname
from urllib.parse import urljoin
import datetime


import cvm_scrapper

# CVM webpage
CVM_URL = "http://dados.cvm.gov.br"

# Database to crawl
FI_DIR = "/dados/FI/"
FI_CAD_SUFIX = "/dados/FI/CAD/DADOS/"
FI_BAL_SUFIX = '/dados/FI/DOC/BALANCETE/DADOS/'
FI_CDA_SUFIX = '/dados/FI/DOC/CDA/DADOS/'
FI_CDA_HIST_SUFIX = '/dados/FI/DOC/CDA/DADOS/HIST/'
FI_EVN_SUFIX = '/dados/FI/DOC/EVENTUAL/DADOS/'
FI_EXT_SUFIX = '/dados/FI/DOC/EXTRATO/DADOS/'
FI_DIA_SUFIX = '/dados/FI/DOC/INF_DIARIO/DADOS/'
FI_DIA_HIST_SUFIX = '/dados/FI/DOC/INF_DIARIO/DADOS/HIST/'

# Full url paths to crawl.
FI_URL = urljoin(CVM_URL, FI_DIR)
FI_CAD_URL = urljoin(CVM_URL, FI_CAD_SUFIX)
FI_BAL_URL = urljoin(CVM_URL, FI_BAL_SUFIX)
FI_CDA_URL = urljoin(CVM_URL, FI_CDA_SUFIX)
FI_CDA_HIST_URL = urljoin(CVM_URL, FI_CDA_HIST_SUFIX)
FI_EVN_URL = urljoin(CVM_URL, FI_EVN_SUFIX)
FI_EXT_URL = urljoin(CVM_URL, FI_EXT_SUFIX)
FI_DIA_URL = urljoin(CVM_URL, FI_DIA_SUFIX)
FI_DIA_HIST_URL = urljoin(CVM_URL, FI_DIA_HIST_SUFIX)


# Directory to store raw data.
RAW_DATA_DIR = join(dirname("__file__"), 'fundos_cvm', 'database', 'raw')

# Create directories for each page.
FI_CAD_DIR = join(RAW_DATA_DIR, 'FI', 'CAD')
FI_BAL_DIR = join(RAW_DATA_DIR, 'FI', 'BALANCETE')
FI_CDA_DIR = join(RAW_DATA_DIR, 'FI', 'CDA')
FI_CDA_HIST_DIR = join(RAW_DATA_DIR, 'FI', 'CDA', 'HIST')
FI_EVN_DIR = join(RAW_DATA_DIR, 'FI', 'EVENTUAL')
FI_EXT_DIR = join(RAW_DATA_DIR, 'FI', 'FI_EXTRATO')
FI_DIA_DIR = join(RAW_DATA_DIR, 'FI', 'FI_DIARIO')
FI_DIA_HIST_DIR = join(RAW_DATA_DIR, 'FI', 'FI_DIARIO', 'HIST')


URL_DIR_MAP = {
    FI_CAD_URL: FI_CAD_DIR,
    FI_BAL_URL: FI_BAL_DIR,
    FI_CDA_URL: FI_CDA_DIR,
    FI_CDA_HIST_URL: FI_CDA_HIST_DIR,
    FI_EVN_URL: FI_EVN_DIR,
    FI_EXT_URL: FI_EXT_DIR,
    FI_DIA_URL: FI_DIA_DIR,
    FI_DIA_HIST_URL: FI_DIA_HIST_DIR,
    }

F_TYPES = ['.csv', '.txt', '.zip']


def update_raw_files():
    dt = datetime.date.today()
    for url, dir_name in URL_DIR_MAP.items():
        for ftype in F_TYPES:
            print(url)
            print(dir_name)
            cvm_scrapper.rename_outofdate_files(url, dir_name, ftype, dt)
            cvm_scrapper.populate_dir(url, dir_name, ftype)


update_raw_files()
