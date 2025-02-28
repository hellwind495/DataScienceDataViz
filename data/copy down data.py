import urllib.request
url = "https://github.com/dutangc/CASdatasets/raw/refs/heads/master/data/"
file_names = ["fremotor1freq0304a.rda", "fremotor1sev0304a.rda", "fremotor1prem0304a.rda"]
for file_name in file_names:
    urllib.request.urlretrieve("%s%s" % (url, file_name), file_name)