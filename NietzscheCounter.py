import urllib, json, os, datetime
from unidecode import unidecode
import unicodecsv as csv
import time

nietzsche = 0

#Define Nietzsche counter:
def nietzscheCounter( str ):
    global nietzsche    
    if "Nietzsche" in str:
        nietzsche = nietzsche + 1
    if "nietzsche" in str:
        nietzsche = nietzsche + 1
    if "neech" in str:
        nietzsche = nietzsche + 1
    return;

#CHANGE THESE SETTINGS!
saveDirectory = '/home/nietzsche/Desktop/BeautifulSoup/'

#Get the 4chan board catalog JSON file and open it
url = "https://a.4cdn.org/lit/catalog.json"
response = urllib.urlopen(url)
threadCatalog = json.loads(response.read())

#There are eleven pages per board (0 - 10). Loop through each in order to access pages on each board.
i = 0
while i < 10:

    #loads content of current page:    
    currentPage = threadCatalog[i]['threads']
    
    #There are 15 threads per page (except for last page). Loop through each:
    j = 0
    while j < 15:    

        
        print("Page %s " %(i + 1))
        print("Thread %s" %(j + 1)) 
        print "\n"
    
        #Get json file for threads on each page. If there is less than 151 threads then an exception is raised
        try:
            url = "https://a.4cdn.org/lit/thread/" + str(currentPage[j]['no']) + ".json"
        except IndexError:
            print "\nEnd of threads"
            j = 15
            i = 10            
            break
        response = urllib.urlopen(url)
        individualThread = json.loads(response.read())
        
        #Increment through each comment in each thread. Post comments.
        k = 0
        for post in individualThread['posts']:
            if 'com' in individualThread['posts'][k]:
                commentText = individualThread['posts'][k]['com']
            else:
                commentText = "No Comment Text Provided\n"
            nietzscheCounter( commentText )            
            print commentText
            print "\n"
            k = k + 1
        j = j + 1

    #increment i (number of pages)    
    i = i + 1

#There are 151 threads total (1 thread on the 11th page). So we need to loop one last time:

#Print page and thread
print("Page %s " %(i + 1))
print("Thread 1") 
print "\n"

#Get page eleven json info:
currentPage = threadCatalog[i]['threads']

#We don't need to loop through each thread since there's only one on this page:
url = "https://a.4cdn.org/lit/thread/" + str(currentPage[0]['no']) + ".json"
response = urllib.urlopen(url)
individualThread = json.loads(response.read())

#Get information for last thread:
k = 0
for post in individualThread['posts']:
    if 'com' in individualThread['posts'][k]:
        commentText = individualThread['posts'][k]['com']
    else:
        commentText = "No Comment Text Provided\n"
    print commentText
    print "\n"
    k = k + 1

print("Nietzsche was mentioned %s times" % nietzsche) 
