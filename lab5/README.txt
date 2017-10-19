Assignment:  Lab5
By:          Alena Borisenko 
Created:     October 18th, 2017
Submitted:   October 18th, 2017
===============================================================================

-------------------------------------------------------------------------------
Part 1: Word vector matrix
-------------------------------------------------------------------------------
    
    prog  used: generate_matrix.py
    files made: keys, words, Xmatrix.npy, Umatrix.npy, kUmatrix.npy

    The program takes two categories of the Brown corpus (romance and 
    adventure) and turns it into a term x term matrix X of word vectors.
    Then, the program performs a SVD decomposition of matrix X to produce 
    matrix U; this step takes the longest to complete compared to the rest of
    the program (see timing details below). 
    Next, matrix kU is created by taking the first k columns of matrix U.
    Finally, the matrices are saved to respective .npy files.

    The matrices are saved in:
         Xmatrix.npy --- ~ 500 MB
         Umatrix.npy --- ~1000 MB (big bc of precision; too big to provide)
        kUmatrix.npy --- ~  90 MB

    Sample terminal output: 
        λ py -3.5 generate_matrix.py
        Made  X in 1.5666651725769043 seconds
        Made  U in 503.9229567050934 seconds
        Made kU in 0.0 seconds
        Saved  Xmatrix.npy in 2.7588350772857666 seconds
        Saved  Umatrix.npy in 5.110588312149048 seconds
        Saved kUmatrix.npy in 0.4085845947265625 seconds

-------------------------------------------------------------------------------
Part 2: Analogy completion via matrix X
-------------------------------------------------------------------------------

    prog  used: analogy.py (line 101 un-commented)
    files used: keys, words, Xmatrix.npy

    The program reads in the matrices generated in Part 1 (U is optional).
    Then, matrix X is used to attempt to complete an analogy.

    Out of the analogies I tried, the only successful ones were:
        cheese is to eat as coffee is to drink
        black is to white as day is to night

    Other ones that I tried that turned out funny:
        foot is to leg as arm is to rifle 
            (maybe arm as in right to bear arms?)
        knife is to stab as gun is to holster
            (at least it is kind of a gun-related thing)
        fish is to salmon as bird is to forgiven
            (I am glad the bird has been forgiven)

-------------------------------------------------------------------------------
Part 3: Analogy completion via matrix U
-------------------------------------------------------------------------------

    prog  used: analogy.py (line 103 un-commented)
    files used: keys, words, kUmatrix.npy

    The program reads in the matrices generated in Part 1 (U is optional).
    Then, matrix kU is used to attempt to complete an analogy.

    None of the analogies I tried made any sense, including ones from Part 2 :(

    Here are some unfortunate samples:
        cheese is to eat as coffee is to tackle
        black is to white as day is to incoherently
        foot is to leg as arm is to cain
        rain is to water as snow is to copper

    I think I misunderstood how to use U/kU because it is clearly performing
    worse than just X. 

-------------------------------------------------------------------------------
Part 4: Analogy that would stump a computer
-------------------------------------------------------------------------------

    I feel like anything that goes beyond strict word meaning and tries to
    associate some sort of an emotion or quality with the words used in the
    analogy would be really tricky to just guess. Word co-occurance doesn not
    really help with negative/positive qualities implied by some analogies.

    So, if somebody feels strongly about PC vs Mac or iPhone vs Android, they
    might say something like:
        mac is to pc as ferrari is to tractor
        or
        mac is to ferrari as pc is to tractor
    A computer might be confused by this because although mac and pc often
    co-occur, ferrari and tractor are only chosen due to opposite features.
    A human might disagree with the analogy, but will probably understand it.


    