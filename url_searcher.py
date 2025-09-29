import requests
import time

# To Do: Make sure to add "/" at the end of the users link if it does not already have it

# To Do: Have it send a message when its completed and print all the valid links it found in the console

# To Do: Fix timeout issue

# To Do: Have the searcher pause for 5 seconds after reaching a counter number divisible by 100 with no remainder

# To Do: Convert the valid_urls_list to a set to remove any duplicates, then have it print all the valid URLS at the end once the search is finished

# To Do: Add time elaspsed from the time module

class UrlSearcher:
    def __init__(self, url: str, path_to_keywords: str) -> None:
        try:
            self.url: str = url
            self.path_to_keywords: str = path_to_keywords
            self.path_to_keywords: str = path_to_keywords
            self._response = requests.get(self.url)
            self.response_code: int = self._response.status_code 
            self._search_keywords: list[str] = [] # Holds all the keywords to add to the end of the url
            self._endpoint_keyword_urls: list[str] = [] # Holds all the urls with a keyword on the endpoint
            self.valid_urls_list: list[str] = [] 
            
        except Exception as error:
            print(f"Error: {error}")
   
    
    def _open_keyword_file_(self):
        try:
            self._response
            if (
                self.response_code == 200
            ):  # Only runs if the url provided from the user is valid
                with open(self.path_to_keywords, "r") as file:
                    for line in file:
                        self._search_keywords.append(
                            line.strip()
                        )  # .strip() removes the '\n' character at the end of each word  
                return self._search_keywords                        
            else:
                return print(
                    f"Error: Status Code {self.response_code} | Could not gain access to url"
                )
        except Exception as error:
            print(f"Error: {error}")    
      
      
    def _add_keywords_to_endpoint_(self):
        self._open_keyword_file_()
        for keyword in self._search_keywords:
            endpoint_urls = f"{self.url}{keyword}"
            self._endpoint_keyword_urls.append(endpoint_urls)
             
         
    def search_url_endpoints(self):
        self._add_keywords_to_endpoint_()
        counter = 0
        valid_url_counter = 0 
        
        for url in self._endpoint_keyword_urls:
            requests.get(url)
            counter += 1
            
            if requests.get(url).status_code == 200:
                print(f"Found Valid Url | {url}")
                self.valid_urls_list.append(url)
                valid_url_counter += 1
            else:
                pass                
             
            print(f"[{counter}/{len(self._endpoint_keyword_urls)}] Endpoints Searched | Valid Urls Found: {valid_url_counter}")
       
            
  
                



website = UrlSearcher( 
    "https://jsonplaceholder.typicode.com/",
    "C:/Users/bluxe/OneDrive/Desktop/Python Projects/api_endpoints.txt",
)

website.search_url_endpoints()
