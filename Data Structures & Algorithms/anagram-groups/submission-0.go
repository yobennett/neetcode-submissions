func groupAnagrams(strs []string) [][]string {
	freqs := make(map[[26]int][]string)
	for _, str := range strs {
		var freq [26]int
		for i := 0; i < len(str); i++ {
			char := str[i]
			freq[char-'a']++
		}
		freqs[freq] = append(freqs[freq], str)
	}
	result := make([][]string, 0, len(freqs))
	for _, group := range freqs {
		result = append(result, group)
	}
	return result
}