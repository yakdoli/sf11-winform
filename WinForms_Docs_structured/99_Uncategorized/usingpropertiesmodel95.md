---
title: usingpropertiesmodel95.md
original_path: WinForms_Docs/99_Uncategorized/usingpropertiesmodel95.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

The following steps explain how to create a slider range through the properties model:**

1.   In the controller, create an instance of **MobSliderModel**.

2.   Set the **Range** and **Values** properties and pass the instance through the **view-specific data** to the **view**.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                             |
|                                                                                                                                                                      |
| [public] [ [ActionResult] Index()]                      |
|                                                                                                                                                                      |
| [        {]                                                                                                                      |
|                                                                                                                                                                      |
| [            [//Create an instance of TabModel.]]                                                          |
|                                                                                                                                                                      |
| [            [SliderModel] myModel = [new][SliderModel]();] |
|                                                                                                                                                                      |
| **[            myModel.Range = [true];]**                                                                   |
|                                                                                                                                                                      |
| **[            myModel.Values = [new][int]\[\] { 25, 50 };]**                          |
|                                                                                                                                                                      |
| []                                                                                                                               |
|                                                                                                                                                                      |
| [            [//Pass the instance through the view data to the view.]]                                     |
|                                                                                                                                                                      |
| [            ViewData\[[\"slider\"]\] = myModel;]                                                        |
|                                                                                                                                                                      |
| [            [return] View();]                                                                              |
|                                                                                                                                                                      |
| [        }]                                                                                                                      |
|                                                                                                                                                                      |
| []                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   In **View**, invoke the slider helper with the view data key as the control ID.**

***[[ [] ]]{.underline}***  

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                     |
| [\<%] [=] [Html.Syncfusion().Slider([\"slider\"])[%\>]] **[]** |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[ \[Razor\]]**                                                                                                                                                            |
|                                                                                                                                                                                                                 |
| [\@{] [ Html.MobSyncfusion().Slider([\"slider\"]).Render();[}]] |
|                                                                                                                                                                                                                 |
| **[[ [] ]]{.underline}**                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.   Build and run the application in the emulator.

The following figure shows the slider output with the specified range.

 

[ {border="0"} ]

Figure 127: Slider Range

 

[]{#related-topics}

