---
title: gaugecustomization.md
original_path: WinForms_Docs/04_Controls/Gauge/gaugecustomization.md
created_at: 2025-08-05
---






##### Gauge Customization {#gauge-customization style="tab-stops: 0pt"}

 

The first, second and center frame colors can be set using its **FirstFrameFillColor**, **SecondFrameFillColor** and **CenterFrameFillColor** properties. The foreground color of the digital gauge can be set using its **Foreground** property.

 

Frame Types

The Frame type of the digital gauge can be customized using its **FrameType** property. There are four types of frames available for digital gauge. They are:

 

Rectangle

Digital Gauge with default template will be displayed as a Rectangle.

 

{border="0"}

Figure 127: Rectangular Frame**[]**

[                                            ][]

CroppedRectangle

 Digital Gauge with CroppedRectangle.

 

{border="0"}

Figure 128: Cropped Rectangular Frame**[]**

 

BoltedRectangle

Digital Gauge frame with BoltedRectangle.

 

{border="0"}

Figure 129: BoltedRectangular Frame**[]**

[                                       ]

RoundedRectangleWithInnerTopGradient

 Digital Gauge frame with inner top gradient.

 

{border="0"}

Figure 130: RoundedRectangular Frame with WithInnerGradient

[] 

 


Property



Description

Type of Property

Value It Accepts

Any other dependencies/Sub properties associated

FirstFrameFillColor

Sets the background of the first frame.

System.Windows.Media.[Brushes]

Refer to the below Link for  Value for the Brushes class

