import os
import re
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
        product_names, previous_year, curr_year = self.parse_excel()
        for index, row in self.df.iterrows():
            if index % 10 == 0:
                print(f'Adding row {index}')
            for product in product_names:
                # Current year data
                p = Pharmacy(cip=row['CIP'], pharma_name=row['pharma_name'],
                             subtype=product.replace('gamme_', '').replace('_', ' '),
                             unit=row.get(f'{product}_unit_1'), year=curr_year, ca=row.get(f'{product}_ca_1'),
                             type=self.get_type(product), group=row['group'])

                # Compute Evolution
                p.unit_evolution = row.get(f'{product}_unit_1') / row.get(f'{product}_unit_0') \
                    if product != 'total' and row.get(f'{product}_unit_0') else None
                p.ca_evolution = row.get(f'{product}_ca_1') / row.get(f'{product}_ca_0') \
                    if row.get(f'{product}_ca_0') else None
                p.save()

                # Previous year data
                p = Pharmacy(cip=row['CIP'], pharma_name=row['pharma_name'],
                             subtype=product.replace('gamme_', '').replace('_', ' '),
                             unit=row.get(f'{product}_unit_0'), year=previous_year, ca=row.get(f'{product}_ca_0'),
                             type=self.get_type(product), group=row['group'])
                p.save()

    @staticmethod
    def get_type(product):
        if 'gamme' in product:
            return 'gamme'
        if 'total' in product:
            return 'total'
        return 'produit'

    def parse_excel(self):
        products_names, previous_year, curr_year = self.get_products_name_and_years()
        self.df = pd.read_excel('bilan COS + CPC pour 2018 nov 2017 envoi (2).xlsx',
                                sheet_name='suivi obj ', skiprows=5)
        self.df.dropna(subset=["CIP"], inplace=True)
        self.df.rename(columns={self.df.columns[2]: "pharma_name"}, inplace=True)
        self.df.rename(columns={self.df.columns[-1]: 'group'}, inplace=True)
        self.rename_columns(products_names)

        # Convert CA and Unite columns to be integer
        columns_to_convert = [col for col in self.df.columns if self.is_integer_column(col)]
        self.df[columns_to_convert] = self.df[columns_to_convert].astype(int)
        self.df = self.df[['CIP', 'pharma_name', 'group'] + columns_to_convert]
        return products_names, previous_year, curr_year

    def get_products_name_and_years(self):
        # Find all products names
        products_names = pd.read_excel('bilan COS + CPC pour 2018 nov 2017 envoi (2).xlsx', sheet_name='suivi obj ',
                                       skiprows=3, nrows=3)
        names = [col for col in products_names.columns if 'Unnamed' not in col and 'evolu' not in col]
        names = [n.replace('CA', '').strip().replace(' ', '_').lower() for n in names]

        # Find years
        row_string = products_names.iloc[1].to_string(index=False)
        years = set([int(x) for x in re.findall(r'\d+', row_string)])
        return names, min(years), max(years)

    @staticmethod
    def is_integer_column(col):
        return any(name in col for name in ['unit_0', 'unit_1', 'ca_0', 'ca_1'])

    def rename_columns(self, products_names):
        products_seen = 0
        changed_columns = set()
        skip_unit = False
        for i, col in enumerate(self.df.columns):
            if 'unit' in col:
                if skip_unit:
                    skip_unit = False
                    continue
                new_column_name = self.rename_column(field_name='unit', products_names=products_names,
                                                     product_idx=products_seen, column_index=i,
                                                     changed_columns=changed_columns)
                changed_columns.add(f"{new_column_name}")
            if re.search(r'CA( )+\d+', col):
                new_column_name = self.rename_column(field_name='ca', products_names=products_names,
                                                     product_idx=products_seen, column_index=i,
                                                     changed_columns=changed_columns)
                if new_column_name in changed_columns:
                    products_seen += 1
                    skip_unit = True
                changed_columns.add(new_column_name)

    def rename_column(self, field_name, products_names, product_idx, column_index, changed_columns):
        new_column_name = f"{products_names[product_idx]}_{field_name}"
        suffix = '0' if new_column_name in changed_columns else '1'
        self.df.rename(columns={self.df.columns[column_index]: f"{new_column_name}_{suffix}"}, inplace=True)
        return new_column_name


if __name__ == '__main__':
    dh = DataHandler()
    dh.file_to_db()
