---
title: workbook.md
original_path: WinForms_Docs/99_Uncategorized/workbook.md
created_at: 2025-08-05
---






##### Workbook {#workbook style="tab-stops: 0pt"}

[] 

The worksheets in a workbook can be displayed as tabs for easier view and selection of worksheets, similar to Excel. This is achieved by using the Tab Bar Splitter control. You can add any number of Tab Bar pages to the Tab Bar Splitter control, and then add the Grid control to each Tab Bar page, to get the appearance similar to the Workbook in Excel.

[] 

1.   Using C#

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                              |
|                                                                                                                                                                             |
| []                                                                                                                        |
|                                                                                                                                                                             |
| [this][.tabBarSplitterControl1.Controls.Add([this].tabBarPage1);] |
|                                                                                                                                                                             |
| [this][.tabBarSplitterControl1.Controls.Add([this].tabBarPage2);] |
|                                                                                                                                                                             |
| [this][.tabBarSplitterControl1.Controls.Add([this].tabBarPage3);] |
|                                                                                                                                                                             |
| []                                                                                                                                      |
|                                                                                                                                                                             |
| [// Adding Grid controls to the Tab Bar Pages.]                                                                           |
|                                                                                                                                                                             |
| [this][.tabBarPage1.Controls.Add([this].gridControl1);]           |
|                                                                                                                                                                             |
| [this][.tabBarPage2.Controls.Add([this].gridControl2);]           |
|                                                                                                                                                                             |
| [this][.tabBarPage3.Controls.Add([this].gridControl3);]           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                     |
|                                                                                                                                                                        |
| []                                                                                                                   |
|                                                                                                                                                                        |
| [Me][.tabBarSplitterControl1.Controls.Add([Me].tabBarPage1)] |
|                                                                                                                                                                        |
| [Me][.tabBarSplitterControl1.Controls.Add([Me].tabBarPage2)] |
|                                                                                                                                                                        |
| [Me][.tabBarSplitterControl1.Controls.Add([Me].tabBarPage3)] |
|                                                                                                                                                                        |
| []                                                                                                                                 |
|                                                                                                                                                                        |
| [\' Adding Grid controls to the Tab Bar Pages.]                                                                      |
|                                                                                                                                                                        |
| [Me][.tabBarPage1.Controls.Add([Me].gridControl1)]           |
|                                                                                                                                                                        |
| [Me][.tabBarPage2.Controls.Add([Me].gridControl2)]           |
|                                                                                                                                                                        |
| [Me][.tabBarPage3.Controls.Add([Me].gridControl3)]           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

*[Figure ][120][: Workbook]*

 

[]{#p110} 

 

[]{#related-topics}

