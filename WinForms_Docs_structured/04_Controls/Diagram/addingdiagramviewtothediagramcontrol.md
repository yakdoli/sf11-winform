---
title: addingdiagramviewtothediagramcontrol.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Diagram\addingdiagramviewtothediagramcontrol.md
created_at: 2025-07-03
---








  









### Adding Diagram View to the Diagram Control {#adding-diagram-view-to-the-diagram-control style="tab-stops: 0pt"}

[] 

The view obtains items of data from the model and presents them to the user. It typically manages the overall layout of the data obtained from the model.

 

Apart from presenting the data, view also handles navigation between the items, and some aspects of item selection. The views also implement basic user interface features, such as rulers, and drag and drop.

 

A view can be constructed without a model, but a model must be provided before it can display useful information. Views can also render additional visual information that does not exist inside the model such as bounding boxes and grids. These additional view-specific objects are referred to as decorators, because they provide additional visual aids and window dressing to the view; but they are not actually a part of the model.

 

The following code illustrates adding a Diagram View to the Diagram control:

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<][UserControl][ x][:][Class][=\"SilverlightApplication1.MainPage\"][ xmlns][=\"http://schemas.microsoft.com/winfx/2006/xaml/presentation\"]                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [xmlns][:][x][=\"http://schemas.microsoft.com/winfx/2006/xaml\"][  Height][=\"400\"][ Width][=\"600\"]                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [xmlns][:][sfdiagram][=\"clr-namespace:Syncfusion.Windows.Diagram;assembly=Syncfusion.Diagram.Silverlight\"][ xmlns][:][local][=\"clr-namespace:SilverlightApplication1\"\>]                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [    ][\<][Grid][ Name][=\"diagramgrid\"\>]                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [        ][\<][sfdiagram][:][DiagramControl][ IsSymbolPaletteEnabled][=\"True\"\>]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [            ][\<][sfdiagram][:][DiagramControl.View][\>]                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [                ][\<][sfdiagram][:][DiagramView][ \>\</][sfdiagram][:][DiagramView][\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [            ][\</][sfdiagram][:][DiagramControl.View][\>]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [        ][\</][sfdiagram][:][DiagramControl][\>]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [    ][\</][Grid][\>]                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\</][UserControl][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                         |
|                                                                                                                                                                                        |
| []                                                                                                                                    |
|                                                                                                                                                                                        |
| [DiagramControl][ dc = [new] [DiagramControl]();] |
|                                                                                                                                                                                        |
| [dc.IsSymbolPaletteEnabled = [true];]                                                                                         |
|                                                                                                                                                                                        |
| [DiagramView][ view = [new] [DiagramView]();]     |
|                                                                                                                                                                                        |
| [view.Bounds = [new] System.Drawing.[Thickness](0, 0, 1000, 1000);]                                   |
|                                                                                                                                                                                        |
| [dc.View = view;]                                                                                                                                  |
|                                                                                                                                                                                        |
| [diagramgrid.Children.Add(dc);]                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []{#p16}**[\[VB\]]**                                                                                                                          |
|                                                                                                                                                                                                 |
| []                                                                                                                                             |
|                                                                                                                                                                                                 |
| [Dim][ dc [As] [New] [DiagramControl]()] |
|                                                                                                                                                                                                 |
| [dc.IsSymbolPaletteEnabled = [True]]                                                                                                   |
|                                                                                                                                                                                                 |
| [Dim][ view [As] [New] [DiagramView]()]  |
|                                                                                                                                                                                                 |
| [view.Bounds = [New] System.Drawing.Thickness(0, 0, 1000, 1000)]                                                                       |
|                                                                                                                                                                                                 |
| [dc.View = view]                                                                                                                                            |
|                                                                                                                                                                                                 |
| [diagramgrid.Children.Add(dc)][]                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

