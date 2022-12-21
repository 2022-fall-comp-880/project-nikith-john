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

### def get_valuation
> Parameters: None

> Returns: 'individual_companies' of type list.

> Design steps: 
> * Create empty list 'individual_companies'.
> * We will iterate through the companies in 'self.unicorn_info'
using for loop.
> * As the companies in the dataset are already in order of valuation, 
we will append the companies until index 10.
> * So, if index is less than 10, append company into 'individual_companies'.
> * Return 'individual_companies'

### def get_growth
> Parameters: None

> Returns: growth_company of type list.

> Design steps: 
> * Create an empty list 'growth_company'.
> * We will iterate through 'company', 'valuation', 'fundsraised' in 'self.unicorn_info'.
> * Here, we will build a logic 'g_logic'. 'g_logic' is equal to 'fundsraised*2'.
> * If 'valuation' is greater than 2 times of fundsraised, it means that the 
company has grown more than 100 percent.
> * So, we iterate through 'valuation' using if condition. If 'valuation' is 
greater than 'fundsraised*2', append to 'growth_company'.
> * Return 'get_company'

### def get_investors
> Parameters: None
> 
> Returns: sorted set of investors_list
> 
> Design steps: 
> * Create an empty list 'investors_list'.
> * We will iterate through 'investor' in 'self.unicorn_info'.
> * We will append all the investors to 'investor_list'.
> * Then we return sorted set of investors so that we don't have duplicates 
> and we get the output in alphabetical order.

### def get_top_countries
> Parameters: None
> 
> Returns: 'top_countries' - Dictionary with key as country and value as 
> number of companies in it.
> 
> Design steps:
> * Create an empty dictionary.
> * We will iterate through country in 'self.unicorn_info'.
> * We use if condition to iterate and every time we come accross a particular 
> * country, the number of 'country' will be added.
> * Return 'top_countries'.
