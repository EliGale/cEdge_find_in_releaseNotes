import urllib.request
from tqdm import tqdm
import ssl

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

website_urls = [
    'https://www.cisco.com/c/en/us/td/docs/routers/sdwan/release/notes/17-10/sd-wan-rel-notes-xe-17-10.html',
    'https://www.cisco.com/c/en/us/td/docs/routers/sdwan/release/notes/xe-17-9/sd-wan-rel-notes-xe-17-9.html',
    'https://www.cisco.com/c/en/us/td/docs/routers/sdwan/release/notes/xe-17-8/sd-wan-rel-notes-xe-17-8.html',
    'https://www.cisco.com/c/en/us/td/docs/routers/sdwan/release/notes/xe-17-7/sd-wan-rel-notes-xe-17-7.html',
    'https://www.cisco.com/c/en/us/td/docs/routers/sdwan/release/notes/xe-17-6/sd-wan-rel-notes-xe-17-6.html',
    'https://www.cisco.com/c/en/us/td/docs/routers/sdwan/release/notes/xe-17-5/sd-wan-rel-notes-xe-17-5.html',
    'https://www.cisco.com/c/en/us/td/docs/routers/sdwan/release/notes/xe-17-4/sd-wan-rel-notes-xe-17-4.html',
    'https://www.cisco.com/c/en/us/td/docs/routers/sdwan/release/notes/xe-17-3/sd-wan-rel-notes-xe-17-3.html',
    'https://www.cisco.com/c/en/us/td/docs/routers/sdwan/release/notes/xe-17-2/ios-xe-sd-wan-re-notes-17-2.html',
    'https://www.cisco.com/c/en/us/td/docs/routers/sdwan/release/notes/xe-16-12/ios-xe-sd-wan-re-notes-16-12.html',
    'https://www.cisco.com/c/en/us/td/docs/routers/sdwan/release/compatibility/sdwan-device-compatibility.html',
    'https://www.cisco.com/c/en/us/products/routers/catalyst-8300-series-edge-platforms/interfaces-and-modules.html',
    'https://www.cisco.com/c/en/us/products/routers/catalyst-8200-series-edge-platforms/interfaces-and-modules.html',
    'https://www.cisco.com/c/en/us/products/routers/catalyst-8200-series-edge-ucpe/interfaces-and-modules.html',
    'https://www.cisco.com/c/en/us/products/routers/4000-series-integrated-services-routers-isr/relevant-interfaces-and-modules.html',
]

# Define the text string to search for
text_to_find = input("Enter the text to search for: ")


results = []
# Loop through each website URL and search for the text
for url in tqdm(website_urls, desc="Searching in release Notes"):
    with urllib.request.urlopen(url) as response:
        html = response.read()
        html = html.decode('utf-8')
        lines = html.split("\n")
        for i, line in enumerate(lines):
            if text_to_find in line:
                results.append("Found '{}' on line {} of {}".format(text_to_find, i+1, url))
                
# Print the results after all searches have finished
if results:
    print("\n\n\n===== Here are the results =====")
    print("\n".join(results))
    print("=====================================")

else:
    print("No results found.")
