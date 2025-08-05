---
title: usingpropertiesmodel40.md
original_path: WinForms_Docs/99_Uncategorized/usingpropertiesmodel40.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

The following steps explain the addition of the DatePicker control to an application using the properties model.

1.  [In the **controller**, create an instance of the **MobDatePickerModel**, define the properties, and pass the instance through **View Specific Data** to the **view** as given below.]

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                     |
|                                                                                                                                                                                                          |
| [public] [ [ActionResult] DatePicker()]                                                     |
|                                                                                                                                                                                                          |
| [{]                                                                                                                                                                  |
|                                                                                                                                                                                                          |
| [       MobDatePickerModel] [ model = [new][MobDatePickerModel]();] |
|                                                                                                                                                                                                          |
| [       model.DateFormat=[\"mm/dd/yyy\"];]                                                                                                   |
|                                                                                                                                                                                                          |
| [       model.Mode = [Mode].Simple;]                                                                                                         |
|                                                                                                                                                                                                          |
| [       model.ShowButton = [true];]                                                                                                             |
|                                                                                                                                                                                                          |
| [       model.CalStartDay = 1;]                                                                                                                                      |
|                                                                                                                                                                                                          |
| [       ViewData\[[\"DatePicker \"]\] = model; ]                                                                                             |
|                                                                                                                                                                                                          |
| [       [return] View();]                                                                                                                       |
|                                                                                                                                                                                                          |
| [}]                                                                                                                                                                  |
|                                                                                                                                                                                                          |
| []                                                                                                                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.  [In the **view**, invoke the **DatePicker** helper with the view data key as the control ID.]

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

3.  [Build and run the application. The output is shown in the following screenshot.]

{border="0"} []

Figure 177: DatePicker Input

[]{#related-topics}

