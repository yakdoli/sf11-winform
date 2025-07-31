---
title: addingthroughxaml8.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\addingthroughxaml8.md
created_at: 2025-07-03
---






#### Adding through XAML {#adding-through-xaml style="tab-stops: 0pt"}

Following are the steps to add the PropertyGrid control by using Visual Studio in XAML.

1.   Create a new application in Visual Studio.

2.   In the Visual Studio Toolbox, click Syncfusion WPF Toolbox tab and select PropertyGrid.

3.   Drag-and-drop the PropertyGrid to Design View, to add PropertyGrid to your application.

4.   In the properties window, customize the properties of the PropertyGrid.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [           ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<][Window][ x][:][Class][=\"PropertyGridSample.MainWindow\"][\                                                                                                                                                                                                                |
|        [ xmlns][=\"http://schemas.microsoft.com/winfx/2006/xaml/presentation\"]\                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|        [ xmlns][:][x][=\"http://schemas.microsoft.com/winfx/2006/xaml\"]\                                                                                                                                                                                                                                                                                                                                                                                                                            |
|        [ Title][=\"MainWindow\"][ Height][=\"350\"][ Width][=\"525\"]\                                                                                                                                                                                                                                                                                                                                                                                      |
|        [ xmlns][:][syncfusion][=\"clr-namespace:Syncfusion.Windows.PropertyGrid;assembly=Syncfusion.PropertyGrid.Wpf\"\>]\                                                                                                                                                                                                                                                                                                                                                                           |
| [    ][\<][Grid][ x][:][Name][=\"LayoutRoot\"\>]\                                                                                                                                                                                                                                                                                                                                                                               |
| [        ][\<][syncfusion][:][PropertyGrid][ Margin][=\"109,32,117,47\"][ SelectedObject][=\"{][Binding][ ElementName][=LayoutRoot}\"][ BorderBrush][=\"Gray\"][ BorderThickness][=\"2\"/\>][        ]\ |
| [    ][\</][Grid][\>]\                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\</][Window][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 817: PropertyGrid\
\

[]{#related-topics}

