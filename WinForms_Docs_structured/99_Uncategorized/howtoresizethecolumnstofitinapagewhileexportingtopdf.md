---
title: howtoresizethecolumnstofitinapagewhileexportingtopdf.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoresizethecolumnstofitinapagewhileexportingtopdf.md
created_at: 2025-07-03
---






#### How to resize the columns to fit in a page while exporting to PDF? {#how-to-resize-the-columns-to-fit-in-a-page-while-exporting-to-pdf style="tab-stops: 0pt"}

            To resize columns to fit in a page, you can use the property **ExportRange** of the **GridPDFConverter.** The property is used to set number of rows to be exported in a page. The **ExportToPdfWithMerge** method is used to export the grid.

Example

**[]** 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[C#]**                                                                                                                                                                                            |
|                                                                                                                                                                                                                                         |
| [    GridPDFConverter pdfConvertor = [new] GridPDFConverter();]                                                                                                                |
|                                                                                                                                                                                                                                         |
| [         ][// Range of rows to be exported in a PDF file][]                                     |
|                                                                                                                                                                                                                                         |
| [         pdfConvertor.ExportRange = 40;]                                                                                                                                                           |
|                                                                                                                                                                                                                                         |
| [      ]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                         |
| [        //Merged Export][]                                                                                                                       |
|                                                                                                                                                                                                                                         |
| [        pdfConvertor.ExportToPdfWithMerge([ref] doc, [this].gridGroupingControl1.TableControl );]                                                        |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [       [//To resize the column to fit in PDF]]                                                                                                                               |
|                                                                                                                                                                                                                                         |
| [       float][ temppercent = currentPercent;]                                                                                                     |
|                                                                                                                                                                                                                                         |
| [       [this].gridGroupingControl1.BeginUpdate();]                                                                                                                            |
|                                                                                                                                                                                                                                         |
| [       PdfDocument doc = [new] PdfDocument();]                                                                                                                                |
|                                                                                                                                                                                                                                         |
| [       Hashtable][ ht = [new] [Hashtable]();]                                                     |
|                                                                                                                                                                                                                                         |
| [       [for] ([int] i = 0; i \< gridGroupingControl1.TableDescriptor.Columns.Count; i++)]                                                                |
|                                                                                                                                                                                                                                         |
| [                       ht.Add(i, gridGroupingControl1.TableDescriptor.Columns\[i\].Width)]                                                                                                         |
|                                                                                                                                                                                                                                         |
| [       [float] gridWidth = [this].gridGroupingControl1.TableModel.ColWidths.GetTotal(0,            gridGroupingControl1.TableDescriptor.Columns.Count);] |
|                                                                                                                                                                                                                                         |
| [       [if] (gridWidth \> doc.PageSettings.Width + 80)]                                                                                                                       |
|                                                                                                                                                                                                                                         |
| [          {]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                         |
| [             [float] scale = (gridWidth / (doc.PageSettings.Width + 80)) - currentPercent;]                                                                                   |
|                                                                                                                                                                                                                                         |
| [                zoomGrid(currentPercent - scale);]                                                                                                                                                 |
|                                                                                                                                                                                                                                         |
| [          }]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

 

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[VB]**                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                             |
| **[         ]**[Dim][ pdfConvertor [As] [New] GridPDFConverter()]                                                                        |
|                                                                                                                                                                                                                                                                                                             |
| [     ]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                             |
| [         \'Range of rows to be exported in a PDF file][]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                             |
| [          pdfConvertor.ExportRange = 40]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                             |
| [      \'Merged Export][]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                             |
| [       pdfConvertor.ExportToPdfWithMerge(doc, [Me].gridGroupingControl1.TableControl)]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                             |
| [   \'To Resize the column to fit in PDF][]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                             |
| [       Dim][ temppercent [As] [Single] = currentPercent]                                                                                                                    |
|                                                                                                                                                                                                                                                                                                             |
| [       Me][.gridGroupingControl1.BeginUpdate()]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                             |
| [       Dim][ doc [As] [New] PdfDocument()]                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                             |
| [       Dim][ ht [As] [New] Hashtable()]                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                             |
| [       For][ i [As] [Integer] = 0 [To] gridGroupingControl1.TableDescriptor.Columns.Count - 1]                                                         |
|                                                                                                                                                                                                                                                                                                             |
| [      ht.Add(i, gridGroupingControl1.TableDescriptor.Columns(i).Width)]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                             |
| [       Next][ i]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                             |
| [       Dim][ gridWidth [As] [Single] = [Me].gridGroupingControl1.TableModel.ColWidths.GetTotal(0, gridGroupingControl1.TableDescriptor.Columns.Count)] |
|                                                                                                                                                                                                                                                                                                             |
| [       If][ gridWidth \> doc.PageSettings.Width + 80 [Then]]                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                             |
| [                        [Dim] scale [As] [Single] = (gridWidth / (doc.PageSettings.Width + 80)) - currentPercent]                                                                                       |
|                                                                                                                                                                                                                                                                                                             |
| [            zoomGrid(currentPercent - scale)]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                             |
| [       [End] [If]]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

 

 

[]{#related-topics}

