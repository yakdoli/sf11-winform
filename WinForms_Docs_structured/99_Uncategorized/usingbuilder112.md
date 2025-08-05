---
title: usingbuilder112.md
original_path: WinForms_Docs/99_Uncategorized/usingbuilder112.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps explain the orientation setting through Builder:

1.   In **View**, invoke the rating helper followed by the **Orientation** method with the desired orientation as an argument.

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
| [                    .CurrentValue(3)]                                                                                                                                                |
|                                                                                                                                                                                                                           |
| [  **.Orientation([MobRatingOrientation].Vertical)**[%\>]]                                                                        |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                |
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
| [                    .CurrentValue(3)]                                                                                                                                         |
|                                                                                                                                                                                                                    |
| [                   **.Orientation([MobRatingOrientation].Vertical)**] [                ]                          |
|                                                                                                                                                                                                                    |
| [     .Render();]                                                                                                                                                              |
|                                                                                                                                                                                                                    |
| [    [}]]                                                                                                                                          |
|                                                                                                                                                                                                                    |
| []                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Build and run the application in emulator.

 

 

{border="0"}

Figure 102: Rating Control with Vertical Orientation

 

[]{#related-topics}

