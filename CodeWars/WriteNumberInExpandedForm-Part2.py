def expanded_form(num):
    integer_num = ' + '.join([e + ('0' * (len(str(num).split('.')[0]) - i - 1)) for i, e in
                              enumerate(str(num).split('.')[0]) if int(e) > 0])
    float_num = ' + '.join([e + '/' + '10' + '0' * i for i, e in enumerate(str(num).split('.')[1]) if int(e) > 0])
    return integer_num + ' + ' + float_num if str(num).split('.')[0] != '0' else float_num
