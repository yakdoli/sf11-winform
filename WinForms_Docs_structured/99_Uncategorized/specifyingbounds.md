---
title: specifyingbounds.md
original_path: WinForms_Docs/99_Uncategorized/specifyingbounds.md
created_at: 2025-08-05
---








  









### Specifying Bounds {#specifying-bounds style="tab-stops: 0pt"}

[] 

The **Bounds** property of the Diagram View class enables a user to specify the rectangular area where the tree layout is to be displayed. The root of the tree layout is placed at the center of the bounds value.

[] 

Property:

[] 

  ---------- --------------------------------------------------------------------------------------------------------- ---------------------- ------------------ ---------------------------------------------------
  Property   Description                                                                                               Type of the property   Value it accepts   Any other dependencies/ sub properties associated
  Bounds     Gets or sets the bounds value which specifies the position of the root node in case of the tree layout.   CLR Property           Thickness          No
  ---------- --------------------------------------------------------------------------------------------------------- ---------------------- ------------------ ---------------------------------------------------

[] 

The following code can be used to set the Bounds property.

 

Bounds can be specified in two ways namely:

[] 

[·      ]Through XAML

[·      ]Through Code Behind

[] 

[] 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<][UserControl][ x][:][Class][=\"SilverlightApplication1.MainPage\"][ xmlns][=\"http://schemas.microsoft.com/winfx/2006/xaml/presentation\"]                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [xmlns][:][x][=\"http://schemas.microsoft.com/winfx/2006/xaml\"][  Height][=\"400\"][ Width][=\"600\"]                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [xmlns][:][sfdiagram][=\"clr-namespace:Syncfusion.Windows.Diagram;assembly=Syncfusion.Diagram.Silverlight\"][ xmlns][:][local][=\"clr-namespace:SilverlightApplication1\"\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<][Grid][ Name][=\"diagramgrid\"\>]                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [    ][\<][sfdiagram][:][DiagramControl][ IsSymbolPaletteEnabled][=\"True\" \>]                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [        ][\<][sfdiagram][:][DiagramControl.View][ \>]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [            ][\<][sfdiagram][:][DiagramView][ Bounds][=\"0,0,500,500\"\>]                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [            ][\</][sfdiagram][:][DiagramView][\>]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [        ][\</][sfdiagram][:][DiagramControl.View][\>]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [    ][\</][sfdiagram][:][DiagramControl][\>]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\</][Grid][\>]                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\</][UserControl][\>]                                                                                                                                                                                                                                                                                                                                                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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
| [view.Bounds = [new] System.Drawing.[Thickness](0, 0, 500, 500);]                                     |
|                                                                                                                                                                                        |
| [dc.View = view;]                                                                                                                                  |
|                                                                                                                                                                                        |
| [diagramgrid.Children.Add(dc);]                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

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
| [view.Bounds = [New] System.Drawing.Thickness(0, 0, 500, 500)]                                                                         |
|                                                                                                                                                                                                 |
| [dc.View = view]                                                                                                                                            |
|                                                                                                                                                                                                 |
| [diagramgrid.Children.Add(dc)][]                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

