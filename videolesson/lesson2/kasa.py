source = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
target = 'd e f g h i j k l m n o p q r s t u v w x y z a b c'
information = input('input information')
while information != 'end':
    encryption = ''
    for i in information:
        t = target[source.find(i)].lower()
        encryption += t
    print(encryption)
    information = input('input information')
