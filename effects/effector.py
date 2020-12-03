import sys
import os
import multiprocessing
from PIL import Image
import numpy as np
from tqdm import trange

def run(do, inputDir, outputDir, inputList, i):
    Image.fromarray(do(np.asarray(Image.open(inputDir+"/"+inputList[i])))).save(outputDir+"/"+inputList[i])

def invert(im):
    return 255-im

def topPixelSorter(im):
    return np.flip(np.sort(im, axis=0), axis=0)

def bottomPixelSorter(im):
    return np.sort(im, axis=0)

def leftPixelSorter(im):
    return np.flip(np.sort(im, axis=1), axis=1)

def rightPixelSorter(im):
    return np.sort(im, axis=1)

def centerVerticalPixelSorter(im):
    tmp = np.sort(im, axis=0)
    return np.concatenate((np.flip(tmp[1::2], axis=0),tmp[::2]), axis=0)

def invCenterVerticalPixelSorter(im):
    tmp = np.sort(im, axis=0)
    return np.concatenate((tmp[::2],np.flip(tmp[1::2], axis=0)), axis=0)

def centerHorizontalPixelSorter(im):
    tmp = np.sort(im, axis=1)
    return np.concatenate((np.flip(tmp[:,1::2], axis=1),tmp[:,::2]), axis=1)

def invCenterHorizontalPixelSorter(im):
    tmp = np.sort(im, axis=1)
    return np.concatenate((tmp[:,::2],np.flip(tmp[:,1::2], axis=1)), axis=1)

if __name__ == "__main__":
    # get params
    inputDir = sys.argv[1]
    outputDir = sys.argv[2]
    effect = sys.argv[3]

    # setup some vars
    inputList = os.listdir(inputDir)
    inputLen = len(inputList)

    # determine effect
    try:
        exec(f"do = {effect}")
    except:
        raise Exception("Specified effect does not exist.")

    # use effect on each image
    for i in trange(inputLen, unit="img"):
        multiprocessing.Process(target=run, args=[do, inputDir, outputDir, inputList, i]).start()
