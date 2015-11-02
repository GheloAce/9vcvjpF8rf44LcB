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
6. [ ] __Rework: Less User Input__.  Recode the Odoofier to run in '1 go' and not
    need the user to input the prefixes manually.
    1. I think you can do better with the input parameters validation and format.
        The help shown is a bit misleading.  Actually, if you are not a developer
        and you do not look at the source, it will be hard to understand how to
        use the tool.
    2. I think you should not expect any user input (like relational prefixes,
        just generate them in the tool, i.e. hardcode a string as a prefix. This
        should be enough.)
    3. Both files should be processed in one run. In the current version I need
        to run the tool twice.  Also, I can enter different prefixes for the users in
        the 1st and 2nd run, which I think will brake the Odoo import later.

        In a few words, you are processing the files in a detached manner,
        relying on the user to enter the correct prefixes.

        This way, the tool will work with any file or files, but the goal is to make
        a tool, which works for this particular case and is automated as much
        as possible.  There is no need to create a “generic” Odoo  “Odoofier” tool.

## Issues ##

1. What if Landlord wants to create a new Leaser user; or just consider changing the group Title.