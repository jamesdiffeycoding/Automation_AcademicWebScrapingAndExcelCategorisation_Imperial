import requests
from bs4 import BeautifulSoup

print("------ Running script.py ------")

# Send a GET request to ResearchGate
url = "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8499625/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

try:
    # Send the request
    page_to_scrape = requests.get(url, headers=headers, timeout=5)

    # Check if the request was successful
    page_to_scrape.raise_for_status()  # Raises an HTTPError for bad responses (4xx, 5xx)

    # Parse the content of the page
    soup = BeautifulSoup(page_to_scrape.content, 'html.parser')
    
    # Print all <div> elements (for debugging)
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


    # Print all <p> elements (for debugging)
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

    # NIH --- 
    all_divs = soup.findAll("div")
    for div in all_divs:

        # CHECK IDs
        if 'id' in div.attrs:
            id_given = div.attrs['id']
            if (id_given == "abstract-a.c.b.q"):
                abstract_text = div.get_text().replace("Abstract", "").strip() # remove Abstract Heading
                print(abstract_text)



except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.ConnectionError as conn_err:
    print(f"Connection error occurred: {conn_err}")
except requests.exceptions.Timeout as timeout_err:
    print(f"Timeout error occurred: {timeout_err}")
except requests.exceptions.RequestException as req_err:
    print(f"Error occurred: {req_err}")
