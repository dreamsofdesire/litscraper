# litscrape
A simple python utility for scraping story text from literotica story url or extracting all the stories of any literotica author and and exporting them as txt file.  
It supports extracting multiple pages in the same story and exports single txt file.  
It supports new literotica website changes, working as tested on 18th-Dec-2021.  

Requirements - python>3.2, beautifulsoup library, jupyter notebook (optional)
  
Instructions  
Run litscrape.ipynb or litscrape.py and provide literotica story url as input   
Story url format as input example- https://www.literotica.com/s/oops-sorry-dean-flashes-wife-1   
Run by using command - python litscrape.py  

For scraping all the stories of an author use extractAuthor/authscraper.ipynb  or extractAuthor/authscraper.py utility   
Author url format as input example- https://www.literotica.com/stories/memberpage.php?uid=1253141&page=submissions   
Run by using command - python extractAuthor/authscraper.py  