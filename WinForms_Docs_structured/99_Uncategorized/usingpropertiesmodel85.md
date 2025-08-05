---
title: usingpropertiesmodel85.md
original_path: WinForms_Docs/99_Uncategorized/usingpropertiesmodel85.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

The following steps explain how to set Syncfusion themes using the properites model:

1.   In the controller, create an instance of **RatingModel**.

2.   Set the **AutoFormat** property with desired theme.

**[]**  

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]** []                                                                                                                                                                                          |
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
| [            myModel.CurrentValue =  3;                              ]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                       |
| [           ** myModel.AutoFormat = [MobSkins].Spinach;**]                                                                                                                                                                                |
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

3.   In **View**, invoke the rating helper with the view data key as the control ID.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **[ \[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\<%] [=] [Html.MobSyncfusion().Rating([\"myRating\"]) [%\>]]                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **[\[Razor\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\@{] [Html.MobSyncfusion().] [Rating] [(] [\"] [myRating] [\"] [).Render();[}]] [] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.   Build and run the application in emulator.

 

[ {border="0"} ]

Figure 107 : Ratting Appearance[]

 

The following shows the four Syncfusion themes used for ratings.

{border="0"}

Figure 108: Rating Themes

 

[]{#related-topics}

