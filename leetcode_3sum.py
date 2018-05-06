#时间复杂度为0 n3
class Solution:
    def threeSum(self, nums):
        list1 = []
        temp = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = [nums[i], nums[j], nums[k]]
                        temp.sort()
                        if (self.judgesame(list1, temp)):
                            list1.append(temp)
        return list1
    def judgesame(self, lista, listb):
        if (len(lista) == 0):
            return True
        temp = 0
        temp1 = len(lista[0])
        for x in lista:
            temp=0
            for y in range(len(x)):
                if (x[y] == listb[y]):
                    temp += 1
            if (temp == len(x)):
                return False
        return True