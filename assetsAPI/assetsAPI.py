import urllib3
import requests

# disable SSL certificate warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class RidgeAssetsAPI:
    """
    Class to encapsulate the asset api functionalities of RidgeBot

    Methods
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
    __split_bytes(x)
        Helper function returns byte conversion of parameter

    handle_getHost(size, page, search, asc_field, asc)

    handle_deleteHost(ips)

    handle_updateHost(host_name, ip, os, owner, tags)

    handle_addSite(ip, overwrite, service, site, tags, title)

    handle_deleteSite(sites):

    handle_updateSite(ip, owner, service, site, tags, title):

    handle_getUser():

    handle_getSites(doc_type, size, page, search, asc_field, asc):

    """
    def __init__(self, RidgeBotAPIURL, RidgeBotAuthToken): 
        self.RidgeBotAPIURL = RidgeBotAPIURL
        Content_Type = "application/json"
        self.RidgeBotAPIHeader = {'Authorization': RidgeBotAuthToken, 'Content-Type': Content_Type}

    def __split_bytes(self, x):
        try:
            return int(x)
        except ValueError:
            return x   

    def handle_getHost(self, size, page, search=None, asc_field=None, asc=None):
        # merge the input size and page to the request URL
        RidgeBotRequestURL = self.RidgeBotAPIURL + "/assets/host" + "?" + "size=" + size + "&page=" + page 
        
        # add optional fields to request URL if fields are non-null
        if search:
            RidgeBotRequestURL += "&search=" + search
        if asc_field:    
            RidgeBotRequestURL += "&asc_field=" + asc_field
        if asc:    
            RidgeBotRequestURL += "&asc=" + asc

        # get response from API about getHost
        getHostResponse = requests.get(url = RidgeBotRequestURL, headers = self.RidgeBotAPIHeader, verify = False)

        # if status code is not 200 which means error occur, the function will exist immediately
        if getHostResponse.status_code != 200 or getHostResponse.json()["code"] == 400:
            print("\nPossible RidgeBot authentication user error.\n")
            print("Server response: " + getHostResponse.json()["message"]["key"])
            exit()

        # getHost raw content from response
        getHost_content = getHostResponse._content

        #translate the raw content from bytes to String with utf-8 encode
        strGetHost = str(getHost_content, encoding = "utf-8")
        
        #convert to list by spliting the Host information from String format raw content
        splitedStrGetHost = ([self.__split_bytes(x) for x in strGetHost.split(',"tags":')])    

        return splitedStrGetHost

    def handle_deleteHost(self, ips):
        # add related API postfit to the request URL
        RidgeBotRequestURL = self.RidgeBotAPIURL + "/assets/host/delete"

        # use received list of ips to create json object for request
        deleteHostPayload = {"ips": ips}

        # post the client request and get response from server about API 
        deleteHostResponse = requests.post(RidgeBotRequestURL, headers = self.RidgeBotAPIHeader, verify = False, json = \
            deleteHostPayload)
        
        # if status code is not 200 which means an error occured, the function will exit immediately
        if deleteHostResponse.status_code != 200 or deleteHostResponse.json()["code"] == 400:
            print("\nPossible RidgeBot authentication user error or invalid input.\n")
            print("Server response: " + deleteHostResponse.json()["message"]["key"])
            exit()
        
        return deleteHostResponse._content
        
    def handle_updateHost(self, host_name, ip, os, owner, tags):
        # add related API postfit to the request URL
        RidgeBotRequestURL = self.RidgeBotAPIURL + "/assets/host/update"
        
        # create json payload using inputted parameters
        updateHostPayload = {"hostname": host_name, "ip": ip, "os": os, "owner": owner, "tags": tags}

        # post the client request and get response from server about API 
        updateHostResponse = requests.post(RidgeBotRequestURL, headers = self.RidgeBotAPIHeader, verify = False, json = \
            updateHostPayload)

        # if status code is not 200 which means an error occured, the function will exit immediately
        if updateHostResponse.status_code != 200 or updateHostResponse.json()["code"] == 400:
            print("\nPossible RidgeBot authentication user error or invaild input.\n")
            print("Server response: " + updateHostResponse.json()["message"]["key"])
            exit()

        return updateHostResponse._content

    def handle_addSite(self, ip, overwrite, service, site, tags, title):
        # add related API postfit to the request URL
        RidgeBotRequestURL = self.RidgeBotAPIURL + "/assets/site/add"

        # create json payload using inputted parameters
        addSitePayload = {"ip": ip, "overwrite": overwrite, "service": service, "site": site, \
            "tags": tags, "title": title}

        # post the client request and get response from server about API 
        addSiteResponse = requests.post(RidgeBotRequestURL, headers = self.RidgeBotAPIHeader, verify = False, \
            json = addSitePayload)
        
        # if status code is not 200 which means an error occured, the function will exit immediately
        if addSiteResponse.status_code != 200 or addSiteResponse.json()["code"] == 400:
            print("\nPossible RidgeBot authentication user error or invaild input.\n")
            print("Server response: " + addSiteResponse.json()["message"]["key"])
            exit()
        
        return addSiteResponse._content

    def handle_deleteSite(self, sites):
        # add related API postfit to the request URL
        RidgeBotRequestURL = self.RidgeBotAPIURL + "/assets/site/delete"
        
        # create json payload using inputted parameters
        deleteSitePayload = {"sites": sites}

        # post the client request and get response from server about API 
        deleteSiteResponse = requests.post(RidgeBotRequestURL, headers = self.RidgeBotAPIHeader, verify = False, \
            json = deleteSitePayload)
    
        # if status code is not 200 which means an error occured, the function will exit immediately
        if deleteSiteResponse.status_code != 200 or deleteSiteResponse.json()["code"] == 400:
            print("\nPossible RidgeBot authentication user error or invaild input.\n")
            print("Server response: " + deleteSiteResponse.json()["message"]["key"])
            exit()

        return deleteSiteResponse._content

    def handle_updateSite(self, ip, owner, service, site, tags, title):
        # add related API postfit to the request URL
        RidgeBotRequestURL = self.RidgeBotAPIURL + "/assets/site/update"

        # create json payload using inputted parameters
        updateSitePayload = {"ip": ip, "owner": owner, "service": service, "site": site, \
            "tags": tags, "title": title}
        
        # post the client request and get response from server about API 
        updateSiteResponse = requests.post(RidgeBotRequestURL, headers = self.RidgeBotAPIHeader, verify = False, \
            json = updateSitePayload)

        # if status code is not 200 which means an error occured, the function will exit immediately
        if updateSiteResponse.status_code != 200 or updateSiteResponse.json()["code"] == 400:
            print("\nPossible RidgeBot authentication user error or invaild input.\n")
            print("Server response: " + updateSiteResponse.json()["message"]["key"])
            exit()

        return updateSiteResponse._content

    def handle_getUser(self):
        # add related postfit to the request URL
        RidgeBotRequestURL = self.RidgeBotAPIURL + "/assets/user"

        # get response from server about API 
        getUserResponse = requests.get(RidgeBotRequestURL, headers = self.RidgeBotAPIHeader, verify = False)

        # if status code is not 200 which means an error occured, the function will exit immediately
        if getUserResponse.status_code != 200 or getUserResponse.json()["code"] == 400:
            print("\nPossible RidgeBot authentication user error.\n")
            print("Server response: " + getUserResponse.json()["message"]["key"])
            exit()

        return getUserResponse._content

    def handle_getSites(self, doc_type, size, page, search=None, asc_field=None, asc=None):
        # merge the input size and page to the request URL
        RidgeBotRequestURL = self.RidgeBotAPIURL + "/assets/" + doc_type + "?" + "size=" + size + "&page=" + page
        
         # add optional fields to request URL if fields are non-null
        if search:
            RidgeBotRequestURL += "&search=" + search
        if asc_field:
            RidgeBotRequestURL += "&asc_field=" + asc_field
        if asc:   
            RidgeBotRequestURL += "&asc=" + asc

        # get response from server about API 
        getSitesResponse = requests.get(RidgeBotRequestURL, headers = self.RidgeBotAPIHeader, verify = False)

        # if status code is not 200 which means an error occured, the function will exit immediately
        if getSitesResponse.status_code != 200 or getSitesResponse.json()["code"] == 400:
            print("\nPossible RidgeBot authentication user error.\n")
            print("Server response: " + getSitesResponse.json()["message"]["key"])
            exit()

        # getHost raw content from response
        getSites_content = getSitesResponse._content

        # translate the raw content from bytes to String with utf-8 encode
        strGetSites = str(getSites_content,encoding = "utf-8")
        
        #convert to list by spliting the Host information from String format raw content
        splitedStrGetHost = ([self.__split_bytes(x) for x in strGetSites.split('},')])
        
        return splitedStrGetHost

