import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    if not seqs:
        return np.zeros((0, 0))

    max_len_seq = np.max([len(seq) for seq in seqs])
    max_len = max_len_seq if max_len is None else max_len

    ans = [list(seq) for seq in seqs]
    for i in range(len(seqs)):
        ans[i] = seqs[i][:max_len] if len(seqs[i]) > max_len else ans[i]

    for i in range(len(seqs)):
        pad_arr = np.full(shape=max_len - len(ans[i]), fill_value=pad_value) if len(ans[i]) < max_len else []

        ans[i] = np.concatenate([np.array(ans[i]), np.array(pad_arr)])

    return ans
    pass