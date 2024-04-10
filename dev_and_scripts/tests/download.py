# Early attempt to play with pysciebo, to download files programmatically


import os
from pysciebo import ScieboClient

url = "https://uni-bonn.sciebo.de"


# Login
client = ScieboClient(url, username, password)

# Upload a file to sciebo
#client.upload("/sciebo/file/path", "/local/file/path")

# Download a file from sciebo (local path is optional)
client.download("/AIfA-Bilder-17.12.2023", "/Volumes/Mars 2/AIfA-Bilder-17.12.2023")

# Delete a file from sciebo
#client.delete("/sciebo/file/path")
