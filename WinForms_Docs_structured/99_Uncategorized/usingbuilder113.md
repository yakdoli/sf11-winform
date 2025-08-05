---
title: usingbuilder113.md
original_path: WinForms_Docs/99_Uncategorized/usingbuilder113.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps explain the setting of rating precision through Builder:

[1.   ]In **View**, invoke the rating helper with the desired **Precision** as an argument.[]

[] 

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
| [                    .ShapeWidth(40)]                                                                                                                                                 |
|                                                                                                                                                                                                                           |
| [                    .ShapeHeight(40)]                                                                                                                                                |
|                                                                                                                                                                                                                           |
| [                    .CurrentValue(2.4)]                                                                                                                                              |
|                                                                                                                                                                                                                           |
| [  **.Precision([MobRatingPrecision].Exact)**[%\>]]                                                                               |
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
| [            .IncrementStep(1)]                                                                                                                                                |
|                                                                                                                                                                                                                    |
| [                    .MaximumValue(5)]                                                                                                                                         |
|                                                                                                                                                                                                                    |
| [                    .ShapeWidth(40)]                                                                                                                                          |
|                                                                                                                                                                                                                    |
| [                    .ShapeHeight(40)]                                                                                                                                         |
|                                                                                                                                                                                                                    |
| [                    .CurrentValue(2.4)]                                                                                                                                       |
|                                                                                                                                                                                                                    |
| [                    **.Precision([MobRatingPrecision].Exact)**] [     ]                                           |
|                                                                                                                                                                                                                    |
| [                     .Render();]                                                                                                                                              |
|                                                                                                                                                                                                                    |
| [    [}]]                                                                                                                                          |
|                                                                                                                                                                                                                    |
| []                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Build and run the application in emulator.

**[]**  

The following figure shows the rating control output.

{border="0"}

Figure 104: Rating with Exact Precision

[]{#related-topics}

