import pandas as pd
import pytest
from pytest import mark
import numpy as np

from src.transformer import Transformer

@pytest.fixture
def order_data_instance():
    return pd.DataFrame({
        'orderId': ['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8'],
        'amount': ['10', '2000', '30', '40', '5000', '60', '70', '80'],
        'customer': ['Harpal', 'Kelcey',  'Augustus', 'Callum', 'Yulia', 'Brandon', 'Sam', 'Umit'],
        'date': ['2022-01-01', '2022-01-02', '2022-01-04', '2022-01-04', '2022-01-05', '2022-01-06', '2022-01-07', '2022-01-08'],
    })

@pytest.fixture
def order_countries():
    return ['GBR', 'AUS', 'USA', 'GBR', 'RUS', 'GBR', 'KOR', 'NZ']

class TestTransformer:

    # Task 1
    def test__enrich_orders(self, order_data_instance):
        df = order_data_instance
        transformer = Transformer()

        enriched_orders = transformer.enrich_orders(df, 'Country', order_countries)
        assert np.all(enriched_orders['Country'] == order_countries)

    # Task 2
    def test__split_customers(self, order_data_instance, order_countries):
        df = order_data_instance
        transformer = Transformer()

        # Setting the threshold amount to be 100
        threshold = 100
        # For the given test data, 6 customers have purchase amount less than threshold
        # and 2 customers have purchase amount greater than threshold
        low_count = 6
        high_count = 2

        low_spending_customers, high_spending_customers = transformer.split_customers(df, threshold)

        # ensure that all the amounts in the low_spending_customers are less than threshold
        for amount in low_spending_customers['amount']:
            assert int(amount) <= threshold

        # ensure that all the amounts in the high_spending_customers are more than threshold
        for amount in high_spending_customers['amount']:
            assert int(amount) > threshold

        assert len(low_spending_customers) == 6
        assert len(high_spending_customers) == 2
        