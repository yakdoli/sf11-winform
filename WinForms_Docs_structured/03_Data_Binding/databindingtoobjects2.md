---
title: databindingtoobjects2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\databindingtoobjects2.md
created_at: 2025-07-03
---






##### Data-Binding to Objects {#data-binding-to-objects style="tab-stops: 0pt"}

The MenuAdv control also supports binding to objects. The following example shows this.

 

1.   Create a class that act as a model for MenuAdv.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [public][ [class] [Model]]                                                                       |
|                                                                                                                                                                                                                                    |
| [    {]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                    |
| [        [public] Model()]                                                                                                                                                |
|                                                                                                                                                                                                                                    |
| [        {]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [            SubItems = [new] [ObservableCollection]\<[Model]\>();]                                                       |
|                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [        [public] [string] Header { [get]; [set]; }]                                                       |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [        [public] [ObservableCollection]\<[Model]\> SubItems { [get]; [set]; }] |
|                                                                                                                                                                                                                                    |
| [        ]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                    |
| [    }]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   Create a *ViewModel* class and initialize the items.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [  [public] [class] [ViewModel]]                                                                                              |
|                                                                                                                                                                                                                                     |
| [    {]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                     |
| [        [public] ViewModel()]                                                                                                                                             |
|                                                                                                                                                                                                                                     |
| [        {]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                     |
| [            MenuItems = [new] [ObservableCollection]\<[Model]\>();]                                                       |
|                                                                                                                                                                                                                                     |
| [            PopulateData();]                                                                                                                                                                   |
|                                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [        [public] [ObservableCollection]\<[Model]\> MenuItems { [get]; [set]; }] |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [        [private] [void] PopulateData()]                                                                                                             |
|                                                                                                                                                                                                                                     |
| [        {]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                     |
| [            [Model] product = [new] [Model]() { Header = [\"Products\"] };]                       |
|                                                                                                                                                                                                                                     |
| [            PopulateSubSubItems(product);]                                                                                                                                                     |
|                                                                                                                                                                                                                                     |
| [            MenuItems.Add(product);            ]                                                                                                                                               |
|                                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [        [private] [void] PopulateSubSubItems([Model] product)]                                                               |
|                                                                                                                                                                                                                                     |
| [        {]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                     |
| [            [Model] bi = [new] [Model]() { Header = [\"Business Intelligence\"] };]               |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [            [Model] ui = [new] [Model]() { Header = [\"User Interface\"] };]                      |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [            [Model] wpf = [new] [Model]() { Header = [\"WPF\"] };]                                |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [            [Model] tools = [new] [Model]() { Header = [\"Tools\"] };]                            |
|                                                                                                                                                                                                                                     |
| [            [Model] chart = [new] [Model]() { Header = [\"Chart\"] };]                            |
|                                                                                                                                                                                                                                     |
| [            [Model] grid = [new] [Model]() { Header = [\"Grid\"] };]                              |
|                                                                                                                                                                                                                                     |
| [            [Model] diagram = [new] [Model]() { Header = [\"Diagram\"] };]                        |
|                                                                                                                                                                                                                                     |
| [            [Model] gauge = [new] [Model]() { Header = [\"Gauge\"] };]                            |
|                                                                                                                                                                                                                                     |
| [            [Model] schedule = [new] [Model]() { Header = [\"Schedule\"] };]                      |
|                                                                                                                                                                                                                                     |
| [            [Model] edit = [new] [Model]() { Header = [\"Edit\"] };]                              |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [            wpf.SubItems.Add(tools);]                                                                                                                                                          |
|                                                                                                                                                                                                                                     |
| [            wpf.SubItems.Add(chart);]                                                                                                                                                          |
|                                                                                                                                                                                                                                     |
| [            wpf.SubItems.Add(grid);]                                                                                                                                                           |
|                                                                                                                                                                                                                                     |
| [            wpf.SubItems.Add(diagram);]                                                                                                                                                        |
|                                                                                                                                                                                                                                     |
| [            wpf.SubItems.Add(gauge);]                                                                                                                                                          |
|                                                                                                                                                                                                                                     |
| [            wpf.SubItems.Add(schedule);]                                                                                                                                                       |
|                                                                                                                                                                                                                                     |
| [            wpf.SubItems.Add(edit);]                                                                                                                                                           |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [            [Model] sl = [new] [Model]() { Header = [\"Silverlight\"] };]                         |
|                                                                                                                                                                                                                                     |
| [            ui.SubItems.Add(wpf);]                                                                                                                                                             |
|                                                                                                                                                                                                                                     |
| [            ui.SubItems.Add(sl);]                                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [            [Model] reporting = [new] [Model]() { Header = [\"Reporting\"] };]                    |
|                                                                                                                                                                                                                                     |
| [            product.SubItems.Add(bi);]                                                                                                                                                         |
|                                                                                                                                                                                                                                     |
| [            product.SubItems.Add(ui);]                                                                                                                                                         |
|                                                                                                                                                                                                                                     |
| [            product.SubItems.Add(reporting);]                                                                                                                                                  |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                     |
| [    }]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

3.   Create a *ViewModel* instance and use it as *DataContext* for the root window.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**[]                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][Window.DataContext][\>][]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                          |
| [   ][\<][local][:][ViewModel][/\>][] |
|                                                                                                                                                                                                                                                                                                                                                                                          |
| [\</][Window.DataContext][\>]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.   Now configure the *ItemsSource* and *ItemTemplate* of MenuAdv.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**[]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][syncfusion][:][MenuAdv][ ItemsSource][=\"{][Binding][ MenuItems][}\"\>][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [            ][\<][syncfusion][:][MenuAdv.ItemTemplate][\>][]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [                ][\<][HierarchicalDataTemplate][ ItemsSource][=\"{][Binding][ SubItems][}\"\>][]                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [                    ][\<][TextBlock][ Text][=\"{][Binding][ Header][}\" /\>][]                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [                ][\</][HierarchicalDataTemplate][\>][]                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [            ][\</][syncfusion][:][MenuAdv.ItemTemplate][\>][]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [        ][\</][syncfusion][:][MenuAdv][\>][]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Implementing the above code will generate the following control.

 

{border="0"}

Figure 714: MenuAdv with Object bindng

 

[]{#related-topics}

