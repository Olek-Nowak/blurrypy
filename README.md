# Project

Face detection & blurrying in python.
Includes pre-trained frontal-face adaboost detector from opencv2, as well as a custom Haar Cascade Filter trained on 124 positive and 130 negative samples (collected with custom script `data-collection.py`, and annotated with `annotation-util.py`). 

# Use
By default `blurry.py` script runs using devices built-in webcam (may fail without it), and pre-trained opencv2 detection.
By default script only takes a single frame at a time - press spacebar to update, or hold for live feed.
To change to custom detection, uncomment line:
```python
classifier = dirname + "/cascade/cascade.xml"
```
To use single images instead, uncomment line:
```python
img = cv2.imread(dirname + '/res/face1.png')
```

<img src="res/face1.png" width="200"> <img src="res/face1-blurred.png" width="200">


# Licencing


                        Intel License Agreement
                For Open Source Computer Vision Library

 Copyright (C) 2000, Intel Corporation, all rights reserved.
 Third party copyrights are property of their respective owners.

 Redistribution and use in source and binary forms, with or without modification,
 are permitted provided that the following conditions are met:

   * Redistribution's of source code must retain the above copyright notice,
     this list of conditions and the following disclaimer.

   * Redistribution's in binary form must reproduce the above copyright notice,
     this list of conditions and the following disclaimer in the documentation
     and/or other materials provided with the distribution.

   * The name of Intel Corporation may not be used to endorse or promote products
     derived from this software without specific prior written permission.

 This software is provided by the copyright holders and contributors "as is" and
 any express or implied warranties, including, but not limited to, the implied
 warranties of merchantability and fitness for a particular purpose are disclaimed.
 In no event shall the Intel Corporation or contributors be liable for any direct,
 indirect, incidental, special, exemplary, or consequential damages
 (including, but not limited to, procurement of substitute goods or services;
 loss of use, data, or profits; or business interruption) however caused
 and on any theory of liability, whether in contract, strict liability,
 or tort (including negligence or otherwise) arising in any way out of
 the use of this software, even if advised of the possibility of such damage.