---
title: addacustomreport.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\addacustomreport.md
created_at: 2025-07-03
---








  









## Add a Custom Report {#add-a-custom-report style="tab-stops: 0pt"}

To add a custom report:

Use the AddCustomReport method available in OlapClient.

It will get report name and an OlapReport as argument and add the given report to current report list of OlapClient.

The following is the code snippet for adding the Custom Report:

 

+------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                           |
|                                                                                                            |
| [//// To add custom report\                                                                                |
| this.OlapClient.AddCustomReport(\"SalesReport\", CreateOlapReport());] |
|                                                                                                            |
| []                                                                     |
+------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                         |
|                                                                                                          |
| [\'To add custom report]                                             |
|                                                                                                          |
| [Me.OlapClient.AddCustomReport(\"SalesReport\", CreateOlapReport())] |
+----------------------------------------------------------------------------------------------------------+

 

The CreateOlapReport() will be in the following link.

See also 

[]{#related-topics}

