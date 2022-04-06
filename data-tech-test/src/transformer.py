from typing import (
    List,
    Tuple,
)

import pandas as pd


class Transformer:

    def __init__(self):
        self

    def read_orders(self) -> pd.DataFrame:
        orders = pd.read_csv("C:/data-tech-test-deliverables/data-tech-test/orders.csv", header=0)
        return orders

    def enrich_orders(self, orders: pd.DataFrame, col_name: str, value: List[str]) -> pd.DataFrame:
        """
        Adds a column to the data frame

        Args:
            orders (pd.Dataframe): The dataframe to be enriched
            col_name (str): Name of the new enriched column
            value (List[str]): Data to go into the new column

        Returns:
            The enriched dataframe
        """
        orders[col_name] = value
        return orders

    def split_customers(self, orders: pd.DataFrame, threshold: int) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        Splits customers into two groups based on a threshold

        Args:
            orders (pd.DataFrame): The dataframe to be split
            threshold (int): Value to split the customer base on

        Returns:
            Tuple containing the split dataframes
        """
        amount = orders['amount'].astype(int)
        low_spending_customers_mask = amount <= threshold
        high_spending_customers_mask = amount > threshold

        low_spending_customers  = orders[low_spending_customers_mask]
        high_spending_customers = orders[high_spending_customers_mask]
        return (low_spending_customers, high_spending_customers)

class Bonus:

    def __init__(self):
        pass

    def find_customer_with_highest_order_amount(self, orders: pd.DataFrame) -> str:
        """
        Find the customer name with the highest order amount from the orders list

        Args:
            orders (pd.DataFrame): The dataframe to be split

        Returns:
            Name of the customer who placed the highest order amount
        """
        # Extract the column with all the amounts
        amount_col = orders['amount']
        # Convert the amounts from string to integer for integer comparision purposes 
        amount_col = amount_col.astype(int)
        # Find the index with the highest amount
        idx = amount_col.argmax()
        # Find the row with the index obtained in the step above
        row = orders.iloc[idx]
        # Find the customer name from the extracted row
        name = row['customer']
        # Return the name of the customer with highest amount
        return name

    def find_customer_with_lowest_order_amount(self, orders: pd.DataFrame) -> str:
        """
        Find the customer name with the lowest order amount from the orders list

        Args:
            orders (pd.DataFrame): The dataframe to be split

        Returns:
            Name of the customer who placed the lowest order amount
        """
        # Extract the column with all the amounts
        amount_col = orders['amount']
        # Convert the amounts from string to integer for integer comparision purposes 
        amount_col = amount_col.astype(int)
        # Find the index with the lowest amount
        idx = amount_col.argmin()
        # Find the row with the index obtained in the step above
        row = orders.iloc[idx]
        # Find the customer name from the extracted row
        name = row['customer']
        # Return the name of the customer with lowest amount
        return name

    def find_average_order_amount(self, orders: pd.DataFrame) -> str:
        """
        Find the average order amount from the orders list across all customers

        Args:
            orders (pd.DataFrame): The dataframe to be split

        Returns:
            Average order amount across all customers
        """
        # Extract the column with all the amounts
        amount_col = orders['amount']
        return amount_col.mean()

    def find_customer_with_earliest_order(self, orders: pd.DataFrame) -> str:
        """
        Find the customer who placed the earliest order

        Args:
            orders (pd.DataFrame): The dataframe to be split

        Returns:
            Name of the customer who placed the earliest order
        """
        # Extract the column with all the dates
        date_col = orders['date']
        # Convert date column to datetime and find the index with the earliest date
        idx = pd.to_datetime(date_col).argmin()
        # Find the row with the index obtained in the step above
        row = orders.iloc[idx]
        # Find the customer name from the extracted row
        name = row['customer']
        # Return the name of the customer with lowest amount
        return name

    def find_month_with_most_orders(self, orders: pd.DataFrame) -> str:
        # Obtain all the months in which the order took place

        # Month can be obtained by splitting the date using the delimiter '-' and extracting the field
        # corresponding to index = 1 
        order_months = list(map(lambda x: x.split('-')[1], orders['date']))

        # Calculate the maximum occuring month
        return max(order_months, key=order_months.count)

if __name__ == '__main__':
    transformer = Transformer()
    data = transformer.read_orders()

    countries = ['GBR', 'AUS', 'USA', 'GBR', 'RUS', 'GBR', 'KOR', 'NZ']
    data = transformer.enrich_orders(data, 'Country', countries)

    threshold = 700
    low_spending_customers, high_spending_customers = transformer.split_customers(data, threshold)
    print('\n############')
    print('Low spending customers:\n', low_spending_customers)
    print('\nHigh spending customers:\n', high_spending_customers)

    print('############\n')

    print('Running the bonus tasks\n')

    bonus = Bonus()

    print('Customer with highest order amount:', bonus.find_customer_with_highest_order_amount(data))
    print('Customer with lowest order amount:', bonus.find_customer_with_lowest_order_amount(data))
    print('Average order amount:', bonus.find_average_order_amount(data))
    print('Customer with earliest order:', bonus.find_customer_with_earliest_order(data))
    print('Month with most orders:', bonus.find_month_with_most_orders(data))

    print()