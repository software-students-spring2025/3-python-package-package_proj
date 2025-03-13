import logging

def pytest_configure():
    """Configure logging to print to the console during tests."""
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