[[Brushes]](http://msdn.microsoft.com/en-us/library/system.windows.media.brushes.aspx)

NA

SecondFrameFillColor

Sets the background of the second frame.

System.Windows.Media.[Brushes]

Refer to the below Link for  Value for the Brushes class

[[Brushes]](http://msdn.microsoft.com/en-us/library/system.windows.media.brushes.aspx)

NA

CenterFrameFillColor

Sets the background of the center frame.

System.Windows.Media.[Brushes]

Refer to the below Link for  Value for the Brushes class

[[Brushes]](http://msdn.microsoft.com/en-us/library/system.windows.media.brushes.aspx)

NA

Foreground

Sets the foreground color for the Digital Gauge values.

System.Windows.Media.[Brushes]

Refer to the below Link for  Value for the Brushes class

[[Brushes]](http://msdn.microsoft.com/en-us/library/system.windows.media.brushes.aspx)

NA

FrameType

Sets the frame type of the Digital Gauge.

 

[enum]

[DigitalGaugeFrameType].BoltedRectangle

 

[DigitalGaugeFrameType].CroppedRectangle

 

[DigitalGaugeFrameType].Rectangle

 

[DigitalGaugeFrameType].RoundedRectangleWithInnerGradient

 

DimmedBrush

Sets the brush used for drawing the dim segments.

System.Windows.Media.[Brushes]

 

Refer to the below Link for  Value for the Brushes class

[[Brushes]](http://msdn.microsoft.com/en-us/library/system.windows.media.brushes.aspx)

NA

Height

Sets the height of the Digital Gauge.

 

[double]

[double]

NA

FirstFrameThickness

Sets the first frame thickness of the Gauge.

System.Windows.[Thickness]

[System.Windows.[Thickness]][]

NA

SecondFrameThickness

Sets the second frame thickness of the Gauge.

System.Windows.[Thickness]

[System.Windows.[Thickness]][]

NA

Width

Sets the width  of the Gauge.

[double]

[double][]

NA

[] 

###### 5.3.3.1.2.1 Through View Customization {#through-view-customization style="tab-stops: 0pt"}

[] 

Step 1:

View:

The first, second and center frame colors can be set using its **FirstFrameFillColor**, **SecondFrameFillColor** and **CenterFrameFillColor** properties. The Foreground color of the digital gauge can be set using its **Foreground** property. The color of the dimmed brushes can be set using its **DimmedBrush** property. The Height and Width of the Digital Gauge can be controlled using its **Height** and **Width** properties.  The Width of the first and second frame can be customized by its **FirstFrameThickness** and **SecondFrameThickness** properties.

 

Add the below code in your aspx file.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[ASPX\]]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                     |
| [\<%][=][Html.Syncfusion().DigitalGauge([\"Gauge\"], gauge=\>] |
|                                                                                                                                                                                                                                     |
| [        {]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                     |
| [        gauge]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                     |
| [            [//Setting first, second and center frame colors.]]                                                                                                          |
|                                                                                                                                                                                                                                     |
| [            .FirstFrameFillColor([Brushes].LightGray)]                                                                                                                 |
|                                                                                                                                                                                                                                     |
| [            .SecondFrameFillColor([Brushes].DarkGray)]                                                                                                                 |
|                                                                                                                                                                                                                                     |
| [            .CenterFrameFillColor([Brushes].Gray)]                                                                                                                     |
|                                                                                                                                                                                                                                     |
| [            [//Setting height and width of the gauge.]]                                                                                                                  |
|                                                                                                                                                                                                                                     |
| [            .Height(105)]                                                                                                                                                                      |
|                                                                                                                                                                                                                                     |
| [            .Width(450)]                                                                                                                                                                       |
|                                                                                                                                                                                                                                     |
| [            [//Setting first and second frame thickness.]]                                                                                                               |
|                                                                                                                                                                                                                                     |
| [            .FirstFrameThickness([new] System.Windows.[Thickness](8))]                                                                            |
|                                                                                                                                                                                                                                     |
| [            .SecondFrameThickness([new] System.Windows.[Thickness](6))]                                                                           |
|                                                                                                                                                                                                                                     |
| [            [//Sets the color for the bright segments.]]                                                                                                                 |
|                                                                                                                                                                                                                                     |
| [            .Foreground([Brushes].Red)]                                                                                                                                |
|                                                                                                                                                                                                                                     |
| [            [//Sets the color for the dimmed segments.]]                                                                                                                 |
|                                                                                                                                                                                                                                     |
| [            .DimmedBrush([Brushes].LightGray)]                                                                                                                         |
|                                                                                                                                                                                                                                     |
| [            .Value([\"10000\"])]                                                                                                                                       |
|                                                                                                                                                                                                                                     |
| [            [//Setting the frame type for the Digital Gauge.    ]]                                                                                                       |
|                                                                                                                                                                                                                                     |
| [            .FrameType([DigitalGaugeFrameType].CroppedRectangle);]                                                                                                     |
|                                                                                                                                                                                                                                     |
| [            ]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                     |
| [                  })]                                                                                                                                                                          |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [                 [%\>]]                                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[cshtml\]]                                                                                                                   |
|                                                                                                                                                                        |
| [  [@]Html.Syncfusion().DigitalGauge([\"Gauge\"], gauge=\>]       |
|                                                                                                                                                                        |
| [        {]                                                                                                           |
|                                                                                                                                                                        |
| [        gauge]                                                                                                       |
|                                                                                                                                                                        |
| [            [//Setting first, second and center frame colors.]]                                |
|                                                                                                                                                                        |
| [            .FirstFrameFillColor([Brushes].LightGray)]                                       |
|                                                                                                                                                                        |
| [            .SecondFrameFillColor([Brushes].DarkGray)]                                       |
|                                                                                                                                                                        |
| [            .CenterFrameFillColor([Brushes].Gray)]                                           |
|                                                                                                                                                                        |
| [            [//Setting height and width of the gauge.]]                                        |
|                                                                                                                                                                        |
| [            .Height(105)]                                                                                            |
|                                                                                                                                                                        |
| [            .Width(450)]                                                                                             |
|                                                                                                                                                                        |
| [            [//Setting first and second frame thickness.]]                                     |
|                                                                                                                                                                        |
| [            .FirstFrameThickness([new] System.Windows.[Thickness](8))]  |
|                                                                                                                                                                        |
| [            .SecondFrameThickness([new] System.Windows.[Thickness](6))] |
|                                                                                                                                                                        |
| [            [//Sets the color for the bright segments.]]                                       |
|                                                                                                                                                                        |
| [            .Foreground([Brushes].Red)]                                                      |
|                                                                                                                                                                        |
| [            [//Sets the color for the dimmed segments.]]                                       |
|                                                                                                                                                                        |
| [            .DimmedBrush([Brushes].LightGray)]                                               |
|                                                                                                                                                                        |
| [            .Value([\"10000\"])]                                                             |
|                                                                                                                                                                        |
| [            [//Setting the frame type for the Digital Gauge.    ]]                             |
|                                                                                                                                                                        |
| [            .FrameType([DigitalGaugeFrameType].CroppedRectangle);]                           |
|                                                                                                                                                                        |
| [            ]                                                                                                        |
|                                                                                                                                                                        |
| [                  })]                                                                                                |
|                                                                                                                                                                        |
| []                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

Step 2:

Controller:

**[]** 

Add the below code in your controller.

[] 

+--------------------------------------------------------------------------------------------------------------------------+
| []                                                                                   |
|                                                                                                                          |
| [      [public] [ActionResult] Index()] |
|                                                                                                                          |
| [        {          ]                                                                |
|                                                                                                                          |
| [            [return] View();]                                  |
|                                                                                                                          |
| [        }]                                                                          |
+--------------------------------------------------------------------------------------------------------------------------+

[] 

Step 3:

Run the code. You will get the following output.

 

{border="0"}

Figure 131: Gauge customization**[]**

[                                     ]

###### 5.3.3.1.2.2 Through DigitalGaugeModel {#through-digitalgaugemodel style="tab-stops: 0pt"}

[] 

Step 1:

View:

 

Add the below code in your aspx file.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[ASPX\]]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                           |
| [\<%][\--Rendering the Digital Gauge\--][%\>][] |
|                                                                                                                                                                                                                                                           |
| [     [\<%][=]Html.Syncfusion().DigitalGauge([\"Gauge\"], [\"GaugeModel\"])[%\>]]        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[cshtml\]]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                        |
| [@\*][\--Rendering the Digital Gauge\--][\*@][]              |
|                                                                                                                                                                                                                                                                        |
| [     ][@][Html.Syncfusion().DigitalGauge([\"Gauge\"], [\"GaugeModel\"])] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

Step 2:

Controller:

 

Add the below code in your controller. The first, second and center Frame colors can be set using its **FirstFrameFillColor, SecondFrameFillColor** and **CenterFrameFillColor** properties. The foreground color of the digital gauge can be set using its **Foreground** property. The color of the dimmed brushes can be set using its **DimmedBrush** property.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                            |
|                                                                                                                                                                                   |
| [public][ [ActionResult] Index()]                                    |
|                                                                                                                                                                                   |
| [        {]                                                                                                                                   |
|                                                                                                                                                                                   |
| [            [DigitalGaugeModel] d_Gauge = [new] [DigitalGaugeModel]();] |
|                                                                                                                                                                                   |
| [            [//Setting height and width of the gauge.]]                                                                |
|                                                                                                                                                                                   |
| [            d_Gauge.Height = 105;]                                                                                                           |
|                                                                                                                                                                                   |
| [            d_Gauge.Width = 450;]                                                                                                            |
|                                                                                                                                                                                   |
| [            [//Setting first and second frame thickness.]]                                                             |
|                                                                                                                                                                                   |
| [            d_Gauge.FirstFrameThickness = [new] System.Windows.[Thickness](8);]                 |
|                                                                                                                                                                                   |
| [            d_Gauge.SecondFrameThickness = [new] System.Windows.[Thickness](6);]                |
|                                                                                                                                                                                   |
| [            [//Setting the frame type of the digital gauge.]]                                                          |
|                                                                                                                                                                                   |
| [            d_Gauge.FrameType = [DigitalGaugeFrameType].CroppedRectangle;]                                           |
|                                                                                                                                                                                   |
| [            [//Setting first, second and center frame colors.]]                                                        |
|                                                                                                                                                                                   |
| [            d_Gauge.FirstFrameFillColor = [Brushes].LightGray;]                                                      |
|                                                                                                                                                                                   |
| [            d_Gauge.SecondFrameFillColor = [Brushes].DarkGray;]                                                      |
|                                                                                                                                                                                   |
| [            d_Gauge.CenterFrameFillColor = [Brushes].Gray;]                                                          |
|                                                                                                                                                                                   |
| [            [//Sets the color for the bright segments.]]                                                               |
|                                                                                                                                                                                   |
| [            d_Gauge.Foreground = [Brushes].Red;]                                                                     |
|                                                                                                                                                                                   |
| [            d_Gauge.Value = [\"10000\"];]                                                                            |
|                                                                                                                                                                                   |
| [            [//Sets the color for the dimmed segments.]]                                                               |
|                                                                                                                                                                                   |
| [            d_Gauge.DimmedBrush = [Brushes].LightGray;]                                                              |
|                                                                                                                                                                                   |
| [            [//Passing the gauge model to the view.]]                                                                  |
|                                                                                                                                                                                   |
| [            ViewData\[[\"GaugeModel\"]\] = d_Gauge;]                                                                 |
|                                                                                                                                                                                   |
| [            [return] View();]                                                                                           |
|                                                                                                                                                                                   |
| []                                                                                                                                            |
|                                                                                                                                                                                   |
| [        }]                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Step 3:

Run the code. You will get the following output.

[] 

{border="0"}

Figure 132: Gauge customization**[]**

[                                         ]

[]{#related-topics}
