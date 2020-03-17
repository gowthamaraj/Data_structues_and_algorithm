#############################
# List vs Array
# flexible vs rigid
# no need to import vs import
# Lists can also be re-sized quickly in a time-efficient manner vs Not quick
# heterogeneous data vs heterogeneous 
from time import perf_counter

my_list = list(range(10_000))
start = perf_counter()
for i in range(0,len(my_list)):
  x = (my_list[i])
stop = perf_counter()
print(stop-start)

from array import array
arr = array('i',my_list)
start = perf_counter()
for i in range(0,len(my_list)):
  x = (arr[i])
stop = perf_counter()
print(stop-start)