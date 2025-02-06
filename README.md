# Automated web scraping tool

Research papers often involve repetitive tasks, such as categorising online research papers by the presence or absence of **keywords** in their abstracts as part of **[Systematic Reviews](https://library-guides.ucl.ac.uk/systematic-reviews/what)**. To save time, I created a script to automate this for an Excel file containing URLs to online research papers hosted by **The National Library of Medicine (NLM)**. Note that schemas need to be made for scraping data from different academic journal websites and some block any attempt to do so. 

# Technologies used

- Python is ideal for this kind of data extraction task where we are also happy working in a Command Line Interface.
- BeautifulSoup is useful for parsing HTML documents.
- OpenPandas is useful for importing and exporting XLSX spreadsheets.
- OpenPYXL is useful for conditional formatting in XLSX spreadsheets.
- ExcelViewer (extension) allows checking XLSX files within VSCode.

# Functionality completed

- Import URLs from an Excel file. ✔
- Correctly scrape for all URLs from the NLM. ✔
- Scan text for developer-defined keywords. ✔
- Export analysis to a new 'output' Excel file. ✔ 
- Calculate abstract length with a 'abstract_length_concerns' variable to safeguard against errors identifying the paper's abstract. ✔
- Input all data into spreadsheet: abstract information, any concerns, and keyword results. ✔
- Apply colour formatting based on cell values. ✔
- Add clear error handling and logs throughout the application. ✔
- Add code that works for the two alternating versions of their DOM structure (which they change alternate between to prevent data-stealing). ✔

For the future

- Include automatic detection of which schema is being used
- Extract domain name automatically from a URL and create schema for accessing abstracts on other popular domains (e.g. Scopus and ResearchGate)

# Run this project yourself

- Requires Python and packages installed
- Enter "python script.py" in you terminal.
- Download and xlsx viewer in VSCode extensions library if desired.
- Note you must not be editing past 'output' files while running the script.
