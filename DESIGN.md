# Unicorn Company

## Contributors: Nikith Kaithalapuram & John Evans Tallapally 

## Source Files

> 1. `main.py` - Contains five classes `Main` and other 4 classes for answering
> all the queries.

### Main Class

> - `read_csv()` method reads the csv file as a list of lists and store in `df`
> variable.
> - The `df` variable is then passed to the `feature_engineering()` method. 
> Clean up the and perform Feature Engineering. Create a feature `Growth` using
> `Valuation ($B)` and `Total Raised` columns and sore in the `df` variable.
> - `get_data()` method returns the `df` variable.

### What is the valuation of the individual companies?

> - Under `Valuation` class `get_valuation()` method answers this query.
> - Filter out the companies that are not acquired and store in a variable 
> `individual_companies`.
> - Print the top 10 individual companies having the highest valuation stored
> in `top_10`.

### Companies that has growth of more than 100 percent?

> - Under `Growth` class `get_growth()` method answers this query.
> - Filter out the companies that have growth more than 100 percentage and 
> store in a variable output.
> - Print out the list of companies that has growth of more than 100 percent 
> using variable output.

### Investors that invested in companies that grew more than 100 percent?

> - Under Investors class `get_investors()` method answers this query.
> - Create a variable `investors` to store the investor names
> - Loop through-out the growth companies on feature Select Investors and split 
> on delimiter `,`  and add to the variable `investors` created above.
> - Make a set of the investors so that we have only unique investors.
> - Print out the list of Investors that invested in companies that grew
> more than 100 percent

### Number of unicorn companies in a country.

- Under `Count` class `get_count()` method answers this query.
- Calculate the count of companies by grouping on `country` and store the `counter` in a variable.
- Print out the `counter` dictionary with country as key and number of unicorns as value.
