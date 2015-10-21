# bookmarks-html2markdown
Convert a Chrome/IE/Firefox formatted bookmarks list to Markdown tables for easier management and handling.

PHASE 1
  - Fault Tolerant
  - Blindly parse a Chrome Bookmarks export file looking for H3 to indicate folders
  - and A tags with HREF attributes for URLs to add to bookmarks.


PHASE 2
	- Visit each URL to identify if it is dead/deprecated/broken.
	- Strip out invalid links and only add valid links.
	- Leverage or extend the following code snippet
	    t = lxml.html.parse(url)
	    print t.find(".//title").text

