# 要求一
def calculate(min, max):
    # 請用你的程式補完這個函式的區塊
    sum = 0
    for i in range(min, max + 1):
        sum += i
    print(sum)

calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30

# 要求二
def avg(data):
    # 請用你的程式補完這個函式的區塊
    num = data["count"]
    employees = data["employees"]
    sum = 0
    for employee in employees:
        sum += employee["salary"]
    avg = sum / num
    print(avg)

avg({
    "count":3,
    "employees":[
        {
            "name":"John",
            "salary":30000
        },
        {
            "name":"Bob",
            "salary":60000
        },
        {
            "name":"Jenny",
            "salary":50000
        }
    ]
})

# 要求三
def maxProduct(nums):
    # 請用你的程式補完這個函式的區塊
    length = len(nums)
    for i in range(length):
        for j in range(i + 1, length):
            product = nums[i] * nums[j]
            if ("max" not in vars()):
                max = product
            if max < product:
                max = product
    print(max)

maxProduct([5, 20, 2, 6]) # 得到 120 因為 20 和 6 相乘得到最大值
maxProduct([10, -20, 0, 3]) # 得到 30 因為 10 和 3 相乘得到最大值

# 要求四
def twoSum(nums, target):
    # your code here
    length = len(nums)
    result = []
    for i in range(length):
        for j in range(i + 1, length):
            if (nums[i] + nums[j]) == target:
                result.extend([i, j])
    return result

result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

# 要求五
def maxZeros(nums):
    # 請用你的程式補完這個函式的區塊
    maxCount = 0
    count = 0
    for i in nums:
        if i == 0:
            count += 1
            if maxCount < count:
                maxCount = count
        else:
            count = 0
    print(maxCount)
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到4
maxZeros([1, 1, 1, 1, 1]) # 得到 0