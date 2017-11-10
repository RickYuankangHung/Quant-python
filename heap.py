import random
class MinHeap:
    def __init__(self):
        self.data=[None]
    def pop(self):
        if len(self.data)==2:
            return self.data.pop(1)
        answer=self.data[1]
        self.data[1]=self.data.pop(len(self.data)-1)
        self.sift_down()
        return answer

    def sift_down(self):
        parent_index=1
        sorted_heap=False
        while True:
            left_child=2*parent_index
            right_child=2*parent_index+1
            heap_size=len(self.data)
            if left_child>=heap_size:
                break
            if self.data[left_child]<self.data[right_child]:
                min_child_index=left_child
            else:
                min_child_index=right_child
            if self.data[parent_index]<=self.data[min_child_index]:
                break
            self.data[parent_index],self.data[min_child_index]=self.data[min_child_index],self.data[parent_index]
            parent_index=min_child_index
    def push(self,value):
        child_index=len(self.data)

        self.data.append(value)
        while child_index>1:
            parent_index = int(child_index / 2)
            if self.data[parent_index] <= value:
                break
            self.data[parent_index],self.data[child_index]=self.data[child_index],self.data[parent_index]
            child_index=parent_index

        def __repr__(self):
            return "MinHeap(" + str(self.data) + ")"


m = MinHeap()
for i in range(1,100):
    m.push(random.random())
print(m.data)
#
#
#         child_index=len(self.data)-1
#         return (sift_up(child_index))
#     def sift_up(child_index):
#         if child_index==1:
#             return 1
#
#         if self.data[parent_index]>self.data[child_index]
#
#             child_index=parent_index
#             return (sift_up(child_index))
#         else:
#             return child_index
#     def pop(self):
#
# a_list=[2,5,3,11,6,12,5,4]
# min_heap=MinHeap()
# for x in a_list:
#     MinHeap.push(x)
# print(MinHeap.data)
#
#
# while len(MinHeap.data)>1;
#     print(MinHeap.data)