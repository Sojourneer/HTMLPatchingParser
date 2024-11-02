[Alpha status. Not yet packaged]

# Purpose
Support programmatic modification of HTML files while preserving formatting, which is handy if your HTML files are under source control.

# Overview
This library leverages the SAX-style streaming HTMLParser to parse the HTML, and string operations on the underlying raw text to modify it.

An API for specifying string insertion or replacement operations that can be called from the HTMLParser tag handlers.
These changes can then be applied in reverse order to the raw text to obtain the desired modifications.

Examples are provided in the examples/ directory.
