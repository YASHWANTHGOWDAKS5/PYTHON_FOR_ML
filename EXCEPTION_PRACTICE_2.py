# 1. Custom Bank Withdrawal System
# Goal: Create a program that simulates a bank withdrawal.
# Raise a custom exception if the user tries to withdraw more than their balance or enters a negative amount.
# Requirements:
# Balance = ₹10,000
# User enters amount to withdraw
# Raise InsufficientFundsError or InvalidAmountError
# Use try-except-else-finally to log transaction status

#----------------------------------------------------------

# 2. Nested Try: Student Grade File Reader
# Goal: Read student marks from a file, calculate the average, and handle:
# File not found
# Empty file
# Invalid marks in file (e.g., non-integer or >100)
# Requirements:
# Use nested try blocks
# Log all errors to a separate log file

#------------------------------------------------

# Goal: Ask the user to input a valid email address.
# Raise a ValueError if no "@" or "." present
# Allow only 3 attempts
# On 3rd failed attempt, raise a custom MaxAttemptsReached exception
# Requirements:
# Use a loop with try-except
# After success, log the email to a file
# Use finally for attempt status

#--------------------------------------------------

# 4. CSV File Processor with Exception Mapping
# Goal: Read a CSV file of numbers and calculate square roots.

# Some rows may contain invalid data (negative number or string)
#Example txt file:
# 25
# abc
# -16
# 49

# Requirements:
# Skip invalid rows but log them
# Use try-except inside a loop
# Use math.sqrt() and handle ValueError

#----------------------------------------------------

# 5. API Simulation with Random Failures
# Goal: Simulate calling an API that randomly fails with different exceptions.
# Simulate 5 requests using a loop
# Exceptions to simulate: TimeoutError, ConnectionError, ValueError
# Requirements:
# Use random.choice() to raise different errors
# Handle each with a specific except
# Count successful vs failed attempts
# Use finally to print status per request

#---------------------------------------------------------------

# ⭐ Bonus Challenge:
# For any 1 of the above, also:
# Create a log.txt file to append each success/failure with timestamp.
# Raise your own custom exception class (e.g., class InvalidEmail(Exception): pass)

#--------END OF EXCEPTION HANDLING TOPIC IN PYTHON-------------------------------------