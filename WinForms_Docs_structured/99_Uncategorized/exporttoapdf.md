---
title: exporttoapdf.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\exporttoapdf.md
created_at: 2025-07-03
---








  









### Export to a PDF {#export-to-a-pdf style="tab-stops: 0pt"}

[] 

To export a chart to a PDF, call the ExportToPDF function, which returns true if exported successfully.

 

The ExporttoPDF function contains the SaveImagetoDisk argument, which specifies if the image needs to be saved separately in a disk or not.

[] 


\[C#\]

**[]** 

[chartModel.ExportToPDF(FileName, [ChartImageFormat].Jpeg, [false]);]


[] 

 

 

 

 

\
 Figure 343: Exported chart to a PDF

[] 

Chart can be exported through two ways:

[·      ]Builder

[·      ]ChartModel

[] 

[]{#related-topics}

