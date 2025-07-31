---
title: gaugecustomization1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Gauge\gaugecustomization1.md
created_at: 2025-07-03
---






##### Gauge Customization {#gauge-customization style="tab-stops: 0pt"}

 

The Height and Width of the Gauge can be customized using its **Height** and **Width** properties. Using its RadiusX and RadiusY properties, you can get the rounded corner for the rolling gauge.

 

 


+-----------------+------------------------------------------+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+
| Property        | Description                              | Type of Property                                    | Value It Accepts                                                                                                                                              | Any other dependencies/Sub properties associated |
+-----------------+------------------------------------------+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+
| Height          | Sets the height of the gauge.            | [double]                       | [double]                                                                                                                                 | NA                                               |
+-----------------+------------------------------------------+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+
| Width           | Sets the Width of the gauge.             | [double]                       | [double]                                                                                                                                 | NA                                               |
+-----------------+------------------------------------------+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+
| BackgroundColor | Sets the Background color for the gauge. | System.Drawing.[Color]      | Refer to the below link for Value for the Colors Class.                                                                                                       | NA                                               |
|                 |                                          |                                                     |                                                                                                                                                               |                                                  |
|                 |                                          |                                                     | [[Colors]](http://msdn.microsoft.com/en-us/library/system.drawing.color_members.aspx) |                                                  |
+-----------------+------------------------------------------+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+
| BorderColor     | Sets the Border color for the gauge.     | System.Drawing.[Color]      | Refer to the below link for Value for the Colors Class.                                                                                                       | NA                                               |
|                 |                                          |                                                     |                                                                                                                                                               |                                                  |
|                 |                                          |                                                     | [[Colors]](http://msdn.microsoft.com/en-us/library/system.drawing.color_members.aspx) |                                                  |
+-----------------+------------------------------------------+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+
| BorderWidth     | Sets the Border width for the gauge.     | [int]                          | [int]                                                                                                                                    | NA                                               |
+-----------------+------------------------------------------+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+
| FontColor       | Sets the Font color for the gauge.       | System.Drawing.[Color]      | Refer to the below link for Value for the Colors Class.                                                                                                       | NA                                               |
|                 |                                          |                                                     |                                                                                                                                                               |                                                  |
|                 |                                          |                                                     | [[Colors]](http://msdn.microsoft.com/en-us/library/system.drawing.color_members.aspx) |                                                  |
+-----------------+------------------------------------------+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+
| FontFamily      | Sets the Font family for the gauge.      | System.Drawing.[FontFamily] | System.Drawing.[FontFamily]                                                                                                           | NA                                               |
+-----------------+------------------------------------------+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+
| FontSize        | Sets the Font size for the gauge.        | [double]                       | [double]                                                                                                                                 | NA                                               |
+-----------------+------------------------------------------+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+


[] 

###### 5.4.3.1.2.1 Through View Customization {#through-view-customization style="tab-stops: 0pt"}

 

Step 1:

View:

 

Add the below code in your aspx file.

The Height and Width of the Gauge can be customized using its **Height** and **Width** properties. Using its **RadiusX** and **RadiusY** properties, you can get the rounded corner for the rolling gauge.

 

The background, border and font colors can be set using its **BackgroundColor**, **BorderColor** and **FontColor** properties.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[ASPX\]]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                           |
| [\<%][\--Rendering the rolling gauge\--][%\>][] |
|                                                                                                                                                                                                                                                           |
| [    [\<%][=]Html.Syncfusion().RollingGauge([\"Gauge\"])]                                                                                    |
|                                                                                                                                                                                                                                                           |
| [        [//Setting the height and width of the rolling gauge.]]                                                                                                                                |
|                                                                                                                                                                                                                                                           |
| [         .Height(50)]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                           |
| [         .Width(300)]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                           |
| [        [//Setting the RadiusX and RadiusY values to get the rounded corner for the gauge.]]                                                                                                   |
|                                                                                                                                                                                                                                                           |
| [         .RadiusX(6)]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                           |
| [         .RadiusY(6)]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                           |
| [            [//Setting the background and border color for the gauge.]]                                                                                                                        |
|                                                                                                                                                                                                                                                           |
| [         .BackgroundColor(System.Drawing.[Color].LightGray)]                                                                                                                                 |
|                                                                                                                                                                                                                                                           |
| [         .BorderColor(System.Drawing.[Color].DarkGray)]                                                                                                                                      |
|                                                                                                                                                                                                                                                           |
| [            [//Setting the border width.]]                                                                                                                                                     |
|                                                                                                                                                                                                                                                           |
| [         .BorderWidth(7)]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                           |
| [            [//Setting the font color for the gauge value.]]                                                                                                                                   |
|                                                                                                                                                                                                                                                           |
| [         .FontColor(System.Drawing.[Color].Red)]                                                                                                                                             |
|                                                                                                                                                                                                                                                           |
| [         .SegmentCount(5)]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                           |
| [            [//Setting the value for the gauge.]]                                                                                                                                              |
|                                                                                                                                                                                                                                                           |
| [         .Value([\"Gauge\"])]                                                                                                                                                                |
|                                                                                                                                                                                                                                                           |
| [            [//Setting the font size.]]                                                                                                                                                        |
|                                                                                                                                                                                                                                                           |
| [         .FontSize(30)]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                           |
| [         .SpaceBetWeenSegment(2)]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| [    [%\>]]                                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[cshtml\]]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                           |
| [@\*][\--Rendering the rolling gauge\--][\*@][] |
|                                                                                                                                                                                                                                                           |
| [    [\@{] Html.Syncfusion().RollingGauge([\"Gauge\"])]                                                                                                           |
|                                                                                                                                                                                                                                                           |
| [        [//Setting the height and width of the rolling gauge.]]                                                                                                                                |
|                                                                                                                                                                                                                                                           |
| [         .Height(50)]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                           |
| [         .Width(300)]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                           |
| [        [//Setting the RadiusX and RadiusY values to get the rounded corner for the gauge.]]                                                                                                   |
|                                                                                                                                                                                                                                                           |
| [         .RadiusX(6)]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                           |
| [         .RadiusY(6)]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                           |
| [            [//Setting the background and border color for the gauge.]]                                                                                                                        |
|                                                                                                                                                                                                                                                           |
| [         .BackgroundColor(System.Drawing.[Color].LightGray)]                                                                                                                                 |
|                                                                                                                                                                                                                                                           |
| [         .BorderColor(System.Drawing.[Color].DarkGray)]                                                                                                                                      |
|                                                                                                                                                                                                                                                           |
| [            [//Setting the border width.]]                                                                                                                                                     |
|                                                                                                                                                                                                                                                           |
| [         .BorderWidth(7)]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                           |
| [            [//Setting the font color for the gauge value.]]                                                                                                                                   |
|                                                                                                                                                                                                                                                           |
| [         .FontColor(System.Drawing.[Color].Red)]                                                                                                                                             |
|                                                                                                                                                                                                                                                           |
| [         .SegmentCount(5)]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                           |
| [            [//Setting the value for the gauge.]]                                                                                                                                              |
|                                                                                                                                                                                                                                                           |
| [         .Value([\"Gauge\"])]                                                                                                                                                                |
|                                                                                                                                                                                                                                                           |
| [            [//Setting the font size.]]                                                                                                                                                        |
|                                                                                                                                                                                                                                                           |
| [         .FontSize(30)]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                           |
| [         .SpaceBetWeenSegment(2).Render();]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| [    [}]]                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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

Run the code to achieve the below output.

 

{border="0"}

Figure 145: Gauge Customization**[]**

[] 

###### 5.4.3.1.2.2 Through RollingGaugeModel {#through-rollinggaugemodel style="tab-stops: 0pt"}

**[]** 

Step 1:

View:

 

Add the below code in your aspx file.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[ASPX\]]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                           |
| [\<%][\--Rendering the rolling gauge\--][%\>][] |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| [  [\<%][=]Html.Syncfusion().RollingGauge([\"Gauge\"], [\"GaugeModel\"])[%\>]]           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[cshtml\]]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                     |
| [@\*][\--Rendering the rolling gauge\--][\*@][]           |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                     |
| [  ][@][Html.Syncfusion().RollingGauge([\"Gauge\"], [\"GaugeModel\"])] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

Step 2:

Controller:

 

Add the below code in the controller.

 

The Height and Width of the Gauge can be customized using its **Height** and **Width** properties. Using its **RadiusX** and **RadiusY** properties, you can get rounded corner for the rolling gauge.

 

The background, border and font colors can be set using its **BackgroundColor, BorderColor** and **FontColor** properties.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                               |
| [         [public] [ActionResult] Index()]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                               |
| [        {]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                               |
| [            ][RollingGaugeModel][ r_Gauge = [new] [RollingGaugeModel]();] |
|                                                                                                                                                                                                                                                                               |
| [            [//Setting the height and width of the rolling gauge.]]                                                                                                                                   |
|                                                                                                                                                                                                                                                                               |
| [            r_Gauge.Height = 50;]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                               |
| [            r_Gauge.Width = 300;]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                               |
| [            [//setting the RadiusX and RadiusY values to get the rounded corner for the gauge.]]                                                                                                      |
|                                                                                                                                                                                                                                                                               |
| [            r_Gauge.RadiusX = 6;]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                               |
| [            r_Gauge.RadiusY = 6;]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                               |
| [            [//Setting the background and border color for the gauge.]]                                                                                                                               |
|                                                                                                                                                                                                                                                                               |
| [            r_Gauge.BackgroundColor = System.Drawing.[Color].LightGray;]                                                                                                                            |
|                                                                                                                                                                                                                                                                               |
| [            r_Gauge.BorderColor = System.Drawing.[Color].DarkGray;]                                                                                                                                 |
|                                                                                                                                                                                                                                                                               |
| [            [//Setting the border width.]]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                               |
| [            r_Gauge.BorderWidth = 7;]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                               |
| [            [//Setting the font color for the gauge value.]]                                                                                                                                          |
|                                                                                                                                                                                                                                                                               |
| [            r_Gauge.FontColor = System.Drawing.[Color].Red;]                                                                                                                                        |
|                                                                                                                                                                                                                                                                               |
| [            r_Gauge.SegmentCount = 5;]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                               |
| [            [//Setting the value for the gauge.]]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                               |
| [            r_Gauge.Value = [\"Gauge\"];]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                               |
| [            [//Setting the font size.]]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                               |
| [            r_Gauge.FontSize = 30;]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                               |
| [            r_Gauge.SpaceBetWeenSegment = 2;]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                               |
| [            ViewData\[[\"GaugeModel\"]\] = r_Gauge;]                                                                                                                                                |
|                                                                                                                                                                                                                                                                               |
| [            [return] View();]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                               |
| [        }][]                                                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Step 3:

Run the code to achieve the below output.

 

{border="0"}

Figure 146: Gauge Customization[]

[                                                      ]

[]{#related-topics}

