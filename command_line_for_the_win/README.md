using sftp to transefer my local file to sandbox
steps on how i  did it
=======================
1) cloned the repository in sandbox root directory
2) created a folder in my local machine to store the screenshots on C:\users\HP\Desktop\screenshot
3) on my terminal on local machine i used the sftp which i copied from sandbox
4) navigated to my sandbox terminal to the repository of my git to be saved (cd)
5) navigated to the screenshot folder on my local machine (lcd)
6) used pwd and lpwd to get my actual path for both local machine folder and sandbox repository respectively
7) used the command put to upload from local to sandbox using 'put C:\users\HP\Desktop\screenshot\* alx...'
DONE!  