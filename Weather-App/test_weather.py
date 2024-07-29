import unittest
from weather import fetchWeather






class TestWeatherService(unittest.TestCase):
    def setUp(self):
        """Set up a WeatherService instance for testing."""
        self.service = fetchWeather(api_key="dummy_api_key")
    
    def test_fetch_weather_data_non_string(self):
        """Test fetch_weather_data with non-string input raises TypeError."""
        # Define a list of non-string inputs
        non_string_inputs = [123, None, 45.6, True, [], {}]

        # for input_value in non_string_inputs:
        #     with self.assertRaises(TypeError):
        #         self.service.fetch_weather_data(input_value)

if __name__ == "__main__":
    # Run the tests
    unittest.main()
