def maxArea(height) -> int:
    n=len(height)
    ans=0
    left,right=0,n-1
    while(left<right):
        area=(right-left)*(min(height[left],height[right]))
        ans=area if area>ans else ans
        max_height=max(height[left],height[right])
        if max_height==height[left]:
            right-=1
        else:
            left+=1
    return ans
    
height =[1,8,6,2,5,4,8,3,7]
area=maxArea(height)
print(area)