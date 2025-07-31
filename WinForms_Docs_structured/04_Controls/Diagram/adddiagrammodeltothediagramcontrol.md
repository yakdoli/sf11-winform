---
title: adddiagrammodeltothediagramcontrol.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Diagram\adddiagrammodeltothediagramcontrol.md
created_at: 2025-07-03
---








  









### Add Diagram Model to the Diagram Control {#add-diagram-model-to-the-diagram-control style="tab-stops: 0pt"}

A model represents data for an application and contains the logic for adding, accessing, and manipulating the data.

[] 

Features

[] 

[·      ]Nodes and connectors are added to the Diagram Control using the **Model** property.

[·      ]A predefined layout is applied using the **LayoutType** property.

[·      ]A data template is applied to the layout using the Hierarchical **DataTemplate** property.

[] 

The following code shows how the **Model** property can be applied to the Diagram control.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][Window][ x][:][Class][=\"WpfApplication1.Window1\"][ xmlns][=\"http://schemas.microsoft.com/winfx/2006/xaml/presentation\"]                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [xmlns][:][x][=\"http://schemas.microsoft.com/winfx/2006/xaml\"][ Title][=\"EssentialDiagramWPF\"][ Height][=\"420\"][ Width][=\"600\"] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [xmlns][:][sfdiagram][=\"clr-namespace:Syncfusion.Windows.Diagram;assembly=Syncfusion.Diagram.WPF\"][ xmlns][:][local][=\"clr-namespace:WpfApplication1\"\>]                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [    ][\<][Grid][ Name][=\"diagramgrid\"\>]                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [        ][\<][sfdiagram][:][DiagramControl][ IsSymbolPaletteEnabled][=\"True\"\>]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [            ][\<][sfdiagram][:][DiagramControl.Model][\>]                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                ][\<][sfdiagram][:][DiagramModel][ x][:][Name][=\"diagramModel\"\>]                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                ][\</][sfdiagram][:][DiagramModel][\>]                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [            ][\</][sfdiagram][:][DiagramControl.Model][\>]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [            ][\<][sfdiagram][:][DiagramControl.View][\>]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                ][\<][sfdiagram][:][DiagramView][\>\</][sfdiagram][:][DiagramView][\>]                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [            ][\</][sfdiagram][:][DiagramControl.View][\>]                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [        ][\</][sfdiagram][:][DiagramControl][\>]                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [    ][\</][Grid][\>]                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\</][Window][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                               |
|                                                                                                                                                                                              |
| []                                                                                                                                         |
|                                                                                                                                                                                              |
| [DiagramControl][ dc = [new] [DiagramControl]();]       |
|                                                                                                                                                                                              |
| [dc.IsSymbolPaletteEnabled = [true];]                                                                                               |
|                                                                                                                                                                                              |
| [DiagramView][ view = [new] [DiagramView]();]           |
|                                                                                                                                                                                              |
| [view.Bounds = [new] System.Drawing.[Thickness](0, 0, 1000, 1000);]                                         |
|                                                                                                                                                                                              |
| [dc.View = view;]                                                                                                                                        |
|                                                                                                                                                                                              |
| [DiagramModel][ diagramModel = [new] [DiagramModel]();] |
|                                                                                                                                                                                              |
| [dc.Model = diagramModel;]                                                                                                                               |
|                                                                                                                                                                                              |
| [diagramgrid.Children.Add(dc);]                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                          |
|                                                                                                                                                                                                         |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                         |
| [Dim][ dc [As] [New] [DiagramControl]()]         |
|                                                                                                                                                                                                         |
| [dc.IsSymbolPaletteEnabled = [True]]                                                                                                           |
|                                                                                                                                                                                                         |
| [Dim][ view [As] [New] [DiagramView]()]          |
|                                                                                                                                                                                                         |
| [view.Bounds = [New] System.Drawing.Thickness(0, 0, 1000, 1000)]                                                                               |
|                                                                                                                                                                                                         |
| [dc.View = view]                                                                                                                                                    |
|                                                                                                                                                                                                         |
| [Dim][ diagramModel [As] [New] [DiagramModel]()] |
|                                                                                                                                                                                                         |
| [dc.Model = diagramModel]                                                                                                                                           |
|                                                                                                                                                                                                         |
| [diagramgrid.Children.Add(dc)][]                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

This adds a model to the Diagram Control, and defines **Bounds** Property for DiagramModel

 

[]{#related-topics}

