s=input('Enter the paranthasis:')
par=set(['(','{','['])
des={'[':']','{':'}','(':')'}
stack=[]

for ch in s:
    if ch in par:
        stack.append(des[ch])
        
    elif stack and ch==stack[-1]:
        stack.pop()
        
        
    elif ch in des.values():
        print('Not balanced')
        break
    
else:
    print('balanced' if not stack else 'Not balanced')

