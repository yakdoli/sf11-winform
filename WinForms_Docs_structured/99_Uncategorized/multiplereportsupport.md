---
title: multiplereportsupport.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\multiplereportsupport.md
created_at: 2025-07-03
---








  









## Multiple Report Support {#multiple-report-support style="tab-stops: 0pt"}

OLAP Client control allows you to create any number of reports for a current session. You can also perform Add, Remove and Rename operations on reports in the current session.

 

[]{#_Add_Report}Add Report

Add report will add a new report to the current session and set that report as the current report of the session. By using this, you can add any number of reports to the current session. The report will be listed in the Report List present in the OLAP Client Tool Bar.

 

Code Snippet for Adding a Report

 

+------------------------------------------------------------------------------------+
| **[\[C#\]]**                                   |
|                                                                                    |
| [ //// To add a new report to current session] |
|                                                                                    |
| [\                                                                                 |
|  this.OlapClient.AddReport();]                 |
|                                                                                    |
| []                                             |
+------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------+
| **[\[VB\]]**                                  |
|                                                                                   |
| [\'// To add a new report to current session] |
|                                                                                   |
| [Me.OlapClient.AddReport()]                   |
+-----------------------------------------------------------------------------------+

 

[]{#_Remove_Report}Remove Report

 

Remove Report will remove the current report from the session by deleting it.

Code snippet for Removing the Report:

 

+-----------------------------------------------------------------------+
| **[\[C#\]]**                      |
|                                                                       |
| [//// To remove the current report from current session\              |
| this.OlapClient.RemoveReport();]  |
|                                                                       |
| []                                |
+-----------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                          |
|                                                                                           |
| [\'To remove the current report from current session] |
|                                                                                           |
| [Me.OlapClient.RemoveReport()]                        |
+-------------------------------------------------------------------------------------------+

 

[]{#_Rename_Report}Rename Report

Rename Report will get the new name for the current report and rename it with the new name.

Code snippet for Renaming the Report:

 

+-----------------------------------------------------------------------+
| **[\[C#\]]**                      |
|                                                                       |
| [//// To rename the current report \                                  |
| this.OlapClient.RenameReport();]  |
|                                                                       |
| []                                |
+-----------------------------------------------------------------------+

 

+-----------------------------------------------------------------------+
| **[\[VB\]]**                      |
|                                                                       |
| [\'To rename the current report ] |
|                                                                       |
| [Me.OlapClient.RenameReport()]    |
+-----------------------------------------------------------------------+

 

[]{#related-topics}

