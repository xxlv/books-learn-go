#!/usr/bin/python3

import json 

if __name__=="__main__":
    with open("../_build/result.json","r+") as f:
        body=f.read()
    result=json.loads(body)
    message=result["message"]
    with open("../_build/gens/{}.md".format((result["title"]).strip()),"w+") as f:
        f.write(message)
