import requests
from bs4 import BeautifulSoup
import pandas as pd


print("////////////////////////////////////////////////////// Running script.py //////////////////////////////////////////////////////")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# Keywords
keywords = ["technology", "mitigation", "financing", "adaptation", "financing", "climate"]
keyword_results = {keyword: [] for keyword in keywords}  # Initialize a dictionary for keyword results


# Make requests to the websites? Be careful of getting blocked.
make_requests = True

# Importing spreadsheet data
df = pd.read_excel('papers.xlsx', sheet_name='urls')  # You can specify the sheet name or index
urls = []
abstract_data = {
    "abstract_text": [],
    "abstract_length": [],
    "abstract_concerns": []
}

if 'URLS' in df.columns:
    for url in df['URLS']:
        urls.append(url)
else:
    print("The 'URLS' column does not exist in the DataFrame.")

if (make_requests):
    for index, url in enumerate(urls):
        try:
            # Send the request, check if successful, and parse content
            print(f"\n_________________________ NEW URL ({index}) - {url} ______________________________________________\n")
            page_to_scrape = requests.get(url, headers=headers, timeout=5)
            page_to_scrape.raise_for_status()  # Raises an HTTPError for bad responses (4xx, 5xx)
            soup = BeautifulSoup(page_to_scrape.content, 'html.parser')


            # NIH CONFIGURATION -----------------------------------------------------------------------------------------------------------------------------------
            # STRATEGY: find div that has class "tsec" and a child h2 element with text "Abstract"
            all_divs = soup.findAll("div")

            # FLAGS
            abstract_found = False 
            # step: loop through all divs
            for div in all_divs:
                # step: check if div has class "tsec"
                if ('class' in div.attrs):
                    div_classes = div.attrs['class']
                    if 'tsec' in div_classes:
                        # step: get all direct h2 children
                        all_h2s = div.findAll("h2", recursive=False) # recursive = False allows finding direct parents only, preventing duplicate prints
                        # Step: Find the first h2 with 'Abstract' or 'Summary'
                        first_h2 = next((h2 for h2 in all_h2s if 'Abstract' in h2.getText() or 'Summary' in h2.getText()), None) # A shorthand form of looping through the h2s

                        if first_h2:
                            abstract_found = True
                            div_text = div.getText().replace("Abstract", "").replace("Summary", "").strip().lower()

                            # update abstract info
                            abstract_data["abstract_text"].append(div_text)
                            abstract_data["abstract_length"].append(len(div_text))

                            if len(div_text) < 500:
                                abstract_data["abstract_concerns"].append("Short?")
                            elif len(div_text) > 2200:
                                abstract_data["abstract_concerns"].append("Long?")
                            else:
                                abstract_data["abstract_concerns"].append("OK")



                            # update keyword info
                            for keyword in keywords:
                                if keyword in div_text:
                                    print(f"Keyword '{keyword}' found ✅")
                                    keyword_results[keyword].append(True)
                                else:
                                    print(f"Keyword '{keyword}' NOT found ❌")
                                    keyword_results[keyword].append(False)

                            
                            break  # Exit the loop after processing the first found abstract


            if(abstract_found == False):
                print("!!! Cannot find parent div")
                for keyword in keywords:
                    keyword_results[keyword].append("ERROR - ABSTRACT NOT FOUND")


            print("\n")
            # END OF NIH CONFIGURATION -----------------------------------------------------------------------------------------------------------------------------------


        
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
        except requests.exceptions.RequestException as req_err:
            print(f"Error occurred: {req_err}")


# Exporting analysis
try: 
    for abstract in abstract_data:
        df[abstract] = abstract_data[abstract]

    for keyword in keywords:
        df[keyword] = keyword_results[keyword]

    df.to_excel('output.xlsx', index=False, sheet_name='urls')  # index=False to omit row indices
    print("Output file generated successfully.")
except Exception as e:
    print("Error exporting analysis")






    # EXAMPLE CODE
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