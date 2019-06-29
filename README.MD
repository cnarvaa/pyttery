# Pyttery
This project aims to take care of your PC's battery life. It will show a Windows notification when: **battery level > 95** and **PC is plugged**.

To create the .exe paste this command on the cmd:

`pyinstaller -F -w  --hiddenimport=plyer.platforms.win.notification pyttery.py`

## Setting as windows service
1. Create a shortcut.
2. In the window opened by the command windows+E paste `shell:common startup`.
3. In the opened folder paste the shortcut access.

Now when you start your pc pyttery will start. For this session, try clicking the pyttery executable.