---
title: orientations.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\orientations.md
created_at: 2025-07-03
---






#### Orientations {#orientations style="tab-stops: 0pt"}

The rating control supports both horizontal and vertical orientations.

**[]** 

Properties

+-------------+-------------------------------------------------------------------+------------------+-------------------------------+-------------+
| Name        | Description                                                       | Type of property | Value it accepts              | Dependency  |
+-------------+-------------------------------------------------------------------+------------------+-------------------------------+-------------+
| Orientation | Defines the orientation in which the control has to be generated. | double           | RatingOrientation.Horizontal, | NA          |
|             |                                                                   |                  |                               |             |
|             |                                                                   |                  | RatingOrientation.Vertical    |             |
+-------------+-------------------------------------------------------------------+------------------+-------------------------------+-------------+

 

Using Builder

The following steps explain the orientation setting through Builder.

1.   In **View**, invoke the rating helper followed by the **Orientation** method with the desired orientation as an argument.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[ASPX\]**                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                |
| [\<%][=][Html.Syncfusion().Rating([\"myRating\"])] |
|                                                                                                                                                                                                                                                                |
| [  .AutoFormat([Skins].Vista)]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                |
| [  **.Orientation([RatingOrientation].Vertical)**[%\>]]                                                                                                   |
|                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Build and run the application.

 

Using Properties Model

The following steps explain the orientation setting through the Properties model.

1.   In Controller, create an instance of **RatingModel**.

2.   Define the **Orientation** property and pass the instance through **view-specific data** to **View**.

**[]** 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [      ]**\[Controller\]**                                                                                                                                                     |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                    |
| [public][ [ActionResult] Index()]                                                                     |
|                                                                                                                                                                                                                    |
| [        {]                                                                                                                                                                    |
|                                                                                                                                                                                                                    |
| [//Creating an instance of RatingModel.][           \                                                                                               |
| [RatingModel] myModel = [new] [RatingModel]();]                                                           |
|                                                                                                                                                                                                                    |
| [            myModel.AutoFormat = [Skins].Vista;]                                                                                                      |
|                                                                                                                                                                                                                    |
| [            **myModel.Orientation = [RatingOrientation].Vertical;**]                                                                                  |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                    |
| [            ][//Passing the instance through the view data to the view.][] |
|                                                                                                                                                                                                                    |
| [ViewData\[[\"myRating\"]\] = myModel;]                                                                                                                |
|                                                                                                                                                                                                                    |
| [            [return] View();]                                                                                                                            |
|                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                    |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   In **View**, invoke the rating helper with the view data key as the control ID.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                           |
| [\<%][=][Html.Syncfusion().Rating([\"myRating\"]) [%\>]] |
|                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

**[]** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                                                |
|                                                                                                                                                                                                                |
| **View\[cshtml\]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                |
|                                                                                                                                                                                                                |
|                                                                                                                                                                                                                |
| [\@{][ Html.Syncfusion().Rating([\"myRating\"]).Render(); [}]] |
|                                                                                                                                                                                                                |
|                                                                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

4.   Build and run the application.**

The following shows the rating control output.

{border="0"}

Figure 180: Rating Control with Vertical Orientation

*[]* 

[]{#related-topics}

