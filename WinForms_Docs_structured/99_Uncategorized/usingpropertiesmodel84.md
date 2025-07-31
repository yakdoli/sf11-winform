---
title: usingpropertiesmodel84.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingpropertiesmodel84.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

The following steps explain the setting of rating precision through the properties model:

1.   In Controller, create an instance of **RatingModel**.

2.   Define the **Precision** property and pass the instance through **view-specific data** to **View**.

**[]**  

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                       |
| [public] [ [ActionResult] Index()]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                       |
| [        {]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                       |
| [//Creating instance of RatingModel] [           \                                                                                                                                                                                                  |
| ] [MobRatingModel] [ myModel = [new]] [MobRatingModel] [();] |
|                                                                                                                                                                                                                                                                                                       |
| [            myModel.IncrementStep =  1;]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                       |
| [            myModel.MaximumValue =  5;]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                       |
| [            myModel.ShapeWidth =  40;]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                       |
| [            myModel.ShapeHeight =  40;]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                       |
| [            myModel.CurrentValue = 2.4;]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                       |
| [            **myModel.Precision = [MobRatingPrecision].Exact;**]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                       |
| [            ] [//passing the instance through view data to view] []                                                                                                        |
|                                                                                                                                                                                                                                                                                                       |
| [ViewData\[[\"myRating\"]\] = myModel;]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                       |
| [            [return] View();]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                       |
| [        }]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   In **View**, invoke the rating helper with the view data key as the control ID.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\<%] [=] [Html.MobSyncfusion().Rating([\"myRating\"]) [%\>]]                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **[\[Razor\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\@{] [Html.MobSyncfusion().] [Rating] [(] [\"] [myRating] [\"] [).Render();[}]] [] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Build and run the application in emulator.

The following figure shows the rating control output:

{border="0"}

Figure 105: Rating with Exact Precision

 

[]{#related-topics}

