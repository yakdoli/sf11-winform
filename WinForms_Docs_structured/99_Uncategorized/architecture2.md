---
title: architecture2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\architecture2.md
created_at: 2025-07-03
---








  









## Architecture {#architecture style="tab-stops: 0pt"}

The Spreadsheet control supports *ControlTemplate* to define its content. By default, its content includes a *TabControlExt* object that contains number of *TabItemExt* based on sheet count. The *TabItemExt* contains a ScrollViewer object that contains a *SpreadsheetGrid* object.

 

The following sketch illustrates the Spreadsheet control architecture.

 

{border="0"}

Figure 12: Spreadsheet Architecture

*[]* 

Accessing the Underlying Grid control

The Spreadsheet control is a control derived class that has its own properties. You can use Grid control derived property namely *ActiveSpreadsheetGrid to* get its grid-like behavior. To access the underlying Grid control associated with the Spreadsheet control, you can use the *SpreadsheetControl.GridProperties.ActiveSpreadsheetGrid* property.

 

[]{#related-topics}

