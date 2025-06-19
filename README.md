**This troubleshooting offshoot branch was created as a response to the fact that the master_doc could not cover the entire database of errors from python 3.13.3 (bottom right of Visual Studio Code.**

The prompt used to build the offshoot branches is:

Using the format from the Python Error Troubleshooting Guide, create a new version that focuses on syntax-related errors only. 
Include examples and explanations for IndentationError, SyntaxError, TabError, UnboundLocalError, ModuleNotFoundError, and ImportError. 
Follow the same structure with a try/except example and a corrected version: (Copy and paste the troubleshooting master doc into the GPT)

The only gpts capable of understanding this prompt (as of 06/18/2025) are:
GPT 4(perfect understanding), GPT-4o mini(kinda, not well), Deepseek(the best), and GPT reasoning.

Claude did build the original troubleshooting doc (it did take hours of guidance lol) but was unable to understand that I wanted it to build new guides using the master doc as a reference.

Substitute the error guide you want to make with the error types above.

**To use all troubleshooting guides seamlessly (Source Deepseek):**

In your **user terminal not the program**, without running any code, verify that you have the most recent version of Python installed (3.13.3):

  1. python --version

  2.install pip:
  python -m ensurepip --upgrade
  
  3. install requests:
     python -m pip install requests

If the above fails:
1. # Download get-pip.py
   curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
2. # Install pip
   python get-pip.py
3. # Now install requests
   python -m pip install requests
Verify successful installation:
python -c "import requests; print(requests.__version__)"


If you want to make the errors appear colorful instead of white per deepseek's recommendation (some of the traceback errors appear colorful some don't because deepseek insisted on making everything more human readable, thoughtful of it but frustrating lol)

pip install colorama
