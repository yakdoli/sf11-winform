---
title: customizinglegendlocation.md
original_path: WinForms_Docs/99_Uncategorized/customizinglegendlocation.md
created_at: 2025-08-05
---








  









### Customizing Legend Location {#customizing-legend-location style="tab-stops: 0pt"}

Chart Legend Customization

[]{#RichViewCheckpoint0}Essential Chart also supports the legend placement and legend alignment properties.[]{#RichViewCheckpoint1} It allows you to decide whether the legend should be placed inside or outside the chart, also the legend alignment can be done according to the chart content.

Legends Placement

The legend can be placed inside or outside the ChartArea by using the LegendsPlacement property. By default it is set to Inside.

Properties

The following table lists more information on the property:


+-----------------------------------+-----------------------------------------------------------------------------------------------------+
| Chart Property                    | Description                                                                                         |
+-----------------------------------+-----------------------------------------------------------------------------------------------------+
| LegendsPlacement                  | Specifies the placement of the legend relative to the ChartArea. It includes the following options: |
|                                   |                                                                                                     |
|                                   | [·      ]Inside: Legend is placed inside the ChartArea.                |
|                                   |                                                                                                     |
|                                   | [·      ]Outside: Legend is placed outside the ChartArea.              |
+-----------------------------------+-----------------------------------------------------------------------------------------------------+


**[]** 

Legend Position

You can set the position for the legend in a Chart control by using the LegendPosition property.

Properties

The following table lists more information on the property:


+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| Chart Property                    | Description                                                                                                                |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| LegendPosition                    | Specifies the position relative to the chart for which to render the legend. It includes the following options:            |
|                                   |                                                                                                                            |
|                                   | [·      ]Top - Above the chart.                                                               |
|                                   |                                                                                                                            |
|                                   | [·      ]Left - Left of the chart.                                                            |
|                                   |                                                                                                                            |
|                                   | [·      ]Right - Right of the chart.                                                          |
|                                   |                                                                                                                            |
|                                   | [·      ]Bottom - Below the chart.                                                            |
|                                   |                                                                                                                            |
|                                   | [·      ]Floating - Will not be docked to any specific location. This is the default setting. |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+


**[]** 

Legend Alignment

The legend can be aligned to the center, near, or far in the ChartModel or ChartArea by using the LegendAlignment property.

Properties

The following table lists more information on the property:

 


+-----------------------------------+----------------------------------------------------------------------------------------------------------------+
| Chart Property                    | Description                                                                                                    |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------+
| LegendAlignment                   | Specifies the legend alignment relative to the ChartArea and Chart control. It includes the following options: |
|                                   |                                                                                                                |
|                                   | [·      ]Center: Legend placed at the center.                                     |
|                                   |                                                                                                                |
|                                   | [·      ]Near: Legend placed near the position.                                   |
|                                   |                                                                                                                |
|                                   | [·      ]Far: Legend placed far from the position.                                |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------+


 

The following screenshots show different combinations of the above properties:

[] 

{border="0"}

Figure 297: Legend Position Top, LegendAlignment Center, and LegendsPlacement Inside

**[]** 

{border="0"}

Figure 298: Legend Position Left, LegendAlignment Far, and LegendsPlacement Inside

**[]** 

**[]** 

{border="0"}

Figure 299: Legend Position Right, LegendAlignment Near, and LegendsPlacement Outside

**[]** 

{border="0"}

Figure 300: Legend Position Bottom, LegendAlignment Near, and LegendsPlacement Outside

 

{border="0"}

Figure 301: Legend Position Top, LegendAlignment Center, and LegendsPlacement Outside

Legend customization in any chart can be created in two ways:

[·      ]Builder

[·      ]ChartModel

More:







