books = ["ULYSSES", "ANIMAL FARM", "BRAVE NEW WORLD", "ENDER'S GAME"]
the_dict = {}
for book in books:
    a = 0
    chardict = {}
    for letter in book:
        if letter not in chardict:
            chardict[letter] =1
            a +=1
        else:
            chardict[letter] += 1
            b = (len(book) + a)//2
            the_dict[book] = (len(book), a, b)
for key,value in the_dict.items():
  print(key,"->",value)

