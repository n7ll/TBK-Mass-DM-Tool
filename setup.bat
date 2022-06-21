echo off


:start
cls

set python_ver=36

python ./get-pip.py

cd \
cd \python%python_ver%\Scripts\
pip install discord
pip install colorama
pip install requests
pip install datetime
pip install random
pip install init
pip install sys
pip install subprocess
pip install os

pause
exit