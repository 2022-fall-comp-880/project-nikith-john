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

