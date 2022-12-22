import csv

class Unicorn:
    def __init__(self, unicorn_info: list):
        """
        Method to initiate unicorn_info for dataset.
        :param unicorn_info: We will store the dataset in it.
        :type unicorn_info: list
        """
        self.unicorn_info = unicorn_info

    def write(self, unicorn_info_row, filename: str) -> None:
        """
        Method to create row with attributes.
        :param unicorn_info_row: Row in self.unicorn
        :param filename: Name of the file
        :type filename: string
        :return: None
        :rtype: None
        """
        self.unicorn_info_row = unicorn_info_row
        with open(filename, 'w', encoding='utf8') as unicorn_info_file_obj:
            for company, valuation, country, industry, investor, fundsraised in self.unicorn_info:
                unicorn_info_row = f'{company},{valuation},{country},{industry},{investor},{fundsraised}\n'
                unicorn_info_file_obj.write(unicorn_info_row)

    def get_valuation(self) -> list:
        """
        Method to get companies with top 10 valuation.
        :return: individual_companies
        :rtype: list
        """
        i = 0
        individual_companies = []
        for company in self.unicorn_info:
            if i < 10:
                individual_companies.append(company)
                i = i + 1
        print(individual_companies)
        return individual_companies

    def get_growth(self) -> list:
        """
        Method to get companies that grew more than 100 percent.
        :return: growth_company
        :rtype: list
        """
        growth_company = []
        for company, valuation, _, _, _, fundsraised in self.unicorn_info:
            g_logic = fundsraised * 2
            if valuation > g_logic:
                growth_company.append(company)
        print(growth_company)
        return growth_company

    def get_investors(self) -> set:
        """
        Method to get the list of unique investors.
        :return: investor_list
        :rtype: set
        """
        investors_list = []
        for _, _, _, _, _, investor in self.unicorn_info:
            investors_list.append(investor)
        print(sorted(set(investors_list)))
        return sorted(set(investors_list))

    def get_top_countries(self) -> dict:
        """
        Method to get the country and the number of companies in it.
        :return: top_countries
        :rtype: dictionary
        """
        top_countries = {}
        for _, _, _, country, _, _ in self.unicorn_info:
            if country in top_countries:
                top_countries[country] += 1
            else:
                top_countries[country] = 1
        print(top_countries)
        return top_countries



    def __str__(self):
        """Create string representation of data."""
        return str(self.unicorn_info)

    @staticmethod
    def create_standard_dataset() -> "Unicorn":
        """
        Create the dataset for Unicorn
        :return: unicorn_info is the list where we store the data.
        :rtype: list
        """
        companies = [
            'Bytedance',
            'SpaceX',
            'SHEIN',
            'Stripe',
            'Klarna',
            'Canva',
            'Checkout.com',
            'Instacart',
            'JUUL Labs',
            'Databricks',
            'Revolut',
            'Epic Games',
            'FTX',
            'Fanatics',
            'Chime',
            'BYJUs',
            'J&T Express',
            'Xiaohongshu',
            'Miro',
            'Yuanfudao',
            'Rapyd',
            'Discord',
            'Genki Forest',
            'goPuff',
            'Blockchain.com',
            'Plaid',
            'Devoted Health',
            'OpenSea',
            'Grammarly',
            'Argo AI',
            'Northvolt',
            'Faire',
            'Airtable',
            'Brex',
            'Getir',
            'Biosplice Therapeutics',
            'Bitmain',
            'GoodLeap',
            'Xingsheng Selected',
            'ZongMu Technology',
            'Bolt',
            'Swiggy',
            'Weilong Foods',
            'Global Switch',
            'Bolt',
            'Celonis',
            'Zuoyebang',
            'Ripple',
            'OYO Rooms',
            'OutSystems',
            'ServiceTitan',
            'Alchemy',
            'Chehaoduo',
            'Digital Currency Group',
            'Figma',
            'Gusto',
            'Lalamove',
            'Notion Labs',
            'reddit',
            'Talkdesk',
            'Thrasio',
            'Dunamu',
            'Yanolja',
            'Pony.ai',
            'Nuro',
            'Snyk',
            'Kavak',
            'N26',
            'Klaviyo',
            'Niantic',
            'Tanium',
            'Dream11',
            'DJI Innovations',
            'Netskope',
            'Razorpay',
            'Dapper Labs',
            'Lacework',
            'Tipalti',
            'Hopin',
            'Caris Life Sciences',
            'Ramp',
            'Tempus',
            'Fireblocks',
            'Flexport',
            'National Stock Exchange of India',
            'Meicai',
            'Impossible Foods',
            'CRED',
            'Attentive',
            'Ola Cabs',
            'Rippling',
            'Carta',
            'Toss',
            'Ziroom',
            'Scale AI',
            'Gong',
            'TripActions',
            '1Password',
            'Automation Anywhere',
            'Gemini',
            'Zopa'

        ]

        valuations = [
            180,
            100,
            100,
            95,
            46,
            40,
            40,
            39,
            38,
            38,
            33,
            32,
            32,
            27,
            25,
            22,
            20,
            20,
            18,
            17,
            15,
            15,
            15,
            15,
            14,
            13,
            13,
            13,
            13,
            12,
            12,
            12,
            12,
            12,
            12,
            12,
            12,
            12,
            12,
            11,
            11,
            11,
            11,
            11,
            11,
            11,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            8,
            8,
            8,
            8,
            8,
            8,
            8,
            8,
            8,
            8,
            8,
            8,
            8,
            7,
            7,
            7,
            7,
            7,
            7,
            7,
            7,
            7,
            7,
            7,
            7,
            7,
            7,
            7,
            7,
            1
        ]

        industries = [
            'Artificial intelligence',
            'Other',
            'E-commerce & direct-to-consumer',
            'Fintech',
            'Fintech',
            'Internet software & services',
            'Fintech',
            'Supply chain, logistics, & delivery',
            'Consumer & retail',
            'Data management & analytics',
            'Fintech',
            'Other',
            'Fintech',
            'E-commerce & direct-to-consumer',
            'Fintech',
            'Edtech',
            'Supply chain, logistics, & delivery',
            'E-commerce & direct-to-consumer',
            'Internet software & services',
            'Edtech',
            'Fintech',
            'Internet software & services',
            'Consumer & retail',
            'E-commerce & direct-to-consumer',
            'Fintech',
            'Fintech',
            'Health',
            'E-commerce & direct-to-consumer',
            'Internet software & services',
            'Artificial intelligence',
            'Other',
            'Artificial intelligence',
            'Internet software & services',
            'Fintech',
            'E-commerce & direct-to-consumer',
            'Health',
            'Hardware',
            'Internet software & services',
            'E-commerce & direct-to-consumer',
            'Auto & transportation',
            'Auto & transportation',
            'Supply chain, logistics, & delivery',
            'Consumer & retail',
            'Hardware',
            'Fintech',
            'Data management & analytics',
            'Edtech',
            'Fintech',
            'Travel',
            'Internet software & services',
            'Internet software & services',
            'Fintech',
            'E-commerce & direct-to-consumer',
            'Fintech',
            'Internet software & services',
            'Fintech',
            'Supply chain, logistics, & delivery',
            'Internet software & services',
            'Internet software & services',
            'Internet software & services',
            'Other',
            'Fintech',
            'Travel',
            'Artificial intelligence',
            'Auto & transportation',
            'Cybersecurity',
            'E-commerce & direct-to-consumer',
            'Fintech',
            'Internet software & services',
            'Mobile & telecommunications',
            'Cybersecurity',
            'Internet software & services',
            'Hardware',
            'Cybersecurity',
            'Fintech',
            'Fintech',
            'Cybersecurity',
            'Fintech',
            'Internet software & services',
            'Health',
            'Fintech',
            'Health',
            'Fintech',
            'Supply chain, logistics, & delivery',
            'Fintech',
            'Mobile & telecommunications',
            'Consumer & retail',
            'Fintech',
            'Mobile & telecommunications',
            'Auto & transportation',
            'Internet software & services',
            'Fintech',
            'Fintech',
            'E-commerce & direct-to-consumer',
            'Artificial intelligence',
            'Artificial intelligence',
            'Travel',
            'Cybersecurity',
            'Artificial intelligence',
            'Fintech',
            'Fintech'
        ]

        countries = [
            'China',
            'United States',
            'China',
            'United States',
            'Sweden',
            'Australia',
            'United Kingdom',
            'United States',
            'United States',
            'United States',
            'United Kingdom',
            'United States',
            'Bahamas',
            'United States',
            'United States',
            'India',
            'Indonesia',
            'China',
            'United States',
            'China',
            'United Kingdom',
            'United States',
            'China',
            'United States',
            'United Kingdom',
            'United States',
            'United States',
            'United States',
            'United States',
            'United States',
            'Sweden',
            'United States',
            'United States',
            'United States',
            'Turkey',
            'United States',
            'China',
            'United States',
            'China',
            'China',
            'Estonia',
            'India',
            'China',
            'United Kingdom',
            'United States',
            'Germany',
            'China',
            'United States',
            'India',
            'United States',
            'United States',
            'United States',
            'China',
            'United States',
            'United States',
            'United States',
            'Hong Kong',
            'United States',
            'United States',
            'United States',
            'United States',
            'South Korea',
            'South Korea',
            'United States',
            'United States',
            'United States',
            'Mexico',
            'Germany',
            'United States',
            'United States',
            'United States',
            'India',
            'China',
            'United States',
            'India',
            'Canada',
            'United States',
            'United States',
            'United Kingdom',
            'United States',
            'United States',
            'United States',
            'United States',
            'United States',
            'India',
            'China',
            'United States',
            'India',
            'United States',
            'India',
            'United States',
            'United States',
            'South Korea',
            'China',
            'United States',
            'United States',
            'United States',
            'Canada',
            'United States',
            'United States',
            'United Kingdom'

        ]

        fundsraiseds = [
            8,
            7,
            2,
            2,
            4,
            0.57,
            2,
            3,
            14,
            3,
            2,
            7,
            2,
            4,
            2,
            4,
            5,
            0.91,
            0.47,
            4,
            0.77,
            0.97,
            0.72,
            4,
            0.49,
            0.73,
            4,
            0.42,
            0.4,
            4,
            4,
            1,
            1,
            1,
            2,
            0.79,
            0.76,
            0.8,
            5,
            0.37,
            1,
            5,
            0.55,
            5,
            1,
            1,
            3,
            0.29,
            3,
            0.57,
            1,
            0.56,
            4,
            1,
            0.33,
            0.69,
            2,
            0.34,
            1,
            0.49,
            2,
            0.07,
            2,
            1,
            2,
            1,
            2,
            2,
            0.67,
            0.77,
            0.77,
            2,
            0.1,
            1,
            0.74,
            0.6,
            2,
            0.54,
            1,
            1,
            0.66,
            0.82,
            1,
            2,
            0.29,
            1,
            2,
            0.92,
            0.86,
            4,
            0.44,
            1,
            0.84,
            2,
            0.6,
            0.58,
            0.91,
            0.92,
            0.84,
            0.42,
            0.79
        ]

        investors = [
            'Sequoia Capital China, SIG Asia Investments, Sina Weibo, Softbank Group',
            'Founders Fund, Draper Fisher Jurvetson, Rothenberg Ventures',
            'Tiger Global Management, Sequoia Capital China, Shunwei Capital Partners',
            'Khosla Ventures, LowercaseCapital, capitalG',
            'Institutional Venture Partners, Sequoia Capital, General Atlantic',
            'Sequoia Capital China, Blackbird Ventures, Matrix Partners',
            'Tiger Global Management, Insight Partners, DST Global',
            'Khosla Ventures, Kleiner Perkins Caufield & Byers, Collaborative Fund',
            'Tiger Global Management',
            'Andreessen Horowitz, New Enterprise Associates, Battery Ventures',
            'index Ventures, DST Global, Ribbit Capital',
            'Tencent Holdings, KKR, Smash Ventures',
            'Sequoia Capital, Thoma Bravo, Softbank',
            'SoftBank Group, Andreessen Horowitz, Temasek Holdings',
            'Forerunner Ventures, Crosslink Capital, Homebrew',
            'Tencent Holdings, Lightspeed India Partners, Sequoia Capital India',
            'Hillhouse Capital Management, Boyu Capital, Sequoia Capital China',
            'GGV Capital, ZhenFund, Tencent',
            'Accel, AltaIR Capital, Technology Crossover Ventures',
            'Tencent Holdings, Warbug Pincus, IDG Capital',
            'Target Global, General Catalyst, Durable Capital Partners',
            'Benchmark, Greylock Partners, Tencent Holdings',
            'Sequoia Capital China, Longfor Capitalm, Gaorong Capital',
            'Accel, Softbank Group, Anthos Capital',
            'Lightspeed Venture Partners, Google Ventures, Lakestar',
            'New Enterprise Associates, Spar Capital, Index Ventures',
            'Andreessen Horowitz, F-Prime Capital, Venrock',
            'Andreessen Horowitz, Thirty Five Ventures, Sound Ventures',
            'General Catalyst, Institutional Venture Partners, Breyer Capital',
            'Volkswagen Group, Ford Autonomous Vehicles',
            'Vattenfall, Volkswagen Group, Goldman Sachs',
            'Khosla Ventures, Forerunner Ventures, Sequoia Capital',
            'Caffeinated Capital, CRV, Founder Collective',
            'DST Global, Ribbit Capital, Greenoaks Capital Management',
            'Tiger Global Management, Sequoia Capital, Revo Capital',
            'Vickers Venture Partners, IKEA GreenTech',
            'Coatue Management, Sequoia Capital China, IDG Capital',
            'New Enterprise Associates, BDT Capital Partners, Davidson Kempner Capital Management',
            'KKR, Tencent Holdings, Sequoia Capital China',
            'LTW Capital, Legend Capital, Qualcomm Ventures',
            'Didi Chuxing, Diamler, TMT Investments',
            'Accel India, SAIF Partners, Norwest Venture Partners',
            'Tencent Holdings, Hillhouse Capital Management, Yunfeng Capital',
            'Aviation Industry Corporation of China, Essence Financial, Jiangsu Sha Steel Group',
            'Activant Capital, Tribe Capital, General Atlantic',
            'Accel, 83North',
            'Sequoia Capital China, Xiang He Capital, GGV Capital',
            'IDG Capital, Venture51, Lightspeed Venture Partners',
            'SoftBank Group, Sequoia Capital India,Lightspeed India Partners',
            'KKR, ES Ventures, North Bridge Growth Equity',
            'Bessemer Venture Partners, ICONIQ Capital, Battery Ventures',
            'DFJ Growth Fund, Coatue Management, Addition',
            'Sequoia Capital China, GX Capital',
            'Ribbit Capital, capitalG, Softbank Group',
            'Index Ventures, Greylock Partners, Kleiner Perkins Caufield & Byers',
            'General Catalyst Partners, Google Ventures, Kleiner Perkins Caufield & Byers',
            'MindWorks Ventures, Shunwei Capital Partners, Xiang He Capital',
            'Index Ventures, Draft Ventures, Felicis Ventures',
            'Y Combinator, Sequoia Capital, Coatue Management',
            'DJF, Salesforce Ventures, Storm Ventures',
            'Upper90, RiverPark Ventures, Advent International',
            'Qualcomm Ventures, Woori Investment, Hanwha Investment & Securities',
            'SBI Investment Korea, Partners Investment, GIC',
            'Sequoia Capital China, IDG Capital, DCM Ventures',
            'SoftBank Group, Greylock Partners, Gaorong Capital',
            'BOLDstart Ventures, Google Ventures, Accel',
            'DST Global, SoftBank Group, Mountain Nazca',
            'Redalpine Venture Partners, Earlybird Venture Capital, Valar Ventures',
            'Summit Partners, Accel, Astral Capital',
            'Nintendo, Google, Pokemon Company International, Spark Capital',
            'Andreessen Horowitz, Nor-Cal Invest, TPG Growth',
            'Kaalari Capital, Tencent Holdings, Steadview Capital',
            'Accel Partners, Sequoia Capital',
            'Lightspeed Venture Partners, Social Capital, Accel',
            'Sequoia Capital India, Tiger Global Management, Matrix Partners India',
            'Union Square Ventures, Venrock, Andreessen Horowitz',
            'Sutter Hill Ventures, Liberty Global Ventures, Coatue Management',
            '01 Advisors, Zeev Ventures, Group 11',
            'Accel, Northzone Ventures, Institutional Venture Partners',
            'Sixth Street Partners, OrbiMed Advisors, Highland Capital Management',
            'D1 Capital Partners, Stripe, Coatue Management',
            'New Enterprise Associates, T. Rowe Associates, Lightbank',
            'Tenaya Capital, Coatue Management, Stripes Group',
            'Bloomberg Beta, Founders Fund, First Round Capital',
            'TA Associates, SoftBank Group, GS Growth',
            'Tiger Global Management, Blue Lake Capital, ZhenFund',
            'Khosla Ventures, Horizons Ventures, Temasek Holdings',
            'Tiger Global Management, DST Global, Sequoia Capital India',
            'NextView Ventures, Eniac Ventures, Sequoia Capital',
            'Accel Partners, SoftBank Group, Sequoia Capital',
            'Initialized Capital, Y Combinator, Kleiner Perkins Caufield & Byers',
            'Menlo Ventures, Spark Capital, Union Square Ventures',
            'Bessemer Venture Partners, Qualcomm Ventures, Kleiner Perkins Caufield & Byers',
            'Sequoia Capital China, Warburg Pincus, General Catalyst',
            'Accel, Y Combinator, Index Ventures',
            'Norwest Venture Partners, Next World Capital, Wing Venture Capital',
            'Andreessen Horowitz, Lightspeed Venture Partners, Zeev Ventures',
            'Slack Fund, Accel, Skip Capital',
            'General Atlantic, Goldman Sachs, New Enterprise Associates',
            'Morgan Creek Digital, Marcy Venture Partners, 10T Fund',
            'IAG Capital Partners, Augmentum Fintech, Northzone Ventures'

        ]
        unicorn_info = []
        for idx, company in enumerate(companies):
            unicorn_info.append((company, valuations[idx], industries[idx],
                                 countries[idx], investors[idx],
                                 fundsraiseds[idx]))
        return Unicorn(unicorn_info)


    def __str__(self):
        """Create string representation of data."""
        return str(self.unicorn_info)


    @staticmethod
    def read_dataset(filename: str) -> "Unicorn":
        """
        Method to assign attributes to columns.
        :param filename: Name of the file.
        :type filename: string
        :return: unicorn_info
        :rtype: list
        """
        companies = []
        valuations = []
        industries = []
        countries = []
        investors = []
        fundsraiseds = []
        with open(filename, "r") as file:
            csv_reader = csv.reader(file, quotechar=",")
            print(csv_reader)
            for company, valuation, industry, country, investor, fundsraised in csv_reader:
                companies.append(company)
                valuations.append(valuation)
                industries.append(industry)
                countries.append(country)
                investors.append(investor)
                fundsraiseds.append(fundsraised)
        unicorn_info = []
        idx = 0
        for company in companies:
            unicorn_info.append((company, valuations[idx], industries[idx],
                                 countries[idx], investors[idx],
                                 fundsraiseds[idx]))
            idx += 1
        return Unicorn(unicorn_info)

def main():
    unicorn_data: Unicorn = Unicorn.create_standard_dataset()
    print(unicorn_data)
    Unicorn.get_valuation(Unicorn.create_standard_dataset())
    Unicorn.get_growth(Unicorn.create_standard_dataset())
    Unicorn.get_investors(Unicorn.create_standard_dataset())
    Unicorn.get_top_countries(Unicorn.create_standard_dataset())


if __name__ == '__main__':
    main()
