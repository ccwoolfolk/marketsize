import csv
import io
from datetime import datetime
import requests
from typing import Dict, List

import config


ProductCode = str
ProductCodeDescription = str

def get_product_codes() -> Dict[ProductCode, ProductCodeDescription]:
    product_codes: Dict[ProductCode, ProductCodeDescription] = dict()

    with open(config.PRODUCT_CODE_FILEPATH, 'rb') as csv_file:
        # read into in-memory file-like object, so we can decode
        text = io.StringIO(csv_file.read().decode('cp1252'))
        csv_reader = csv.reader(text, delimiter='|')
        next(csv_reader) # Skip header

        for row in csv_reader:
            product_code = row[2]
            description = row[3]
            if product_code in config.PRODUCT_CODE_WEIGHTS:
                product_codes[product_code] = description

    return product_codes

def code_query(codes: List[str]) -> str:
    '''
    This seems to pick up the "classification produce code" field but not the
    "subsequent product code" field; the documentation is strangely silent
    on the entire topic, so this is an educated guess.
    '''
    combined_codes = '+'.join(codes)
    return f'product_code:({combined_codes})'

def country_query(country: str) -> str:
    return f'country_code:{country}'

def date_query(start_date: str, end_date: str) -> str:
    return f'date_received:[{start_date}+TO+{end_date}]'

def search_param(queries: List[str]) -> str:
    combined_queries = '+AND+'.join(queries)
    return f'search={combined_queries}'

def count_param() -> str:
    return 'count=product_code'

def make_url(params: List[str]) -> str:
    base_url = 'https://api.fda.gov/device/510k.json'
    combined_params = '&'.join(params)
    return f'{base_url}?{combined_params}'

def get_n_years_between(st: str, en: str) -> float:
    difference = datetime.strptime(en, '%Y-%m-%d') - datetime.strptime(st, '%Y-%m-%d')
    return round(difference.days / 365, 1)

def get_n_filings_per_year () -> int:
    product_codes = get_product_codes()
    url = make_url([
        search_param([
            code_query(list(product_codes.keys())),
            country_query(config.COUNTRY),
            date_query(config.START_DATE, config.END_DATE),
        ]),
        count_param(),
    ])

    response = requests.get(url)
    total = 0

    print(f'GET: {url}')
    for r in response.json()['results']:
        count = r['count']
        code = r['term']
        weight = config.PRODUCT_CODE_WEIGHTS[code]
        total += count*weight
        desc = product_codes[code]
        print(f'{count: <6} ({round(count*weight)}) -- {code}: {desc}')

    print(f'{total} matching entries found.')

    n_years = get_n_years_between(config.START_DATE, config.END_DATE)
    n_filings_per_year = int(total / n_years)
    print(f'{n_filings_per_year} per year')
    return n_filings_per_year
