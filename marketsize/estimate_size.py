import config
from get_counts import get_n_filings_per_year

def total_market_size(
    n_filings_per_year: int,
    dollars_per_filing: int, 
) -> int:
    return n_filings_per_year * dollars_per_filing

market_size = total_market_size(
    get_n_filings_per_year(),
    config.DOLLARS_PER_FILING,
)

assumed_market = market_size * config. HYPOTHETICAL_PROPORTION_OF_MARKET
n_devs = int(round(assumed_market / config.COST_PER_DEV_FULLY_LOADED, 0))

print(f'Total market size ($, millions): {round(market_size / 1_000_000, 0)}')
print(f'Assumed addressable ($, millions): {round(assumed_market / 1_000_000, 0)}')
print(f'Assumed addressable (n devs): {n_devs}')
