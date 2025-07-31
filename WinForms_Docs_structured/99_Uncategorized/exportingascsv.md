---
title: exportingascsv.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\exportingascsv.md
created_at: 2025-07-03
---








  









### Exporting as CSV {#exporting-as-csv style="LINE-HEIGHT: 150%; tab-stops: 0pt"}

Apart from exporting **.ics** files, the schedule control supports exporting to **CSV** format as well; this process is similar to that of **.ics** file exporting, except that the code for exporting is different.

Code for Exporting to CSV

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[][C#\]]                                                                      |
|                                                                                                                                                                                  |
| [Schedule][ schedule = [new] [Schedule]();] |
|                                                                                                                                                                                  |
| [schedule.ExportCSV();][]                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Once the exported **CSV** file is opened in a spreadsheet application like **Microsoft Excel** or **OpenOfficeCalc**, appointments can be entered in a tabular format.

[] 

[]{#related-topics}

