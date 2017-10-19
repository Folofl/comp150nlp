Assignment:  Lab5
By:          Alena Borisenko 
Submitted:   October 18th, 2017


Part 1:
    uses: generate_matrix.py
    The program takes two categories of the Brown corpus (romance and 
    adventure) and turns it into a term x term matrix X of word vectors.
    Then, the program also performs an SVD decomposition to produce matrix U,
    which takes roughly 8 minutes to complete while the rest of the program
    only takes a couple of seconds.
    The matrices are saved in:
        Xmatrix.npy, ~500 MB.
        Umatrix.npy, ~  1 GB

Part 2:
    uses: analogy.py
    The program reads in the two matrices generated in Part 1 and uses X
    in order to attempt to complete an analogy.
    Out of the ones I tried, the only successful one was:
        cheese is to eat as coffee is to drink
    Other ones that I tried that turned out funny:
        foot is to leg as arm is to rifle
            (maybe arm as in right to bear arms?)
        knife is to stab as gun is to holster
            (at least it is kind of a gun-related thing)
        fish is to salmon as bird is to forgiven
            (I am glad the bird has been forgiven)