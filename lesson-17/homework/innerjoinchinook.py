import sqlite3
import pandas as pd

# Load the chinook.db database
conn = sqlite3.connect('chinook.db')

# Perform an inner join between customers and invoices tables
query = '''
SELECT customers.CustomerId, customers.FirstName, customers.LastName, COUNT(invoices.InvoiceId) AS TotalInvoices
FROM customers
INNER JOIN invoices ON customers.CustomerId = invoices.CustomerId
GROUP BY customers.CustomerId
'''
df_inner_join = pd.read_sql_query(query, conn)

print(df_inner_join.head())

# Close the connection
conn.close()