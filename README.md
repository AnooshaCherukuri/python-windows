# python-windows

When we need to run python scripts or applications on windows machines that are not connected to Internet we will follow the following method:
- we will download Python and copy that into remote windows machine.
- then we will install by double clicking.

Now when we start to run the python scripts we will need python modules. usuall we can install by pip install python-module-name and it will download the module from https://pypi.python.org.

In the cases where we don't have internet access for the server, we have to manually download the modules from https://pypi.org/ and install.

The python module file that we download would be a .whl file or .tar.gz file. Sometimes some python modules have dependencies in that case we will first install the sub module and then we will install main module.
we will install it with the command C:\Python27\Scripts pip install python-module-name

ex: C:\Python27\Scripts\pip install os3-0.1.2.tar.gz
