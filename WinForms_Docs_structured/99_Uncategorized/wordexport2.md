---
title: wordexport2.md
original_path: WinForms_Docs/99_Uncategorized/wordexport2.md
created_at: 2025-08-05
---








  









### Word Export {#word-export style="tab-stops: 0pt"}

BI Pivot Grid for Silverlight can be exported as a Word document using Essential DocIO. The user can export the contents of the **PivotGrid** to the Word document for further archival, references and analysis purposes.

 

Call Export method

The [GridWordExport][ ]class provides support for exporting data from a PivotGrid to a Word document for verification. The following dlls should be added, along with the default dlls in the reference folder:

 

[·      ]Syncfusion.PivotGridConverter.Silverlight

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                           |
| [//// Export to Word Document]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                           |
| [SaveFileDialog][ saveFileDialog = [new] [SaveFileDialog] { DefaultExt = [\".doc\"], Filter = [\"(\*.doc)\|\*.doc\"] };\ |
| \                                                                                                                                                                                                                                                                         |
| ]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                           |
| [  [if] (saveFileDialog.ShowDialog() == [true])\                                                                                                                                                                                |
| \                                                                                                                                                                                                                                                                         |
| ]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                           |
| [{\                                                                                                                                                                                                                                                                       |
| \                                                                                                                                                                                                                                                                         |
| ]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                           |
| [    [Stream] stream = saveFileDialog.OpenFile();\                                                                                                                                                                                                |
| \                                                                                                                                                                                                                                                                         |
| ]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                           |
| [    [GridWordExport] gridWordExport = [new] [GridWordExport]([this].pivotGrid1);\                                                                                              |
| \                                                                                                                                                                                                                                                                         |
| ]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                           |
| [    gridWordExport.Export(stream);\                                                                                                                                                                                                                                      |
| \                                                                                                                                                                                                                                                                         |
| ]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                           |
| [    stream.Close();\                                                                                                                                                                                                                                                     |
| \                                                                                                                                                                                                                                                                         |
| ]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                  |
|                                                                                                                                                                                   |
| [' Export to Word]                                                                                                              |
|                                                                                                                                                                                   |
| [Dim][ saveFileDialog [As New ]SaveFileDialog() With { \_]              |
|                                                                                                                                                                                   |
| [        Key .DefaultExt = [\".doc\"], \_]                                                                            |
|                                                                                                                                                                                   |
| [        Key .Filter = [\"(\*.doc)\|\*.doc\"] \_]                                                                     |
|                                                                                                                                                                                   |
| [}]                                                                                                                                           |
|                                                                                                                                                                                   |
| [If][ saveFileDialog.ShowDialog() = [True] [Then]] |
|                                                                                                                                                                                   |
| [        [Dim] stream [As ]Stream = saveFileDialog.OpenFile()]                                      |
|                                                                                                                                                                                   |
| [        [Dim] gridWordExport  [As New ]GridWordExport([Me].pivotGrid1)]       |
|                                                                                                                                                                                   |
| [        gridWordExport.Export(stream)]                                                                                                       |
|                                                                                                                                                                                   |
| [        stream.Close()]                                                                                                                      |
|                                                                                                                                                                                   |
| [End][ [If]]                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 18: Exported Word Document from PivotGrid

**[]** 

**[]** 

[]{#related-topics}

