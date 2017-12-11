# SMCoordinator

## SETUP

***All downloaded and saved files must be in the same location***

1. Create New Folder on ```Desktop``` (or wherever you want to store ALL your SMC files), called ```SMCoordination```
2. Download the following files from ```goo.gl/2L1yDP```, and **PUT IT IN SMCoordination FOLDER**
- **TheSMCoordinator > SMCoordinator >** ```SMCoordinator.py```
  - If I ask you in the future to download an updated program/Python file, this is the file I'm talking about.
- ```python-3.6.3-macosx10.6.pkg``` for MacOSX
- ```python-3.6.3-amd64.exe``` for Windows


## COORDINATION
*Do this for every new move*

***Follow the specified naming directions - or the program won't work***
1. From ```goo.gl/2L1yDP```, open ```SMCoordinator.gsheet```
2. Duplicate the ***MC*** tab, and rename the tab to **{MOVE#}** (e.g. the tab for move 100 should be called **100**)
- Optional: colour the tab to your corresponding Ongoing Moves colour
3. Edit the coloured fields according to MC planning and move requirements

***Proceed to the next steps only when all planning steps are done, spreadsheet is complete, and you are ready to send out the itinerary.
In other words, any changes you make to your itinerary after this point, will not be reflected in the final output, unless you redo them. So if you need to make changes, start at step 3, and then repeat steps 4-10, replacing/overwriting the old files when prompted.***

4. **File > Download as > Comma-separated values (.csv, current sheet)**

**IMPORTANT: Make sure this is saved to the same folder that contains** ``` SMCoordinator.py```

**Do NOT change the name of the file. Keep the default file name.**
- If when you click on it, it downloads right away to an unknown location, it is probably saved in your Downloads folder, and you will have to move it to the SMCoordination folder manually. If you want to be able to save it directly to SMCoordination, message me and I'll show you how to change that setting.
  - Google Chrome: Settings > Advanced > Downloads > Location > Ask where to save each file before downloading
  - Safari: Safari > Preferences > File download location: > Ask for each download
5. Open ```SMCoordinator.py``` file in IDLE
6. **Run > Run Module**
7. Enter Move# when prompted (same as what you named the tab in step 2.)
8. After program has successfully run, you will be able to find an ```{MOVE#}MoveItinerary.html``` file in the SMCoordination folder. Open this file (it will open in one of your web browsers)
9. Copy and Paste the contents of the .html file into your Move Itinerary email
10. Hide the **{MOVE#}** tab in the GSheet when your move is complete
