---
title: usingbuilder74.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingbuilder74.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps explain the handling of client-side events of the DatePicker control using Builder:

1.  [In the **view**, invoke the **DatePicker** handler with the control ID as the first argument followed by the event handler methods with the desired handler as an argument.]

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                         |
|                                                                                                                                                                                 |
| [\<%] [{=Html.MobSyncfusion().DatePicker([\"DatePicker\"])] |
|                                                                                                                                                                                 |
| [         .AutoFormat([MobSkins].Spinach)]                                                                          |
|                                                                                                                                                                                 |
| [         .Mode([Mode].Advanced)]                                                                                   |
|                                                                                                                                                                                 |
| [         .CalStartDay(0)]                                                                                                                  |
|                                                                                                                                                                                 |
| [         .OnDatePickerLoad([\"OnDatePickerLoad\"])]                                                                |
|                                                                                                                                                                                 |
| [         .OnDateSelected([\"OnDateSelected\"])]                                                                    |
|                                                                                                                                                                                 |
| [         .OnMonthChanged([\"OnMonthChanged\"])]                                                                    |
|                                                                                                                                                                                 |
| [         \-\-\-\-\-\-\-\-\-\-\--]                                                                                                          |
|                                                                                                                                                                                 |
| [}[%\>]]                                                                                                        |
|                                                                                                                                                                                 |
| []                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[Razor\]]**                                                                                                                       |
|                                                                                                                                                                                |
| [\@{] [ Html.MobSyncfusion().DatePicker([\"DatePicker\"])] |
|                                                                                                                                                                                |
| [         .AutoFormat([MobSkins].Spinach)]                                                                         |
|                                                                                                                                                                                |
| [         .Mode([Mode].Advanced)]                                                                                  |
|                                                                                                                                                                                |
| [         .CalStartDay(0)]                                                                                                                 |
|                                                                                                                                                                                |
| [         .OnDatePickerLoad([\"OnDatePickerLoad\"])]                                                               |
|                                                                                                                                                                                |
| [         .OnDateSelected([\"OnDateSelected\"])]                                                                   |
|                                                                                                                                                                                |
| [         .OnMonthChanged([\"OnMonthChanged\"])]                                                                   |
|                                                                                                                                                                                |
| [         \-\-\-\-\-\-\-\-\-\-\--]                                                                                                         |
|                                                                                                                                                                                |
| [         .Render();]                                                                                                                      |
|                                                                                                                                                                                |
| [}] []                                                                             |
|                                                                                                                                                                                |
| []                                                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.  [  In the **JavaScript**, define the handlers as given below:]

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                                                                                                                           |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                         |
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

3.  [Build and run the application. You can observe the callback methods triggered when the corresponding events are raised.]

[]{#related-topics}

