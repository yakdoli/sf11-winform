---
title: savingasapdfdocument.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\savingasapdfdocument.md
created_at: 2025-07-03
---








  





### Saving as a PDF Document {#saving-as-a-pdf-document style="tab-stops: 0pt"}

The RDL report generated using the Report Designer can be exported as a PDF document using the following code.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                             |
|                                                                                                                                                                                              |
| [//Instantiate the report writer with the parameter \"ReportPath\" and ]                                                                   |
|                                                                                                                                                                                              |
| ["ReportDataSource" Collection]                                                                                                            |
|                                                                                                                                                                                              |
| [ReportWriter ][reportWriter = new [ReportWriter](reportpath, dataSources);] |
|                                                                                                                                                                                              |
| [reportWriter.Save(\"Sample.pdf\", ][WriterFormat][.PDF);]       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                  |
| [\'Instantiate the report writer with the parameter \"ReportPath\" and ]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                  |
| [ReportDataSource Collection]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                  |
| [Dim ][reportWriter [As New ]][ReportWriter][ (reportpath, dataSources)] |
|                                                                                                                                                                                                                                                                                  |
| [reportWriter.Save(\"Sample.pdf\", ][WriterFormat][.PDF);]                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

