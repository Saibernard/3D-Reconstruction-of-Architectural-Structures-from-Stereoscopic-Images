import numpy as np

def pose_candidates_from_E(E):
  transform_candidates = []
  ##Note: each candidate in the above list should be a dictionary with keys "T", "R"
  """ YOUR CODE HERE
  """
  U, S, Vt = np.linalg.svd(E)
  Rz_piby2= np.array([[0,-1,0],[1,0,0],[0,0,1]])
  print(np.shape(Rz_piby2))
  Rz_minuspiby2 = np.array([[0,1,0],[-1,0,0],[0,0,1]])

  T1 = (U[:,2:].T).reshape(3)
  T2 = -T1

  print(T1)
  print(T2)

  R1 = U @ Rz_piby2.T@Vt
  R2 = U@Rz_minuspiby2.T@Vt

  print(R1)
  print(R2)

  sol1 = {'T':T1,'R':R1}
  sol2 = {'T':T1,'R':R2}
  sol3 = {'T':T2,'R':R1}
  sol4 = {'T':T2,'R':R2}


  transform_candidates = [sol1, sol2, sol3, sol4]


  """ END YOUR CODE
  """
  return transform_candidates