func isAnagram(s string, t string) bool {
  if len(s) != len(t) {
	return false
  }

  var ss [26]int
  var tt [26]int

  for i := 0; i < len(s); i++ {
	c := s[i]
	if c >= 'a' && c <= 'z' {
		ss[c - 'a']++
	}
  }

  for i := 0; i < len(t); i++ {
	c := t[i]
	if c >= 'a' && c <= 'z' {
		tt[c - 'a']++
	}
  }

  for i := range ss {
	if ss[i] != tt[i] {
		return false
	}
  }

  return true
}
