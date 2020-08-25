def strStr(haystack, needle):
  test = ""
  if needle == "":
    return 0
  for x in range(0,len(haystack)-len(needle)+1):
    test = haystack[x:x+len(needle)]
    if test==needle:
      return x
  return -1
  pass