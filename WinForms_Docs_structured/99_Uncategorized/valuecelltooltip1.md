---
title: valuecelltooltip1.md
original_path: WinForms_Docs/99_Uncategorized/valuecelltooltip1.md
created_at: 2025-08-05
---








  





### Value Cell ToolTip {#value-cell-tooltip style="tab-stops: 0pt"}

The OLAP grid provides cell information (measure, column header value, row header value, and cell value) when the mouse pointer hovers on the value cells. This property can be enabled as shown in the following code snippets:

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                  |
|                                                                                                                                                                                                   |
| [// Enabling Value Cell ToolTip.]                                                                                                               |
|                                                                                                                                                                                                   |
| [this][.OlapGrid1.ShowValueCellTooltip = [true];][] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                         |
|                                                                                                                                                          |
| [\'Enabling Value Cell ToolTip.][]                                 |
|                                                                                                                                                          |
| [Me][.OlapGrid1.ShowValueCellTooltip = [True]] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 28: OLAP Grid with Value Cell ToolTip

 

Table 15: Properties


  ---------------------- -------------------------------------------------------------------------------- ------------- -----------
  Property               Description                                                                      Type          Data Type
  ShowHeaderToolTip      Gets or sets a value to show or hide drill down information on Header Tooltip.   Server side   boolean
  ShowValueCellTooltip   Gets or sets a value to showor hide Value cell Tooltip.                          Server side   boolean
  ---------------------- -------------------------------------------------------------------------------- ------------- -----------


[] 

Sample Location

A sample demo is available in the following location:

**..\\Syncfusion\\EssentialStudio\\\<VersionNumber\>\\BI\\Web\\OlapGrid.Web\\Samples\\3.5\\Tooltip\\Tooltip Demo**

 

[]{#related-topics}

