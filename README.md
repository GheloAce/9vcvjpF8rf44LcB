# Ghelo's Examination #

## Objectives ##

1. [x] __CSV Fields__.  Customize Odoo in order to accommodate the data from the CSV files
2. [x] __Apartment Features__.  In Odoo, the user must be able to see the following:
    1. [x] Must be able to find a person by name or email
    2. [x] Must be able to see a list of all persons
    3. [x] Must be able to see a list of all apartments
    4. [x] Must be able to see which apartment(s) is(are) owned by a given person
    5. [x] Must be able to see the overall balance for a person
    6. [x] Must be able to see the total sum of sq. meters owned by a person
3. [x] __New Access Kinds__.  Provide 2 levels of access in Odoo:
    1. [x] A group of users who can see persons and apartments, but are not able 
        to see balance info data.
    2. [x] A group of users who can see persons, apartments, and balance info data
4. [x] __CSV Converter__.  Transform these “plain” CSV files into “Odoo” CSV
    format, which can be directly imported. Use Python to write a separate tool 
    (not part of Odoo), which just takes the CSV files as input and outputs 
    “Odoo” CSV files, which are ready for direct import in Odoo.
5. [x] __CSV Importation__.  Use the built-in Odoo import functionality to import the
    necessary data from your transformed CSV files

## Issues ##

1. What if Landlord wants to create a new Leaser user; or just consider changing the group Title.