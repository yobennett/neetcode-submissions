func twoSum(nums []int, target int) []int {
	seen := make(map[int]int)
	for i, num := range nums {
		complement := target - num
		if prev, ok := seen[complement]; ok {
			return []int{prev, i}
		}
		seen[num] = i
	}
	return []int{}
}