def make_one_xpath(loc):
    loc_list = loc.split(",")
    key_index = 0
    value_index = 1
    option_index = 2
    result = ""
    if len(loc_list) == 3:
        if loc_list[option_index] == "1":
            result = "contains(@{},'{}')".format(loc_list[key_index], loc_list[value_index])
        else:
            result = "@{}='{}'".format(loc_list[key_index], loc_list[value_index])
    elif len(loc_list) == 2:
        result = "@{}='{}'".format(loc_list[key_index], loc_list[value_index])
    return result


def make_xpath(loc):
    result = ""
    if isinstance(loc, str):
        # 如果是正常的xpath：
        if loc.startswith("//"):
            return loc
        # 如果是自己的格式：
        else:
            return "//*[]".format(make_one_xpath(loc))
    else:
        for i in loc:
            result += (make_one_xpath(i) + "and")
        return "//*[{}]".format(result.rstrip("and"))


def main():
    loc = ["text,设置,0", "text,设置,1", "text,设置", "text,设置,1"]
    # loc = "text,设置,0"
    # loc = "//*[@text='设置']"
    a = make_xpath(loc)
    print(a)


main()
