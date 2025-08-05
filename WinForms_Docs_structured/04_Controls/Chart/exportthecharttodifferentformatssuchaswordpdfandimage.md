---
title: exportthecharttodifferentformatssuchaswordpdfandimage.md
original_path: WinForms_Docs/04_Controls/Chart/exportthecharttodifferentformatssuchaswordpdfandimage.md
created_at: 2025-08-05
---








  









## Export the Chart to Different Formats Such as Word, PDF and Image? {#export-the-chart-to-different-formats-such-as-word-pdf-and-image style="tab-stops: 0pt"}

The export can be done using the following functions, by passing the file name along with the extension.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                           |
|                                                                                                                                                                                                  |
| [exportFileName = fileName + [\".doc\" or \".pdf\" or \".gif\"]; //Extension according to the export option.[]] |
|                                                                                                                                                                                                  |
| [this][.olapChart1.ExportIntoImage(exportFileName);]                                                        |
|                                                                                                                                                                                                  |
| [this][.olapChart1.ExportintoNewDoc(exportFileName);]                                                       |
|                                                                                                                                                                                                  |
| [this][.olapChart1.ExportIntoNewPdf(exportFileName);]                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**[]                                                                                                           |
|                                                                                                                                                                                                  |
| [exportFileName = fileName + [\".doc\" or \".pdf\" or \".gif\"]  \'Extension according to the export option.[]] |
|                                                                                                                                                                                                  |
| [Me][.olapChart1.ExportIntoImage(exportFileName)]                                                           |
|                                                                                                                                                                                                  |
| [Me][.olapChart1.ExportintoNewDoc(exportFileName)]                                                          |
|                                                                                                                                                                                                  |
| [Me][.olapChart1.ExportIntoNewPdf(exportFileName)][]      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

