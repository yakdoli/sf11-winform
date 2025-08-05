---
title: exporttoadocument.md
original_path: WinForms_Docs/99_Uncategorized/exporttoadocument.md
created_at: 2025-08-05
---








  









### Export to a Document {#export-to-a-document style="tab-stops: 0pt"}

**[]** 

**[]** 

To export a chart to a document, call the **ExportToDocument** function by specifying the **DocIO** FormatType as the **DOC** format, which returns true if exported successfully.

 

The **ExporttoDocument** function contains the **SaveImagetoDisk** argument, which specifies if the image needs to be saved separately in a disk or not.

 

**[]** 


\[C#\]

 

[chartModel.ExportToDocument(FileName, [ChartImageFormat].Jpeg, , [bool ]IsSaveimagetoDisk, Syncfusion.DocIO.[FormatType].Doc);]

[] 


[] 

[] 

{border="0"}

Figure 341: Exported chart to a document

[] 

[]{#related-topics}

