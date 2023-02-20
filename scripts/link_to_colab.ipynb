#mount google drive

from google.colab import drive
drive.mount('/content/drive/')

#import library, authenticate, and create interface so can access files and google sheets

from google.colab import auth
auth.authenticate_user()

import gspread
from oauth2client.client import GoogleCredentials


# read corpus from file

df = pd.read_csv('/content/drive/My Drive/nlp_datasets/filename.csv', header = 0)
#df.dropna(axis = 0, inplace=True)
corpus = df['article'].tolist()

# save corpus/data to csv file in drive
corpus.to_csv('/content/drive/My Drive/new_filename.csv', index=False)


#you can also import data into google sheets for later

from gspread_dataframe import set_with_dataframe

gc = gspread.authorize(GoogleCredentials.get_application_default())
sh = gc.create('my_keyword_results')

worksheet = sh.add_worksheet(title="keyword_filtering_2023-02-20", rows="100", cols="20")
set_with_dataframe(worksheet, key_1)

#to add to the same google workbook
sh = gc.open('my_keyword_results')
#then add new worksheet
worksheet = sh.add_worksheet(title="keyword_filtering_2023-02-21", rows="100", cols="20")
set_with_dataframe(worksheet, key_2)
