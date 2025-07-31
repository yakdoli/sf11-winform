---
title: pdfexport5.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\pdfexport5.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### PDF Export {#pdf-export style="tab-stops: 0pt"}

 

PivotGrid for WPF can be exported as a PDF file using Essential PDF. . The user can export the contents of the PivotGrid to the PDF document for future archival, references and analysis purposes.

 

Call Export method

The [GridPdfExport][]class provides support for exporting data from a PivotGrid to a PDF document for verification. The following dlls should be added, along with the default dlls in the reference folder:

 

[·      ]Syncfusion.PivotGridConverter.Wpf

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                          |
|                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                |
|                                                                                                                                                                                                           |
| [//// Export to PDF.]                                                                                                                                   |
|                                                                                                                                                                                                           |
| [SaveFileDialog] [ savedialog = [new][SaveFileDialog]();]            |
|                                                                                                                                                                                                           |
| [savedialog.AddExtension = [true];]                                                                                                              |
|                                                                                                                                                                                                           |
| [savedialog.FileName = [\"Sample\"];]                                                                                                         |
|                                                                                                                                                                                                           |
| [savedialog.DefaultExt = [\"pdf\"];]                                                                                                          |
|                                                                                                                                                                                                           |
| [savedialog.Filter = [\"Pdf file (.pdf)\|\*.pdf\"];]                                                                                          |
|                                                                                                                                                                                                           |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                           |
| [if] [ (savedialog.ShowDialog() == [true])]                                                     |
|                                                                                                                                                                                                           |
| [{]                                                                                                                                                                   |
|                                                                                                                                                                                                           |
| [     fileName = savedialog.FileName;]                                                                                                                                |
|                                                                                                                                                                                                           |
| [     [GridPdfExport] pdfExport = [new][GridPdfExport]([this].pivotGrid1);] |
|                                                                                                                                                                                                           |
| [     pdfExport.Export(fileName);]                                                                                                                                    |
|                                                                                                                                                                                                           |
| [}] []                                                                                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                        |
|                                                                                                                                                                                                         |
| **[]**                                                                                                                                                              |
|                                                                                                                                                                                                         |
| [\' ] [Export to PDF.]                                                                              |
|                                                                                                                                                                                                         |
| [Dim] [ savedialog [As] SaveFileDialog = [New] SaveFileDialog()]         |
|                                                                                                                                                                                                         |
| [savedialog.AddExtension = [True]]                                                                                                             |
|                                                                                                                                                                                                         |
| [savedialog.FileName = [\"Sample\"]]                                                                                                        |
|                                                                                                                                                                                                         |
| [savedialog.DefaultExt = [\"pdf\"]]                                                                                                         |
|                                                                                                                                                                                                         |
| [savedialog.Filter = [\"Pdf file (.pdf)\|\*.pdf\"]]                                                                                         |
|                                                                                                                                                                                                         |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                         |
| [If] [ savedialog.ShowDialog() = [True][Then]]                           |
|                                                                                                                                                                                                         |
| [    fileName = savedialog.FileName]                                                                                                                                |
|                                                                                                                                                                                                         |
| [    [Dim] pdfExport [As] GridPdfExport = [New] GridPdfExport([Me].pivotGrid1)] |
|                                                                                                                                                                                                         |
| [    pdfExport.Export(fileName)]                                                                                                                                    |
|                                                                                                                                                                                                         |
| [End] [ [If] ] **[]**                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 23:  Exported PDF document from PivotGrid

 

[]{#related-topics}

