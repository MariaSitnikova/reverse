from copy import deepcopy 
def arrange(s):
    S = deepcopy(s)
    T = []
    while len(S) != 0:
        if len(S) >= 2:
            T.append(S[0])
            T.append(S[-1])
            S.pop(-1)
            S.pop(0)
            S = S[::-1]
        else:
            T.append(S[0])
            S.pop(0)
    return T