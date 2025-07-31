---
title: diagramview.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Diagram\diagramview.md
created_at: 2025-07-03
---








  









## Diagram View {#diagram-view style="tab-stops: 0pt"}

 

[]{#p75}The Diagram View is responsible for bringing the objects and the data, which are added into the view through the model. In other words, it deals with the visual representation of data. The following code can be used to add the view.

[] 

Properties

[] 

+----------------------+-----------------------------------------------------------------------------------------------------------+----------------------+----------------------+---------------------------------------------------+
| Property             | Description                                                                                               | Type of the property | Value it accepts     | Any other dependencies/ sub properties associated |
+======================+===========================================================================================================+======================+======================+===================================================+
| Bounds               | Gets or sets the bounds value which specifies the position of the root node in case of tree layout.       | CLR Property         | Thickness            | No                                                |
+----------------------+-----------------------------------------------------------------------------------------------------------+----------------------+----------------------+---------------------------------------------------+
| IsPageEditable       | Gets or sets a value indicating whether the page is enabled or not.                                       | Dependency property  | Boolean(True/False)  | No                                                |
|                      |                                                                                                           |                      |                      |                                                   |
|                      | Default value: True                                                                                       |                      |                      |                                                   |
+----------------------+-----------------------------------------------------------------------------------------------------------+----------------------+----------------------+---------------------------------------------------+
| ShowVerticalRulers   | Gets or sets a value indicating whether vertical rulers are displayed or not.                             | Dependency property  | Boolean(True/False)  | No                                                |
|                      |                                                                                                           |                      |                      |                                                   |
|                      |                                                                                                           |                      |                      |                                                   |
|                      |                                                                                                           |                      |                      |                                                   |
|                      | Default value: True                                                                                       |                      |                      |                                                   |
+----------------------+-----------------------------------------------------------------------------------------------------------+----------------------+----------------------+---------------------------------------------------+
| ShowHorizontalRulers | Gets or sets a value indicating whether horizontal rulers are displayed or not.                           | Dependency property  | Boolean(True/False)  | No                                                |
|                      |                                                                                                           |                      |                      |                                                   |
|                      |                                                                                                           |                      |                      |                                                   |
|                      |                                                                                                           |                      |                      |                                                   |
|                      | Default value: True                                                                                       |                      |                      |                                                   |
+----------------------+-----------------------------------------------------------------------------------------------------------+----------------------+----------------------+---------------------------------------------------+
| PortVisibility       | Gets or sets a value indicating whether all the ports of all the nodes on the page are visible or not.    | Dependency property  | Visibility.Visible   | No                                                |
|                      |                                                                                                           |                      |                      |                                                   |
|                      |                                                                                                           |                      | Visibility.Collapsed |                                                   |
|                      |                                                                                                           |                      |                      |                                                   |
|                      | If individual node's PortVisibility is set, then the node's PortVisibility property will take precedence. |                      | Visibility.Hidden    |                                                   |
|                      |                                                                                                           |                      |                      |                                                   |
|                      |                                                                                                           |                      |                      |                                                   |
|                      |                                                                                                           |                      |                      |                                                   |
|                      | Default value: Visibility.Visible                                                                         |                      |                      |                                                   |
+----------------------+-----------------------------------------------------------------------------------------------------------+----------------------+----------------------+---------------------------------------------------+
| Page                 | Gets or sets the DiagramPage.                                                                             | Dependency property  | Panel                | No                                                |
|                      |                                                                                                           |                      |                      |                                                   |
|                      |                                                                                                           |                      |                      |                                                   |
+----------------------+-----------------------------------------------------------------------------------------------------------+----------------------+----------------------+---------------------------------------------------+

[] 

[] 

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
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
| **[]**                                                                                                                               |
|                                                                                                                                                                                        |
| [DiagramControl][ dc = [new] [DiagramControl]();] |
|                                                                                                                                                                                        |
| [dc.IsSymbolPaletteEnabled = [true];]                                                                                         |
|                                                                                                                                                                                        |
| [DiagramView][ view = [new] [DiagramView]();]     |
|                                                                                                                                                                                        |
| [view.Bounds = [new] [Thickness](0, 0, 1000, 1000);]                                                  |
|                                                                                                                                                                                        |
| [dc.View = view;]                                                                                                                                  |
|                                                                                                                                                                                        |
| [diagramgrid.Children.Add(dc);]                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                  |
|                                                                                                                                                                                                 |
| **[]**                                                                                                                                        |
|                                                                                                                                                                                                 |
| [Dim][ dc [As] [New] [DiagramControl]()] |
|                                                                                                                                                                                                 |
| [dc.IsSymbolPaletteEnabled = [True]]                                                                                                   |
|                                                                                                                                                                                                 |
| [Dim][ view [As] [New] [DiagramView]()]  |
|                                                                                                                                                                                                 |
| [view.Bounds = [New] Thickness(0, 0, 1000, 1000)]                                                                                      |
|                                                                                                                                                                                                 |
| [dc.View = view]                                                                                                                                            |
|                                                                                                                                                                                                 |
| [diagramgrid.Children.Add(dc)][]                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The drawing area has many properties that can be used to customize a view.

[] 

**[]** 

**[]** 

See Also

[] 

[[·      ]]{.UGHyperlink}[Create Rulers]{.UGHyperlink}[]{.UGHyperlink}

[[·      ]]{.UGHyperlink}[Specify Bounds]{.UGHyperlink}[]{.UGHyperlink}

[[·      ]]{.UGHyperlink}[Create Page]{.UGHyperlink}[]{.UGHyperlink}

[[·      ]]{.UGHyperlink}[Page Editing option]{.UGHyperlink}[]{.UGHyperlink}

More:

















































