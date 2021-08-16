#Window-keylogger

Source is available on python2.7

First thing to do

Install external librarys at eLib.
<ul>pywin32</ul>
<ul>pyHook</ul>

Use `wheel`
```shell
wheel unpack pyHook-1.5.1-cp27-cp27m-win_amd64.whl
wheel unpack pywin32-228-cp27-cp27m-win_amd64.whl
```
and move those into your virtual env library.

then,

Execute
<ul>pywin32-228.data/scrips/pywin32_postinstall.py</ul>