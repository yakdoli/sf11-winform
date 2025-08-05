---
title: throughdigitalgaugemodel.md
original_path: WinForms_Docs/04_Controls/Gauge/throughdigitalgaugemodel.md
created_at: 2025-08-05
---






#### Through DigitalGaugeModel {#through-digitalgaugemodel style="tab-stops: 0pt"}

 

Step 1:

View:

Add the following code in your aspx file.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<%][@][ [Page] [Language][=\"C#\"] [MasterPageFile][=\"\~/Views/Shared/Site.Master\"] [Inherits][=\"System.Web.Mvc.ViewPage\"] [%\>]]                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<][asp][:][Content][ [ID][=\"Content1\"] [ContentPlaceHolderID][=\"TitleContent\"] [runat][=\"server\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [    Digital Gauge]                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\</][asp][:][Content][\>][]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<][asp][:][Content][ [ID][=\"Content2\"] [ContentPlaceHolderID][=\"MainContent\"] [runat][=\"server\"\>]]  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<%][\--Rendering the digital gauge\--][%\>][]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [     [\<%][=]Html.Syncfusion().DigitalGauge([\"Gauge\"], [\"GaugeModel\"])[%\>]]                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\</][asp][:][Content][\>][]                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                               |
| [\<][div][\>][]                                                  |
|                                                                                                                                                                                                                                                                                               |
| [@\*][\--Rendering the digital gauge\--][\*@][] |
|                                                                                                                                                                                                                                                                                               |
| [    ][@][Html.Syncfusion().DigitalGauge([\"Gauge\"], [\"GaugeModel\"])]   |
|                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                               |
| [\</][div][\>][]                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

**[]** 

Step 2:

Controller:

 

Add the below code in your controller. The Height and Width of the Digital Gauge can be controlled using its **Height** and **Width** properties.  The Width of the first and second frame can be customized by its **FirstFrameThickness** and **SecondFrameThickness** properties. The segments and characters of the digital gauge can be customized.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                            |
|                                                                                                                                                                                            |
| [public][ [ActionResult] Index()]                           |
|                                                                                                                                                                                            |
| [        {]                                                                                                                                   |
|                                                                                                                                                                                            |
| [            [//Creating the Digital Gauge.]]                                                                           |
|                                                                                                                                                                                            |
| [            [DigitalGaugeModel] d_Gauge = [new] [DigitalGaugeModel]();] |
|                                                                                                                                                                                            |
| [            [//Setting the height and width for the digital gauge.]]                                                   |
|                                                                                                                                                                                            |
| [            d_Gauge.Width = 350;]                                                                                                            |
|                                                                                                                                                                                            |
| [            d_Gauge.Height = 100;]                                                                                                           |
|                                                                                                                                                                                            |
| [            [//Setting the first and second frame thickness.]]                                                         |
|                                                                                                                                                                                            |
| [            d_Gauge.FirstFrameThickness = [new] System.Windows.[Thickness](8);]                 |
|                                                                                                                                                                                            |
| [            d_Gauge.SecondFrameThickness = [new] System.Windows.[Thickness](6);]                |
|                                                                                                                                                                                            |
| [            [//Setting first, second and center frame colors.]]                                                        |
|                                                                                                                                                                                            |
| [            d_Gauge.FirstFrameFillColor = [Brushes].LightGray;]                                                      |
|                                                                                                                                                                                            |
| [            d_Gauge.SecondFrameFillColor = [Brushes].DarkGray;]                                                      |
|                                                                                                                                                                                            |
| [            d_Gauge.CenterFrameFillColor = [Brushes].Gray;]                                                          |
|                                                                                                                                                                                            |
| [            [//Sets the color for the bright segments.]]                                                               |
|                                                                                                                                                                                            |
| [            d_Gauge.Foreground = [Brushes].Red;]                                                                     |
|                                                                                                                                                                                            |
| [            [//Sets the color for the dimmed segments.]]                                                               |
|                                                                                                                                                                                            |
| [            d_Gauge.DimmedBrush = [Brushes].DarkGray;]                                                               |
|                                                                                                                                                                                            |
| []                                                                                                                                            |
|                                                                                                                                                                                            |
| [            [//Setting the frame type.]]                                                                               |
|                                                                                                                                                                                            |
| [            d_Gauge.FrameType = [DigitalGaugeFrameType].CroppedRectangle;]                                           |
|                                                                                                                                                                                            |
| [            [//Setting the space between the segments.]]                                                               |
|                                                                                                                                                                                            |
| [            d_Gauge.SegmentSpacing = 0.8;]                                                                                                   |
|                                                                                                                                                                                            |
| [            [//Setting the character type.]]                                                                           |
|                                                                                                                                                                                            |
| [            d_Gauge.CharacterType = [CharacterType].SegmentFourteen;]                                                |
|                                                                                                                                                                                            |
| [            [//Setting character height and character count.]]                                                         |
|                                                                                                                                                                                            |
| [            d_Gauge.CharacterHeight = 28;]                                                                                                   |
|                                                                                                                                                                                            |
| [            d_Gauge.CharacterCount = 10;]                                                                                                    |
|                                                                                                                                                                                            |
| [            [//Setting the space between the characters.]]                                                             |
|                                                                                                                                                                                            |
| [            d_Gauge.CharacterSpacing = 5;]                                                                                                   |
|                                                                                                                                                                                            |
| [            [//Setting the segment width.]]                                                                            |
|                                                                                                                                                                                            |
| [            d_Gauge.SegmentWidth = 2;]                                                                                                       |
|                                                                                                                                                                                            |
| [            [//Setting the value for the gauge.]]                                                                      |
|                                                                                                                                                                                            |
| [            d_Gauge.Value = [\"Syncfusion\"];]                                                                       |
|                                                                                                                                                                                            |
| [            [//Passing the gauge model to the view.]]                                                                  |
|                                                                                                                                                                                            |
| [            ViewData\[[\"GaugeModel\"]\] = d_Gauge;]                                                                 |
|                                                                                                                                                                                            |
| [            [return] View();]                                                                                           |
|                                                                                                                                                                                            |
| [        }]                                                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Step 3:

Run the code. You will get the below output.

 

[{border="0"}]

Figure 122: Digital Gauge**[]**

[                                    ]

A sample which demonstrates[ a ]Digital Gauge control can be downloaded from the below mentioned link.

[] 


[ASPX Application](http://files2.syncfusion.com/support/ASP%20MVC/UG/Gauge/Digital%20Gauge%20(ASPX).zip)

[Razor Application](http://files2.syncfusion.com/support/ASP%20MVC/UG/Gauge/Digital%20Gauge%20(Razor).zip)

 

{border="0"} Note: The version number for the assemblies has been set to 9.4.0.62 in the Web.config file of the attached sample.


[]{#related-topics}

