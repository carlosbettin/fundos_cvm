from bs4 import BeautifulSoup
import datetime
# import logging
import requests
import urllib
import wget

import os
from os.path import join


# CVM webpage
CVM_URL = "http://dados.cvm.gov.br"

# Ignore links with the following components.
IGNORE_LIST = [
    CVM_URL,
    "/",
    "?C=N;O=D",
    "?C=M;O=A",
    "?C=S;O=A",
    "?C=D;O=A",
    "/dataset",
    "https://twitter.com/adamwhitcroft"
    ]

# types of files
F_TYPES = ['.csv', '.txt', '.zip']


def file_date_string(dt):
    """Convert string to datetime."""
    return datetime.datetime.strftime(dt, "%Y%m%d")


def time_str_to_datetime(string, fmt="%Y-%m-%d %H:%M  "):
    "Convert the last mod string found in the webpage to a datetime."
    return datetime.datetime.strptime(string, fmt)


def get_page(url):
    """Request page using GET method and return a BeautifulSoup object."""
    r = requests.get(url)
    soup = BeautifulSoup(r.content, features='lxml')
    return soup


def get_file_list_from_page(url, ftype='csv'):
    """Get a list of all the files of specific type from the webpage."""
    soup = get_page(url)
    link_list = []
    for a_attr in soup.find_all('a'):
        download_link = a_attr.get('href')
        if ftype in download_link:
            link_list.append(download_link)
    return link_list


def files_with_timestamp_from_page(url, ftype='csv'):
    """Get a list of all the files of specific type from the webpage."""
    soup = get_page(url)
    # Get tags that contain the time of last modificatin in the file.
    last_mod_tag = soup.find_all('td', {'class': 'indexcollastmod'})[1:]
    # Return only the datetime string.
    last_mod_list = [time_str_to_datetime(tag.text) for tag in last_mod_tag]
    link_list = []
    for a_attr in soup.find_all('a'):
        download_link = a_attr.get('href')
        if ftype in download_link:
            link_list.append(download_link)
    dic = dict(zip(link_list, last_mod_list))
    return dic


today = datetime.date.today()


def get_updated_files_from_page(url, ftype, dt=today):
    f_dic = files_with_timestamp_from_page(url, ftype)
    files = [f for f, d in f_dic.items() if datetime.datetime.date(d) == dt]
    return files


def download_file_from_url(fname, url, dir_name):
    """Download a file from a webpage."""
    output_file = join(dir_name, fname)
    data_url = urllib.parse.urljoin(url, fname)
    wget.download(data_url, output_file)
    return None


def populate_dir(url, dir_name, ftype='csv'):
    """Download all files of a page and populate directory."""
    file_list = get_file_list_from_page(url, ftype)

    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    dir_files = os.listdir(dir_name)

    for file in file_list:
        if file not in dir_files:
            download_file_from_url(fname=file, url=url, dir_name=dir_name)
    return


def list_files_to_update(url, dir_name, ftype, dt=today):
    """Get a list of files in directory that are out of date."""
    dir_files = os.listdir(dir_name)
    new_files = get_updated_files_from_page(url, ftype, dt)
    return list(set(dir_files) & set(new_files))


def rename_outofdate_files(url, dir_name, ftype, dt=today):
    """Rename files that are out of date."""
    files = list_files_to_update(url, dir_name, ftype, dt)
    files_to_rename = [os.path.join(dir_name, file) for file in files]
    for file_to_rename in files_to_rename:
        os.rename(
            file_to_rename, "{}_outofdate{}{}".format(
                file_to_rename[:-4], dt, ftype)
        )
