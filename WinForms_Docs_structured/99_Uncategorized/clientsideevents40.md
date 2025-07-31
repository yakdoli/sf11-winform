---
title: clientsideevents40.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\clientsideevents40.md
created_at: 2025-07-03
---






#### Client-Side Events {#client-side-events style="tab-stops: 0pt"}

 

The slider control supports client-side event handling.

 

Events

 

Table 6: Event Table

  -------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------- ----------------
  Name                 Description                                                                                                                                                                                                                                                  Arguments   Reference Link
  ClientSideOnChange   This event is triggered when the slider stops, or if the value is changed programmatically (by the Value method). It takes the Arguments event and UI. Use event.orginalEvent to detect whether the value changes by mouse, keyboard, or programmatically.   event,ui    NA
  ClientSideOnSlide    This event is triggered when the pointer moves the slider. Use ui.value (single-handled sliders) to obtain the value of the current handle.                                                                                                                  event,ui    NA
  ClientSideOnStart    This event is triggered when the user starts sliding.                                                                                                                                                                                                        event,ui    NA
  ClientSideOnStop     This event is triggered when the user stops sliding.                                                                                                                                                                                                         event,ui    NA
  -------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------- ----------------

 

Using Builder

 

[The following steps explain how to handle events using Builder.**]

1.   In **View**, invoke the slider helper with the control ID as an argument followed by the **ClientSideOnChange**, **ClientSideOnSlide**, **ClientSideOnStart**, and **ClientSideOnStop** methods with the desired handlers as arguments.[]

