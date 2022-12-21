# Design
## Source Files
> unicorn.py : contains the code-base for **class Unicorn**. 
> test_get_valuation.py :  test case for **get_valuation** method.
> test_get_growth.py : test case for **get_growth** method.
> test_get_investors.py : test case for **get_investors** method.

## Implementation

### def write
> Creates row assigning 'company', 'valuation', 'country', 'industry', 
> 'investor', 'fundsraised' to each column.
>
> We are writing the row in **unicorn_info_file_obj**.

### def read_dataset
> In this method, we will append the the attribute to it's repestive row.
> 
> Example, we will append company to companies, valuation to valuations and 
> so on.
