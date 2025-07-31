---
title: usingpropertiesmodel41.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingpropertiesmodel41.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

The following steps explain how you can set the themes for the DatePicker control:

1.  [In the **controller**, create an instance of **MobDatePickerModel**, set the **AutoFormat** property with the desired theme as an argument, and pass the instance through **View Specific Data** to the **view** as given below. ]

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                     |
|                                                                                                                                                                                                          |
| [public] [ [ActionResult] DatePicker()]                                                     |
|                                                                                                                                                                                                          |
| [{]                                                                                                                                                                  |
|                                                                                                                                                                                                          |
| [       MobDatePickerModel] [ model = [new][MobDatePickerModel]();] |
|                                                                                                                                                                                                          |
| [       \-\-\-\-\-\-\--]                                                                                                                                             |
|                                                                                                                                                                                                          |
| [       model.AutoFormat = [MobSkins].Spinach;]                                                                                              |
|                                                                                                                                                                                                          |
| [       \-\-\-\-\-\-\--]                                                                                                                                             |
|                                                                                                                                                                                                          |
| [       ViewData\[[\"DatePicker \"]\] = model; ]                                                                                             |
|                                                                                                                                                                                                          |
| [       [return] View();]                                                                                                                       |
|                                                                                                                                                                                                          |
| [}]                                                                                                                                                                  |
|                                                                                                                                                                                                          |
| []                                                                                                                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.  [Pass the instance through **View Specific Data** to the **view** as given below.]

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                           |
|                                                                                                                                                                                                                   |
| [\<%] [{=Html.MobSyncfusion().DatePicker([\"DatePicker\"])}[%\>]] |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[Razor\]]**                                                                                                                                                               |
|                                                                                                                                                                                                                        |
| [@] [{ Html.MobSyncfusion().DatePicker([\"DatePicker\"]).Render();[}]] |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.  [Build and run the application in an emulator. The output will be as follows:]

{border="0"} []

Figure 180: Simple Mode with Spinach Theme

[] 

[\
] {border="0"} []

Figure 181: Android Mode with Spinach Theme

 

[]{#related-topics}

