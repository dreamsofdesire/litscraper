Modified authscraper.py to be able to pass it the authurl via the command line.
I also added a check to see if fullfilename already exists to cut down on
re-transferring any stories that have already been downloaded.

Add option for a save directory passed as argv 2

Added meta keywords from story page at the end of the file
WIP -  right now this is the raw HTML tag - need to work on splitting it out
based on author/story name
