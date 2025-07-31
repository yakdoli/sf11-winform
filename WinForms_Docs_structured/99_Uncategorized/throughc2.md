---
title: throughc2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\throughc2.md
created_at: 2025-07-03
---






##### Through C# {#through-c style="tab-stops: 0pt"}

To create the MenuAdv control through C#, include the following namespace to the directives list.

 

+---------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                          |
|                                                                                                                           |
| [using][ Syncfusion.Windows.Shared;] |
|                                                                                                                           |
| []                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------+

 

 Next, create the MenuAdv as follows.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[ \[C#\]]**                                                                                                                                                                                           |
|                                                                                                                                                                                                                                             |
| [MenuAdv][ mAdv = [new] [MenuAdv]();]                                                                  |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [     [MenuItemAdv] product = [new] [MenuItemAdv]() { Header = [\"Products\"] };]                          |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [     [MenuItemAdv] bi = [new] [MenuItemAdv]() { Header = [\"Business Intelligence\"] };            ]      |
|                                                                                                                                                                                                                                             |
| [     ]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                             |
| [       [MenuItemAdv] ui = [new] [MenuItemAdv]() { Header = [\"User Interface\"] };]                       |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [          [MenuItemAdv] wpf = [new] [MenuItemAdv]() { Header = [\"WPF\"] };]                              |
|                                                                                                                                                                                                                                             |
| [                ]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [            [MenuItemAdv] tools = [new] [MenuItemAdv]() { Header = [\"Tools\"] };]                        |
|                                                                                                                                                                                                                                             |
| [            [MenuItemAdv] chart = [new] [MenuItemAdv]() { Header = [\"Chart\"] };]                        |
|                                                                                                                                                                                                                                             |
| [            [MenuItemAdv] grid = [new] [MenuItemAdv]() { Header = [\"Grid\"] };]                          |
|                                                                                                                                                                                                                                             |
| [            [MenuItemAdv] diagram = [new] [MenuItemAdv]() { Header = [\"Diagram\"] };]                    |
|                                                                                                                                                                                                                                             |
| [            [MenuItemAdv]  gauge= [new] [MenuItemAdv]() { Header = [\"Gauge\"] };]                        |
|                                                                                                                                                                                                                                             |
| [            [MenuItemAdv] schedule = [new] [MenuItemAdv]() { Header = [\"Schedule\"] };]                  |
|                                                                                                                                                                                                                                             |
| [            [MenuItemAdv] edit = [new] [MenuItemAdv]() { Header = [\"Edit\"] };                         ] |
|                                                                                                                                                                                                                                             |
| [  ]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                             |
| [            wpf.Items.Add(tools);]                                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| [            wpf.Items.Add(chart);]                                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| [            wpf.Items.Add(grid);]                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [            wpf.Items.Add(diagram);]                                                                                                                                                                   |
|                                                                                                                                                                                                                                             |
| [            wpf.Items.Add(gauge);]                                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| [            wpf.Items.Add(schedule);]                                                                                                                                                                  |
|                                                                                                                                                                                                                                             |
| [            wpf.Items.Add(edit);]                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [          [MenuItemAdv] sl = [new] [MenuItemAdv]() { Header = [\"Silverlight\"] };]                       |
|                                                                                                                                                                                                                                             |
| [          ui.Items.Add(wpf);]                                                                                                                                                                          |
|                                                                                                                                                                                                                                             |
| [          ui.Items.Add(sl);]                                                                                                                                                                           |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [        [MenuItemAdv] reporting = [new] [MenuItemAdv]() { Header = [\"Reporting\"] };]                    |
|                                                                                                                                                                                                                                             |
| [        product.Items.Add(bi);]                                                                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [        product.Items.Add(ui);                ]                                                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [        product.Items.Add(reporting);]                                                                                                                                                                 |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [   mAdv.Items.Add(product);]                                                                                                                                                                           |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

