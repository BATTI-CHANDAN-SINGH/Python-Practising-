s=input('Enter the paranthasis:')
par=set(['(','{','['])
des={'[':']','{':'}','(':')'}
stack=[]

for i in s:
    if i in par:
        stack.append(des[i])
        
    elif stack and i==stack[-1]:
        stack.pop()
        
        
    elif i in des.values():
        print('Not balanced')
        break
    
else:
    print('balanced' if not stack else 'Not balanced')

