import time

def buscar_suma(nums, target):
  hashTable = {}

  for i in range (len(nums)):
    menor = target - nums [i]
    if menor in hashTable:
      print((nums[i], menor))
    hashTable[nums[i]] = nums[i]
    
if __name__ == '__main__':
 
    arreglo = [1,9,5,0,20,-4,12,16,7]
    sum = 12

    buscar_suma(arreglo, sum)
    t1=time.perf_counter()
    print(t1)