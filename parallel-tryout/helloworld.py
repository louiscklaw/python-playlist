from multiprocessing import Pool

def f(a,b):
  print(a,b)
  return a *b

def paralllel_helper(c): return f(*c)

if __name__ == '__main__':
  p = Pool(20)
  p.map(paralllel_helper, [(1, 2), (3, 4)])
  p.close()
  p.join()
