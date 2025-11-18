import pandas as pd
import os

base = os.path.join(os.path.dirname(__file__), '..')
data_dir = os.path.join(base, 'data')
powerbi_dir = os.path.join(base, 'powerbi_dashboard')

# If you have a Microsoft sample Excel (e.g., Retail Analysis), set its filename here
sample_file = os.path.join(powerbi_dir, 'sample_sales.xlsx')  # <-- replace with your downloaded file

output_csv = os.path.join(data_dir, 'business_sales_data_prepared.csv')

def prepare_from_csv(csv_path):
    df = pd.read_csv(csv_path, parse_dates=['OrderDate'])
    max_date = df['OrderDate'].max()
    cutoff = max_date - pd.DateOffset(months=6)
    df6 = df[df['OrderDate'] >= cutoff].copy()
    df6.to_csv(output_csv, index=False)
    print('Prepared data saved to', output_csv)

def prepare_from_excel(excel_path, sheet_name=None):
    df = pd.read_excel(excel_path, sheet_name=sheet_name, parse_dates=['OrderDate'])
    max_date = df['OrderDate'].max()
    cutoff = max_date - pd.DateOffset(months=6)
    df6 = df[df['OrderDate'] >= cutoff].copy()
    df6.to_csv(output_csv, index=False)
    print('Prepared data saved to', output_csv)

if __name__ == '__main__':
    print('Edit this script to point to your sample file and run it to prepare a 6-month dataset.')
