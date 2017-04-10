#%%
NUMBER_LIST = '1234567890'

def chem_resolve(s):
    element_list = []
    char_content = ''
    it = iter(s.upper())
    mark = True
    try:
        c = next(it)
        while True:
            if c == '(':
                if char_content != '':
                    element_list.append(char_content)
                    char_content = ''
            elif c == ')':
                if char_content != '':
                    char_content+='$'
                    try:
                        while True:
                            c = next(it)
                            if c in NUMBER_LIST:
                                char_content += c
                            else:
                                element_list.append(char_content)
                                char_content = ''
                                mark = False
                                break
                    except StopIteration:
                        element_list.append(char_content)
                        char_content = ''
                        break
            else:
                char_content += c
            if mark:
                c = next(it)
            else:
                mark = True
    except StopIteration:
        pass
    if char_content != '':
        element_list.append(char_content)
    result = {}
    level = 0
    for ele in element_list:
        tmp= chem_resolve_core(ele)
        for k in tmp:
            if k in result:
                result[k] += tmp[k]
            else:
                result[k] = tmp[k]
    return result


def chem_resolve_core(s):
    result = {}
    element_list = []
    tmp = ''
    mark = False
    coef=1
    for i, c in enumerate(s):
        if c == '$':
            mark=True
            coef=int(s[i+1:])
            break
        elif c in NUMBER_LIST:
            tmp += c
        else:
            if tmp != '':
                element_list.append(int(tmp))
                tmp = ''
            element_list.append(c)
    if tmp != '':
        element_list.append(int(tmp))
    for i, x in enumerate(element_list):
        if isinstance(x, int):
            continue
        elif i < len(element_list) - 1 and isinstance(element_list[i + 1],
                                                      int):
            if x in result:
                result[x] += element_list[i + 1]
            else:
                result[x] = element_list[i + 1]
        else:
            if x in result:
                result[x] += 1
            else:
                result[x] = 1
    if mark:
        for k in result:
            result[k] *= coef
    return result

    


if __name__ == "__main__":
    s = '(c2(h20S3)3o(No)2)'
    print(chem_resolve(s))