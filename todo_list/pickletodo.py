import sys
import pickle
#PICKLING is a good way to convert complex data into binary data and put it into a txt or any file extension in an efficient manner
class ToDo:
    def _init(self,title,important,category='normal'):
        self.title=title
        self.important=important
        self.category=category

file = open('pickle_data.txt','r')
todos = pickle.load(file)
file.close()

# Add Todo
def add_todo():
    todo=sys.argv[2]
    try:
        todos.append(f'{todo}'+"\n")
    except Exception as e:
        print('******you encountered the following error******')
        print(e)
    
#remove Todo
def rm_todo():
    try:
        todo=int(sys.argv[2])-1
        del(todos[todo])
    except Exception as e:
        print('******you encountered the following error trying to remove something******')
        print(e)

# Print Commands
#print(f"To view ToDos:\n{sys.argv[0]}")
#print(f"\nTo add a ToDo:\n{sys.argv[0]} add \"Clean Room\"\n")
#print(f"To remove or complete ToDo:\n{sys.argv[0]} remove 2\n")



#save file
if len(sys.argv) >=3 and sys.argv[1] == 'add': 
    add_todo()
elif len(sys.argv) >=3 and sys.argv[1] == 'remove':
    rm_todo()
else:
    print("Sorry, you've gotta put an add/remove in the command line. ")
file = open('pickle_data.txt','wb')
pickle.dump(todos,file)
file.close()

# Print List
file = open('pickle_data.txt','r')
lines = file.readlines()
if len(todos)==0:
    print('you have nothing to do yet! :)')
else:
    print("\nHere's your ToDo list \n")
    for x in range(len(lines)):
        print(f'{x+1}. {lines[x]}')
file.close()


#PICKLING OBJECTS IN PYTHON
def do_pickle():
    age =24
    #when you open the file make sure to add the b to do binary
    file = open('text.txt','wb')
    #dump the pickled object into the file
    pickle.dump(age,file)
    file.close()

def unpickle():
    file = open('text.txt','rb')
    #put the pickle object into a variable
    new_age = pickle.load(file)
    file.close()
    print(new_age)