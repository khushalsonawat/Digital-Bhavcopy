# import zipfile

# with zipfile.ZipFile('../../data/PR041022.zip', 'r') as zip_ref:
#     zip_ref.extract('Pd041022.csv', '../../data')
# import requests

# url = "https://archives.nseindia.com/content/equities/EQUITY_L.csv"

# response = requests.get(url)

# with open('../../data/Pd041022.csv', 'w+') as csv_file:
#     csv_file.write(response.text)
# import datetime

# day = datetime.datetime.now().strftime('%Y-%m-%d')[2:].split('-')

# print(''.join(day[::-1]))
# import wget

# wget.download(
#     "https://archives.nseindia.com/archives/equities/bhavcopy/pr/PR041022.zip",
#     "../../data"
# )
