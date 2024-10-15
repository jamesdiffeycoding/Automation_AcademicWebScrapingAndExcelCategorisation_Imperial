# academic-abstract-scraper

# Background

Research papers often involve repetitive tasks. Automation can help reduce time spent on menial tasks.

When conducting a **[Systematic Review](https://library-guides.ucl.ac.uk/systematic-reviews/what)** of literature, you may need to categorise a great number of papers.

One common way of categorising a large volume of papers is by the presence of various keywords in their abstracts.

These papers are likely to be stored in an Excel file as URLs, where the papers are hosted on various web pages.

To prevent time-consuming analsysis, an algorithm can be used to check each of the websites and scan the abstracts for keywords.

# Required steps

MVP

- Extract URLs from an Excel file into Python.
- Configure a web scraping programme that can go to the URL and scrape the text from the abstract of an article.
- Return whether the articles contain that keyword.

EXTENSION

- Return a dataset that shows the presence or absence of keywords for many articles.
- Export the analysis to a new Excel file.
- Identify schema for accessing abstracts on different domains (e.g. Scopus vs ResearchGate)
- Extract domain name automatically from a URL

# Why Python?

Python is ideal for this kind of data extraction task where we are also happy working in a Command Line Interface.

# Dev environment

With Python installed, use the Command Line to run the script file

- Enter "python script.py" in the terminal.
