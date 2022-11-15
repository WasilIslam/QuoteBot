import json

from file_helper import *

FILE_NAME="./data/quotes.json"
f=open(FILE_NAME,encoding="utf-8")
data= json.load(f)


def read_quote():
    curr=read_curr()
    return dict(data["quotes"][curr]);

print(read_quote())
