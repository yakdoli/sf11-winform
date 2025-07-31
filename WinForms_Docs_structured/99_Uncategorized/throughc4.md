---
title: throughc4.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\throughc4.md
created_at: 2025-07-03
---






##### Through C# {#through-c style="tab-stops: 0pt"}

To create the TileViewControl through C#, include the following namespace to the directives list.

 

+---------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                          |
|                                                                                                                           |
| [using][ Syncfusion.Windows.Shared;] |
|                                                                                                                           |
| []                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------+

 

Next, create the TileViewControl as follows.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                     |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [       TileViewControl][ tvControl = [new] [TileViewControl]();]               |
|                                                                                                                                                                                                                      |
| [       [TileViewItem] tvitem1 = [new] [TileViewItem]() { Header = [\"Item 1\"] };] |
|                                                                                                                                                                                                                      |
| [       [TileViewItem] tvitem2 = [new] [TileViewItem]() { Header = [\"Item 2\"] };] |
|                                                                                                                                                                                                                      |
| [       [TileViewItem] tvitem3 = [new] [TileViewItem]() { Header = [\"Item 3\"] };] |
|                                                                                                                                                                                                                      |
| [       [TileViewItem] tvitem4 = [new] [TileViewItem]() { Header = [\"Item 4\"] };] |
|                                                                                                                                                                                                                      |
| [       tvControl.Items.Add(tvitem1);]                                                                                                                                           |
|                                                                                                                                                                                                                      |
| [       tvControl.Items.Add(tvitem2);]                                                                                                                                           |
|                                                                                                                                                                                                                      |
| [       tvControl.Items.Add(tvitem3);]                                                                                                                                           |
|                                                                                                                                                                                                                      |
| [       tvControl.Items.Add(tvitem4);]                                                                                                                                           |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

This will generate the following TileViewControl.

{border="0"}

Figure 1064: TileViewControl

 

[]{#related-topics}

