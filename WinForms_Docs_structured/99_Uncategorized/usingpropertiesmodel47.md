---
title: usingpropertiesmodel47.md
original_path: WinForms_Docs/99_Uncategorized/usingpropertiesmodel47.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

The following steps explain the handling of client side events of the DatePicker using the properties model.

1.  [In the Controller, create an instance of the **[MobDatePickerModel]**, set the client-side events, and pass the instance through the **View Specific Data** to the **view** as given below.]

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
| [       model.AutoFormat = [MobSkins].Spinach;]                                                                                              |
|                                                                                                                                                                                                          |
| [       model.OnDatePickerLoad = [\"OnDatePickerLoad\"];]                                                                                    |
|                                                                                                                                                                                                          |
| [       model.OnDateSelected = [\"OnDateSelected\"];]                                                                                        |
|                                                                                                                                                                                                          |
| [       model.OnMonthChanged = [\"OnMonthChanged\"];]                                                                                        |
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

3.  [In the **JavaScript**, define the handlers as given below.]

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                                                                                                                           |
|                                                                                                                                                                                                                                    |
| [\<] [script] [ [type] [=\"text/javascript\"\>] ] |
|                                                                                                                                                                                                                                    |
| [          [function] OnDatePickerLoad(event, dpModel) {]                                                                                                                 |
|                                                                                                                                                                                                                                    |
| [              [//event - event Object]]                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [              [//dpModel -DatePicker Model Object]]                                                                                                                 |
|                                                                                                                                                                                                                                    |
| [          }]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                    |
| [          [function] OnDateSelected(event, data) {]                                                                                                                      |
|                                                                                                                                                                                                                                    |
| [              [//event - event Object]]                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [              [//data  - selected date]]                                                                                                                            |
|                                                                                                                                                                                                                                    |
| [          }]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                    |
| [          [function] OnMonthChanged(event, data) {]                                                                                                                      |
|                                                                                                                                                                                                                                    |
| [              [//event - event Object]]                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [              [//data  - changed date value]]                                                                                                                       |
|                                                                                                                                                                                                                                    |
| [          }]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                    |
| [\</] [script] [\>] []                    |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.  [Build and run the application. You can observe the handlers being invoked when the corresponding event is triggered.]

[]{#related-topics}

