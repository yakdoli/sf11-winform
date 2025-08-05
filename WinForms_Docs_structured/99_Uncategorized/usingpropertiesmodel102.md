---
title: usingpropertiesmodel102.md
original_path: WinForms_Docs/99_Uncategorized/usingpropertiesmodel102.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

The following steps explain how to handle events through the properties model.**

1.   In the controller, create an instance of **MobSliderModel**.

2.   Define the **ClientSideOnChange**, **ClientSideOnSlide**, **ClientSideOnStart**, **ClientSideOnStop,** and **ClientSideOnLoad.** properties and pass the instance through the view-specific data to the view.[]

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                  |
|                                                                                                                                                                           |
| [public] [ [ActionResult] Index()]                           |
|                                                                                                                                                                           |
| [        {]                                                                                                                           |
|                                                                                                                                                                           |
| [            [MobSliderModel] slider = [new][MobSliderModel]();] |
|                                                                                                                                                                           |
| [            slider.Value = 20;]                                                                                                      |
|                                                                                                                                                                           |
| **[            slider.ClientSideOnChange = [\"OnChange\"];]**                                                 |
|                                                                                                                                                                           |
| **[            slider.ClientSideOnLoad = [\"OnLoad\"];]**                                                     |
|                                                                                                                                                                           |
| **[            slider.ClientSideOnSlide = [\"OnSlide\"];]**                                                   |
|                                                                                                                                                                           |
| **[            slider.ClientSideOnStart = [\"OnStart\"];]**                                                   |
|                                                                                                                                                                           |
| **[            slider.ClientSideOnStop = [\"OnStop\"];]**                                                     |
|                                                                                                                                                                           |
| [            [return] View();]                                                                                   |
|                                                                                                                                                                           |
| [        }]                                                                                                                           |
|                                                                                                                                                                           |
| []                                                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   In **View**, invoke the slider helper with view data key as the control ID.**

***[[ [] ]]{.underline}***  

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                     |
| [\<%] [=] [Html.Syncfusion().Slider([\"slider\"])[%\>]] **[]** |
|                                                                                                                                                                                                                                                                                                     |
| **[[ [] ]]{.underline}**                                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[ \[Razor\]]**                                                                                                                                                            |
|                                                                                                                                                                                                                 |
| [\@{] [ Html.MobSyncfusion().Slider([\"slider\"]).Render();[}]] |
|                                                                                                                                                                                                                 |
| **[[ [] ]]{.underline}**                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.   In JavaScript, define the handlers.[]

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                                                                                                                           |
|                                                                                                                                                                                                                                    |
| [\<] [script] [ [type] [=\"text/javascript\"\>] ] |
|                                                                                                                                                                                                                                    |
| [        [function] OnChange(event, data) {]                                                                                                                              |
|                                                                                                                                                                                                                                    |
| [            [//event     - object sent by jQuery event trigger]]                                                                                                    |
|                                                                                                                                                                                                                                    |
| [            [//data:]]                                                                                                                                              |
|                                                                                                                                                                                                                                    |
| [            [//  value   - current value of the slider]]                                                                                                            |
|                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [        [function] OnSlide(event, data) {]                                                                                                                               |
|                                                                                                                                                                                                                                    |
| [            [//event     - object sent by jQuery event trigger]]                                                                                                    |
|                                                                                                                                                                                                                                    |
| [            [//data:]]                                                                                                                                              |
|                                                                                                                                                                                                                                    |
| [            [//  value   - current value of the slider]]                                                                                                            |
|                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [        [function] OnStart(event, data) {]                                                                                                                               |
|                                                                                                                                                                                                                                    |
| [            [//event     - object sent by jQuery event trigger]]                                                                                                    |
|                                                                                                                                                                                                                                    |
| [            [//data:]]                                                                                                                                              |
|                                                                                                                                                                                                                                    |
| [            [//  value   - current value of the slider]]                                                                                                            |
|                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [        [function] OnStop(event, data) {]                                                                                                                                |
|                                                                                                                                                                                                                                    |
| [            [//event     - object sent by jQuery event trigger]]                                                                                                    |
|                                                                                                                                                                                                                                    |
| [            [//data:]]                                                                                                                                              |
|                                                                                                                                                                                                                                    |
| [            [//  value   - current value of the slider]]                                                                                                            |
|                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [      [\</][script][\>]]                                                                                                     |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

5.   Build and run the application in emulator.

You can observer the handlers being invoked when the corresponding events are triggered.

 

[]{#related-topics}

