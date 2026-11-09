import "slices"

func isAnagram(s string, t string) bool {
  ss := strings.Split(s, "")
  tt := strings.Split(t, "")
  slices.Sort(ss)
  slices.Sort(tt)
  return slices.Equal(ss, tt)
}
