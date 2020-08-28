# Game-of-Life
It's a simple simulation of Conway's Game of Life

![image](https://user-images.githubusercontent.com/52712038/91567111-e529ef00-e944-11ea-9b74-185bbbd47672.png)
## Getting started
### Prerequisites
There are two ways of running this application, either using an simple ***EXE*** for **Windows** that has to be launched within its folder (because they contain all the python modules, application data etc...) and that requires no installer. 
**Or** by **running the source code** of the application with Python and all the modules. In which case you'll need :
- [**Python version 3.7.7 (or upper)**](https://www.python.org/downloads/)

- **Numpy** module version ***1.19.0***, to deal with matrixes and data
```bash
pip install numpy
```
- **Matplotlib** module version ***3.2.2*** *(upper versions don't work if you want the EXE)*, to do annimated 3D plotting 
```bash
pip install matplotlib==3.2.2
```
### Installation
Like i said there no installer, just a folder wich contains all the necessary files.
If you want the Windows EXE version than :
- **download** the Github repository as a ZIP
- **UnZIP** it and open it
- **UnZIP** the *"Game of life executable"*
- **Open** the folder *"Game of life executable"* and find the executable named *"Game of life.exe"*

If you want to run the source code than :
- **download** the Github repository as a ZIP
- **UnZIP** it and open it
- **find** the file *"Game of Life.py"*
- **Run** it with your editor (Python's IDLE, Vscode, etc...)

## How to use 
- Pause, if you want to pause
- Reload if you want to generate a random matrix
- Ones % is the % of "live" vs "dead" cells in the random generated matrix
