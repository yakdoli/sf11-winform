---
title: report.md
original_path: WinForms_Docs/99_Uncategorized/report.md
created_at: 2025-08-05
---








  









### Report {#report style="tab-stops: 0pt"}

Report List

**Report List** will hold all the reports of the current session of the OLAP Client control.

{border="0"}

 

{border="0"}

 

Figure 28: Report List

On report change

When we make a change in the report, all the controls will get populated with the data contained in the selected report.

The Cube Dimension Browser will get populated with the cube data mentioned in the selected report.

Each axis in the Axis Element Builder will get loaded with the appropriate element mentioned in the selected report.

The Chart and Grid will reflect the output of the selected report.

 

[]{#_Creating_a_new}Creating a new report

On clicking **Create a new report**, a dialog appears asking for the report name and on the **Ok** event a new report is added to the existing **Report List** clearing all the existing report(s).

[] 

{border="0"}

 

Figure 29: Creating a new report

[] 

{border="0"}

 

Figure 30: Report Name

 

 

This can also be done through an **API** which is mentioned in the following code snippet.

+------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                             |
|                                                                                                                              |
| [this][.olapClient1.CreateNewReport();] |
+------------------------------------------------------------------------------------------------------------------------------+

 

 

+---------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                          |
|                                                                                                                           |
| [Me][.olapClient1.CreateNewReport()] |
+---------------------------------------------------------------------------------------------------------------------------+

 

Adding a new report

On clicking **Add a new report**, a dialog appears asking for the report name and on the **Ok** event a new report is added to the existing report list.

[] 

{border="0"}

 

Figure 31: Add a new report

[] 

{border="0"}

 

Figure 32: Report Name

[]{#_Removing_a_report}Removing a report

On clicking **Remove the selected report**, the current report is removed. If only one report is available in the report list, then it will be automatically disabled.

[] 

{border="0"}

 

Figure 33: Remove the selected report

[] 

{border="0"}

 

Figure 34: Selecting the desired report for deletion

 

This can also be done through an **API** which is mentioned in the following code snippet.

+---------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                          |
|                                                                                                                           |
| [this][.olapClient1.RemoveReport();] |
+---------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                        |
|                                                                                                                         |
| [Me][.olapClient1.RemoveReport ()] |
+-------------------------------------------------------------------------------------------------------------------------+

 

 

Renaming a report

On clicking **Rename the selected report**, a dialog appears asking for a new report name to replace the existing report name.

[] 

{border="0"}

 

Figure 35: Rename the selected report

 

{border="0"}

 

Figure 36: Report Name

[]{#_Saving_a_report}Saving a report

**Save the current report** stores the current report set contained in the report list in a user specified location.

{border="0"}

 

Figure 37: Save the current report

{border="0"}

 

Figure 38[: Saving the report]

This can also be done through an **API** which is mentioned in the following code snippet.

+----------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                           |
|                                                                                                                            |
| [this][.olapClient1.SaveReportSet();] |
+----------------------------------------------------------------------------------------------------------------------------+

 

 

+--------------------------------------------------------------------------+
| **[\[VB\]]**                         |
|                                                                          |
| **[Me.olapClient1.SaveReportSet()]** |
+--------------------------------------------------------------------------+

 

[]{#_Loading_a_report}Loading a report

**Load saved report** option in the toolbar loads a report from the user specified location and binds it in the report list as well as in the *chart and grid* controls.

{border="0"}

{border="0"}

 

Figure 39: Loading a report

[]{#related-topics}

