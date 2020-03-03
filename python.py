#ANOTHER WAY OF GENERATING EVEN NUMBER USING GENERATOR
def even(limit):
   n=0
   while (n<limit):
        yield n
        n = n + 2

out=even(200)

for i in out:
    print(i)

