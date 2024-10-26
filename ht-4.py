some_list_1 = [1, 2, 3, 4, 5]
some_list_2 = [101, 102, 103, 104, 105]
print(some_list_1)
print(some_list_2)
print('=================')
some_list_1.append(6)
some_list_1.insert(0,0)
print(some_list_1)
some_list_2.append(106)
some_list_2.insert(0,100)
print(some_list_2)
print('=================')
some_list_1.extend(some_list_2)
print(some_list_1)
print('=====================')
some_dzen =u'''\nThe Zen of Python, by Tim Peters\n \nBeautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex.\nComplex is better than complicated.\nFlat is better than nested.\nSparse is better than dense.\nReadability counts.\nSpecial cases aren't special enough to break the rules.\nAlthough practicality beats purity.\nErrors should never pass silently.\nUnless explicitly silenced.\nIn the face of ambiguity, refuse the temptation to guess.\nThere should be one-- and preferably only one --obvious way to do it.\nAlthough that way may not be obvious at first unless you're Dutch.\nNow is better than never.\nAlthough never is often better than *right* now.\nIf the implementation is hard to explain, it's a bad idea.\nIf the implementation is easy to explain, it may be a good idea.\nNamespaces are one honking great idea -- let's do more of those!'''
print(some_dzen)
print('=========')
some_dzen_lines =some_dzen.count('\n')
some_dzen_is =some_dzen.count(' is ')
some_dzen_and =some_dzen.count(' and ')
some_dzen_or =some_dzen.count(' or ' )
print('lines',some_dzen_lines)
print('=========')
print('is', some_dzen_is)
print('and', some_dzen_and)
print('or', some_dzen_or)
some_dzen_dict = {"is":some_dzen_is, "and":some_dzen_and, "or":some_dzen_or or None}
print(some_dzen_dict)
some_dzen_isnot = some_dzen.replace( "is", "is not")
print(some_dzen_isnot)




