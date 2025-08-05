---
title: usingpropertiesmodel45.md
original_path: WinForms_Docs/99_Uncategorized/usingpropertiesmodel45.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

The following section explains the setting of the **DateFormat** and **ShowOtherMonths** properties of the date picker using the properties model.

1.  [In the **controller**, create an instance of the **MobDatePickerModel**, set the **DateFormat()** and **ShowOtherMonths()** properties with desired arguments and pass the instance through the **View Specific Data** to the **view** as given below.]

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
| [       model.DateFormat=[\"d MM,y\"];]                                                                                                      |
|                                                                                                                                                                                                          |
| [       model.ShowOtherMonths = [true];]                                                                                                        |
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

 

2.  [In the **view**, invoke the **DatePicker** helper with the view data key as the control ID.]

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                           |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                        |
|                                                                                                                                                                                                                   |
| [\<%] [{=Html.MobSyncfusion().DatePicker([\"DatePicker\"])}[%\>]] |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                  |
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

3.  [Build and run the application.]

[]{#related-topics}

