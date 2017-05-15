# Python For Engineers
Exercises and code from the [Python For Engineers](http://pythonforengineers.com/) book

### Installing the libraries
Download [Anaconda Python](https://www.continuum.io/downloads)

Setup conda environment (in this case it's called `pyeng`)
```
conda create -n pyeng python=3.5
source activate pyeng
conda install numpy
conda install anaconda-client
anaconda search -t conda opencv3
conda install --channel https://conda.anaconda.org/menpo opencv3
```

Test Open CV with below code. It should return the installed Open CV version.
```
python -c "import cv2;print('OpenCV version: {}'.format(cv2.__version__))"
```
