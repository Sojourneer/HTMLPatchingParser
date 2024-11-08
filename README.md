[Alpha status. Not yet packaged]

# Purpose
Python library to support programmatic modification of HTML files while preserving formatting, which is handy if your HTML files are under source control.

# Overview
This library leverages the SAX-style streaming HTMLParser to parse the HTML, and string operations on the underlying raw text to modify it.

Modifications are queued from the HTMLParser tag handlers by calling addChange() with a string insertion or replacement operation.
These changes can then be applied in reverse order to the raw text by calling applyChanges() which returns the modified raw text.

Example(s) are provided in the examples/ directory.

# Note
A required minor change to return the position of the attributes is included in this copy of HTMLParser.
