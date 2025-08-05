---
title: throughc.md
original_path: WinForms_Docs/99_Uncategorized/throughc.md
created_at: 2025-08-05
---






##### Through C# {#through-c style="tab-stops: 0pt"}

To create the CardView control through C#, include the following namespace to the directives list.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                     |
|                                                                                                                                                                                      |
| [using][ Syncfusion.Windows.Tools.Controls;][] |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Next, create the CardView control as illustrated in the following code example.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                               |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [            CardView][ cardView = [new] [CardView]();]                   |
|                                                                                                                                                                                                                |
| [            [CardViewItem] cardViewItem1 = [new] [CardViewItem]();]                                  |
|                                                                                                                                                                                                                |
| [            [TextBlock] tBlock = [new] [TextBlock]() { Text = [\"John\"] };] |
|                                                                                                                                                                                                                |
| [            cardViewItem1.Content = tBlock;]                                                                                                                              |
|                                                                                                                                                                                                                |
| [            cardView.Items.Add(cardViewItem1);]                                                                                                                           |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

