import numpy as np

def least_squares_estimation(X1, X2):
  """ YOUR CODE HERE
  """
  A = np.zeros((X1.shape[0],9))

  for i in range(X1.shape[0]):
    A[i,0:3] = X2[i][0] * X1[i]
    A[i,3:6] = X2[i][1] * X1[i]
    A[i,6:9] = X2[i][2] * X1[i]

  # print(np.shape(A))
  # A = np.vstack([fsc,ssc,tsc])
  # print(A)
  # E = (X1-X2)
  U, S, V = np.linalg.svd(A)
  # print(V)

  E_matrix = V[-1,:] #taking the last right singular vector
  print(E_matrix)

  E_obtained = E_matrix.reshape(3,3)

  # print(E_matrix)
  # print(np.shape(E_matrix))


  # E_new = np.vstack(E_matrix,)

  # S = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 0]])

  # E_obtained =
  u, s, vt = np.linalg.svd(E_obtained)

  E = -u@np.diag((1,1,0))@vt



  """ END YOUR CODE
  """
  return E





