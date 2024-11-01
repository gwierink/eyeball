# Reading digits from an image - example 1

## Introduction
This is a small example to test reading numbers from an image. The use case is
reading from images of a utility meter to be processed elsewhere.

## The environment
This example was created and tested on Ubuntu 24.04 using a virtual python
environment, with python 3.12.3. The virtual environment is sueful to mess
around with python in a safe, "sandboxed" way, and needed for later use on
Raspberry Pi.

### Create a new virtual environment
First, make sure you have virtualenv and virtualenvwrapper installed.
Then, you can create a virtual environment by:
```bash
  python -m venv .venv
```
where `.venv` is the name of the virtual environment, to be stored in a
folder name ".venv" in the current directory. Note that the name of the virtual
environment does not have to be ".venv"  and does not have to be a hidden (.")
folder.Once the virtual environment has been created, the shell shows the name
of the environment in round brackets (`(.env)`). For more in virtual
environments and pip, see [Python Virtual Environments: A Primer][pyvenv] and a
nice video tutorial here:
"[Python Virtual Environment and pip for Beginners][pipbeg]".

In the virtual environment, install [PyTorch][pytor], [EasyOCR][ocr], and
[OpenCV][ocv]:
```bash
  pip install torch torchvision torchaudio
  pip install easyocr
  pip install opencv-python
```
Note that you also need `numpy` and that it will be pulled in when installing
the above packages.

## Reading numbers from an image
(update this section)

## Resources and references
References are linked above and are listed in this section in raw text. This
markdown file was written and tested using the
[Dillinger Markdown editor][dillinger].

[//]: # (These are reference links used in the body of this note and get
  stripped out when the markdown processor does its job. There is no need to
  format nicely because it shouldn't be seen. Thanks SO - 
  http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dillinger]: <https://dillinger.io/>
   [pipbeg]: <https://www.youtube.com/watch?v=eDe-z2Qy9x4>
   [pyvenv]: <https://realpython.com/python-virtual-environments-a-primer/>
   [ocv]: <https://pypi.org/project/opencv-python/>
   [ocr]: <https://pypi.org/project/easyocr/>
   [pytor]: <https://pytorch.org/>
