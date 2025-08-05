---
title: usingbuilder115.md
original_path: WinForms_Docs/99_Uncategorized/usingbuilder115.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps explain how to handle client-side events using Builder:

1.   In **View**, invoke the rating helper followed by the **ClientSideOnLoad**, **ClientSideOnClick**, and **ClientSideValueChange** methods with the desired handlers as arguments.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                        |
|                                                                                                                                                                                                                           |
| [\<%] [=] [Html.Syncfusion().Rating([\"myRating\"])] |
|                                                                                                                                                                                                                           |
| [                   .IncrementStep(1)]                                                                                                                                                |
|                                                                                                                                                                                                                           |
| [                    .MaximumValue(5)]                                                                                                                                                |
|                                                                                                                                                                                                                           |
| [                    .ShapeWidth(20)]                                                                                                                                                 |
|                                                                                                                                                                                                                           |
| [                    .ShapeHeight(20)]                                                                                                                                                |
|                                                                                                                                                                                                                           |
| [                    .CurrentValue(3)]                                                                                                                                                |
|                                                                                                                                                                                                                           |
| [.**ClientSideClick([\"OnClick\"])**]                                                                                                                         |
|                                                                                                                                                                                                                           |
| **[.ClientSideOnLoad([\"OnLoad\"])]**                                                                                                                         |
|                                                                                                                                                                                                                           |
| **[.ClientSideValueChange([\"OnValueChange\"])]** [%\>]                                               |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                |
|                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                         |
|                                                                                                                                                                                                                    |
| [    ] [\@{] [Html.MobSyncfusion().Rating([\"myRating\"])] |
|                                                                                                                                                                                                                    |
| [                    .IncrementStep(1)]                                                                                                                                        |
|                                                                                                                                                                                                                    |
| [                    .MaximumValue(5)]                                                                                                                                         |
|                                                                                                                                                                                                                    |
| [                    .ShapeWidth(20)]                                                                                                                                          |
|                                                                                                                                                                                                                    |
| [                    .ShapeHeight(20)]                                                                                                                                         |
|                                                                                                                                                                                                                    |
| [                    .CurrentValue(3)]                                                                                                                                         |
|                                                                                                                                                                                                                    |
| [.**ClientSideClick([\"OnClick\"])**]                                                                                                                  |
|                                                                                                                                                                                                                    |
| **[.ClientSideOnLoad([\"OnLoad\"])]**                                                                                                                  |
|                                                                                                                                                                                                                    |
| **[            .ClientSideValueChange([\"OnValueChange\"])]** [.Render();]                                         |
|                                                                                                                                                                                                                    |
| [    [}]]                                                                                                                                          |
|                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   In JavaScript, define the handlers.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                                                                                                                           |
|                                                                                                                                                                                                                                    |
| [\<] [script] [ [type] [=\"text/javascript\"\>] ] |
|                                                                                                                                                                                                                                    |
| [       [function] OnLoad(inst, currValue) {]                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [           [//inst       - instance of rating client-side object]]                                                                                                  |
|                                                                                                                                                                                                                                    |
| [           [//currValue  - current value of rating]]                                                                                                                |
|                                                                                                                                                                                                                                    |
| [       }]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                    |
| [       [function] OnClick(inst, currValue) {]                                                                                                                            |
|                                                                                                                                                                                                                                    |
| [           [//inst       - instance of rating client-side object]]                                                                                                  |
|                                                                                                                                                                                                                                    |
| [           [//currValue  - current value of rating]]                                                                                                                |
|                                                                                                                                                                                                                                    |
| [       }]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                    |
| [       [function] OnValueChange(inst, currValue) {]                                                                                                                      |
|                                                                                                                                                                                                                                    |
| [           [//inst       - instance of rating client-side object]]                                                                                                  |
|                                                                                                                                                                                                                                    |
| [           [//currValue  - current value of rating]]                                                                                                                |
|                                                                                                                                                                                                                                    |
| [       }]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                    |
| [      [\</][script][\>]]                                                                                                     |
|                                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]**

**[of rating client nt view asow this ties in with this section.]**

3.   Build and run the application in emulator.

**[]**  

[]{#related-topics}

