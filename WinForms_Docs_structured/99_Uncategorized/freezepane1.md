---
title: freezepane1.md
original_path: WinForms_Docs/99_Uncategorized/freezepane1.md
created_at: 2025-08-05
---






#### FreezePane {#freezepane style="tab-stops: 0pt"}

 

It is difficult to read and understand very large spreadsheets. When you scroll too far to the right or down, you will not be able to view the headings that are located at the top and at the the left side of the worksheet. Without the headings, its hard to keep track of the columns or rows of data, you are currently viewing.

 

Excel features Freeze Panes to avoid this problem. This feature can be enabled by selecting Freeze option from the Window menu. It allows you to \"freeze\" certain areas or panes of the spreadsheet, so that they remain visible at all times while scrolling to the right or bottom. Headings make it easier to read the data in the spreadsheet.

 

XlsIO provides support for the freeze panes functionality through the FreezePanes method of IRange.

  

+----------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                               |
|                                                                                                                |
| **[]**                                                                     |
|                                                                                                                |
| [// Applying Freeze Pane to the sheet by specifying a cell.] |
|                                                                                                                |
| [sheet.Range\[[\"B2\"]\].FreezePanes();]           |
+----------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                           |
|                                                                                                                |
| **[]**                                                                     |
|                                                                                                                |
| [\' Applying Freeze Pane to the sheet by specifying a cell.] |
|                                                                                                                |
| [sheet.Range([\"B2\"]).FreezePanes()]               |
+----------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 148: XlsIO with Freeze Pane[]

 

XlsIO also allows you to scroll to the first row in the bottom pane and first column in the right pane. It helps you to navigate to the top row while opening a spreadsheet with large number of rows/columns. Note that this works only with the sheet that has the freeze panes.

 

+-----------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                    |
|                                                                                                     |
| **[]**                                                          |
|                                                                                                     |
| [// Sets first visible row in the bottom pane.]   |
|                                                                                                     |
| [sheet.FirstVisibleRow = 2;]                      |
|                                                                                                     |
| []                                                |
|                                                                                                     |
| [// Sets first visible column in the right pane.] |
|                                                                                                     |
| [sheet.FirstVisibleColumn = 2; ]                  |
+-----------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                |
|                                                                                                     |
| **[]**                                                          |
|                                                                                                     |
| [\' Sets first visible row in the bottom pane.]   |
|                                                                                                     |
| [sheet.FirstVisibleRow = 2]                       |
|                                                                                                     |
| []                                                |
|                                                                                                     |
| [\' Sets first visible column in the right pane.] |
|                                                                                                     |
| [sheet.FirstVisibleColumn = 2]                    |
+-----------------------------------------------------------------------------------------------------+


 

{border="0"}Note: FirstVisibleColumn and FirstVisibleRow indexes are \"zero-based\".


 

[]{#related-topics}

