"""
THIS IS THE SAME EVEN NUMBER PROGRAM HERE A LIST li IS USED GET THE COPY OF THE GENERATOR FUNCTION
"""

def even():
   n=0
   while True:
        yield n
        n = n + 2  

copy=even()
li=[]
for i in range(1000):
    li.append(next(copy))   
print(li)
    
