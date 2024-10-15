# academic-abstract-scraper

# Background

Research papers often involve repetitive tasks. Automation can help reduce time spent on menial tasks.

When conducting a **[Systematic Review](https://library-guides.ucl.ac.uk/systematic-reviews/what)** of literature, you may need to categorise a great number of papers.

One common way of categorising a large volume of papers is by the presence of various keywords in their abstracts.

These papers are likely to be stored in an Excel file as URLs, where the papers are hosted on various web pages.

To prevent time-consuming analsysis, an algorithm can be used to check each of the websites and scan the abstracts for keywords.

# Functionality achieved so far:

- Extract URLs from an Excel file into Python (completed)
- Configure a web scraping programme that can go to a list of URLs and scrape the text from the abstract of an article (completed)
- Return whether the articles contain various keywords (completed)
- Export the analysis to a new Excel file (completed)
- Add the abstract, abstract length, and any abstract length concerns that suggest human validation is worthwhile (completed)
- Automatically colour code the new Excel file (completed)

For the future:

- Identify schema for accessing abstracts on different domains (e.g. Scopus vs ResearchGate)
- Extract domain name automatically from a URL

# Technologies used

- Python is ideal for this kind of data extraction task where we are also happy working in a Command Line Interface.
- BeautifulSoup is useful for parsing HTML documents.
- OpenPandas is useful for importing and exporting XLSX spreadsheets.
- OpenPYXL is useful for conditional formatting in XLSX spreadsheets.
- ExcelViewer (extension) allows checking XLSX files within VSCode.

# Dev environment

With Python and the packages installed installed, use the Command Line to run the script file

- Enter "python script.py" in the terminal.

Note, you can use a VSCode extension to view xls files.
