# Business Sales Dashboard (Power BI / Excel)

This repository contains a Business Sales Dashboard project using a Microsoft-style sample dataset. The included dataset covers **6 months (half-year)** of sales data across regions and product categories.

## Contents
- `data/` - contains `business_sales_data.csv` (synthetic half-year data) and `data_dictionary.md`
- `excel_dashboard/` - Excel workbook template and guide
- `powerbi_dashboard/` - Power BI build guide and DAX formulas (PBIX not included)
- `scripts/` - data preparation scripts
- `visuals/` - PNG screenshots and charts
- `documentation/` - project summary and instructions

## Using a Microsoft Sample Dataset
If you prefer to use an official Microsoft sample dataset (recommended for Power BI), download one of the Power BI samples such as **Retail Analysis**, **Store Sales**, or **AdventureWorks** from Microsoft:
- Power BI samples: https://learn.microsoft.com/power-bi/create-reports/sample-datasets
- AdventureWorks samples: https://learn.microsoft.com/sql/samples/adventureworks-install-configure

Place the downloaded Excel (.xlsx) or .pbix into the `powerbi_dashboard/` folder and run the `scripts/data_preparation.py` to extract a 6-month subset (or use the provided `business_sales_data.csv`).

## Quick start
1. Open `data/business_sales_data.csv`; use it as the data source in Excel or Power BI.
2. For Power BI, open Power BI Desktop and import the CSV or your downloaded .pbix sample.
3. For Excel dashboard, open `excel_dashboard/Business_Sales_Dashboard_DataOnly.xlsx` or create pivot tables from the CSV.
