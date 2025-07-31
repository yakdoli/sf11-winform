---
title: howtoassigntaskfortoolstripitemwhenitisclicked.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoassigntaskfortoolstripitemwhenitisclicked.md
created_at: 2025-07-03
---






##### How to assign task for ToolStrip item when it is clicked? {#how-to-assign-task-for-toolstrip-item-when-it-is-clicked style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This can be done by handling the **ItemClicked** event and assigning value for **ClickedItem** property.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                     |
| [private][ [void] toolStripEx1_ItemClicked([object] sender, [ToolStripItemClickedEventArgs] e)] |
|                                                                                                                                                                                                                                                     |
| [{]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                     |
| [    [switch] (e.ClickedItem.Text [as] [string])]                                                                                                |
|                                                                                                                                                                                                                                                     |
| [    {]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                     |
| [        [case] [\"toolStripLabel1\"]:]                                                                                                                             |
|                                                                                                                                                                                                                                                     |
| [            e.ClickedItem.ForeColor = [Color].Red;]                                                                                                                                       |
|                                                                                                                                                                                                                                                     |
| [            [break];]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                     |
| [        [case] [\"toolStripSplitButton1\"]:]                                                                                                                       |
|                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                     |
| [            e.ClickedItem.DisplayStyle = [ToolStripItemDisplayStyle].][ImageAndText][;]                           |
|                                                                                                                                                                                                                                                     |
| [            [break];]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                     |
| [    }]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                     |
| [} ][]                                                                                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                           |
| [Private][ [Sub] toolStripEx1_ItemClicked([ByVal] sender [As] [Object], [ByVal] e [As] ToolStripItemClickedEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                           |
| [    [Select] [Case] [CType](ConversionHelpers.AsWorkaround(e.ClickedItem.Text, [GetType]([String])), [String])]                                                        |
|                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                           |
| [        [Case] [\"toolStripLabel1\"]]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                           |
| [            e.ClickedItem.ForeColor = Color.Red]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                           |
| [            [\' break ]]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                           |
| [        [Case] [\"toolStripSplitButton1\"]]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                           |
| [            e.ClickedItem.DisplayStyle = ToolStripItemDisplayStyle.ImageAndText]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                           |
| [            [\' break ]]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                           |
| [    [End] [Select]]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                           |
| [End][ [Sub]][]                                                                                                                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

