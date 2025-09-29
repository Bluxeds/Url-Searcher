import requests
import time


class UrlSearcher:
    def __init__(self, url: str, path_to_keywords: str) -> None:
        try:
            self.url = url
            self.endpoint_url: str = url
            self.path_to_keywords: str = path_to_keywords
            self.path_to_keywords: str = path_to_keywords
            self._response = requests.get(self.url)
            self.response_code: int = self._response.status_code 
            self._search_keywords: list[str] = [] # Holds all the keywords to add to the end of the url
            self._endpoint_keyword_urls: list[str] = [] # Holds all the urls with a keyword on the endpoint
            self._subdomain_keyword_urls: list[str] = []
            self.valid_endpoint_urls_list: list[str] = []
            
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
        
        if self.endpoint_url[-1] != "/":
            self.endpoint_url = f"{self.endpoint_url}/"
        
        for keyword in self._search_keywords:
            endpoint_urls = f"{self.endpoint_url}{keyword}"
            self._endpoint_keyword_urls.append(endpoint_urls)
                                   
          
    def search_url_endpoints(self):
        self._add_keywords_to_endpoint_()
        counter = 0
        valid_url_counter = 0 
        seconds_counter = 0
        minutes_counter = 0
        
        for url in self._endpoint_keyword_urls:
            
            # Pauses every 100 searches to avoid timeout
            if counter % 100 == 0 and counter != 0:
                requests.get(url)
                counter += 1
                print("Pausing For 5 Seconds To Avoid Timeout")
                time.sleep(5)
            else:
                requests.get(url)
                counter += 1
             
                                
            if requests.get(url).status_code == 200:
                print(f"Found Valid Url | {url}")
                self.valid_endpoint_urls_list.append(url)
                valid_url_counter += 1
            else:
                pass
           
            print(f"[{counter}/{len(self._endpoint_keyword_urls)}] Endpoints Searched | Valid Urls Found: {valid_url_counter}")
            
            # Time Elapsed Counter 
            if seconds_counter < 60 and minutes_counter == 0:
                seconds_counter += 1
                print(f"Time Elapsed | {seconds_counter}s")
            elif seconds_counter == 60:
                seconds_counter = 0
                minutes_counter += 1
                print(f"Time Elapsed | {minutes_counter}m")
            else:
                seconds_counter += 1
                print(f"Time Elapsed | {minutes_counter}m {seconds_counter}s")
                                
     
            
            if counter == len(self._endpoint_keyword_urls):      
                non_duplicate_valid_urls = set(self.valid_endpoint_urls_list)
                non_duplicate_valid_urls_list = list(non_duplicate_valid_urls)
                  
                if valid_url_counter == 0:  
                    print(f"\nSearch Completed | {valid_url_counter} URLs found")      
                elif valid_url_counter != 0 and valid_url_counter < 2:
                    print(f"\nSearch Completed | {valid_url_counter} URL found")
                    for number, url in enumerate(non_duplicate_valid_urls_list, start=1):
                        print(f"Url {number}: {url}")                           
                else:
                    print(f"\nSearch Completed | {valid_url_counter} URLs found") 
                    for number, url in enumerate(non_duplicate_valid_urls_list, start=1):
                        print(f"Url {number}: {url}")
                        
                        