[] 

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| [\<%][=][Html.Syncfusion().Slider([\"mySlider\"])] |
|                                                                                                                                                                                                                         |
| [.**ClientSideOnChange([\"OnChange\"])**]                                                                                                                   |
|                                                                                                                                                                                                                         |
| **[.ClientSideOnSlide([\"OnSlide\"])]**                                                                                                                     |
|                                                                                                                                                                                                                         |
| **[.ClientSideOnStart([\"OnStart\"])]**                                                                                                                     |
|                                                                                                                                                                                                                         |
| **[.ClientSideOnStop([\"OnStop\"])]**[%\>]                                                          |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                           |
|                                                                                                                                                                                                              |
| [\@{][ Html.Syncfusion().Slider([\"mySlider\"])]                                         |
|                                                                                                                                                                                                              |
| [.**ClientSideOnChange([\"OnChange\"])**]                                                                                                        |
|                                                                                                                                                                                                              |
| **[.ClientSideOnSlide([\"OnSlide\"])]**                                                                                                          |
|                                                                                                                                                                                                              |
| **[.ClientSideOnStart([\"OnStart\"])]**                                                                                                          |
|                                                                                                                                                                                                              |
| **[.ClientSideOnStop([\"OnStop\"])]**[.Render();][}] |
|                                                                                                                                                                                                              |
| []                                                                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

2.   In JavaScript, define the handlers.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                                                                                                                       |
|                                                                                                                                                                                                                                |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                |
| [        [function] OnChange(event, ui) {]                                                                                                                            |
|                                                                                                                                                                                                                                |
| [            [//event     - object sent by jQuery event trigger]]                                                                                                |
|                                                                                                                                                                                                                                |
| [            [//ui:]]                                                                                                                                            |
|                                                                                                                                                                                                                                |
| [            [//  handle  - handle as a DOM element]]                                                                                                            |
|                                                                                                                                                                                                                                |
| [            [//  value   - current value of the slider]]                                                                                                        |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [        [function] OnSlide(event, ui) {]                                                                                                                             |
|                                                                                                                                                                                                                                |
| [            [//event     - object sent by jQuery event trigger]]                                                                                                |
|                                                                                                                                                                                                                                |
| [            [//ui:]]                                                                                                                                            |
|                                                                                                                                                                                                                                |
| [            [//  handle  - handle as a DOM element]]                                                                                                            |
|                                                                                                                                                                                                                                |
| [            [//  value   - current value of the slider]]                                                                                                        |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [        [function] OnStart(event, ui) {]                                                                                                                             |
|                                                                                                                                                                                                                                |
| [            [//event     - object sent by jQuery event trigger]]                                                                                                |
|                                                                                                                                                                                                                                |
| [            [//ui:]]                                                                                                                                            |
|                                                                                                                                                                                                                                |
| [            [//  handle  - handle as a DOM element]]                                                                                                            |
|                                                                                                                                                                                                                                |
| [            [//  value   - current value of the slider]]                                                                                                        |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [        [function] OnStop(event, ui) {]                                                                                                                              |
|                                                                                                                                                                                                                                |
| [            [//event     - object sent by jQuery event trigger]]                                                                                                |
|                                                                                                                                                                                                                                |
| [            [//ui:]]                                                                                                                                            |
|                                                                                                                                                                                                                                |
| [            [//  handle  - handle as a DOM element]]                                                                                                            |
|                                                                                                                                                                                                                                |
| [            [//  value   - current value of the slider]]                                                                                                        |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [      [\</][script][\>]]                                                                                                 |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

3.   Build and run the application.

**[]** 

Using Properties Model

The following steps explain how to handle events through the properties model.**

1.   In the controller, create an instance of **SliderModel**.

2.   Define the **ClientSideOnChange**, **ClientSideOnSlide**, **ClientSideOnStart**, and **ClientSideOnStop.** properties and pass the instance through the view-specific data to the view.[]

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[ \[Controller\]]**                                                                                                             |
|                                                                                                                                                                       |
| [public][ [ActionResult] Index()]                        |
|                                                                                                                                                                       |
| [        {]                                                                                                                       |
|                                                                                                                                                                       |
| [            [//Create an instance of TabModel.]]                                                           |
|                                                                                                                                                                       |
| [            [SliderModel] myModel = [new] [SliderModel]();] |
|                                                                                                                                                                       |
| [            **myModel.ClientSideOnChange = [\"OnChange\"];**]                                            |
|                                                                                                                                                                       |
| **[            myModel.ClientSideOnSlide = [\"OnSlide\"];]**                                              |
|                                                                                                                                                                       |
| **[            myModel.ClientSideOnStart = [\"OnStart\"];]**                                              |
|                                                                                                                                                                       |
| **[            myModel.ClientSideOnStop = [\"OnStop\"];]**                                                |
|                                                                                                                                                                       |
| []                                                                                                                                |
|                                                                                                                                                                       |
| [            [//Pass the instance through view data to the view.]]                                          |
|                                                                                                                                                                       |
| [            ViewData\[[\"mySlider\"]\] = myModel;]                                                       |
|                                                                                                                                                                       |
| [            [return] View();]                                                                               |
|                                                                                                                                                                       |
| [        }]                                                                                                                       |
|                                                                                                                                                                       |
| []                                                                                                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   In **View**, invoke the slider helper with view data key as the control ID.**

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                          |
| [\<%][=][Html.Syncfusion().Slider([\"mySlider\"])[%\>]] |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                            |
|                                                                                                                                                                                                               |
| [\@{][ Html.Syncfusion().Slider([\"mySlider\"]).Render();[}]] |
|                                                                                                                                                                                                               |
| []                                                                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

***[[[]]]{.underline}*** 

4.   In JavaScript, define the handlers.[]

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[JavaScript\]**                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                       |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                                                       |
| [        [function] OnChange(event, ui) {]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [            [//event     - object sent by jQuery event trigger]]                                                                                                                          |
|                                                                                                                                                                                                                                                                       |
| [            [//ui:]]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [            [//  handle  - handle as a DOM element]]                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [            [//  value   - current value of the slider]]                                                                                                                                  |
|                                                                                                                                                                                                                                                                       |
| [        }]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                       |
| [        [function] OnSlide(event, ui) {]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                       |
| [            [//event     - object sent by jQuery event trigger]]                                                                                                                          |
|                                                                                                                                                                                                                                                                       |
| [            [//ui:]]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [            [//  handle  - handle as a DOM element]]                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [            [//  value   - current value of the slider]]                                                                                                                                  |
|                                                                                                                                                                                                                                                                       |
| [        }]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                       |
| [        [function] OnStart(event, ui) {]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                       |
| [            [//event     - object sent by jQuery event trigger]]                                                                                                                          |
|                                                                                                                                                                                                                                                                       |
| [            [//ui:]]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [            [//  handle  - handle as a DOM element]]                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [            [//  value   - current value of the slider]]                                                                                                                                  |
|                                                                                                                                                                                                                                                                       |
| [        }]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                       |
| [        [function] OnStop(event, ui) {]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                       |
| [            [//event     - object sent by jQuery event trigger]]                                                                                                                          |
|                                                                                                                                                                                                                                                                       |
| [            [//ui:]]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [            [//  handle  - handle as a DOM element]]                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [            [//  value   - current value of the slider]]                                                                                                                                  |
|                                                                                                                                                                                                                                                                       |
| [        }]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                       |
| [       [\</][script][\>]]                                                                                                                          |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

5.   Build and run the application.

You can observer the handlers being invoked when the corresponding events are triggered.

 

[]{#related-topics}

