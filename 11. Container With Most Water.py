height = [1,1,9,4,1,1,1,1,9]

i = 0
j= len(height) - 1

area = min(height[i], height[j]) * (j - i)

while i < j:
    area = max(area, min(height[i], height[j]) * (j - i))
    if height[i] < height[j]:
        i += 1
    else:
        j -= 1
        
print(area)