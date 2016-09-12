# Classifier-Sample-Extractor
## Installation

* You need to install opencv, python and numpy for your operating sytsem
([Windows](http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_setup/py_setup_in_windows/py_setup_in_windows.html), [Linux - Ubuntu](http://www.pyimagesearch.com/2015/06/22/install-opencv-3-0-and-python-2-7-on-ubuntu/), [Mac OSX](http://www.pyimagesearch.com/2015/06/15/install-opencv-3-0-and-python-2-7-on-osx/))

* Clone this repository 

        $ git clone https://github.com/fabianbormann/Classifier-Sample-Extractor.git 

* Copy images containing objects that you wish to detect to the data/ folder
* Replace the cascade.xml with your own classifier (current cascade.xml is the frontal eye detector by Shameem Hameed bundled with the opencv installation)

## Setup
* Update the properties in sample_extractor.py line 71 
  `cascade.detectMultiScale(image, scaleFactor=1.2, minNeighbors=10,minSize=(20,20), maxSize=(45,45))` the sizes should fit to your training samples
* My images use the name convention data/image-xxx.png so that your positives and negatives will be named 'xxx_yyy_zzz.png' yyy and zzz describes the position (center) of this subimage in the image-xxx.png. If you don't want to use this feature simply edit line 37 and 39.

## Run
        $ python sample_extractor.py

 Your classifier will run at a random image from your data folder. Every detected object will be presented by a white border.
 
 If you click with the `left mouse button` the border will be change it's color to green and the subimage will move to the positives folder. In contrast if you click the `right mouse button` border color switch to red and the subimge move to negatives folder. The `middle mouse button` load the next image from the data folder.
