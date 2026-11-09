import "slices"

func hasDuplicate(nums []int) bool {
	slices.Sort(nums)
    seen := make(map[int]struct{})
	for _, v := range nums {
		if _, ok := seen[v]; ok {
			return true
		}
		seen[v] = struct{}{}
	} 
    return false
}
