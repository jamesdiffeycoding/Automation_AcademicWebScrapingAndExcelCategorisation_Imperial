# academic-abstract-scraper

# Background

Research papers often involve repetitive tasks, such as categorising online research papers by the presence or absence of **keywords** in their abstracts as part of **[Systematic Reviews](https://library-guides.ucl.ac.uk/systematic-reviews/what)**.

To save time, I created a script to automate this for an Excel file containing URLs to online research papers hosted by **The National Library of Medicine**.

I have found other websites, such as **Research Gate**, block my attempts to scrape the data.

# Project milestones

Basic functionality: ✔

✔ Import URLs from an Excel file.

✔ Successfully scrape one URL for its abstract.

✔ Adjust algorithm to correctly scrape for all URLs from the same website.

✔ Scan text for developer-defined keywords.

✔ Export analysis to a new 'output' Excel file.


Extensions: ✔

✔ Calculate abstract length with a 'abstract_length_concerns' variable to safeguard against errors identifying the paper's abstract.

✔ Input all data into spreadsheet: abstract information, any concerns, and keyword results.

✔ Apply colour formatting based on cell values.

✔ Add clear error handling and logs throughout the application.

✔ Add code that works for version 2 of their DOM structure (which they change to prevent malicious web scraping).


Next steps:

- Extract domain name automatically from a URL and create schema for accessing abstracts on other popular domains (e.g. Scopus and ResearchGate)

# Technologies used + reason

- Python is ideal for this kind of data extraction task where we are also happy working in a Command Line Interface.
- BeautifulSoup is useful for parsing HTML documents.
- OpenPandas is useful for importing and exporting XLSX spreadsheets.
- OpenPYXL is useful for conditional formatting in XLSX spreadsheets.
- ExcelViewer (extension) allows checking XLSX files within VSCode.

# Dev guidance

With Python and the packages installed installed, use the Command Line to run the script file

- Enter "python script.py" in the terminal.

Note, you can use various VSCode extensions to view xlsx files.
