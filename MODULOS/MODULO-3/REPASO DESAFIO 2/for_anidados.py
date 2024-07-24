

texto1 = "mok"

texto2 = "abcde"                        # m o k
                                        #             a b c d e
for i in texto1:                        #     i
    for j in texto2:                    #                     j
        print(f' i -> {i} & j -> {j}')  #
        #

"""
 i -> m & j -> a
 i -> m & j -> b
 i -> m & j -> c
 i -> m & j -> d
 i -> m & j -> e
 i -> o & j -> a
 i -> o & j -> b
 i -> o & j -> c
 i -> o & j -> d
 i -> o & j -> e
 i -> k & j -> a
 i -> k & j -> b
 i -> k & j -> c
 i -> k & j -> d
 i -> k & j -> e
"""


for i in [3,5,64,12,43,1]:
    for j in [88,54,23,2,12]:
        if i == j:
            print(f"si hay usuario repetido y es el {i}")
      