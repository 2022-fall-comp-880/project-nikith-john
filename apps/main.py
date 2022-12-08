"""
main.py file to answer the queries for the Unicorn dataset
"""

import os
import csv


class Valuation:
    """Get the top 10 individual companies having highest valuation."""

    def __init__(self, df) -> None:
        """:parameter df: dataframe
        """
        self.df = df

    def get_valuation(self):
        """ Create an empty list individual_companies
        Reads from df(dataframe), for iterator row in dataframe and appends
        top 10 companies in individual_companies
        :return: list of top 10 valuation companies
        """
        individual_companies = []
        for row in self.df:
            if row[5] != "Acquired":
                individual_companies.append(row)

        top_10 = sorted(individual_companies, key=lambda x: x[1], reverse=True)[:10]
        top_10 = [x[0] for x in top_10]
        return top_10

class Growth:
    """Companies that has growth of more than 100 percent.
    Iterates through companies from dataframe and appends if the company grew
    more than 100 percent."""

    def __init__(self, df) -> None:
        """
        :param df: dataframe
        """
        self.df = df

    def get_growth(self):
        """
        Appends the company that grew more than 100 percent.
        :return List of companies that grew more than 100 percent.
        :rtype: List
        """
        output = []
        for row in self.df:
            if row[6] > 100:
                output.append(row)

        out = [x[0] for x in output]
        return out

class Investors:
    """List of Investors that invested in companies that grew more than
    100 percent."""

    def __init__(self, df) -> None:
        """
        :parameter df: dataframe
        """
        self.df = df

    def get_investors(self):
        """ Create an empty list output
                Reads from df(dataframe), for iterator row in dataframe and
                appends in empty list 'investors' that grow more than 100%
                :return: sorted set of investors
        """
        output = []
        for row in self.df:
            if row[6] > 100:
                output.append(row)

        investors = []

        for row in output:
            investors.extend(row[3].split(", "))

        return sorted(set(investors))

    class Count:
        """Number of unicorn companies in a country."""

        def __init__(self, df) -> None:
            self.df = df

        def get_count(self):
            """
            Create a dictionary with country as key and number of unicorns as
            value.
            :return: count.
            :rtype: dictionary.
            """
            counter = {}
            for row in self.df:
                if row[2] in counter:
                    counter[row[2]] += 1
                else:
                    counter[row[2]] = 1
            return counter


class Main:
    """Main class read the CSV and creates the data."""

    def __init__(self, file_path) -> None:
        self.file_path = file_path
        data = self.read_csv()
        self.df = self.feature_engineering(data)

    def get_data(self):
        """
        :return: df
        """
        return self.df

    def read_csv(self):
        """
        Read the CSV and skip unwanted columns.
        :return: df
        :rtype: list
        """
        skip_columns = [
            "Date Joined",
            "City",
            "Founded Year",
            "Investors Count",
            "Deal Terms",
            "Portfolio Exits",
            "Industry",
        ]

        df = []
        with open(self.file_path, encoding="utf-8", newline="") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                df.append([v for k, v in row.items() if k not in skip_columns])
        return df

    def feature_engineering(self, df):
        """
        Create the data feature engineering, and append the data into it
        in the required format for each different attribute.
        :param df: The dataframe that we created in read_csv
        :return: fe
        :rtype: list
        """
        fe = []
        for row in df:
            temp = []
            temp.append(row[0])
            ## Convert currency to float
            val = float(row[1].replace("$", ""))
            temp.append(val)
            temp.append(row[2])
            temp.append(row[3])
            tr = row[4].replace("$", "")
            if tr == "None":
                tr = 0.0
            else:
                if "M" in tr:
                    tr = float(tr[:-1]) / 1000
                elif "K" in tr:
                    tr = float(tr[:-1]) / 1000000
                else:
                    tr = float(tr[:-1])
            temp.append(tr)
            temp.append(row[5].replace("Acq", "Acquired"))
            # growth
            growth = (val - tr) * 100 / tr if tr != 0.0 else 0.0
            temp.append(growth)
            fe.append(temp)
        return fe

if __name__ == "__main__":
    data_dir = os.path.dirname(__file__) + "/../data/full_data.csv"
    main = Main(data_dir)
    df = main.get_data()
    valuation = Valuation(df)
    print("Top 10 Valued Individual Comapnies: ", valuation.get_valuation())
    growth = Growth(df)
    print("\nComanies that has growth of more than 100 percent are:")
    print(growth.get_growth())
    investors = Investors(df)
    print("\nInvestors that invested in companies that grew more than 100 percent are:")
    print(investors.get_investors())
    count = Count(df)
    print("\nNumber of unicorn companies in a country:")
    print(count.get_count())
    string_top10 = str(valuation.get_valuation())
    string_growth = str(growth.get_growth())
    string_investors = str(investors.get_investors())
    string_count = str(count.get_count())
    file = open('outputdata.txt', 'w')
    file.write("Top 10 Unicorn Companies:\n")
    file.write(string_top10)
    file.write("\n\nCompanies that grew more than 100 percent:\n")
    file.write(string_growth)
    file.write(
        "\n\nInvestors that invested in companies which grew more than 100 percent:\n")
    file.write(string_investors)
    file.write("\n\nCountries with number of Unicorn companies:\n")
    file.write(string_count)
    file.close()
