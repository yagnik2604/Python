from typing import List

# def nextGreaterElement(arr: List[int], n: int) -> List[int]:
#     # Initialize the result list with -1
#     result = [-1] * n
#     stack = []
    
#     for i in range(n - 1, -1, -1):
#         while stack and stack[-1] <= arr[i]:
#             stack.pop()
        
#         if stack:
#             result[i] = stack[-1]
        
#         stack.append(arr[i])
    
#     return result


arr = [4, 5, 2, 10, 8]
n = len(arr)

# print(nextGreaterElement(arr, n))  # Output: [5, 10, 10, -1, -1]






for i in range(2,6,2):
    print(i)
