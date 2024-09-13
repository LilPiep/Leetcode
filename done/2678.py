def countSeniors(details):
    c = 0
    for d in details:
        if int(d[11:13]) > 60:
            c += 1
    return c

print(countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"]))