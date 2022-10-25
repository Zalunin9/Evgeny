def openFile():
  f1 = open('data.txt', 'r')
  while True:
      data = f1.readLine().split("-")
      print(data)
      if data[0] == '':
          break
      return daya
      f1.close()
   except IOError:
        print(IOError.with_traceback() )
   def dataMonth()
       data2 = openFile()
       print(data2)
       data1 = ['01', '12', '1900']
       print(data)
       if int(data2[0]) < int(data1[0]):
           data1[0] = data2[0]
        if int(data2[1]) < int(data1[1]):
            data2[1] = data1 [1]
        print(data1[0], "-", data1 [1])


try:
    f1 = open ('data.txt', 'r')
    data1 = ['31', '12', '1900']
    while True:
        data = f1.readLine ().split("-")
        print(data)
        if data[0] =='':
            break
        if int(data[0]) < int(data1[0]):
            data1[0] = data [0]
        if int(data[1]) < int(data1[1]):
            data1[1] = data[1]

            f1.close()
            print(data1[0], " -", data1[1])
except IOError:
    print(IOError.with_traceback())
