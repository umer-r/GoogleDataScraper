@echo off
:: REMOVE ALL THE LINES FROM THE SCRIPT STARTING WITH 'pip3' AFTER FIRST EXECUTION
pip install shutil
pip install bs4
pip install requests
python %cd%\Web_Data_Scrape.py
pause