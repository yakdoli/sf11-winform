---
title: usingbuilder111.md
original_path: WinForms_Docs/99_Uncategorized/usingbuilder111.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps explain how to set the default value through the Builder:

1.   In **View**, invoke the rating helper followed by the **CurrentValue** method with the desired value as an argument.\
\

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[ \[ASPX\]]**                                                                                                                                                                       |
|                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                |
|                                                                                                                                                                                                                           |
| [\<%] [=] [Html.Syncfusion().Rating([\"myRating\"])] |
|                                                                                                                                                                                                                           |
| [                   ] [.IncrementStep(1)]                                                                                                         |
|                                                                                                                                                                                                                           |
| [                    .MaximumValue(5)]                                                                                                                                                |
|                                                                                                                                                                                                                           |
| [                    .ShapeWidth(40)]                                                                                                                                                 |
|                                                                                                                                                                                                                           |
| [                    .ShapeHeight(40)]                                                                                                                                                |
|                                                                                                                                                                                                                           |
| [      .**CurrentValue(3)[%\>]**]                                                                                                                         |
|                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                |
|                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                |
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
| [                    .**CurrentValue(3)**] []                                                                                              |
|                                                                                                                                                                                                                    |
| [                .Render();]                                                                                                                                                   |
|                                                                                                                                                                                                                    |
| [    [}]]                                                                                                                                          |
|                                                                                                                                                                                                                    |
| []                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

2.   Build and run the application in emulator.

**[]**  

**[]**  

The following figure shows the output:

{border="0"}

Figure 100: Rating with Default Value

**[]**  

[]{#related-topics}

