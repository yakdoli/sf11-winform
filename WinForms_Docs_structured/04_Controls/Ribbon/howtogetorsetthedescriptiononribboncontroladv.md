---
title: howtogetorsetthedescriptiononribboncontroladv.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Ribbon\howtogetorsetthedescriptiononribboncontroladv.md
created_at: 2025-07-03
---






##### How to get or set the description on RibbonControlAdv? {#how-to-get-or-set-the-description-on-ribboncontroladv style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

The **GetDescription** or **SetDescription** methods of the RibbonControlAdv can be used to gets / sets the text that is displayed with the component in the quick panel customizing dialog.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                          |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                         |
| [//Gets the description]                                                                                                                                                              |
|                                                                                                                                                                                                                                         |
| [this][.ribbonControlAdv1.GetDescription([this].toolStripTabItem1);]                                                          |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                         |
| [//Sets the description]                                                                                                                                                              |
|                                                                                                                                                                                                                                         |
| [this][.ribbonControlAdv1.SetDescription([this].toolStripTabItem1, [\"This is a drop down button\"]);] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                 |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                    |
| [\'Gets the description]                                                                                                                                                         |
|                                                                                                                                                                                                                                    |
| [this][.ribbonControlAdv1.GetDescription([this].toolStripTabItem1);]                                                     |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                                    |
| [\'Sets the description]                                                                                                                                                         |
|                                                                                                                                                                                                                                    |
| [Me][.ribbonControlAdv1.SetDescription([Me].toolStripTabItem1, [\"This is a drop down button\"])] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 1468: Customize Quick Access Toolbar Dialog with Description at Run Time

 

[]{#related-topics}

