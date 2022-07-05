

"""

1. Write a program to count the number of tables in table.html.

2. Write a program that combines all the information from tables with the class species into a single CSV file.

3. Write a program that produces a plain-text table of contents, using indentation to show nesting:

"""

import pandas as pd
from bs4 import BeautifulSoup

with open("table.html", "r") as reader:
    doc = BeautifulSoup(reader, "html.parser")

# Finding the number of tables in table.html
table = doc.find_all("table")
print(len(table))
# 3

# Combines information from table class species
species_table = doc.find_all("table", attrs={"class": "species"})
# Always define a variable, set breakpoints to see intermediate values
data = []
for table in species_table:
    lns = table.find_all("tr")
    for ln in lns:
        common = ln.contents[0].text
        scientific = ln.contents[1].text
        if common != "Common" and scientific != "Scientific":
            # In good html, there's th, but there's thead and tbody (this is done in tidyverse)
            data.append([common, scientific])
            print(f"{common},{scientific}")

data = pd.DataFrame(data)
data.columns = ['Common', 'Scientific']
data.to_csv("species_table.csv")

# Table of contents
headings = ["h1", "h2", "h3"]
for tags in doc.find_all(headings):
    if tags.name == 'h1':
        print(tags.text.strip())
    elif tags.name == 'h2':
        print("\t"+tags.text.strip())
