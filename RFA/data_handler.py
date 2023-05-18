import os
import django
from datetime import datetime
import pandas as pd

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Initialize
django.setup()

from newapp.models import Pharmacy


class DataHandler:
    file_name = 'exemple-data-rfa.csv'
    df = None

    def file_to_db(self):
        self.df = pd.read_csv(self.file_name)
        for index, row in self.df.iterrows():
            pharma = Pharmacy(name=row.get('PHARMA'), group=row['GROUPE'], labo_name=row['LABO'],
                              type=row.get('TYPE'), subtype=row['SOUS-TYPE'], ca=row['CA'],
                              start_date=row.get('DEBUT'), end_date=row.get('FIN')
                              # start_date=datetime.strptime(row.get('DEBUT'), '%Y-%m-%d').strftime('%Y-%d-%m'),
                              # end_date=datetime.strptime(row.get('FIN'), '%Y-%m-%d').strftime('%Y-%d-%m')
            )
            # Save the Pharmacy object
            pharma.save()

if __name__ == '__main__':
    dh = DataHandler()
    dh.file_to_db()
