def get_period_of_between(period_from, period_to):
    period_from = str(period_from)
    period_to = str(period_to)
    start_year = int(period_from[:-2])
    start_month = int(period_from[-2:])
    end_year = int(period_to[:-2])
    end_month = int(period_to[-2:])
    periods = []
    year_from = start_year
    year_to = end_year
    for year in list(range(year_from, year_to+1)):
        month_from = 1
        month_to = 12
        if year == start_year:
            month_from = start_month
        if year == end_year:
            month_to = end_month
        for month in list(range(month_from, month_to+1)):
            year = str(year)
            month = str(month).zfill(2)
            periods.append(int(f"{year}{month}"))
    return periods
