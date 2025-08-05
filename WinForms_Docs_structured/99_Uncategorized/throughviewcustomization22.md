---
title: throughviewcustomization22.md
original_path: WinForms_Docs/99_Uncategorized/throughviewcustomization22.md
created_at: 2025-08-05
---






##### Through View Customization {#through-view-customization style="tab-stops: 0pt"}

[] 

Step 1:

View:

Add the below code in the aspx file.

 

To automatically update the segment count value dynamically, set its **IsAutomaticSegmentCountEnabled** property to **true**.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[ASPX\]]                                                                                                                         |
|                                                                                                                                                                            |
| [     [\<%][\--Rendering the rolling gauge\--][%\>]] |
|                                                                                                                                                                            |
| [    [\<%][=]Html.Syncfusion().RollingGauge([\"Gauge\"])]     |
|                                                                                                                                                                            |
| []                                                                                                                                     |
|                                                                                                                                                                            |
| [         .Value([\"Gauge\"])]                                                                                 |
|                                                                                                                                                                            |
| [            [//Enabling the IsAutomaticSegmentCountEnabled property to update.]]                                |
|                                                                                                                                                                            |
| [            [//The segment count automatically based on the gauge value.]]                                      |
|                                                                                                                                                                            |
| **[          .IsAutomaticSegmentCountEnabled([true])]**                                                           |
|                                                                                                                                                                            |
| [         .GaugeSkins([GaugeSkins].VS2010)]                                                                    |
|                                                                                                                                                                            |
| [         .Height(50)]                                                                                                                 |
|                                                                                                                                                                            |
| [         ]                                                                                                                            |
|                                                                                                                                                                            |
| [    [%\>]]                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[cshtml\]]                                                                                                                       |
|                                                                                                                                                                            |
| [     [@\*][\--Rendering the rolling gauge\--][\*@]] |
|                                                                                                                                                                            |
| [    [\@{] Html.Syncfusion().RollingGauge([\"Gauge\"])]                            |
|                                                                                                                                                                            |
| []                                                                                                                                     |
|                                                                                                                                                                            |
| [         .Value([\"Gauge\"])]                                                                                 |
|                                                                                                                                                                            |
| [            [//Enabling the IsAutomaticSegmentCountEnabled property to update.]]                                |
|                                                                                                                                                                            |
| [            [//The segment count is automatically based on the gauge value.]]                                   |
|                                                                                                                                                                            |
| **[          .IsAutomaticSegmentCountEnabled([true])]**                                                           |
|                                                                                                                                                                            |
| [         .GaugeSkins([GaugeSkins].VS2010)]                                                                    |
|                                                                                                                                                                            |
| [         .Height(50).Render();         ]                                                                                              |
|                                                                                                                                                                            |
| [    [}]]                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

Step 2:

Controller:

Add the code below in the controller.

 

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

**[]** 

Step 3:

Run the code to achieve the below output.

 

{border="0"}

Figure 153: AutomaticSegment count Enabled-Rolling Gauge**[]**

[                                                         ]

[]{#related-topics}

