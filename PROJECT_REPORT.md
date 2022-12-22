# UNICORN COMPANIES
# Project Report
### COMP880 INTEGRATED PRACTICUM
### NIKITH KAITHALAPURAM & JOHN EVANS TALLAPALLY 
### 12/21/2022

## 1. Purpose 

Unicorn companies or unicorn startups are private companies with a valuation 
over $1 billion. We have unicorn companies is various industries such as Artificial
Intelligence, E-commerce, Fintech, Internet software services, supply chain among 
all the industries.

A private company valued at more than $1 billion is referred to as a unicorn company 
or unicorn startup. There are 1,000 unicorns in the world as of March 2022. A 
few well-known ex-unicorns are Airbnb, Facebook, and Google. A decacorn, worth 
over $10 billion, and a hectocorn, worth over $100 billion, are examples of variants.
Discover each company's valuation, investors, and more by downloading the complete list right away.

The data set has been obtained from website `kaggle` https://www.kaggle.com/ 
data has been collected by https://www.cbinsights.com/research-unicorn-companies 
with scarping technology under CCO: Public Domain licensing.

Author/Contributor : Deep Contractor 

Investigative Questions:
> What is the valuation of the individual companies?
>
> Companies that has growth of more than 100 percent?
> 
> ALl the unique investors?
>
> Countries with number of unicorn companies? 


## 2. Approach 

Question 1: Get the valuation of top 10 companies.
What is the input?
> The input for this question is the CSV file in the first method.

What is the output?
> List of companies with top 10 valuation.

What is the idea of the input-to output transformation?
> * Companies are already in the decreasing order of valuation.
> * We append the companies until index 10 into a list.

Question 2: Companies that has growth more than 100 percent.
What is the input?
> The input for this question is the CSV file in the second method.

What is the output?
> The output is list of companies with more than 100 percent.

What is the idea of the input-to output transformation?
> We built a logic where **g_valuation** is twice of fundsraised.
> From input, we will append these companies to **growth_companies**.


Question 3: List of unique companies.
What is the input?
> Even for third method, the input for this question is the CSV file. 

What is the output?
> Output is the set of the list of companies so that we don't have duplicated.

What is the idea of the input-to output transformation?
> We are reading from CSV and the output is sorted set of list of companies so that we have it in alphabetical order.

## 3. Testing
* Each question is implemented separately in modules.
* Each module is tested by three test cases by using three modules empty, first_5 & last_2.

## *first_module:*
* Module Name: test_get_count.py
* Class Name : TestGetCount

### *test_get_count_empty*
* This method input is  
* out put is 
* This output can be verified from 

### *test_get_count_first_5*
* This method input is 
* out put is 
* This output can be verified from 

### *test_get_count_last_2*
* This method input is 
* out put is 
* This output can be verified from 

## *second_module:*
* Module Name: test_get_growth.py
* Class Name : TestPlayerGrowth

### *test_get_growth_empty*
* This method input is 
* out put is 
* This output can be verified from 

### *test_get_growth_first_5*
* This method input is 
* out put is 
* This output can be verified from 

### *test_get_growth_last_5*
* This method input is 
* out put is 
* This output can be verified from 

## *third_module:*
* Module Name: test_get_investors.py
* Class Name : TestPlayerInvestors

### *test_get_investors_empty*
* This method input is 
* out put is 
* This output can be verified from 

### *test_get_investors_first_5*
* This method input is 
* out put is 
* This output can be verified from 

### *test_get_investors_last_2*
* This method input is 
* out put is 
* This output can be verified from 

## *fourth_module:*
* Module Name: test_get_valuation.py
* Class Name : TestPlayerValuation

### *test_get_valuation_last_2*
* This method input is 
* out put is 
* This output can be verified from 

### *test_get_valuation_last_2*
* This method input is 
* out put is 
* This output can be verified from 

### *test_get_valuation_last_2*
* This method input is 
* out put is 
* This output can be verified from 


