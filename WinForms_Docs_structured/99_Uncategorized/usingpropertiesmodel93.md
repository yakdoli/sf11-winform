---
title: usingpropertiesmodel93.md
original_path: WinForms_Docs/99_Uncategorized/usingpropertiesmodel93.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

The following steps explain how to set the range of the slider through the properties model:**

1.   In the controller, create an instance of **MobSliderModel**.

2.   Set the **Minimum**, **Maximum**, **Step** and **Value** properties and pass the instance through the view-specific data to the view.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                  |
|                                                                                                                                                                           |
| [public] [ [ActionResult] Index()]                           |
|                                                                                                                                                                           |
| [        {]                                                                                                                           |
|                                                                                                                                                                           |
| [            [MobSliderModel] slider = [new][MobSliderModel]();] |
|                                                                                                                                                                           |
| **[            slider.Value = 2;]**                                                                                                   |
|                                                                                                                                                                           |
| **[            slider.Step = 2;]**                                                                                                    |
|                                                                                                                                                                           |
| **[            slider.Maximum = 10;]**                                                                                                |
|                                                                                                                                                                           |
| **[            slider.Minimum = 0;]**                                                                                                 |
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

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                          |
| [\<%] [=] [Html.Syncfusion().Slider([\"slider\"])[%\>]] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[ \[Razor\]]**                                                                                                                                                            |
|                                                                                                                                                                                                                 |
| [\@{] [ Html.MobSyncfusion().Slider([\"slider\"]).Render();[}]] |
|                                                                                                                                                                                                                 |
| **[[ [] ]]{.underline}**                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.   Build and run the application in the emulator.

The following figure shows the slider output.

 

**[]**  

[ {border="0"} ]

Figure 6: Slider with Customized Range

 

[]{#related-topics}

