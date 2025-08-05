---
title: wordexport4.md
original_path: WinForms_Docs/99_Uncategorized/wordexport4.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Word Export {#word-export style="tab-stops: 0pt"}

 

PivotGrid for WPF can be exported as a Word document using Essential DocIO. The user can export the contents of the PivotGrid to the Word document for future archival, references and analysis purposes.

 

Call Export method

The [GridWordExport][]class provides support for exporting data from a PivotGrid to a Word document for verification. The following dlls should be added, along with the default dlls in the reference folder:

 

[·      ]Syncfusion.PivotGridConverter.Wpf

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                             |
|                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                   |
|                                                                                                                                                                                                              |
| [//// Export to Word Document.]                                                                                                                            |
|                                                                                                                                                                                                              |
| [SaveFileDialog] [ savedialog = [new][SaveFileDialog]();]               |
|                                                                                                                                                                                                              |
| [savedialog.AddExtension = [true];]                                                                                                                 |
|                                                                                                                                                                                                              |
| [savedialog.FileName = [\"Sample\"];]                                                                                                            |
|                                                                                                                                                                                                              |
| [savedialog.DefaultExt = [\"Doc\"];]                                                                                                             |
|                                                                                                                                                                                                              |
| [savedialog.Filter = [\"Word file (.Doc)\|\*.Doc\"];]                                                                                            |
|                                                                                                                                                                                                              |
| [if] [ (savedialog.ShowDialog() == [true])]                                                        |
|                                                                                                                                                                                                              |
| [{]                                                                                                                                                                      |
|                                                                                                                                                                                                              |
| [     fileName = savedialog.FileName;]                                                                                                                                   |
|                                                                                                                                                                                                              |
| [     [GridWordExport] wordExport = [new][GridWordExport]([this].pivotGrid1);] |
|                                                                                                                                                                                                              |
| [     wordExport.Export(fileName);]                                                                                                                                      |
|                                                                                                                                                                                                              |
| [}] []                                                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                           |
|                                                                                                                                                                                                            |
| [\' ] [Export to Word Document.]                                                                       |
|                                                                                                                                                                                                            |
| [Dim] [ savedialog [As] SaveFileDialog = [New] SaveFileDialog()]            |
|                                                                                                                                                                                                            |
| [savedialog.AddExtension = [True]]                                                                                                                |
|                                                                                                                                                                                                            |
| [savedialog.FileName = [\"Sample\"]]                                                                                                           |
|                                                                                                                                                                                                            |
| [savedialog.DefaultExt = [\"Doc\"]]                                                                                                            |
|                                                                                                                                                                                                            |
| [savedialog.Filter = [\"Word file (.Doc)\|\*.Doc\"]]                                                                                           |
|                                                                                                                                                                                                            |
| [If] [ savedialog.ShowDialog() = [True][Then]]                              |
|                                                                                                                                                                                                            |
| [    fileName = savedialog.FileName]                                                                                                                                   |
|                                                                                                                                                                                                            |
| [    [Dim] wordExport [As] GridWordExport = [New] GridWordExport([Me].pivotGrid1)] |
|                                                                                                                                                                                                            |
| [    wordExport.Export(fileName)]                                                                                                                                      |
|                                                                                                                                                                                                            |
| [End] [ [If] ] **[]**                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 25:  Exported Word Document from PivotGrid

[]{#related-topics}

