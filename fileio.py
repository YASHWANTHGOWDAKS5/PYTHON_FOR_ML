#File input outut practice question
def CheckWord(word: str) ->str:
      with open('Practice.txt','r') as f:
            data=f.read()
            if(data.find(word)!=-1):
                  print('Found')
            else:
                  print('Not found')

CheckWord('learning')

def check_line(word: str) -> int:
      data=True
      line_no=1
      with open('Practice.txt','r') as f:
            while data:
                  data=f.readline()
                  if(word in data):
                        print(line_no)
                        return
                  line_no+=1
      return -1
print(check_line('learningasdfsd'))

with open('Practice.txt', 'r') as f:
      data=f.read()
      print(data)
      print(type(data))
      

      num=""

      for i in range(len(data)):
            if(data[i]==','):
                  print(int(num))
                  num=""
            else:
                  num+=data[i]
      count = 0 
      nums= data.split(",")
      print(nums)
      for val in nums:
            if(int(val)%2==0):
                  count+=1
      print(count)