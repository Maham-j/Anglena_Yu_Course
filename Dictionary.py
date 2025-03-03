person = { 'name':'maham','gender':'female','age':19 }
person .get (input() .lower() ,'invalid' )








person = { 'name':'maham','gender':'female','age':19 }
key = input ('What info you want?') .lower()
result = person.get( key,'This info is not avaliable' )
print (result)





# Dictionary and list within using for loop to separate in

post_blog = {'python' : ['maham' , 'zeenat' , 'ahsan'] , 'java' : ['faiza' , 'iqra'] }
for post in post_blog:
    print ('about ', post)
    for posts in post_blog [post] :
        print (posts)