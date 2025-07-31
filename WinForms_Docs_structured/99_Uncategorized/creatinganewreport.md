---
title: creatinganewreport.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\creatinganewreport.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Creating a new report {#creating-a-new-report style="tab-stops: 0pt"}

 

On clicking **New report**, a dialog appears asking for the report name and on the **Ok** event a new report is added to the existing **Report List** clearing all the existing report(s).

[] 

{border="0"}

Figure 16: Creating a new report

[] 

{border="0"}

Figure 17: Report Name

This can also be done through an **API** which is mentioned in the following code snippet.

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                       |
|                                                                                                                                                                                    |
| []                                                                                                                                             |
|                                                                                                                                                                                    |
| [this] [.olapClient1.] [CreateNewReport();] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[VB\]]                                                                                                                                    |
|                                                                                                                                                                                 |
| []                                                                                                                            |
|                                                                                                                                                                                 |
| [Me] [.olapClient1.] [CreateNewReport()] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

