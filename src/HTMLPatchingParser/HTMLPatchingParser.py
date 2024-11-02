from HTMLparser import HTMLParser
from collections import deque

class HTMLPatchingParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.lineOffsets = []
        self.changes = deque()

    def feed(self, text):
        self.text = text
        lines = text.split("\n")
        offset = 0
        for i in range(0,len(lines)):
            self.lineOffsets.append(offset)
            offset += len(lines[i]) + 1
        print(self.lineOffsets)
        super().feed(text)

    def line_pos_to_offset(self, line, pos):
        return self.lineOffsets[line-1] + pos - 1

    def addChange(self,change):
        self.changes.appendleft(change)

    def applyChanges(self):
        print(self.changes)
        t = self.text
        for x in list(self.changes):
            print(x)
            if x["action"] == "insert":
                atOffset = self.line_pos_to_offset(x["line"],x["pos"])
                t = t[0:atOffset] + x["text"] + t[atOffset:]
            if x["action"] == "replace":
                p1 = x["from"]
                p2 = x["to"] 
                t = t[0:p1] + x["text"] + t[p2:]
        return t
