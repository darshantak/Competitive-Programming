import camelot
import pandas as pd
pdf=camelot.read_pdf("test.pdf")
print(pdf[0])
first_table=pdf[0]
#translates into pandas df
csv_file=first_table.to_csv("first_table.csv")