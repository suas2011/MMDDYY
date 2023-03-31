# MM/dd/yy
for yy in range(2023,2031):
   for mm in range(1,13):
      for dd in range(1,31):
         for seconds in range(1,86401):
        #    for sec in range(0,29000):
            print('{0:02}/{1:02}/{2:02}'.format(mm,dd,yy,end='\r')) 
      print()     
      