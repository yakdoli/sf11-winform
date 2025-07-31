---
title: usingpropertiesmodel86.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingpropertiesmodel86.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

The following steps explain how to set Syncfusion themes through the properties model:

1.   In the controller, create an instance of **RatingModel**.

2.   Reset the **ClientSideOnLoad**, **ClientSideOnClick**, **ClientSideMouseOut**, **ClientSideMouseOver**,and **ClientSideValueChange** properties and pass the instance through the view-specific data to the view.

**[]**  

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]** []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                       |
| [public] [ [ActionResult] Index()]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                       |
| [        {]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                       |
| [//Creating an instance of MobRatingModel.] [           \                                                                                                                                                                                           |
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
| [            myModel.CurrentValue = 2.4;                      ]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                       |
| [           ** myModel.ClientSideClick = [\"OnClick\"];**]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                       |
| **[            myModel.ClientSideOnLoad = [\"OnLoad\"];]**                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                       |
| **[            myModel.ClientSideValueChange = [\"OnValueChange\"];]** []                                                                                                                             |
|                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                       |
| [            ] [//Passing the instance through the view data to the view.] []                                                                                               |
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

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[ \[ASPX\]]**                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                |
| [\<%] [=] [Html.MobSyncfusion().Rating([\"myRating\"]) [%\>]] |
|                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\@{] [Html.MobSyncfusion().] [Rating] [(] [\"] [myRating] [\"] [).Render();[}]] [] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.   In JavaScript, define the handlers.**

[       ]

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
| []                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

***[[]]{.underline}***  

5.   Build and run the application in emulator.

 

You can observer the callback methods triggering when the corresponding events are raised.

[]{#related-topics}

