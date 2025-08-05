---
title: usingpropertiesmodel100.md
original_path: WinForms_Docs/99_Uncategorized/usingpropertiesmodel100.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

The following steps explain how to customize the slider handle through the properties model:**

1.   In the controller, create an instance of **MobSliderModel**.

2.   Define the ShowThumb and ThumbStyle property and pass the instance through the view-specific data to the view.[]

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
| [            **slider.ShowThumb = [true];**]                                                                     |
|                                                                                                                                                                           |
| **[            slider.Thumb = [ThumbStyle].Diamond;]**                                                        |
|                                                                                                                                                                           |
| [            [return] View();]                                                                                   |
|                                                                                                                                                                           |
| [        }]                                                                                                                           |
|                                                                                                                                                                           |
| []                                                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

3.   In **View**, invoke the slider helper with the view data key as the control ID.**

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

 

4.   Build and run the application in emulator.

 

*[[ [] ]]{.underline}*  

[ {border="0"} ]

Figure 137: Slider with Diamond Thumb style[]

 

 

The following figure shows the output of the slider.

 

[]{#related-topics}

