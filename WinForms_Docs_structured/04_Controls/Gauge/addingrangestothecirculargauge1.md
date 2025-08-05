---
title: addingrangestothecirculargauge1.md
original_path: WinForms_Docs/04_Controls/Gauge/addingrangestothecirculargauge1.md
created_at: 2025-08-05
---






##### Adding Ranges to the Circular Gauge {#adding-ranges-to-the-circular-gauge style="tab-stops: 0pt"}

[] 

Ranges are objects that highlight a range of values. Ranges can be customized using various attributes such as Range Positioning, Distance of the ranges from the scale, Start and End width of the range and so on. The attributes and their descriptions are tabulated below:

[] 


  ------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------
  Property            Description
  StartValue          Specifies the start value of the range.
  EndValue            Specifies the end value of the range.
  StartWidth          Specifies the start width of the Range.
  EndWidth            Specifies the end width of the Range.
  DistanceFromScale   Specifies from which distance the range should be displayed from the scale.
  Range position      Using this attribute, range can be positioned in three areas along the circular scale. It can be inside, outside or cross.**[]**
  ------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------


Table 5: Properties of Circular Range

[] 

The below code snippet helps you to add ranges to the Circular Gauge.

 

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [  ][\<][sfgauge][:][CircularScale.Ranges][\>][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [                                ][\<][sfgauge][:][CircularRange][ StartValue][=\"70\"][ EndValue][=\"100\"][ Name][=\"range\"][ StartWidth][=\"0\"][ EndWidth][=\"15\"][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [       [ RangePosition][=\"Inside\"][ DistanceFromScale][=\"10\"][ Background][=\"White\"\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [                                ][\</][sfgauge][:][CircularRange][\>][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [ ][\</][sfgauge][:][CircularScale.Ranges][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                   |
|                                                                                                                                                                                                  |
| **[]**                                                                                                                                         |
|                                                                                                                                                                                                  |
| [CircularGauge][ circulargauge1 = [new] [CircularGauge]();] |
|                                                                                                                                                                                                  |
| [PivotItem][ pivotitem = [new] [PivotItem]();]              |
|                                                                                                                                                                                                  |
| [pivotitem.Content = circulargauge1; ]                                                                                                                       |
|                                                                                                                                                                                                  |
| [LayoutRoot.Children.Add(pivotitem); ][]                                                                                 |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
|                                                                                                                                                                                                  |
| [CircularScale][ c_scale = [new] [CircularScale]();]        |
|                                                                                                                                                                                                  |
| [c_scale.Radius = 110;]                                                                                                                                      |
|                                                                                                                                                                                                  |
| [c_scale.StartAngle = 120;]                                                                                                                                  |
|                                                                                                                                                                                                  |
| [c_scale.GapSweepAngle = 300;]                                                                                                                               |
|                                                                                                                                                                                                  |
| [c_scale.ScaleBarSize = 10;]                                                                                                                                 |
|                                                                                                                                                                                                  |
| [c_scale.Location = [new] [Point](50, 50);]                                                                     |
|                                                                                                                                                                                                  |
| [c_scale.ShadowOffset = 5;]                                                                                                                                  |
|                                                                                                                                                                                                  |
| [c_scale.ShadowOffset = 5;]                                                                                                                                  |
|                                                                                                                                                                                                  |
| [c_scale.Minimum = 0;]                                                                                                                                       |
|                                                                                                                                                                                                  |
| [c_scale.Maximum = 100;]                                                                                                                                     |
|                                                                                                                                                                                                  |
| [c_scale.MinorIntervalValue = 2;]                                                                                                                            |
|                                                                                                                                                                                                  |
| [c_scale.MajorIntervalValue = 10;]                                                                                                                           |
|                                                                                                                                                                                                  |
| [c_scale.Background = [new] [SolidColorBrush]([Colors].LightGray);]                     |
|                                                                                                                                                                                                  |
| [c_scale.BorderBrush = [new] [SolidColorBrush]([Colors].Blue);]                         |
|                                                                                                                                                                                                  |
| [c_scale.BorderThickness = [new] [Thickness](0.5);]                                                             |
|                                                                                                                                                                                                  |
| [circulargauge1.Scales.Add(c_scale);]                                                                                                                        |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
|                                                                                                                                                                                                  |
| [// Adding Range.]                                                                                                                             |
|                                                                                                                                                                                                  |
| [CircularRange][ c_range = [new] [CircularRange]();]        |
|                                                                                                                                                                                                  |
| [c_range.StartValue = 80;]                                                                                                                                   |
|                                                                                                                                                                                                  |
| [c_range.EndValue = 100;]                                                                                                                                    |
|                                                                                                                                                                                                  |
| [c_range.StartWidth = 1;]                                                                                                                                    |
|                                                                                                                                                                                                  |
| [c_range.EndWidth = 10;]                                                                                                                                     |
|                                                                                                                                                                                                  |
| [c_range.DistanceFromScale = 3;]                                                                                                                             |
|                                                                                                                                                                                                  |
| [c_scale.Ranges.Add(c_range);]                                                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 42: Range added to the Circular Gauge

 

[]{#p44} 

 

[]{#related-topics}

