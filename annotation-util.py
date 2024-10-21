import os
with open('neg.txt', 'w') as f:
    for filename in os.listdir('datasets/3'):
        f.write('datasets/3/'+filename+'\n')
# for positive samples use builtin opencv bin:
# opencv_annotation.exe --annotations=pos.txt --images=datasets/2/
# then convert pos.txt to pos.vec file:
# opencv_createsamples.exe -info pos.txt -w 24 -h 24 -num 150 -vec pos.vec
# after that train cascade:
# opencv_traincascade.exe -data cascade/ -vec pos.vec -bg neg.txt -w 24 -h 24 -numPos 120 -numNeg 200 -numStages 10