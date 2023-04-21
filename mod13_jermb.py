import unittest

def user_input():
    global symbol; symbol = input("Symbol:")
    global type; type = input("Chart type (1 or 2):")
    global series; series = input("Time series (1 - 4):")
    global start; start = input("Start date (YYYY-MM-DD):")
    global end; end = input("End date (YYYY-MM-DD):")
        

class TestInput(unittest.TestCase):


    #   symbol: capitalized, 1-7 alpha characters
    def test_symbol(self):
        self.assertRegex(symbol, r"^[A-Z]{1, 7}$")


    #chart type: 1 numeric character, 1 or 2
    def test_chart_type(self):
        self.assertIn(type, [1, 2])


    #   time series: 1 numeric character, 1 - 4
    def test_time_series(self):        
        self.assertIn(series, [1, 2, 3, 4])


    #   start date: date type YYYY-MM-DD
    def test_start_date(self):
        self.assertRegex(start, r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")


    #   end date: date type YYYY-MM-DD
    def test_start_date(self):        
        self.assertRegex(end, r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")


if __name__ == "__main__":
    user_input()
    unittest.main()
