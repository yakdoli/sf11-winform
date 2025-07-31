---
title: usingbuilder116.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingbuilder116.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps explain the making of a rating read-only using Builder:

1.   In **View**, invoke the rating helper followed by the **EditMode** method with the argument set to False.

**[]**  

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                        |
|                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                |
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
| [                    .CurrentValue(3)] []                                                                                                         |
|                                                                                                                                                                                                                           |
| [.**EditMode([false])[%\>]**]                                                                                                        |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

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
| [                    .CurrentValue(3)] []                                                                                                  |
|                                                                                                                                                                                                                    |
| [                    .**EditMode([false])**] [.Render();]                                                             |
|                                                                                                                                                                                                                    |
| [    [}]]                                                                                                                                          |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

2.   Build and run the application in emulator.

**[]**  

The following figure shows the output:

{border="0"}

Figure 11: Read-Only Rating

**[]**  

[]{#related-topics}

