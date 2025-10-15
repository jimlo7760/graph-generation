import scipy.sparse as sp

A = sp.load_npz("graphs/GraphRNN_RNN_cora_4_128_pred_100_1_1022.npz")
print(A.shape)