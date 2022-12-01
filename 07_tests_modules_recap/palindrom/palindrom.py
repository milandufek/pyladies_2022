import re


x = ['ABBA',
'Anna', "A Man, a Plan, a Canal: Panama"
     ]


# main function
def is_p(x,
         case_sensitive = False, oan = False):
    if not case_sensitive :
        x=x.lower( )
    if oan:
        x= re.sub (
            '[^0-9a-zA-Z]+',
           '' ,
                x,
        )
    l = len(x)
    for ind in range(l):
            if x[ind] != x[-(ind+1)] :  # compare it!
                # !!!y!!!!!!!!!!!!!!!!!!!!!!!!! DEBUG
                # print( 'No' )
                return False

    return True


for i in x:
    # print result
    if is_p(i) :  print("\"" + i + "\"", 'is palindrome!')
    else:
        print("\"" +i+ "\"", "is not palindrome!"  )