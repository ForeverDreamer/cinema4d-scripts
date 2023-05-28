Hi @merkvilson first of all pip and Niklas localimport module is completely two different things.
    pip is a python module manager (similar to package manager in unix). This means once it's installed to a python binary, it will be able to manage other modules, download them, install them with all their dependencies and update them and so on.
    localimport is a python module that let you manage import in a local way while in Cinema 4D by default is global. For more information please read how the import function works in python.
    Meaning if you add a module named xyz to the sys.path from your plugin A and from plugin B you try to import another module named xyz, it will load the one from plugin A (the first one register).
Now how to install pip?
    Downloads https://bootstrap.pypa.io/get-pip.py.
    Downloads the c4dpy version matching your Cinema 4D version. (Already included in R21)
    Moves c4dpy and get-pip.py in the Cinema 4D folder.
    Opens a shell to the Cinema 4D folder:
    Window: Type cmd in the top path and press Enter.
    Mac: Open a new shell, then with cd navigate to your Cinema 4D folder. (You can drag and drop the path).
    Runs this command line c4dpy get-pip.py. This will execute the get-pip script which will, download and install the pip module.
    Now you can start to play with pip c4dpy -m pip install numpy. c4dpy allow to runs any module with the -m argument see c4dpy commandline. in this case I asked to pip to download and install numpy but any other 3rd party compatible with pip can be downloaded and used.
With that's said we do not provide support for 3rd party modules, so if it does not work with Cinema 4D Python environment, we can't help you.

Cheers,
Maxime.