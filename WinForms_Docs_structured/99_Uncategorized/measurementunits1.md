---
title: measurementunits1.md
original_path: WinForms_Docs/99_Uncategorized/measurementunits1.md
created_at: 2025-08-05
---








  









### Measurement Units {#measurement-units style="tab-stops: 0pt"}

As different fields require different units of measure, several measurement units are provided such that you can choose the unit that is most comfortable and suitable to use. All basic properties can be defined in the specified measurement unit. It is also possible to dynamically change the units at run-time. The rulers are updated accordingly to represent the coordinates in the currently selected unit.

Table 67: Property Table

+------------------+---------------------------------------------+----------------------+----------------------------+---------------------------------------------------+
| Property         | Description                                 | Type of the property | Value it accepts           | Any other dependencies/ sub properties associated |
+------------------+---------------------------------------------+----------------------+----------------------------+---------------------------------------------------+
| MeasurementUnits | Gets or sets the Measurement unit property. | DependencyProperty   | MeasureUnits.Pixel         | No                                                |
|                  |                                             |                      |                            |                                                   |
|                  |                                             |                      | MeasureUnits.Point         |                                                   |
|                  |                                             |                      |                            |                                                   |
|                  |                                             |                      | MeasureUnits.Document      |                                                   |
|                  |                                             |                      |                            |                                                   |
|                  |                                             |                      | MeasureUnits.Display       |                                                   |
|                  |                                             |                      |                            |                                                   |
|                  |                                             |                      | MeasureUnits.SixteenthInch |                                                   |
|                  |                                             |                      |                            |                                                   |
|                  |                                             |                      | MeasureUnits.EighthInch    |                                                   |
|                  |                                             |                      |                            |                                                   |
|                  |                                             |                      | MeasureUnits.QuarterInch   |                                                   |
|                  |                                             |                      |                            |                                                   |
|                  |                                             |                      | MeasureUnits.HalfInch      |                                                   |
|                  |                                             |                      |                            |                                                   |
|                  |                                             |                      | MeasureUnits.Inch          |                                                   |
|                  |                                             |                      |                            |                                                   |
|                  |                                             |                      | MeasureUnits.Foot          |                                                   |
|                  |                                             |                      |                            |                                                   |
|                  |                                             |                      | MeasureUnits.Yard          |                                                   |
|                  |                                             |                      |                            |                                                   |
|                  |                                             |                      | MeasureUnits.Mile          |                                                   |
|                  |                                             |                      |                            |                                                   |
|                  |                                             |                      | MeasureUnits.Millimeter    |                                                   |
|                  |                                             |                      |                            |                                                   |
|                  |                                             |                      | MeasureUnits.Centimeter    |                                                   |
|                  |                                             |                      |                            |                                                   |
|                  |                                             |                      | MeasureUnits.Meter         |                                                   |
|                  |                                             |                      |                            |                                                   |
|                  |                                             |                      | MeasureUnits.Kilometer     |                                                   |
|                  |                                             |                      |                            |                                                   |
|                  |                                             |                      |                            |                                                   |
+------------------+---------------------------------------------+----------------------+----------------------------+---------------------------------------------------+

[] 

The measurement units property can be specified in the following way.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<][sfdiagram][:][DiagramControl][ IsSymbolPaletteEnabled][=\"True\" \>]                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [    ][\<][sfdiagram][:][DiagramControl.Model][\>]                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [        ][\<][sfdiagram][:][DiagramModel][ x][:][Name][=\"diagramModel\" \>]                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [        ][\</][sfdiagram][:][DiagramModel][\>]                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [    ][\</][sfdiagram][:][DiagramControl.Model][\>]                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [    ][\<][sfdiagram][:][DiagramControl.View][ \>]                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [        ][\<][sfdiagram][:][DiagramView][ ShowHorizontalGridLine][=\"True\"][ ShowVerticalGridLine][=\"True\"\>]                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [            ][\<][syncfusion][:][DiagramView.Page][\>]                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [                ][\<][syncfusion][:][DiagramPage][ x][:][Name][=\"diagramPage\"][ MeasurementUnits][=\"Inch\"/\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [            ][\</][syncfusion][:][DiagramView.Page][\>]                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [        ][\</][sfdiagram][:][DiagramView][\>]                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [    ][\</][sfdiagram][:][DiagramControl.View][\>]                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\</][sfdiagram][:][DiagramControl][\>]                                                                                                                                                                                                                                                                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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
| [(view.Page [as] [DiagramPage]).MeasurementUnits = [MeasureUnits].Inch;]      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                      |
|                                                                                                                                                                                                     |
| []                                                                                                                                                |
|                                                                                                                                                                                                     |
| [Dim][ dc [As] [New] [DiagramControl]()]     |
|                                                                                                                                                                                                     |
| [dc.IsSymbolPaletteEnabled = [True]]                                                                                                       |
|                                                                                                                                                                                                     |
| [Dim][ view [As] [New] [DiagramView]()]      |
|                                                                                                                                                                                                     |
| [TryCast][(view.Page, DiagramPage).MeasurementUnits = MeasureUnits.Inch][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Once the Measurement unit is specified, all the values must be specified with respect to that unit. For instance, If the unit is set to Inch then the node\'s properties can be set as follows.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                 |
| [Node][ n1 = [new] [Node]([Guid].NewGuid(), [\"Node1\"]);] |
|                                                                                                                                                                                                                                                 |
| [n1.IsLabelEditable = [true];]                                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [n1.Label = [\"Alarm Rings\"];]                                                                                                                                                     |
|                                                                                                                                                                                                                                                 |
| [n1.OffsetX = 1.5;]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [n1.OffsetY = 1.25;]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                 |
| [n1.Width = 1.5;]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                 |
| [n1.Height = 0.75;]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [n1.LabelVerticalAlignment = [VerticalAlignment].Center;]                                                                                                                           |
|                                                                                                                                                                                                                                                 |
| [diagramModel.Nodes.Add(n1);]                                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                    |
| [Dim][ n1 [As] [New] [Node]([Guid].NewGuid(), [\"Node1\"])] |
|                                                                                                                                                                                                                                                                    |
| [n1.IsLabelEditable = [True]]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                    |
| [n1.Label = \"Alarm Rings\"]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                    |
| [n1.OffsetX = 1.5]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                    |
| [n1.OffsetY = 1.25]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                    |
| [n1.Width = 1.5]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                    |
| [n1.Height = 0.75]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                    |
| [n1.LabelVerticalAlignment = VerticalAlignment.Center]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                    |
| [diagramModel.Nodes.Add(n1)][]                                                                                                                                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

You can also dynamically change the units at runtime. The ruler values get changed according to the measurement unit selected. The rulers then indicate the position of the graphical objects with respect to the selected measurement unit.

[] 

{border="0"}

Figure 142: Units changed to Inches[]

[]{#p81} 

[]{#related-topics}

