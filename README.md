# Packaging Python with PyInstaller

## See also

Look at [these instructions](https://datatofish.com/executable-pyinstaller/) for a second point of view.

## Create a new Python virtual environment

Use `venv` to create a new virtual environment. Note that the second `venv` is the name of the virtual environment. We're calling it `venv` here so that **VSCode** will recognise it.

```
C:> python -m venv venv
```

## Activate the virtual environment

Activate the virtual environment as follows.

```
C:> venv\Scripts\activate
```

The prompt will change to show that your environment is active.

## Install PyInstaller

Use `pip` to install **PyInstaller**.

```
(venv) C:> python -m pip install pyinstaller
```

## Install any other packages that you need

If you need any other packages, e.g., `sympy`, then install them into your virtual env using `pip`.

```
(venv) C:> python -m pip install sympy
```

## Use PyInstaller to create a standalone .exe

Run `pyinstaller`, passing it the name of your script (or scripts). If you want the result to be a single file containing everything that you need then pass it the `--onefile` option.

In this example we're assuming that you have a single file called `my_app.py` and it's in the current directory.

```
(venv) C:> pyinstaller --onefile my_app.py
```

If all goes well then this will output your new program as a `.exe` under the `dist/` directory.
