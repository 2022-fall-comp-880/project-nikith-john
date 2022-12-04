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

- Under Valuation class get_valuation() method answers this query.
- Filter out the companies that are not acquired and store in a variable individual_companies.
- Print the top 10 individual companies having highest valuation stored in top_10.
=======
