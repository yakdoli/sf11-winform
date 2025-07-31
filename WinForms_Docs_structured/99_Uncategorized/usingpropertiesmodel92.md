---
title: usingpropertiesmodel92.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingpropertiesmodel92.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

The following steps explain how to set the dimensions of the slider through the properties model:**

1.   In the controller, create an instance of **MobSliderModel**.

2.   Set the **Height** and **Width** properties and pass the instance through the view-specific data to the view.

 

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
| [            **slider.Height = 100;**]                                                                                                |
|                                                                                                                                                                           |
| **[            slider.Width = 400;]**                                                                                                 |
|                                                                                                                                                                           |
| [            ViewData\[[\"slider\"]\] = slider;]                                                              |
|                                                                                                                                                                           |
| [            [return] View();]                                                                                   |
|                                                                                                                                                                           |
| [        }]                                                                                                                           |
|                                                                                                                                                                           |
| **[]**                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

3.   In View, invoke the slider helper with the view data key as the control ID.**

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                             |
| [\<%] [=] [Html.MobSyncfusion().Slider([\"slider\"])[%\>]] |
|                                                                                                                                                                                                                                                             |
| **[[ [] ]]{.underline}**                                                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                             |
|                                                                                                                                                                                                                 |
| [\@{] [ Html.MobSyncfusion().Slider([\"slider\"]).Render();[}]] |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                      |
|                                                                                                                                                                                                                 |
| **[[ [] ]]{.underline}**                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.   Build and run the application in the emulator.

The following figure shows the slider output.

 

[ {border="0"} ]

Figure 123: Slider[]

 

[]{#related-topics}