def __main(): 
    RidgeBotAPIURL = "https://bot58.ridgesecurity.ai/api/v4"
    RidgeBotAuthToken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJrZW4iLCJpYXQiOjE2NTcwNDU3NDEsImRhdGEiOnsidXNlcm5hbWUiOiJqZWZmcmV5IiwiaXNfbmV2ZXJfZXhwaXJlIjp0cnVlLCJpZCI6NSwic29mdHdhcmVfdGltZSI6MTY1MzU1MDE1NS4zNzg1NzQ4LCJyb2xlX2lkIjoxfSwiZXhwIjo0Nzc5MTA5NzQxfQ.5I5kRxZoCJJ1JhZ-bhmkLTqFdZOBHCUQ-POm9XGfhzo"
    # RidgeBotAdminAuthToken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJrZW4iLCJpYXQiOjE2NTM2ODU4MTcsImRhdGEiOnsidXNlcm5hbWUiOiJhZG1pbiIsImlzX25ldmVyX2V4cGlyZSI6dHJ1ZSwiaWQiOjEsInNvZnR3YXJlX3RpbWUiOjE2NTM1NTAxNTUuMzc4NTc0OCwicm9sZV9pZCI6bnVsbH0sImV4cCI6NDc3NTc0OTgxN30.op9FbAjYEpFT4DtE-e50FzWSnU-3TKtCtRt77aRWkPI"

    ridgeAPI = RidgeAssetsAPI(RidgeBotAPIURL, RidgeBotAuthToken)

if __name__ == "__main__":
    __main()
