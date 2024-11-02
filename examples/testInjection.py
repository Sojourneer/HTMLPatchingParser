#from html.parser import HTMLParser
from HTMLPatchingParser import HTMLPatchingParser
#from html.entities import name2codepoint
from collections import deque

class MyHTMLParser(HTMLPatchingParser):
    def __init__(self, options):
        super().__init__()
        self.foundL12N = False
        self.options = options

    def handle_starttag(self, tag, attrs):
        dAttrs = dict((key, {"value":value, "from":r[0], "to":r[1]}) for key, value, r in attrs)

        if tag == "script":
            if "src" in dAttrs and dAttrs["src"]["value"] == self.options["addScript"]:
                #print("Found script")
                self.foundL12N = True
                return
            
        if tag == "body":
            (line,offset) = self.getpos()
            length = len(self.get_starttag_text())
            if "onload" in dAttrs:
                onload = dAttrs["onload"] 
                value = onload["value"]
                if -1 == value.find("postLoad()"):
                    newValue = "try {{ {} }} finally {{ postLoad(); }}".format(value)
                    self.addChange({"action":    "replace",
                                         "from": onload["from"],
                                         "to":   onload["to"],
                                         "text": newValue
                                        })
            else:
                self.addChange({"action":"insert",
                                "text":  " onload='postLoad();' ",
                                "at":   self.getOffset() + len(tag) + 1})

    def handle_endtag(self, tag):
        if tag == "head" and self.foundL12N == False:
            self.addChange({"action":"insert",
                                "text":"<script src='{}'></script>".format(self.options["addScript"]),
                                "at":self.getOffset()
                            })

parser = MyHTMLParser({"addScript": "/scripts/injected.js"})

with open("test.htm", "r") as f:
    text = f.read()

parser.feed(text)
mtext = parser.applyChanges()

with open("test.htm", "w") as f:
    f.write(mtext)
