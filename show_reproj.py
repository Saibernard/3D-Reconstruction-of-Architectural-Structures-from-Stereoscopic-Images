import numpy as np
import matplotlib.pyplot as plt

def show_reprojections(image1, image2, uncalibrated_1, uncalibrated_2, P1, P2, K, T, R, plot=True):

  """ YOUR CODE HERE
  """
  # print(uncalibrated_2.shape) # shape is (3,598), so need to take 1
  # print(P1)
  P1proj = np.zeros(uncalibrated_1.shape)
  P2proj = np.zeros(uncalibrated_2.shape)

  for i in range(uncalibrated_1.shape[1]):
    P1proj[:,i] = K@(R@P1[i] + T)
    P2proj[:,i] = K@(R.T@P2[i] - R.T@T)

    # print(P1proj)
    # print(P1proj.shape)
    # # print(P2proj)
    # print(P2proj.shape)
    # P1proj = P1proj.T
    # P2proj = P2proj.T
    # print(P1proj.shape)
  P1proj = P1proj.T
  P2proj = P2proj.T
  
  """ END YOUR CODE
  """

  if (plot):
    plt.figure(figsize=(6.4*3, 4.8*3))
    ax = plt.subplot(1, 2, 1)
    ax.set_xlim([0, image1.shape[1]])
    ax.set_ylim([image1.shape[0], 0])
    plt.imshow(image1[:, :, ::-1])
    plt.plot(P2proj[:, 0] / P2proj[:, 2],
           P2proj[:, 1] / P2proj[:, 2], 'bs')
    plt.plot(uncalibrated_1[0, :], uncalibrated_1[1, :], 'ro')

    ax = plt.subplot(1, 2, 2)
    ax.set_xlim([0, image1.shape[1]])
    ax.set_ylim([image1.shape[0], 0])
    plt.imshow(image2[:, :, ::-1])
    plt.plot(P1proj[:, 0] / P1proj[:, 2],
           P1proj[:, 1] / P1proj[:, 2], 'bs')
    plt.plot(uncalibrated_2[0, :], uncalibrated_2[1, :], 'ro')
    
  else:
    return P1proj, P2proj