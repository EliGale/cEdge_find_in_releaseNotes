# verify_releaseNotes_cEdges
This is a Python script that help you to verify across all the cEdge release notes and look for a specific word. 

This is helpful to verify where a Module was initially supported.

These are the current websites that this script will check

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
    'https://www.cisco.com/c/en/us/products/routers/catalyst-8300-series-edge-platforms/interfaces-and-modules.html#serial-wan-interface',


## Requirements
You will need the python library tqdm. You can install it using the command
```
pip install tqdm
```

## How to Use this script. 
Run the script and you will be asked to prompt the word you are looking for and it will show you in which url the word was found

Example: 

```
Enter the text to search for: NIM-2GE-CU-SFP
Searching in release Notes: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 15/15 [00:10<00:00,  1.46it/s]



===== Here are the results =====
Found 'NIM-2GE-CU-SFP' on line 10621 of https://www.cisco.com/c/en/us/td/docs/routers/sdwan/release/notes/xe-17-3/sd-wan-rel-notes-xe-17-3.html
Found 'NIM-2GE-CU-SFP' on line 1124 of https://www.cisco.com/c/en/us/products/routers/4000-series-integrated-services-routers-isr/relevant-interfaces-and-modules.html
=====================================
```

