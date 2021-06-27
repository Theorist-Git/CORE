# CORE Virtual assistant

* CORE is a virtual assistant created using python3. It is not a self learning AI, it only responds to explicitly coded stuff. It will get more intelligent
with future commits
## Dependencies

1. **Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the python modules required.**

```bash
$ pip install requirements.txt
```
* **This will install all the packages that you lack. It is highly recommended that you work on this project in a virtualenv.**
```bash
$ pip install virtualenv
```
```bash
$ mkvirtualenv myenv
```
```bash
$ workon myenv
```
```bash
(myenv) $ pip install requirements.txt
```
2. **Troubles with [PyAudio](https://pypi.org/project/PyAudio/) installation**
 ```bash
(myenv) $ pip install PyAudio
```
This may not work for most users as pip doesn't have the necessary .whl file to build the wheel, you have two solutions:
1) Install unofficial binaries from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio). (Recommended)
* Install a suitable wheel from the aforementioned site <br>
  Eg -> <br>The suitable wheel for me is <b>PyAudio-0.2.11-cp39-cp39-win_amd64.whl</b><br> 
  This is because I have python 3.9 (cp39) and it is a 64-bit installation(amd64). 
  After installing it in a directory (say, C:/docs), go to terminal and write
 ```bash
(myenv) $ cd C:/docs
(myenv) $ pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl
```
* This will ensure that pyaudio get installed easily.
2. **Install [Visual studio](https://visualstudio.microsoft.com/) (Not recommended)**
* Only install Microsoft Visual C++ 14.0 (~4 Gigabyte). Get it with ["Build Tools for Visual Studio"](https://visualstudio.microsoft.com/downloads/) 

## Installation
* To clone the repository:
```bash
git clone <repo-url>
```
## Usage
* Run the core.py file and speak.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Authors and acknowledgment
* Author(s): This entire project was coded by [_ Theorist _](https://github.com/Theorist-Git).
## License
[MIT](https://choosealicense.com/licenses/mit/)