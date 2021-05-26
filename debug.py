import numpy as np
from read_file import read_alphabet
from prefix_beam_search import prefix_beam_search
from G import yyn, ynn

# prob1 = np.log(1e-50)
# prob2 = np.log(2.5e-50)
# prob12 = np.logaddexp(prob1, prob2)
# # prob12
# # -113.87649168120691
# print(prob12)
# print(np.exp(prob1))
# print(np.exp(prob2))
# print(np.exp(prob1) + np.exp(prob2))
# print(np.log(np.exp(prob1) + np.exp(prob2)))
# 3.5000000000000057e-50

alphabet = read_alphabet(
    '/afs/inf.ed.ac.uk/user/s20/s2070789/Documents/Work/CSTR/lennoxtown/s3/espnet/egs/modified_yesno/asr_fbank_spk/data/lang_1char/train_yyn_units.txt')
print(alphabet)
ctc = np.load(
    '/afs/inf.ed.ac.uk/user/s20/s2070789/Documents/asr_fbank_spk_sub/data/sam_yyn_noise1.npy')
ctc = np.exp(ctc)
print(ctc.max())
print(ctc.min())
re_before = prefix_beam_search(ctc, alphabet=alphabet, prune=1e-4)
re_after = prefix_beam_search(
    ctc, lm=yyn, alphabet=alphabet, prune=1e-4, beta=100)
print('re_before', re_before)
print('re_after', re_after)