## 4. Results 
> The output of the code are the results of the methods of investigative 
> questions. The out of get_valuation method is:
> [('Bytedance', 180, 'Artificial intelligence', 'China', 'Sequoia Capital China, SIG Asia Investments, Sina Weibo, Softbank Group', 8), ('SpaceX', 100, 'Other', 'United States', 'Founders Fund, Draper Fisher Jurvetson, Rothenberg Ventures', 7), ('SHEIN', 100, 'E-commerce & direct-to-consumer', 'China', 'Tiger Global Management, Sequoia Capital China, Shunwei Capital Partners', 2), ('Stripe', 95, 'Fintech', 'United States', 'Khosla Ventures, LowercaseCapital, capitalG', 2), ('Klarna', 46, 'Fintech', 'Sweden', 'Institutional Venture Partners, Sequoia Capital, General Atlantic', 4), ('Canva', 40, 'Internet software & services', 'Australia', 'Sequoia Capital China, Blackbird Ventures, Matrix Partners', 0.57), ('Checkout.com', 40, 'Fintech', 'United Kingdom', 'Tiger Global Management, Insight Partners, DST Global', 2), ('Instacart', 39, 'Supply chain, logistics, & delivery', 'United States', 'Khosla Ventures, Kleiner Perkins Caufield & Byers, Collaborative Fund', 3), ('JUUL Labs', 38, 'Consumer & retail', 'United States', 'Tiger Global Management', 14), ('Databricks', 38, 'Data management & analytics', 'United States', 'Andreessen Horowitz, New Enterprise Associates, Battery Ventures', 3)]
>
> The output of get_growth method is:
> ['Bytedance', 'SpaceX', 'SHEIN', 'Stripe', 'Klarna', 'Canva', 'Checkout.com', 'Instacart', 'JUUL Labs', 'Databricks', 'Revolut', 'Epic Games', 'FTX', 'Fanatics', 'Chime', 'BYJUs', 'J&T Express', 'Xiaohongshu', 'Miro', 'Yuanfudao', 'Rapyd', 'Discord', 'Genki Forest', 'goPuff', 'Blockchain.com', 'Plaid', 'Devoted Health', 'OpenSea', 'Grammarly', 'Argo AI', 'Northvolt', 'Faire', 'Airtable', 'Brex', 'Getir', 'Biosplice Therapeutics', 'Bitmain', 'GoodLeap', 'Xingsheng Selected', 'ZongMu Technology', 'Bolt', 'Swiggy', 'Weilong Foods', 'Global Switch', 'Bolt', 'Celonis', 'Zuoyebang', 'Ripple', 'OYO Rooms', 'OutSystems', 'ServiceTitan', 'Alchemy', 'Chehaoduo', 'Digital Currency Group', 'Figma', 'Gusto', 'Lalamove', 'Notion Labs', 'reddit', 'Talkdesk', 'Thrasio', 'Dunamu', 'Yanolja', 'Pony.ai', 'Nuro', 'Snyk', 'Kavak', 'N26', 'Klaviyo', 'Niantic', 'Tanium', 'Dream11', 'DJI Innovations', 'Netskope', 'Razorpay', 'Dapper Labs', 'Lacework', 'Tipalti', 'Hopin', 'Caris Life Sciences', 'Ramp', 'Tempus', 'Fireblocks', 'Flexport', 'National Stock Exchange of India', 'Meicai', 'Impossible Foods', 'CRED', 'Attentive', 'Rippling', 'Carta', 'Toss', 'Ziroom', 'Scale AI', 'Gong', 'TripActions', '1Password', 'Automation Anywhere', 'Gemini']
>
> The out of get_investors method is:
> ['01 Advisors, Zeev Ventures, Group 11', 'Accel India, SAIF Partners, Norwest Venture Partners', 'Accel Partners, Sequoia Capital', 'Accel Partners, SoftBank Group, Sequoia Capital', 'Accel, 83North', 'Accel, AltaIR Capital, Technology Crossover Ventures', 'Accel, Northzone Ventures, Institutional Venture Partners', 'Accel, Softbank Group, Anthos Capital', 'Accel, Y Combinator, Index Ventures', 'Activant Capital, Tribe Capital, General Atlantic', 'Andreessen Horowitz, F-Prime Capital, Venrock', 'Andreessen Horowitz, Lightspeed Venture Partners, Zeev Ventures', 'Andreessen Horowitz, New Enterprise Associates, Battery Ventures', 'Andreessen Horowitz, Nor-Cal Invest, TPG Growth', 'Andreessen Horowitz, Thirty Five Ventures, Sound Ventures', 'Aviation Industry Corporation of China, Essence Financial, Jiangsu Sha Steel Group', 'BOLDstart Ventures, Google Ventures, Accel', 'Benchmark, Greylock Partners, Tencent Holdings', 'Bessemer Venture Partners, ICONIQ Capital, Battery Ventures', 'Bessemer Venture Partners, Qualcomm Ventures, Kleiner Perkins Caufield & Byers', 'Bloomberg Beta, Founders Fund, First Round Capital', 'Caffeinated Capital, CRV, Founder Collective', 'Coatue Management, Sequoia Capital China, IDG Capital', 'D1 Capital Partners, Stripe, Coatue Management', 'DFJ Growth Fund, Coatue Management, Addition', 'DJF, Salesforce Ventures, Storm Ventures', 'DST Global, Ribbit Capital, Greenoaks Capital Management', 'DST Global, SoftBank Group, Mountain Nazca', 'Didi Chuxing, Diamler, TMT Investments', 'Forerunner Ventures, Crosslink Capital, Homebrew', 'Founders Fund, Draper Fisher Jurvetson, Rothenberg Ventures', 'GGV Capital, ZhenFund, Tencent', 'General Atlantic, Goldman Sachs, New Enterprise Associates', 'General Catalyst Partners, Google Ventures, Kleiner Perkins Caufield & Byers', 'General Catalyst, Institutional Venture Partners, Breyer Capital', 'Hillhouse Capital Management, Boyu Capital, Sequoia Capital China', 'IAG Capital Partners, Augmentum Fintech, Northzone Ventures', 'IDG Capital, Venture51, Lightspeed Venture Partners', 'Index Ventures, Draft Ventures, Felicis Ventures', 'Index Ventures, Greylock Partners, Kleiner Perkins Caufield & Byers', 'Initialized Capital, Y Combinator, Kleiner Perkins Caufield & Byers', 'Institutional Venture Partners, Sequoia Capital, General Atlantic', 'KKR, ES Ventures, North Bridge Growth Equity', 'KKR, Tencent Holdings, Sequoia Capital China', 'Kaalari Capital, Tencent Holdings, Steadview Capital', 'Khosla Ventures, Forerunner Ventures, Sequoia Capital', 'Khosla Ventures, Horizons Ventures, Temasek Holdings', 'Khosla Ventures, Kleiner Perkins Caufield & Byers, Collaborative Fund', 'Khosla Ventures, LowercaseCapital, capitalG', 'LTW Capital, Legend Capital, Qualcomm Ventures', 'Lightspeed Venture Partners, Google Ventures, Lakestar', 'Lightspeed Venture Partners, Social Capital, Accel', 'Menlo Ventures, Spark Capital, Union Square Ventures', 'MindWorks Ventures, Shunwei Capital Partners, Xiang He Capital', 'Morgan Creek Digital, Marcy Venture Partners, 10T Fund', 'New Enterprise Associates, BDT Capital Partners, Davidson Kempner Capital Management', 'New Enterprise Associates, Spar Capital, Index Ventures', 'New Enterprise Associates, T. Rowe Associates, Lightbank', 'NextView Ventures, Eniac Ventures, Sequoia Capital', 'Nintendo, Google, Pokemon Company International, Spark Capital', 'Norwest Venture Partners, Next World Capital, Wing Venture Capital', 'Qualcomm Ventures, Woori Investment, Hanwha Investment & Securities', 'Redalpine Venture Partners, Earlybird Venture Capital, Valar Ventures', 'Ribbit Capital, capitalG, Softbank Group', 'SBI Investment Korea, Partners Investment, GIC', 'Sequoia Capital China, Blackbird Ventures, Matrix Partners', 'Sequoia Capital China, GX Capital', 'Sequoia Capital China, IDG Capital, DCM Ventures', 'Sequoia Capital China, Longfor Capitalm, Gaorong Capital', 'Sequoia Capital China, SIG Asia Investments, Sina Weibo, Softbank Group', 'Sequoia Capital China, Warburg Pincus, General Catalyst', 'Sequoia Capital China, Xiang He Capital, GGV Capital', 'Sequoia Capital India, Tiger Global Management, Matrix Partners India', 'Sequoia Capital, Thoma Bravo, Softbank', 'Sixth Street Partners, OrbiMed Advisors, Highland Capital Management', 'Slack Fund, Accel, Skip Capital', 'SoftBank Group, Andreessen Horowitz, Temasek Holdings', 'SoftBank Group, Greylock Partners, Gaorong Capital', 'SoftBank Group, Sequoia Capital India,Lightspeed India Partners', 'Summit Partners, Accel, Astral Capital', 'Sutter Hill Ventures, Liberty Global Ventures, Coatue Management', 'TA Associates, SoftBank Group, GS Growth', 'Target Global, General Catalyst, Durable Capital Partners', 'Tenaya Capital, Coatue Management, Stripes Group', 'Tencent Holdings, Hillhouse Capital Management, Yunfeng Capital', 'Tencent Holdings, KKR, Smash Ventures', 'Tencent Holdings, Lightspeed India Partners, Sequoia Capital India', 'Tencent Holdings, Warbug Pincus, IDG Capital', 'Tiger Global Management', 'Tiger Global Management, Blue Lake Capital, ZhenFund', 'Tiger Global Management, DST Global, Sequoia Capital India', 'Tiger Global Management, Insight Partners, DST Global', 'Tiger Global Management, Sequoia Capital China, Shunwei Capital Partners', 'Tiger Global Management, Sequoia Capital, Revo Capital', 'Union Square Ventures, Venrock, Andreessen Horowitz', 'Upper90, RiverPark Ventures, Advent International', 'Vattenfall, Volkswagen Group, Goldman Sachs', 'Vickers Venture Partners, IKEA GreenTech', 'Volkswagen Group, Ford Autonomous Vehicles', 'Y Combinator, Sequoia Capital, Coatue Management', 'index Ventures, DST Global, Ribbit Capital']
> 
> The output of get_count is:
> {'China': 14, 'United States': 56, 'Sweden': 2, 'Australia': 1, 'United Kingdom': 7, 'Bahamas': 1, 'India': 8, 'Indonesia': 1, 'Turkey': 1, 'Estonia': 1, 'Germany': 2, 'Hong Kong': 1, 'South Korea': 3, 'Mexico': 1, 'Canada': 2}

## 5. Evaluation 
> The code should work for any given dataset, provided it has all the attributes needed.
> In the first method 'get_valuation', instead of getting all the details of companies, we can just get the list of only companies. 

