---
title: zooming5.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\zooming5.md
created_at: 2025-07-03
---








  









### Zooming {#zooming style="tab-stops: 0pt"}

 

Zooming feature controls the current document that appears on the screen, no matter how big or small it is. This enables reading the charts and figures in your Microsoft Excel spreadsheet without finding any difficulty.

 

Excel allows zooming the worksheet/range of cells to fit into the window. Default value of Excel zooming is 100 percent, and can be zoomed till 400 percent. Minimum Zooming is 10 percent.

 

{border="0"}

Figure 150: Zoom dialog box in Excel[]

[] 

Zooming in XlsIO

 

XlsIO allows to zoom a worksheet by using the **Zoom** property of **IWorksheet**. It returns or sets the display size of the window as a percentage (100 equals normal size, 200 equals double size, and so on).

 

Following code example illustrates how to zoom a worksheet to 150 percent.

 

+--------------------------------------------------------------------------------+
| **[\[C#\]]**                               |
|                                                                                |
| **[]**                                     |
|                                                                                |
| [// Zooming to 150 percent.] |
|                                                                                |
| [sheet.Zoom = 150;]                        |
+--------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------+
| **[\[VB\]]**                              |
|                                                                               |
| **[]**                                    |
|                                                                               |
| [// Zooming to 150 percent] |
|                                                                               |
| [sheet.Zoom = 150]                        |
+-------------------------------------------------------------------------------+

 

[]{#related-topics}

