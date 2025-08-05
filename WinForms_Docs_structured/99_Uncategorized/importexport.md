---
title: importexport.md
original_path: WinForms_Docs/99_Uncategorized/importexport.md
created_at: 2025-08-05
---








  









## Import / Export {#import-export style="tab-stops: 0pt"}

This section deals with the import and export option in Schedule Silverlight:

[·      ]The schedule control allows users to export or import appointments and events as an **.ics** files.  Appointments and events scheduled with the control can be exported as an **.ics** file and opened or imported in other schedulers such as Microsoft Outlook, Google Calendar, or any other scheduler supporting .**ics** files. 

[·      ]Similarly, files exported from other schedulers can also be imported into Essential Schedule.

The code given below demonstrates the import and export of **.ics** files.

 

Code for implementing Importing and Exporting

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                           |
|                                                                                                                                                                        |
| [Schedule][ schedule = [new] [Schedule]();] |
|                                                                                                                                                                        |
| [schedule.ExportICS();][ ]                                                                          |
|                                                                                                                                                                        |
| [schedule.ImportICS();][ ]                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

More:









