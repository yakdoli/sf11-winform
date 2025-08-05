---
title: interaction1.md
original_path: WinForms_Docs/99_Uncategorized/interaction1.md
created_at: 2025-08-05
---






##### Interaction {#interaction style="tab-stops: 0pt"}

 

Essential Gauge supports business-oriented gauges, which uses pointers and pointer animation to communicate data to the user. Interaction with gauge can be enabled by setting the **EnablePointerInteraction** property to True.

 

Properties:

 


+--------------------------+----------------------------------------+-----------------------------+------------------------------+--------------------------------------------------+
| Property                 | Description                            | Type of Property            | Value It Accepts             | Any other dependencies/Sub properties associated |
+--------------------------+----------------------------------------+-----------------------------+------------------------------+--------------------------------------------------+
| EnablePointerInteraction | To enable the interation with Pointer. | [bool] | [True]  | [NA]                     |
|                          |                                        |                             |                              |                                                  |
|                          |                                        |                             | []      |                                                  |
|                          |                                        |                             |                              |                                                  |
|                          |                                        |                             | [false] |                                                  |
+--------------------------+----------------------------------------+-----------------------------+------------------------------+--------------------------------------------------+


[] 

ClientSide Events:

 


  -------------------- ------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------
  Name                 Description                                                                                                               Arguments
  PointerValueChange   [The event can be triggered while the pointer value is changing during interaction or animation.]   [(GaugeObject, PointerValue)][]
  -------------------- ------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------


[] 

###### 5.2.3.8.1.1 Through View Customization {#through-view-customization style="tab-stops: 0pt"}

 

Step 1:

View:

 

Add the below code in your aspx file. In the function **OnPointerValueChange()**, PointerValueChange event is handled.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<%][@][ [Page] [Language][=\"C#\"] [MasterPageFile][=\"\~/Views/Shared/Site.Master\"] [Inherits][=\"System.Web.Mvc.ViewPage\"] [%\>]]                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<][asp][:][Content][ [ID][=\"Content1\"] [ContentPlaceHolderID][=\"TitleContent\"] [runat][=\"server\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [    Linear Gauge]                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\</][asp][:][Content][\>][]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<][asp][:][Content][ [ID][=\"Content2\"] [ContentPlaceHolderID][=\"MainContent\"] [runat][=\"server\"\>]]  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [    [\<%] Html.RenderPartial([\"PartialView\"]); [%\>]]                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [    [\<][script] [type][=\"text/javascript\"\>]]                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [        [//handling the PointerValueChange  event]]                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [        [function] OnPointerValueChange(gauge, value) {]                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [            alert([\"Pointer Value:\"] + value);]                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [    [\</][script][\>]]                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\</][asp][:][Content][\>]                                                                                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                     |
|                                                                                                                                                                                                              |
| [\<][div][\>]**[]** |
|                                                                                                                                                                                                              |
| [    [@]Html.Partial([\"PartialView\"])]                                                                             |
|                                                                                                                                                                                                              |
| []                                                                                                                                                                       |
|                                                                                                                                                                                                              |
| [    [\<][script] [type][=\"text/javascript\"\>]]                                   |
|                                                                                                                                                                                                              |
| [        [//handling the PointerValueChange  event]]                                                                                           |
|                                                                                                                                                                                                              |
| []                                                                                                                                                                       |
|                                                                                                                                                                                                              |
| [        [function] OnPointerValueChange(gauge, value) {]                                                                                           |
|                                                                                                                                                                                                              |
| []                                                                                                                                                                       |
|                                                                                                                                                                                                              |
| [            alert([\"Pointer Value:\"] + value);]                                                                                                |
|                                                                                                                                                                                                              |
| [        }]                                                                                                                                                              |
|                                                                                                                                                                                                              |
| [    [\</][script][\>]]                                                                                 |
|                                                                                                                                                                                                              |
| [\</][div][\>]                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

**[]** 

Step 2:

PartialView:

 

Add the below code in partial view. Linear Pointer interaction can be enabled by setting its **EnablePointerInteraction** property to True.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[ASPX\]]                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<%][@][ [Control] [Language][=\"C#\"] [Inherits][=\"System.Web.Mvc.ViewUserControl\"] [%\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [\<%][=]Html.Syncfusion().LinearGauge([\"Gauge\"])]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                .Height(130).LinearGaugeParams(([LinearGaugeParams])ViewData\[[\"GaugeParams\"]\])]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [        .FrameType([LinearGaugeFrameType].Rectangle)]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [        .GaugeSkins([GaugeSkins].VS2010)]                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [        .Orientation([GaugeOrientation].Horizontal)]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [            .Width(420)]                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                  .Scales(scale =\>]                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                  {]                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                      scale.Add()]                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                      .Maximum(100)]                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                      .Minimum(0)]                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                      .MajorIntervalValue(10)]                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                      .MinorIntervalValue(2)]                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                      .ScaleDirection([ScaleDirection].Clockwise)]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                       .Labels(label =\>]                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                        {]                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                            label.Add()]                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                                .TickStyle([TickStyle].MajorTick)]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                                .TickPlacement([ScalePlacement].Inside)]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                                .BackgroundBrush([Brushes].White)]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                                .Angle(0)]                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                                .FontSize(16)]                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                                .DistanceFromScale(5)]                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                                .IncludeFirstValue([true]);]                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                        })]                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                      .Ticks(tick =\>]                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                      {]                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                          tick.Add()]                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                              .TickStyle([TickStyle].MajorTick)]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                              .TickWidth(3)]                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                              .TickHeight(12)]                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                              .DistanceFromScale(10);]                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                          tick.Add()]                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                              .TickStyle([TickStyle].MinorTick)]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                              .TickWidth(1)]                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                              .TickHeight(6)]                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                              .DistanceFromScale(10);]                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                      })]                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                      ]                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                       .Pointers(pointer =\>]                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                                  {]                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                                      pointer.AddBarPointer()]                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                                      .EnablePointerInteraction([true])]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                                      .PointerValueChange([\"OnPointerValueChange\"])]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                                      .Value(5);]                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                                      pointer.AddMarker()]                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                                          .Value(5)]                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| **[                                          .EnablePointerInteraction([true])]**                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                                          .PointerPlacement([ScalePlacement].Outside)]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                                          .MarkerStyle([MarkerStyle].Diamond)]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                                          .PointerLength(17)]                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                                          .PointerWidth(12);]                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                                          ]                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                                  });]                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                  })]                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [                 [%\>]]                                                                                                                                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[cshtml\]]                                                                                                                                    |
|                                                                                                                                                                                         |
| [    [\@{] Html.Syncfusion().LinearGauge([\"Gauge\"])]                                          |
|                                                                                                                                                                                         |
| [               .Height(130).LinearGaugeParams(([LinearGaugeParams])ViewData\[[\"GaugeParams\"]\])] |
|                                                                                                                                                                                         |
| [        .FrameType([LinearGaugeFrameType].Rectangle)]                                                                      |
|                                                                                                                                                                                         |
| [        .GaugeSkins([GaugeSkins].VS2010)]                                                                                  |
|                                                                                                                                                                                         |
| [        .Orientation([GaugeOrientation].Horizontal)]                                                                       |
|                                                                                                                                                                                         |
| [            .Width(420)]                                                                                                                           |
|                                                                                                                                                                                         |
| [                  .Scales(scale =\>]                                                                                                               |
|                                                                                                                                                                                         |
| [                  {]                                                                                                                               |
|                                                                                                                                                                                         |
| [                      scale.Add()]                                                                                                                 |
|                                                                                                                                                                                         |
| [                      .Maximum(100)]                                                                                                               |
|                                                                                                                                                                                         |
| [                      .Minimum(0)]                                                                                                                 |
|                                                                                                                                                                                         |
| [                      .MajorIntervalValue(10)]                                                                                                     |
|                                                                                                                                                                                         |
| [                      .MinorIntervalValue(2)]                                                                                                      |
|                                                                                                                                                                                         |
| [                      .ScaleDirection([ScaleDirection].Clockwise)]                                                         |
|                                                                                                                                                                                         |
| [                       .Labels(label =\>]                                                                                                          |
|                                                                                                                                                                                         |
| [                        {]                                                                                                                         |
|                                                                                                                                                                                         |
| [                            label.Add()]                                                                                                           |
|                                                                                                                                                                                         |
| [                                .TickStyle([TickStyle].MajorTick)]                                                         |
|                                                                                                                                                                                         |
| [                                .TickPlacement([ScalePlacement].Inside)]                                                   |
|                                                                                                                                                                                         |
| [                                .BackgroundBrush([Brushes].White)]                                                         |
|                                                                                                                                                                                         |
| [                                .Angle(0)]                                                                                                         |
|                                                                                                                                                                                         |
| [                                .FontSize(16)]                                                                                                     |
|                                                                                                                                                                                         |
| [                                .DistanceFromScale(5)]                                                                                             |
|                                                                                                                                                                                         |
| [                                .IncludeFirstValue([true]);]                                                                  |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [                        })]                                                                                                                        |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [                      .Ticks(tick =\>]                                                                                                             |
|                                                                                                                                                                                         |
| [                      {]                                                                                                                           |
|                                                                                                                                                                                         |
| [                          tick.Add()]                                                                                                              |
|                                                                                                                                                                                         |
| [                              .TickStyle([TickStyle].MajorTick)]                                                           |
|                                                                                                                                                                                         |
| [                              .TickWidth(3)]                                                                                                       |
|                                                                                                                                                                                         |
| [                              .TickHeight(12)]                                                                                                     |
|                                                                                                                                                                                         |
| [                              .DistanceFromScale(10);]                                                                                             |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [                          tick.Add()]                                                                                                              |
|                                                                                                                                                                                         |
| [                              .TickStyle([TickStyle].MinorTick)]                                                           |
|                                                                                                                                                                                         |
| [                              .TickWidth(1)]                                                                                                       |
|                                                                                                                                                                                         |
| [                              .TickHeight(6)]                                                                                                      |
|                                                                                                                                                                                         |
| [                              .DistanceFromScale(10);]                                                                                             |
|                                                                                                                                                                                         |
| [                      })]                                                                                                                          |
|                                                                                                                                                                                         |
| [                      ]                                                                                                                            |
|                                                                                                                                                                                         |
| [                       .Pointers(pointer =\>]                                                                                                      |
|                                                                                                                                                                                         |
| [                                  {]                                                                                                               |
|                                                                                                                                                                                         |
| [                                      pointer.AddBarPointer()]                                                                                     |
|                                                                                                                                                                                         |
| [                                      .EnablePointerInteraction([true])]                                                      |
|                                                                                                                                                                                         |
| [                                      .PointerValueChange([\"OnPointerValueChange\"])]                                     |
|                                                                                                                                                                                         |
| [                                      .Value(5);]                                                                                                  |
|                                                                                                                                                                                         |
| [                                      pointer.AddMarker()]                                                                                         |
|                                                                                                                                                                                         |
| [                                          .Value(5)]                                                                                               |
|                                                                                                                                                                                         |
| **[                                          .EnablePointerInteraction([true])]**                                              |
|                                                                                                                                                                                         |
| [                                          .PointerPlacement([ScalePlacement].Outside)]                                     |
|                                                                                                                                                                                         |
| [                                          .MarkerStyle([MarkerStyle].Diamond)]                                             |
|                                                                                                                                                                                         |
| [                                          .PointerLength(17)]                                                                                      |
|                                                                                                                                                                                         |
| [                                          .PointerWidth(12);]                                                                                      |
|                                                                                                                                                                                         |
| [                                          ]                                                                                                        |
|                                                                                                                                                                                         |
| [                                  });]                                                                                                             |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [                  }).Render();]                                                                                                                    |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [          [}]]                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Step 3:

Controller:

 

Add the below code in your controller. Using the **LinearGaugeParams** class, you can get the Post parameter values for the Interaction.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [using][ System.Web;]                                                                           |
|                                                                                                                                                                                      |
| [using][ System.Web.Mvc;]                                                                       |
|                                                                                                                                                                                      |
| [using][ Syncfusion.Mvc.Gauge;]                                                                 |
|                                                                                                                                                                                      |
| [using][ Syncfusion.Mvc.Shared;]                                                                |
|                                                                                                                                                                                      |
| [using][ System.Windows.Media;]                                                                 |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [namespace][ CircularGauge.Controllers]                                                         |
|                                                                                                                                                                                      |
| [{]                                                                                                                                              |
|                                                                                                                                                                                      |
| [    \[[HandleError]\]]                                                                                                  |
|                                                                                                                                                                                      |
| [    [public] [class] [HomeController] : [Controller]] |
|                                                                                                                                                                                      |
| [    {]                                                                                                                                          |
|                                                                                                                                                                                      |
| [        [public] [ActionResult] Index()]                                                           |
|                                                                                                                                                                                      |
| [        {]                                                                                                                                      |
|                                                                                                                                                                                      |
| [            [return] View();]                                                                                              |
|                                                                                                                                                                                      |
| [        }]                                                                                                                                      |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [        \[[AcceptVerbs]([HttpVerbs].Post)\]]                                                    |
|                                                                                                                                                                                      |
| [        [public] [ActionResult] Index([LinearGaugeParams] param)]          |
|                                                                                                                                                                                      |
| [        {]                                                                                                                                      |
|                                                                                                                                                                                      |
| [     //Passing the LinearGaugeParams values to the view.][]                                   |
|                                                                                                                                                                                      |
| [            ViewData\[[\"GaugeParams\"]\] = param;]                                                                     |
|                                                                                                                                                                                      |
| [            [return] PartialView([\"PartialView\"], [this].ViewData);]        |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [        }]                                                                                                                                      |
|                                                                                                                                                                                      |
| [    }]                                                                                                                                          |
|                                                                                                                                                                                      |
| [}]                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Step 4:

Run the code. You will get the following output.

 

{border="0"}

Figure 113: Linear Gauge-Before Interaction[                                                                    ]

 

Step 5:

Click inside the Gauge to interact with pointer. Then you will get the following output.

[] 

{border="0"}

Figure 114: Linear Gauge-After Interaction**[]**

[] 

###### 5.2.3.8.1.2 Through LinearGaugeModel {#through-lineargaugemodel style="tab-stops: 0pt"}

 

Step 1:

View:

 

Add the below code in your aspx file.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<%][@][ [Page] [Language][=\"C#\"] [MasterPageFile][=\"\~/Views/Shared/Site.Master\"] [Inherits][=\"System.Web.Mvc.ViewPage\"] [%\>]]                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<][asp][:][Content][ [ID][=\"Content1\"] [ContentPlaceHolderID][=\"TitleContent\"] [runat][=\"server\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [    Circular Gauge]                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\</][asp][:][Content][\>][]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<][asp][:][Content][ [ID][=\"Content2\"] [ContentPlaceHolderID][=\"MainContent\"] [runat][=\"server\"\>]]  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [    [\<%][=]Html.Syncfusion().LinearGauge([\"Gauge\"], ([LinearGaugeModel])ViewData\[[\"GaugeModel\"]\])[%\>]]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [    [\<][script] [type][=\"text/javascript\"\>]]                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [        [//Handling the PointerValueChange  event.]]                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [        [function] OnPointerValueChange(gauge, value) {]                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [            alert([\"Pointer Value:\"] + value);]                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [    [\</][script][\>]]                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\</][asp][:][Content][\>]                                                                                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                         |
| [\<][div][\>]**[]**                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                         |
| [  ][@][Html.Syncfusion().LinearGauge([\"Gauge\"], ([LinearGaugeModel])ViewData\[[\"GaugeModel\"]\])] |
|                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                         |
| [    [\<][script] [type][=\"text/javascript\"\>]]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                         |
| [        [//Handling the PointerValueChange  event.]]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                         |
| [        [function] OnPointerValueChange(gauge, value) {]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                         |
| [            alert([\"Pointer Value:\"] + value);]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                         |
| [    [\</][script][\>]]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                         |
| [\</][div][\>]                                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Step 2:

Controller:

 

Add the below code in your controller. In the **LinearGaugeInteraction()** function, lineargauge is created.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [using][ System.Web;]                                                                              |
|                                                                                                                                                                                         |
| [using][ System.Web.Mvc;]                                                                          |
|                                                                                                                                                                                         |
| [using][ Syncfusion.Mvc.Gauge;]                                                                    |
|                                                                                                                                                                                         |
| [using][ Syncfusion.Mvc.Shared;]                                                                   |
|                                                                                                                                                                                         |
| [using][ System.Windows.Media;]                                                                    |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [namespace][ CircularGauge.Controllers]                                                            |
|                                                                                                                                                                                         |
| [{]                                                                                                                                                 |
|                                                                                                                                                                                         |
| [    \[[HandleError]\]]                                                                                                     |
|                                                                                                                                                                                         |
| [    [public] [class] [HomeController] : [Controller]]    |
|                                                                                                                                                                                         |
| [    {]                                                                                                                                             |
|                                                                                                                                                                                         |
| [        [public] [ActionResult] Index()]                                                              |
|                                                                                                                                                                                         |
| [        {]                                                                                                                                         |
|                                                                                                                                                                                         |
| [            [LinearGaugeModel] gauge = LinearGaugeInteraction();]                                                          |
|                                                                                                                                                                                         |
| [            ViewData\[[\"GaugeModel\"]\] = gauge;]                                                                         |
|                                                                                                                                                                                         |
| [            [return] View();]                                                                                                 |
|                                                                                                                                                                                         |
| [        }]                                                                                                                                         |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [        \[[AcceptVerbs]([HttpVerbs].Post)\]]                                                       |
|                                                                                                                                                                                         |
| [        [public] [ActionResult] Index([LinearGaugeParams] param)]             |
|                                                                                                                                                                                         |
| [        {]                                                                                                                                         |
|                                                                                                                                                                                         |
| [            [if] (param.GaugeAction == [GaugeAction].Interaction)]                                    |
|                                                                                                                                                                                         |
| [            {]                                                                                                                                     |
|                                                                                                                                                                                         |
| [                [LinearGaugeModel] c_model = LinearGaugeInteraction();]                                                    |
|                                                                                                                                                                                         |
| [//If gauge action is Interaction or Animation, then you have to pass the circular gauge post parameter values to]                |
|                                                                                                                                                                                         |
| [//LinearGaugeActionResult class.][]                                                          |
|                                                                                                                                                                                         |
| [                [return] c_model.LinearGaugeActionResult(param);]                                                             |
|                                                                                                                                                                                         |
| [            }]                                                                                                                                     |
|                                                                                                                                                                                         |
| [            [else]]                                                                                                           |
|                                                                                                                                                                                         |
| [                [return] View();]                                                                                             |
|                                                                                                                                                                                         |
| [        }]                                                                                                                                         |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [        [LinearGaugeModel] LinearGaugeInteraction()]                                                                       |
|                                                                                                                                                                                         |
| [        {]                                                                                                                                         |
|                                                                                                                                                                                         |
| [            [LinearGaugeModel] model = [new] [LinearGaugeModel]();]           |
|                                                                                                                                                                                         |
| [            model.GaugeSkins = [GaugeSkins].VS2010;]                                                                       |
|                                                                                                                                                                                         |
| [            model.Orientation = [GaugeOrientation].Horizontal;]                                                            |
|                                                                                                                                                                                         |
| [            model.Height = 130;]                                                                                                                   |
|                                                                                                                                                                                         |
| [            model.Width = 420;]                                                                                                                    |
|                                                                                                                                                                                         |
| [            model.FrameType = [LinearGaugeFrameType].Rectangle;]                                                           |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [            [LinearScale] c_Scale = [new] [LinearScale]();]                   |
|                                                                                                                                                                                         |
| [            c_Scale.Maximum = 100;]                                                                                                                |
|                                                                                                                                                                                         |
| [            c_Scale.Minimum = 0;]                                                                                                                  |
|                                                                                                                                                                                         |
| [            c_Scale.MinorIntervalValue = 2;]                                                                                                       |
|                                                                                                                                                                                         |
| [            c_Scale.MajorIntervalValue = 10;]                                                                                                      |
|                                                                                                                                                                                         |
| [            c_Scale.ScaleDirection = [ScaleDirection].Clockwise;]                                                          |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [            [TickMark] \_minor = [new] [TickMark]();]                         |
|                                                                                                                                                                                         |
| [            \_minor.TickStyle = [TickStyle].MinorTick;]                                                                    |
|                                                                                                                                                                                         |
| [            \_minor.TickWidth = 1;]                                                                                                                |
|                                                                                                                                                                                         |
| [            \_minor.TickHeight = 6;]                                                                                                               |
|                                                                                                                                                                                         |
| [            \_minor.DistanceFromScale = 10;]                                                                                                       |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [            [GaugeLabelTick] label = [new] [GaugeLabelTick]();]               |
|                                                                                                                                                                                         |
| [            label.FontSize = 12;]                                                                                                                  |
|                                                                                                                                                                                         |
| [            label.TickPlacement = [ScalePlacement].Inside;]                                                                |
|                                                                                                                                                                                         |
| [            label.BackgroundBrush = [Brushes].White;]                                                                      |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [            [TickMark] \_major = [new] [TickMark]();]                         |
|                                                                                                                                                                                         |
| [            \_major.TickStyle = [TickStyle].MajorTick;]                                                                    |
|                                                                                                                                                                                         |
| [            \_major.TickWidth = 3;]                                                                                                                |
|                                                                                                                                                                                         |
| [            \_major.TickHeight = 12;]                                                                                                              |
|                                                                                                                                                                                         |
| [            \_major.DistanceFromScale = 10;]                                                                                                       |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [            [LinearBarPointer] c_Pointer = [new] [LinearBarPointer]();]       |
|                                                                                                                                                                                         |
| [            c_Pointer.Value = 5;]                                                                                                                  |
|                                                                                                                                                                                         |
| [            c_Pointer.EnablePointerInteraction = [true];]                                                                     |
|                                                                                                                                                                                         |
| [     //To handle the event after pointer value is changed.][]                                |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [            c_Pointer.PointerValueChange = [\"OnPointerValueChange\"];]                                                    |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [            [LinearMarkerPointer] m_Pointer = [new] [LinearMarkerPointer]();] |
|                                                                                                                                                                                         |
| [            m_Pointer.Value = 5;]                                                                                                                  |
|                                                                                                                                                                                         |
| [            m_Pointer.MarkerStyle = [MarkerStyle].Diamond;]                                                                |
|                                                                                                                                                                                         |
| [            m_Pointer.PointerPlacement = [ScalePlacement].Outside;]                                                        |
|                                                                                                                                                                                         |
| [            m_Pointer.PointerLength = 17;]                                                                                                         |
|                                                                                                                                                                                         |
| [            m_Pointer.PointerWidth = 12;]                                                                                                          |
|                                                                                                                                                                                         |
| [            m_Pointer.EnablePointerInteraction = [true];]                                                                     |
|                                                                                                                                                                                         |
| [            //To handle the event after pointer value is changed.][]                         |
|                                                                                                                                                                                         |
| [            m_Pointer.PointerValueChange = [\"OnPointerValueChange\"];]                                                    |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [            c_Scale.Labels.Add(label);]                                                                                                            |
|                                                                                                                                                                                         |
| [            c_Scale.Ticks.Add(\_minor);]                                                                                                           |
|                                                                                                                                                                                         |
| [            c_Scale.Ticks.Add(\_major);]                                                                                                           |
|                                                                                                                                                                                         |
| [            c_Scale.Pointers.Add(c_Pointer);]                                                                                                      |
|                                                                                                                                                                                         |
| [            c_Scale.Pointers.Add(m_Pointer);]                                                                                                      |
|                                                                                                                                                                                         |
| [            model.Scales.Add(c_Scale);]                                                                                                            |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [            [return] model;]                                                                                                  |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [        }]                                                                                                                                         |
|                                                                                                                                                                                         |
| [    }]                                                                                                                                             |
|                                                                                                                                                                                         |
| [}]                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Step 4:

Run the code. You will get the below output.

 

{border="0"}

Figure 115: LinearGauge-Before Interaction[                          ]

 

Step 5:

Click inside the Gauge to interact with pointer. Then you will get the following output.

[] 

{border="0"}

Figure 116: LinearGauge-After Interaction

[] 

[]{#related-topics}

