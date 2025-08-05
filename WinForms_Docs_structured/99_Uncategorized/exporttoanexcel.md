---
title: exporttoanexcel.md
original_path: WinForms_Docs/99_Uncategorized/exporttoanexcel.md
created_at: 2025-08-05
---








  









### Export to an Excel {#export-to-an-excel style="tab-stops: 0pt"}

[] 

To export a chart to an Excel, call the **ExportToExcel** function, which returns true if exported successfully.

 

The **ExporttoExcel** function contains the **SaveImagetoDisk** argument, which specifies if the image needs to be saved separately in a disk or not.

[] 


\[C#\]

**[]** 

[chartModel.ExportT]

[oExcel(FileName, [ChartImageFormat].Jpeg, [bool ]IsSaveImagetoDisk);]

[] 


[] 

{border="0"}

Figure 342: Exported chart to an Excel

[] 

[]{#related-topics}

