# def get_first(list):
#     try:
#         return list[0]
#     except IndexError:
#         print('dsadsds')
#         return None


def get_first(list):
    if list:
        print('List is empty')
        return list[0]
    return None


def get_first(list):
    if list:
        return list[0]
    raise CustomIndexError('List is empty')


print(get_first([]))
