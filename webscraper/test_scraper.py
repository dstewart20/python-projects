from scraper import get_next_meeting, get_fomc_calendar, get_cpi_report

# Test FOMC meeting functions

# Test CPI report
print("\nTesting CPI Report...")
cpi_data = get_cpi_report()
print(f'CPI Data: {cpi_data}')
