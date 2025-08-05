---
title: creatingapage.md
original_path: WinForms_Docs/99_Uncategorized/creatingapage.md
created_at: 2025-08-05
---








  









### Creating a Page {#creating-a-page style="tab-stops: 0pt"}

 

The DiagramView has a **Page** property which refers to the DiagramPage class. The DiagramPage displays the nodes and connections, which are added through the model.

[] 

Property:\
\

+-------------+-------------------------------+----------------------+------------------+---------------------------------------------------+
| Property    | Description                   | Type of the property | Value it accepts | Any other dependencies/ sub properties associated |
+-------------+-------------------------------+----------------------+------------------+---------------------------------------------------+
| Page        | Gets or sets the DiagramPage. | Dependency property  | DiagramPage      | No                                                |
|             |                               |                      |                  |                                                   |
|             |                               |                      |                  |                                                   |
+-------------+-------------------------------+----------------------+------------------+---------------------------------------------------+

[] 

The DiagramPage can be created for DiagramView in the following two ways:

[] 

[·      ]Through XAML

[·      ]Through Code Behind

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<][UserControl][ [x][:][Class][=\"SilverlightApplication1.MainPage\" ][xmlns][=\"http://schemas.microsoft.com/winfx/2006/xaml/presentation\"]]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [xmlns][:][x][=\"http://schemas.microsoft.com/winfx/2006/xaml\" ][ [Height][=\"400\"] [Width][=\"600\"]]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [xmlns][:][sfdiagram][=\"clr-namespace:Syncfusion.Windows.Diagram;assembly=Syncfusion.Diagram.Silverlight\" ][xmlns][:][local][=\"clr-namespace:SilverlightApplication1\"][ [\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<][Grid][ [Name][=\"diagramgrid\"\>]]                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<][sfdiagram][:][DiagramControl][ [IsSymbolPaletteEnabled][=\"True\"] [\>]]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<][sfdiagram][:][DiagramControl.Model][\>]                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<][sfdiagram][:][DiagramModel][ [x][:][Name][=\"diagramModel\"] [\>]]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\</][sfdiagram][:][DiagramModel][\>]                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\</][sfdiagram][:][DiagramControl.Model][\>]                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<][sfdiagram][:][DiagramControl.View][ [\>]]                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<][sfdiagram][:][DiagramView][ [ShowHorizontalGridLine][=\"True\"] [ShowVerticalGridLine][=\"True\"\>]]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<][syncfusion][:][DiagramView.Page][\>]                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [  \<][syncfusion][:][DiagramPage][ [x][:][Name][=\"diagramPage\"] [GridHorizontalOffset][=\"50\"] [GridVerticalOffset][=\"50\"/\>]]                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\</][syncfusion][:][DiagramView.Page][\>]                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\</][sfdiagram][:][DiagramView][\>]                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\</][sfdiagram][:][DiagramControl.View][\>]                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\</][sfdiagram][:][DiagramControl][\>]                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\</][Grid][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\</][UserControl][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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
| [dc.View = view;]                                                                                                                                  |
|                                                                                                                                                                                        |
| [(diagramView.Page [as] [DiagramPage]).GridHorizontalOffset = 50;]                                    |
|                                                                                                                                                                                        |
| [(diagramView.Page [as] [DiagramPage]).GridVerticalOffset = 50;]                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

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
| [dc.View = view]                                                                                                                                            |
|                                                                                                                                                                                                 |
| [TryCast][(diagramView.Page, DiagramPage).GridHorizontalOffset = 50]                                       |
|                                                                                                                                                                                                 |
| [TryCast][(diagramView.Page, DiagramPage).GridVerticalOffset = 50][]   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p79} 

[]{#related-topics}

