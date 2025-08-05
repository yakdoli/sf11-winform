---
title: usingpropertiesmodel97.md
original_path: WinForms_Docs/99_Uncategorized/usingpropertiesmodel97.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

The following steps explain how to display the tick mark through the properties model:**

1.   In the controller, create an instance of **MobSliderModel**, define the **EnableTickMark, SliderTickPosition and TickFrequency** properties and pass the instance through the view-specific data to the view.[]

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
| [            slider.Maximum = 100;]                                                                                                   |
|                                                                                                                                                                           |
| [            **slider.EnableTickMark = [true];**]                                                                |
|                                                                                                                                                                           |
| **[            slider.TickFrequency = 20;]**                                                                                          |
|                                                                                                                                                                           |
| **[            slider.SliderTickPosition = [TickPosition].BottomRight;]**                                     |
|                                                                                                                                                                           |
| [            ViewData\[[\"slider\"]\] = slider;]                                                              |
|                                                                                                                                                                           |
| [            [return] View();]                                                                                   |
|                                                                                                                                                                           |
| [        }]                                                                                                                           |
|                                                                                                                                                                           |
| []                                                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

2.   In **View**, invoke the slider helper with the view data key as the control ID.**

**[]**  

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

 

3.   Build and run the application in emulator.

 

The following figure shows the output of the slider.

 

*[[ [] ]]{.underline}*  

[ {border="0"} ]

Figure 131: Slider with TickMark[]

 

[]{#related-topics}

