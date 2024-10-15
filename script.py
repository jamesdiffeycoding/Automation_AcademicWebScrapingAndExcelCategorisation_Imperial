# IMPORTS ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import PatternFill, Font


print("////////////////////////////////////////////////////// Running script.py //////////////////////////////////////////////////////")

# CONFIGURATION - change me! ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
timeout_seconds = 10
keywords = ["climate", "environment", "sustainability", "anxiety", "sensitivity", "mitigation"]
min_abstract_char_length = 450
max_abstract_char_length = 2500
output_file_name = 'output.xlsx'
input_file_name = 'papers.xlsx'
green_font = Font(color="55C233")
red_font = Font(color="FF0000")


# IMPORT SPREADSHEET DATA ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
df = pd.read_excel(input_file_name, sheet_name='urls')  # You can specify the sheet name or index
# ... DEFINE URLS ////////////////////////////////////
urls = []
if 'URLS' in df.columns:
    for url in df['URLS']:
        urls.append(url)
else:
    print("The 'URLS' column does not exist in the DataFrame.")
# ... KEYWORD AND ABSTRACT PLACEHOLDERS ///////////////
abstract_data = {
    "abstract_text": [],
    "abstract_length": [],
    "abstract_concerns": []
}
keyword_results = {keyword: [] for keyword in keywords}  # Initialize a dictionary for keyword results


# LOOPING THROUGH EACH URL REQUEST ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
for index, url in enumerate(urls):
    try:
        # GENERIC REQUEST AND PASSING///////////////////////////////////////
        print(f"\n_________________________ NEW URL ({index}) - {url} ______________________________________________\n")
        page_to_scrape = requests.get(url, headers=HEADERS, timeout=timeout_seconds)
        page_to_scrape.raise_for_status()  # Raises an HTTPError for bad responses (4xx, 5xx)
        soup = BeautifulSoup(page_to_scrape.content, 'html.parser')


        # DATA HANDLING FOR ARTICLES ON ---- NIH ----- WEBSITE /////////////////////////////////////////////////////////////////////////////////////////////////////
        # NIH STRATEGY: find div that has class "tsec" and a child h2 element with text "Abstract"
        all_divs = soup.findAll("div")
        abstract_found = False # flag
        # step: loop through all divs
        for div in all_divs:
            # step: check if div has class "tsec"
            if ('class' in div.attrs):
                div_classes = div.attrs['class']
                if 'tsec' in div_classes:
                    # step: get all direct h2 children
                    all_h2s = div.findAll("h2", recursive=False) # recursive = False allows finding direct parents only, preventing duplicate prints
                    # step: Find the first h2 with 'Abstract' or 'Summary'
                    first_h2 = next((h2 for h2 in all_h2s if 'Abstract' in h2.getText() or 'Summary' in h2.getText()), None) # A shorthand form of looping through the h2s

                    if first_h2:
                        abstract_found = True
                        div_text = div.getText().replace("Abstract", "").replace("Summary", "").strip().lower()

                        # update abstract info
                        abstract_data["abstract_text"].append(div_text)
                        abstract_data["abstract_length"].append(len(div_text))

                        if len(div_text) < min_abstract_char_length:
                            abstract_data["abstract_concerns"].append("Short - check manually")
                        elif len(div_text) > max_abstract_char_length:
                            abstract_data["abstract_concerns"].append("Long - check manually")
                        else:
                            abstract_data["abstract_concerns"].append("Length: OK")

                        # update keyword info
                        for keyword in keywords:
                            if keyword in div_text:
                                print(f"Keyword '{keyword}' found ✅")
                                keyword_results[keyword].append("present")
                            else:
                                print(f"Keyword '{keyword}' NOT found ❌")
                                keyword_results[keyword].append("missing")

                        
                        break  # Exit the loop after processing the first found abstract


        if(abstract_found == False):
            print("!!! Cannot find parent div")
            for keyword in keywords:
                keyword_results[keyword].append("ERROR - ABSTRACT NOT FOUND")
            for abstract in abstract_data:
                abstract_data[abstract].append("ERROR - ABSTRACT NOT FOUND")


        # END OF DATA HANDLING FOR ARTICLES ON ---- NIH ----- WEBSITE /////////////////////////////////////////////////////////////////////////////////////////////////////


    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Error occurred: {req_err}")



# Exporting analysis ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
try: 
    # Update DataFrame //////////////////////////////////////////////////////////
    for abstract in abstract_data:
        df[abstract] = abstract_data[abstract]
    for keyword in keywords:
        df[keyword] = keyword_results[keyword]

    # Export to Excel ////////////////////////////////////////////////////////////
    df.to_excel(output_file_name, index=False, sheet_name='urls')  # index=False to omit row indices
    print("Export to Excel successful.")

except Exception as e:
    print("Error exporting analysis - do you have the file open?\n", e)





# Apply formatting ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
try:
    workbook = load_workbook(output_file_name)
    sheet = workbook.active

    # Apply styles based on the values ////////////////////////////////////////////////////////
    for row in range(2, len(df) + 2):  # Start from the second row to skip the header
        # Check abstract concerns ////////////////////////////////////////////////////////
        abstract_concern_cell = sheet[f"D{row}"]  # Assuming abstract concerns are in column D
        if "OK" in str(abstract_concern_cell.value):
            abstract_concern_cell.font = green_font
        elif str(abstract_concern_cell.value.startswith("Short")) or abstract_concern_cell.value.startswith("Long"):
            abstract_concern_cell.font = red_font

        # Check keywords ////////////////////////////////////////////////////////
        for col in range(4, len(keywords) + 4):  # Assuming keywords start from column D
            keyword_cell = sheet.cell(row=row, column=col)
            if keyword_cell.value == "present":
                keyword_cell.font = green_font
            elif keyword_cell.value == "missing":
                keyword_cell.font = red_font

    # Save the workbook ////////////////////////////////////////////////////////
    workbook.save(output_file_name)
    print("Colour code successful.\n")

except Exception as e:
    print("Error colour coding the analysis\n", e)













# EXAMPLE CODE FOR BEAUTIFUL SOUP
    # Example code: how to print all div elements, classes and ids
        # all_divs = soup.findAll("div")
        # for div in all_divs:
        #     # CHECK CLASSES
        #     if 'class' in div.attrs:
        #         class_given = div.attrs['class']
        #         print("class:", class_given)

        #     # CHECK IDs
        #     if 'id' in div.attrs:
        #         id_given = div.attrs['id']
        #         print("id:", id_given)

    # Example code: how to print all p elements, classes and ids
        # all_ps = soup.findAll("p")
        # for p in all_ps:
        #     # CHECK CLASSES
        #     if 'class' in p.attrs:
        #         class_given = p.attrs['class']
        #         print("class:", class_given)

        #     # CHECK IDs
        #     if 'id' in p.attrs:
        #         id_given = p.attrs['id']
        #         print("id:", id_given)
