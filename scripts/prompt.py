#!/usr/bin/python3
import sys 
import os 

base_prompt_file="./base.prompt"
constrait_prompt_file="./constrait.prompt"

def build_prompt(need_gen_desc,format="json")->str:
    # 基本提示
    base_prompt=_load_file(base_prompt_file)
    constrait=_load_file(constrait_prompt_file)

    format_constrait_prompt="请确保返回的格式为{}".format(format)

    return "{}\n请确保严格遵守下面约束\n:{}\n{}\n我的问题如下:\n{}".format(base_prompt,constrait,format_constrait_prompt,need_gen_desc)


# ------------------------------------------------
# Privates 
# ------------------------------------------------

def _load_file(f):
    with open(f,"r+") as f:
        return f.read()



# 基于模版构建prompt 
if __name__=="__main__":
    if len(sys.argv)<2:
        print("请提供prompt!")
        os._exit(1)

    p=" ".join(sys.argv[1:])
    r=build_prompt(p)
    print(r)
