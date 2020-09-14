import pandas as pd
import argparse


def find_max_sorted_values(sales_df):
    sorted_sales = sales_df.sort_values('quantity', ascending=False)
    top_value = sorted_sales.quantity.unique()[(top - 1)]

    return sorted_sales[sorted_sales['quantity'] >= top_value]


def drop_unnecessary_cols(sorted_df, required_col_name):
    unnecessary_cols = ~sorted_df.columns.str.contains(required_col_name)
    unnecessary_cols &= ~sorted_df.columns.str.contains('quantity')

    sorted_df.drop(
        sorted_df.columns[unnecessary_cols],
        axis=1,
        inplace=True
    )
    return sorted_df


def get_product_results(sales_df):
    sales_df = sales_df.join(product.set_index('id'), on='product')

    sales_df = sales_df.groupby(['name'], as_index=False).sum()

    sorted_df = find_max_sorted_values(sales_df)

    sorted_df = drop_unnecessary_cols(sorted_df, 'name')

    print('-- top seller product --')
    print(sorted_df.to_string(index=False))
    return


def get_store_results(sales_df):
    sales_df = sales_df.join(store.set_index('id'), on='store')

    sales_df = sales_df.groupby(['name'], as_index=False).sum()

    sorted_df = find_max_sorted_values(sales_df)

    sorted_df = drop_unnecessary_cols(sorted_df, 'name')

    print('-- top seller store --')
    print(sorted_df.to_string(index=False))
    return


def get_brand_results(sales_df):
    sales_df = sales_df.join(product.set_index('id'), on='product')

    sales_df = sales_df.groupby(['brand'], as_index=False).sum()

    sorted_df = find_max_sorted_values(sales_df)

    sorted_df = drop_unnecessary_cols(sorted_df, 'brand')

    print('-- top seller brand --')
    print(sorted_df.to_string(index=False))
    return


def get_city_results(sales_df):
    sales_df = sales_df.join(store.set_index('id'), on='store')

    sales_df = sales_df.groupby(['city'], as_index=False).sum()

    sorted_df = find_max_sorted_values(sales_df)

    sorted_df = drop_unnecessary_cols(sorted_df, 'city')

    print('-- top seller city --')
    print(sorted_df.to_string(index=False))
    return


def find_best_sellers():
    # print("min date is {}, max date is {} and find the top {} seller".format(min_date, max_date, top))

    sales_between_years = sales[(sales['date'] >= min_date) & (sales['date'] <= max_date)]

    get_product_results(sales_between_years)
    get_store_results(sales_between_years)
    get_brand_results(sales_between_years)
    get_city_results(sales_between_years)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--min-date",
        type=str,
        default="2020-01-01",
        help="start of the date range"
    )

    parser.add_argument(
        "--max-date",
        type=str,
        default="2020-06-30",
        help="end of the date range"
    )

    parser.add_argument(
        "--top",
        type=int,
        default=3,
        help="number of rows in the output"
    )

    args = parser.parse_args()
    min_date = args.min_date
    max_date = args.max_date
    top = args.top

    product = pd.read_csv('product.csv')
    store = pd.read_csv('store.csv')
    sales = pd.read_csv('sales.csv')

    find_best_sellers()
