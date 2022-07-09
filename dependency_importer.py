import os

def dep_import(package_name):
    try:
        __import__(package_name)
    except:
        try:
            os.system(f"pip install {package_name}")
            __import__(package_name)
        except:
            raise Exception("Could not install package.")
