class __list_flextape(list): 
  def join(self, s):
    return s.join(self)

def slap(args):
  returnstr = ""
  for arg in args:
    if type(arg) is list:
      listft = __list_flextape(arg)
      returnstr += listft.join(" ")
    else:
      returnstr += str(arg)
  return str(returnstr)

