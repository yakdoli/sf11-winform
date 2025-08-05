---
title: usingpropertiesmodel44.md
original_path: WinForms_Docs/99_Uncategorized/usingpropertiesmodel44.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

The following section explains how to set a default date and enable or disable manual input of the DatePicker control using the properties model.

 

1.  [In the **controller**, create an instance of the **MobDatePickerModel**, set the **DefaultDate** and **DisableManualInput** properties, and pass the instance through the **View Specific Data** to the **view** as given below.]

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
| [       model.DisplayDefaultDate = [true];]                                                                                                     |
|                                                                                                                                                                                                          |
| [       model.DefaultDate = [DateTime].Now;]                                                                                                 |
|                                                                                                                                                                                                          |
| [       model.DisableManualInput=[true];]                                                                                                       |
|                                                                                                                                                                                                          |
| [       \-\-\-\-\-\-\--]                                                                                                                                             |
|                                                                                                                                                                                                          |
| [       ViewData\[[\"DatePicker \"]\] = model; ]                                                                                             |
|                                                                                                                                                                                                          |
| [       [return] View();]                                                                                                                       |
|                                                                                                                                                                                                          |
| [}]                                                                                                                                                                  |
|                                                                                                                                                                                                          |
| []                                                                                                                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.  [In the **view**, invoke the DatePicker helper with the view data key as the Control ID.]

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                           |
|                                                                                                                                                                                                                   |
| []                                                                                                                              |
|                                                                                                                                                                                                                   |
| [\<%] [{=Html.MobSyncfusion().DatePicker([\"DatePicker\"])}[%\>]] |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[Razor\][]]**                                                                                                                                 |
|                                                                                                                                                                                                                        |
| []                                                                                                                                   |
|                                                                                                                                                                                                                        |
| [@] [{ Html.MobSyncfusion().DatePicker([\"DatePicker\"]).Render();[}]] |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.  [Build and run the application.]

[]{#related-topics}

