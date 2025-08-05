---
title: creatingadiagram2.md
original_path: WinForms_Docs/04_Controls/Diagram/creatingadiagram2.md
created_at: 2025-08-05
---








  









## Creating a Diagram {#creating-a-diagram style="tab-stops: 0pt"}

[]{#p13}Essential Diagram WPF can be used to create a rich Visio-like application. This framework provides many utility controls to help you easily put an application together. End users can get started in minutes using this diagram control.

[] 

Following is a basic step to create DiagramControl and initialize the necessary properties. Details about individual parts are explained later in this documentation.

[]{#_How_to_Add} 

Create DiagramControl

The Diagram Control can be added to the application using the following code.

 

DiagramControl can be created in two ways,

[] 

[·      ]Through XAML

[·      ]Through Code Behind

[] 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][Window][ x][:][Class][=\"WpfApplication1.Window1\"][ xmlns][=\"http://schemas.microsoft.com/winfx/2006/xaml/presentation\"]                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [xmlns][:][x][=\"http://schemas.microsoft.com/winfx/2006/xaml\"][ Title][=\"EssentialDiagramWPF\"][ Height][=\"400\"][ Width][=\"600\"] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [xmlns][:][sfdiagram][=\"clr-namespace:Syncfusion.Windows.Diagram;assembly=Syncfusion.Diagram.WPF\"][ xmlns][:][local][=\"clr-namespace:WpfApplication1\"\>]                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][Grid][ Name][=\"diagramgrid\"\>]                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][sfdiagram][:][DiagramControl][\>\</][sfdiagram][:][DiagramControl][\>]                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\</][Grid][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\</][Window][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                         |
|                                                                                                                                                                                        |
| []                                                                                                                                   |
|                                                                                                                                                                                        |
| [DiagramControl][ dc = [new] [DiagramControl]();] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[  ]

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                        |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                  |
|                                                                                                                                                                                                                                       |
| [Dim][ dc [As] [New] [DiagramControl]()][] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

This shows a window with empty diagramcontrol.

[] 

Enabling SymbolPalette

[] 

[·      ]Now you need to add the SymbolPalette to your newly created Diagram control. The SymbolPalette is displayed by setting the **IsSymbolPaletteEnabled** property to *True*. By default, it is set to *False*. The following code enables the SymbolPalette.\
\

SymbolPalette can be enabled in two ways,

[] 

[·      ]Through XAML

[·      ]Through Code Behind

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][Window][ x][:][Class][=\"WpfApplication1.Window1\"][ xmlns][=\"http://schemas.microsoft.com/winfx/2006/xaml/presentation\"]                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [xmlns][:][x][=\"http://schemas.microsoft.com/winfx/2006/xaml\"][ Title][=\"EssentialDiagramWPF\"][ Height][=\"400\"][ Width][=\"600\"] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [xmlns][:][sfdiagram][=\"clr-namespace:Syncfusion.Windows.Diagram;assembly=Syncfusion.Diagram.WPF\"][ xmlns][:][local][=\"clr-namespace:WpfApplication1\"\>]                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][Grid][ Name][=\"diagramgrid\"\>]                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][sfdiagram][:][DiagramControl][ IsSymbolPaletteEnabled][=\"True\"\>]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\</][sfdiagram][:][DiagramControl][\>]                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\</][Grid][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\</][Window][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                     |
|                                                                                                                                                                                                    |
| []                                                                                                                                               |
|                                                                                                                                                                                                    |
| [DiagramControl][ diagramcontrol = [new] [DiagramControl]();] |
|                                                                                                                                                                                                    |
| [diagramcontrol.IsSymbolPaletteEnabled = [true];]                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                              |
|                                                                                                                                                                                                             |
| []                                                                                                                                                        |
|                                                                                                                                                                                                             |
| [Dim][ diagramcontrol [As] [New] [DiagramControl]()] |
|                                                                                                                                                                                                             |
| [diagramcontrol.IsSymbolPaletteEnabled = [True]][]                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Create DiagramModel\
\

[·      ]To add contents into the drawing area, use the **Model** property of the diagram control. The following code can be used to add the model.

[] 

DiagramModel can be created and assigned to DiagramControl's View Property using two ways,

[] 

[·      ]Through XAML

[·      ]Through Code Behind\
\

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][Window][ x][:][Class][=\"WpfApplication1.Window1\"][ xmlns][=\"http://schemas.microsoft.com/winfx/2006/xaml/presentation\"]                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [xmlns][:][x][=\"http://schemas.microsoft.com/winfx/2006/xaml\"][ Title][=\"EssentialDiagramWPF\"][ Height][=\"400\"][ Width][=\"600\"] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [xmlns][:][sfdiagram][=\"clr-namespace:Syncfusion.Windows.Diagram;assembly=Syncfusion.Diagram.WPF\"][ xmlns][:][local][=\"clr-namespace:WpfApplication1\"\>]                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [    ][\<][Grid][ Name][=\"diagramgrid\"\>]                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [        ][\<][sfdiagram][:][DiagramControl][ IsSymbolPaletteEnabled][=\"True\"\>]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [           \<][sfdiagram][:][DiagramControl.Model][\>]                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                ][\<][sfdiagram][:][DiagramModel][\>\</][sfdiagram][:][DiagramModel][\>]                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [            ][\</][sfdiagram][:][DiagramControl.Model][\>]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [        ][\</][sfdiagram][:][DiagramControl][\>]                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [    ][\</][Grid][\>]                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\</][Window][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                         |
|                                                                                                                                                                                        |
| []                                                                                                                                   |
|                                                                                                                                                                                        |
| [DiagramControl][ dc = [new] [DiagramControl]();] |
|                                                                                                                                                                                        |
| [dc.IsSymbolPaletteEnabled = [true];]                                                                                         |
|                                                                                                                                                                                        |
| [DiagramModel][ model = [new] [DiagramModel]();]  |
|                                                                                                                                                                                        |
| [dc.Model = model;]                                                                                                                                |
|                                                                                                                                                                                        |
| [diagramgrid.Children.Add(dc);]                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                   |
|                                                                                                                                                                                                  |
| []                                                                                                                                             |
|                                                                                                                                                                                                  |
| [Dim][ dc [As] [New] [DiagramControl]()]  |
|                                                                                                                                                                                                  |
| [dc.IsSymbolPaletteEnabled = [True]]                                                                                                    |
|                                                                                                                                                                                                  |
| [Dim][ model [As] [New] [DiagramModel]()] |
|                                                                                                                                                                                                  |
| [dc.Model = model]                                                                                                                                           |
|                                                                                                                                                                                                  |
| [diagramgrid.Children.Add(dc)][]                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Create DiagramView

[] 

[·      ]To display the drawing area, use the **View** property of the diagram control. The following code can be used to add the view.

[] 

DiagramView can be created and assigned to DiagramControl's View Property using two ways,

[] 

[·      ]Through XAML

[·      ]Through Code Behind

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][Window][ x][:][Class][=\"WpfApplication1.Window1\"][ xmlns][=\"http://schemas.microsoft.com/winfx/2006/xaml/presentation\"]                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [xmlns][:][x][=\"http://schemas.microsoft.com/winfx/2006/xaml\"][ Title][=\"EssentialDiagramWPF\"][ Height][=\"400\"][ Width][=\"600\"] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [xmlns][:][sfdiagram][=\"clr-namespace:Syncfusion.Windows.Diagram;assembly=Syncfusion.Diagram.WPF\"][ xmlns][:][local][=\"clr-namespace:WpfApplication1\"\>]                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [    ][\<][Grid][ Name][=\"diagramgrid\"\>]                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [        ][\<][sfdiagram][:][DiagramControl][ IsSymbolPaletteEnabled][=\"True\"\>]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [            \<][sfdiagram][:][DiagramControl.Model][\>]                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                ][\<][sfdiagram][:][DiagramModel][\>\</][sfdiagram][:][DiagramModel][\>]                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [            ][\</][sfdiagram][:][DiagramControl.Model][\>]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [            ][\<][sfdiagram][:][DiagramControl.View][\>]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                ][\<][sfdiagram][:][DiagramView][ \>\</][sfdiagram][:][DiagramView][\>]                            |
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

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                         |
|                                                                                                                                                                                        |
| []                                                                                                                                   |
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

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                  |
|                                                                                                                                                                                                 |
| []                                                                                                                                            |
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

[] 

[·      ]This creates a Diagram Control with the SymbolPalette and the drawing area as illustrated in the following image.

 

{border="0"}

Figure 14: Diagram Control[]

 


[]{#p14}{border="0"}Note: For orthogonal and Bezier connectors, the connection always happens at the center of the node\'s edge.


 

For straight line connectors, the connection happens at the intersection point of the edge and the line connector.\
\

More:













