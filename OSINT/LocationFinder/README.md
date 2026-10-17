# Create an instance of the locator
locator = IPLocator(timeout=5)

# Call the method with an IP
data = locator.get_location("8.8.8.8")

# Clean up session when finished
locator.close()