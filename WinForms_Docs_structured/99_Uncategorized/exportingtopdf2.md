---
title: exportingtopdf2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\exportingtopdf2.md
created_at: 2025-07-03
---








  









### Exporting to PDF {#exporting-to-pdf style="tab-stops: 0pt"}

**[]** 

**Essential BI Olap Chart** for web can be exported into a PDF file as an image using **Essential PDF**. The **Olap Chart** provides APIs to convert it to an image, while **Essential PDF** lets you insert this image into a PDF file programmatically as follows:

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                             |
|                                                                                                                                                                                            |
| [this.][olapChart1][.ExportToPdf(\"Sample.pdf\");] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**[]                                                                      |
|                                                                                                                                                                                         |
| [Me.][olapChart1][.ExportToPdf(\"Sample.pdf\")] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

 

Figure 46: Exported to PDF Format

 

 

Table 25: [ExportToPdf]

 


  ------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------- ------------------------------------ ------------------------------ ------------------------------------- ----------------------------------------
  Methods                                                [Description]                                                                                                [Parameters]   [Type]   [Return Type]   [Reference Link]
  [ExportToPdf(String fileName)]   Exports a chart into a new PDF file with the specified file name. It takes the file name as a parameter.[]   string                               Server side                    void                                  \-
  ------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------- ------------------------------------ ------------------------------ ------------------------------------- ----------------------------------------


 

Sample Location

 

A sample demo is available at the following location:

 

**..\\Syncfusion\\EssentialStudio\\\<Version Number\>\\BI\\Web\\OlapChart.Web\\Samples\\3.5\\** **Exporting\\Exporting Chart Demo\\**[]

 

[]{#related-topics}

