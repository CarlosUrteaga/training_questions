def rotate_k_times (nums, k):
    n = len(nums)
    residual = k%n
    tmp = nums + nums
    return nums[residual:n+residual]
arr = [0, 1, 2, 3, 4, 5, 6]
rotate_k_times(nums,2)
