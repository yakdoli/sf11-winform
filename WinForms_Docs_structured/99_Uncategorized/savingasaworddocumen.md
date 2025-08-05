---
title: savingasaworddocumen.md
original_path: WinForms_Docs/99_Uncategorized/savingasaworddocumen.md
created_at: 2025-08-05
---








  





### Saving as a Word Document {#saving-as-a-word-document style="tab-stops: 0pt"}

The RDL report generated using the Report Designer can also be exported as a Word document. The following code example demonstrates how to do this.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                             |
|                                                                                                                                                                                              |
| [// Instantiate the report writer with the parameter \"ReportPath\" and ]                                                                  |
|                                                                                                                                                                                              |
| [ReportDataSource Collection]                                                                                                              |
|                                                                                                                                                                                              |
| [ReportWriter ][reportWriter = new [ReportWriter](reportPath, dataSources);] |
|                                                                                                                                                                                              |
| [reportWriter.Save(\"Sample.doc\", ][WriterFormat][.WORD);]      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                            |
| [\'Instantiate the report writer with the parameter \"ReportPath\" and ]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                            |
| [ReportDataSource Collection.]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                            |
| [Dim ][reportWriter [As New ]][ReportWriter][ (reportPath, dataSources)[]] |
|                                                                                                                                                                                                                                                                                                            |
| [reportWriter.Save(\"Sample.doc\", ][WriterFormat][.WORD);]                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

