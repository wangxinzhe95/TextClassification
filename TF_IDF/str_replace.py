def str_replace(str_source,char,*words):
    str_temp=str_source
    for word in words:
        str_temp=str_temp.replace(word,char)
    return str_temp 