---
title: throughviewcustomiza.md
original_path: WinForms_Docs/99_Uncategorized/throughviewcustomiza.md
created_at: 2025-08-05
---






#### Through View Customization {#through-view-customization style="tab-stops: 0pt"}

 

Step 1:          

View:

 

Add the below code in your aspx file.

The height and width of the rolling gauge can be customized using its **Height** and **Width** properties. The rounded rectangular corner for rolling gauge can be set using its **RadiusX** and **RadiusY** properties. The segments of the rolling gauge can be customized using its SegmentCount, SegmentBorderWidth, etc. The units can be set for the gauge value using its **Unit** property and its position can be customized using its **UnitPosition** property.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[ASPX\]]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| [\<%][\--Rendering the Rolling Gauge\--][%\>][] |
|                                                                                                                                                                                                                                                           |
| [    [\<%][=]Html.Syncfusion().RollingGauge([\"Gauge\"])]                                                                                    |
|                                                                                                                                                                                                                                                           |
| [            [//Specifying the height and width of the gauge.]]                                                                                                                                 |
|                                                                                                                                                                                                                                                           |
| [         .Height(55)]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                           |
| [         .Width(500)]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                           |
| [            [//Setting the segment count value.]]                                                                                                                                              |
|                                                                                                                                                                                                                                                           |
| [         .SegmentCount(5)]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                           |
| [            [//Specifying the value for the gauge.]]                                                                                                                                           |
|                                                                                                                                                                                                                                                           |
| [         .Value([\"10000\"])]                                                                                                                                                                |
|                                                                                                                                                                                                                                                           |
| [            [//Setting the unit value.]]                                                                                                                                                       |
|                                                                                                                                                                                                                                                           |
| [         .Unit([\"KM\"])]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| [            [//Setting the border width for the segments.]]                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| [         .SegmentBorderWidth(1)]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                           |
| [            [//Setting RadiusX and RadiusY values to get the rounded corner.]]                                                                                                                 |
|                                                                                                                                                                                                                                                           |
| [         .RadiusX(8)]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                           |
| [         .RadiusY(8)]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                           |
| [            [//Setting the font-size.]]                                                                                                                                                        |
|                                                                                                                                                                                                                                                           |
| [         .FontSize(20)]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                           |
| [            [//Specifying the space between the segments.]]                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| [         .SpaceBetWeenSegment(2)]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| [            [//Setting the skins for the gauge.]]                                                                                                                                              |
|                                                                                                                                                                                                                                                           |
| [         .GaugeSkins([GaugeSkins].VS2010)]                                                                                                                                                   |
|                                                                                                                                                                                                                                                           |
| [    [%\>]]                                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                           |
| [@\*][\--Rendering the Rolling Gauge\--][\*@][] |
|                                                                                                                                                                                                                                                           |
| [    [\@{] Html.Syncfusion().RollingGauge([\"Gauge\"])]                                                                                                           |
|                                                                                                                                                                                                                                                           |
| [            [//Specifying the height and width of the gauge.]]                                                                                                                                 |
|                                                                                                                                                                                                                                                           |
| [         .Height(55)]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                           |
| [         .Width(500)]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                           |
| [            [//Setting the segment count value.]]                                                                                                                                              |
|                                                                                                                                                                                                                                                           |
| [         .SegmentCount(5)]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                           |
| [            [//Specifying the value for the gauge.]]                                                                                                                                           |
|                                                                                                                                                                                                                                                           |
| [         .Value([\"10000\"])]                                                                                                                                                                |
|                                                                                                                                                                                                                                                           |
| [            [//Setting the unit value.]]                                                                                                                                                       |
|                                                                                                                                                                                                                                                           |
| [         .Unit([\"KM\"])]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| [            [//Setting the border width for the segments.]]                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| [         .SegmentBorderWidth(1)]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                           |
| [            [//Setting RadiusX and RadiusY values to get the rounded corner.]]                                                                                                                 |
|                                                                                                                                                                                                                                                           |
| [         .RadiusX(8)]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                           |
| [         .RadiusY(8)]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                           |
| [            [//Setting the font-size.]]                                                                                                                                                        |
|                                                                                                                                                                                                                                                           |
| [         .FontSize(20)]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                           |
| [            [//Specifying the space between the segments.]]                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| [         .SpaceBetWeenSegment(2)]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| [            [//Setting the skins for the gauge.]]                                                                                                                                              |
|                                                                                                                                                                                                                                                           |
| [         .GaugeSkins([GaugeSkins].VS2010).Render();]                                                                                                                                         |
|                                                                                                                                                                                                                                                           |
| [    [}]]                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

[] 

Step 2:

Controller:

Add the below code in your controller.

 

+----------------------------------------------------------------------------------------------------------------------------+
| []                                                                                     |
|                                                                                                                            |
| [        [public] [ActionResult] Index()] |
|                                                                                                                            |
| [        {]                                                                            |
|                                                                                                                            |
| [            [return] View();]                                    |
|                                                                                                                            |
| [        }]                                                                            |
+----------------------------------------------------------------------------------------------------------------------------+

[] 

Step 3:

Run the Code. You will get the below output.

 

{border="0"}

Figure 139: Rolling Gauge**[]**

[                             ]

[]{#related-topics}

