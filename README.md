# Objectives #

1. __CSV Fields__.  Customize Odoo in order to accommodate the data from the CSV files  [done]
2. __Apartment Features__.  In Odoo, the user must be able to see the following:
    1. Must be able to find a person by name or email [done]
    2. Must be able to see a list of all persons [done]
    3. Must be able to see a list of all apartments [done]
    4. Must be able to see which apartment(s) is(are) owned by a given person [done, user tab]
    5. Must be able to see the overall balance for a person [done, user form]
    6. Must be able to see the total sum of sq. meters owned by a person [done]
3. __New Access Kinds__.  Provide 2 levels of access in Odoo:
    1. A group of users who can see persons and apartments, but are not able 
        to see balance info data.
    2. A group of users who can see persons, apartments, and balance info data
4. __CSV Converter__.  Transform these “plain” CSV files into “Odoo” CSV 
    format, which can be directly imported. Use Python to write a separate tool 
    (not part of Odoo), which just takes the CSV files as input and outputs 
    “Odoo” CSV files, which are ready for direct import in Odoo.
5. __CSV Importation__.  Use the built-in Odoo import functionality to import the 
    necessary data from your transformed CSV files
