import io, time, json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs


def retrieve_html(url):
    """
    Return the raw HTML at the specified URL.

    Args:
        url (string): 

    Returns:
        status_code (integer):
        raw_html (string): the raw HTML content of the response, properly encoded according to the HTTP headers.
    """
    
    # Perform the GET request
    response = requests.get(url)
    
    # Extract the status code and text content from the response
    status_code = response.status_code
    raw_html = response.text
    
    return status_code, raw_html
    url = "https://www.forbes.com/sites/johnwerner/2024/01/08/museum-curation-in-the-age-of-ai/"
    status_code, html_content = retrieve_html(url)

def location_search_params(api_key, location, **kwargs):
    """
    Construct url, headers and url_params. Reference API docs (link above) to use the arguments
    """
    # What is the url endpoint for search?
    url = "https://api.yelp.com/v3/businesses/search"
    # How is Authentication performed?
    headers = {"Authorization": f"Bearer {api_key}"}
    # SPACES in url is problematic. How should you handle location containing spaces?
    url_params = {'location': location.replace(' ', '+')}
    # Include keyword arguments in url_params
    for key, value in kwargs.items():
        url_params[key] = value
    
    return url, headers, url_params
    api_key = read_api_key('yelp_api_key.txt')
    location = "New York City"  # Replace with your actual location
    url, headers, url_params = location_search_params(api_key, location, offset=0, limit=50)



def paginated_restaurant_search_requests(api_key, location, total):
    """
    Returns a list of tuples (url, headers, url_params) for paginated search of all restaurants
    Args:
        api_key (string): Your Yelp API Key for Authentication
        location (string): Business Location
        total (int): Total number of items to be fetched
    Returns:
        results (list): list of tuple (url, headers, url_params)
    """
    # HINT: Use total, offset and limit for pagination
    # You can reuse function location_search_params(...)
    results = []
    limit = 10  # Yelp API allows a maximum of 50, but we'll use 10 as per the instruction
    offset = 0

    while offset < total:
        url, headers, url_params = location_search_params(api_key, location, limit=limit, offset=offset, categories='restaurants')
        results.append((url, headers, url_params))
        offset += limit  # Increase offset by limit for next page

    return results
    
#     return 

def parse_api_response(data):
    """
    Parse Yelp API results to extract restaurant URLs.
    
    Args:
        data (string): String of properly formatted JSON.

    Returns:
        (list): list of URLs as strings from the input JSON.
    """
    
    # Convert the JSON string into a Python dictionary
    data_dict = json.loads(data)
    
    # Initialize an empty list to hold the URLs
    urls = []
    
    # Iterate through each business in the 'businesses' list
    for business in data_dict.get("businesses", []):
        # Extract the 'url' of the business and append it to the 'urls' list
        urls.append(business.get("url"))
    
    return urls


def parse_page(html):
    """
    Parse the reviews on a single page of a restaurant.
    
    Args:
        html (string): String of HTML corresponding to a Yelp restaurant

    Returns:
        tuple(list, string): a tuple of two elements
            first element: list of dictionaries corresponding to the extracted review information
            second element: URL for the next page of reviews (or None if it is the last page)
    """
    soup = BeautifulSoup(html,'html.parser')
    url_next = soup.find('link',rel='next')
    if url_next:
        url_next = url_next.get('href')
    else:
        url_next = None

    reviews = soup.find_all('div', itemprop="review")
    reviews_list = []

    for review in reviews:
        
        author = review.find('meta', itemprop="author").get("content")
        
        date = review.find('meta', itemprop="datePublished").get("content")
        
        description = review.find('p', itemprop="description").text
        
        rating = review.find('div', itemprop="reviewRating").find('meta', itemprop='ratingValue').get("content")

        review_dict = {
            'author': author,
            'rating': float(rating),
            'date': date,
            'description': description
        }
        reviews_list.append(review_dict)
        
    return reviews_list, url_next

# 4% credits
def extract_reviews(url, html_fetcher):
    """
    Retrieve ALL of the reviews for a single restaurant on Yelp.

    Parameters:
        url (string): Yelp URL corresponding to the restaurant of interest.
        html_fetcher (function): A function that takes url and returns html status code and content
        

    Returns:
        reviews (list): list of dictionaries containing extracted review information
    """
    reviews = []
    
    while url:  # Continue looping until there's no next page
        code, html = html_fetcher(url)  # Fetch the HTML for the current page
        if code == 200:  # Proceed only if the page was fetched successfully
            page_reviews, next_page_url = parse_page(html)  # Parse the page to get reviews and the next page URL
            reviews.extend(page_reviews)  # Add the current page's reviews to the total list
            url = next_page_url  # Update the URL for the next iteration to fetch the next page
        else:
            print(f"Failed to fetch page: {url} with status code: {code}")
            break  # Exit the loop if there's an error fetching the page
    
    return reviews