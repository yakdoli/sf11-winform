---
title: buttoncaption.md
original_path: WinForms_Docs/99_Uncategorized/buttoncaption.md
created_at: 2025-08-05
---






#### Button Caption {#button-caption style="tab-stops: 0pt"}

This feature enables you to name your SplitButton as needed.

          []

Adding Caption to the SplitButton  

You can add a button caption to the SplitButton or set the selected item as the caption. 

 

The following code illustrates how to add a caption for the button:

 

+---------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                  |
|                                                                                                   |
| [splitButton1.Text = [\"Click\"];   ] |
+---------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------+
| **[\[VB\]]**                             |
|                                                                                               |
| []                                       |
|                                                                                               |
| [splitButton1.Text = [\"Click\"]] |
+-----------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 1489: Added Button Caption

 

The following code illustrates how to set the selected item from the dropdown as the caption:

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                    |
| [ [private] [void] splitButton1_DropDowItemClicked([object] sender, [ToolStripItemClickedEventArgs] e)] |
|                                                                                                                                                                                                                                    |
| [{             ]                                                                                                                                                                               |
|                                                                                                                                                                                                                                    |
| [             splitButton1.Text = e.ClickedItem.Text;]                                                                                                                                         |
|                                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                  |
| [Private][ [Sub] splitButton1_DropDowItemClicked([ByVal] sender [As] [Object], [ByVal] e [As] ToolStripItemClickedEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                  |
| [                   splitButton1.Text = e.ClickedItem.Text]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                  |
| [End][ [Sub]]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 1490: Selected item is set as caption

 

 

[]{#related-topics}

