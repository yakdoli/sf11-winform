---
title: chartlegend1.md
original_path: WinForms_Docs/04_Controls/Chart/chartlegend1.md
created_at: 2025-08-05
---








  









### ChartLegend {#chartlegend style="tab-stops: 0pt"}

The legend is represented by the ChartLegend type.

**Default Legend**

By default, a custom ChartLegend instance gets added to the legends list in the control. You can access this default legend.

**Legend Look and Feel**

The following table lists some common properties you could use to customize the overall legend appearance:


  ----------------------- ---------------------------------------------------------------------------------------------------------------------------------
  ChartLegend Property    Description
  BackColor               Gets or sets the background color of the legend. The default value is Transparent.
  Border                  Gets or sets the border style of the legend. ShowBorder should be set to true.
  ShowBorder              Specifies whether a border should be drawn. By default it is set to false.
  Font                    Specifies the font that is to be used for the text rendered in the legend items. The default font style is Verdana, 8, Regular.
  BackInterior            Sets the interior appearance for the legend. This overrides the BackColor property.
  BackgroundImage         Sets the background image for the legend. This setting overrides the BackInterior property settings.
  BackgroundImageLayout   Sets the layout for the background image.
  ----------------------- ---------------------------------------------------------------------------------------------------------------------------------


[] 

Legend Positioning

The legend positioning can be affected in the following ways:

 


+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ChartLegend Property              | Description                                                                                                                        |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| Position                          | Specifies the position relative to the chart for which to render the legend.                                                       |
|                                   |                                                                                                                                    |
|                                   | **Top** - Above the chart.                                                                                                         |
|                                   |                                                                                                                                    |
|                                   | **Left** - Left of the chart.                                                                                                      |
|                                   |                                                                                                                                    |
|                                   | **Right** - Right of the chart.                                                                                                    |
|                                   |                                                                                                                                    |
|                                   | **Bottom** - Below the chart.                                                                                                      |
|                                   |                                                                                                                                    |
|                                   | **Floating** - Will not be docked to any specific location. This is the default setting.                                           |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| LegendAlignment                   | When docked to a side, this property specifies how the legend should be aligned with respect to the chart boundaries.              |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| LegendPlacement                   | Specifies the placement of a legend in a chart. It can be placed inside or outside the ChartArea by using the ChartPlacement enum. |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| FloatingAutoSize                  | Specifies whether to determine the size automatically or not, while floating.                                                      |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| OnlyColumnsForFloating            | The legend items will be displayed vertically in columns when floating.                                                            |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| RowsCount                         | Specifies the number of rows in which the legend items should be rendered.                                                         |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ColumnsCount                      | Specifies the number of columns in which the legend items should be rendered.                                                      |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+


[] 

[]{#related-topics}

