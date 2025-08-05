---
title: savingasanexceldocum.md
original_path: WinForms_Docs/99_Uncategorized/savingasanexceldocum.md
created_at: 2025-08-05
---








  





### Saving as an Excel Document {#saving-as-an-excel-document style="tab-stops: 0pt"}

The RDL report generated using the Report Designer can be exported as an Excel document using the following code example.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                             |
|                                                                                                                                                                                              |
| [//Instantiate the report writer with the parameter \"ReportPath\" and ]                                                                   |
|                                                                                                                                                                                              |
| [ReportDataSource Collection]                                                                                                              |
|                                                                                                                                                                                              |
| [ReportWriter ][reportWriter = new [ReportWriter](reportPath, dataSources);] |
|                                                                                                                                                                                              |
| [reportWriter.Save(\"Sample.xls\", ][WriterFormat][.Excel);]     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                  |
| [\'Instantiate the report writer with the parameter \"ReportPath\" and ]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                  |
| [ReportDataSource Collection]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                  |
| [Dim ][reportWriter [As New ]][ReportWriter][ (reportPath, dataSources)] |
|                                                                                                                                                                                                                                                                                  |
| [reportWriter.Save(\"Sample.xls\", ][WriterFormat][.Excel);]                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

