---
title: usingbuilder110.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingbuilder110.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps explain how to set the rating range through the builder:

[1.   ]In **View**, invoke the rating helper followed by the **MaximumValue** and **IncrementStep** methods with the desired values as arguments.[]

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                         |
| [    ] [\<%] [=] [Html.MobSyncfusion().Rating([\"myRating\"])] |
|                                                                                                                                                                                                                                                                         |
| [            .IncrementStep(5)]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                         |
| [            .MaximumValue(50)]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                         |
| [            .ShapeWidth(40)]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                         |
| [            .ShapeHeight(40)]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                         |
| [            .CurrentValue(3)]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                         |
| [            .EditMode([true])]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                         |
| [    [%\>]]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                |
|                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                         |
|                                                                                                                                                                                                                    |
| [    ] [\@{] [Html.MobSyncfusion().Rating([\"myRating\"])] |
|                                                                                                                                                                                                                    |
| [            .IncrementStep(5)]                                                                                                                                                |
|                                                                                                                                                                                                                    |
| [            .MaximumValue(50)]                                                                                                                                                |
|                                                                                                                                                                                                                    |
| [            .ShapeWidth(40)]                                                                                                                                                  |
|                                                                                                                                                                                                                    |
| [            .ShapeHeight(40)]                                                                                                                                                 |
|                                                                                                                                                                                                                    |
| [            .CurrentValue(3)]                                                                                                                                                 |
|                                                                                                                                                                                                                    |
| [            .EditMode([true])]                                                                                                                           |
|                                                                                                                                                                                                                    |
| [           .Render();]                                                                                                                                                        |
|                                                                                                                                                                                                                    |
| [    [}]]                                                                                                                                          |
|                                                                                                                                                                                                                    |
| []                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

6.   Build and run the application in emulator.

 

[ {border="0"} ]

Figure 99: Rating with Customized Range[]

**[]**  

 

 

[]{#related-topics}

