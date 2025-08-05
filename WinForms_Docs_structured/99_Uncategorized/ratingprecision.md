---
title: ratingprecision.md
original_path: WinForms_Docs/99_Uncategorized/ratingprecision.md
created_at: 2025-08-05
---






#### Rating Precision {#rating-precision style="tab-stops: 0pt"}

The rating control supports three precision modes - Full, Half, and Exact - allowing end-users to give more precise ratings.

**[]** 

Properties

+-------------+---------------------------------------------------------------------+------------------+-----------------------+-------------+
| Name        | Description                                                         | Type of property | Value it accepts      | Dependency  |
+-------------+---------------------------------------------------------------------+------------------+-----------------------+-------------+
| Precision   | When set, this property allows the end-user to rate more precisely. | enum             | RatingPrecision.Full, | NA          |
|             |                                                                     |                  |                       |             |
|             |                                                                     |                  | RatingPrecision.Half, |             |
|             |                                                                     |                  |                       |             |
|             |                                                                     |                  | RatingPrecision.Exact |             |
+-------------+---------------------------------------------------------------------+------------------+-----------------------+-------------+

*[[]]{.underline}* 

Using Builder

The following steps explain the setting of rating precision through Builder.

1.   In **View**, invoke the rating helper followed by the **Precision** method with the desired orientation as an argument.[]

[] 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View \[ASPX\]**                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                |
| [\<%][=][Html.Syncfusion().Rating([\"myRating\"])] |
|                                                                                                                                                                                                                                                                |
| [  .AutoFormat([Skins].Vista)]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                |
| [  **.Precision([RatingPrecision].Exact)**[%\>]]                                                                                                          |
|                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                             |
|                                                                                                                                                                                                |
|                                                                                                                                                                                                |
|                                                                                                                                                                                                |
| [\@{][ Html.Syncfusion().Rating([\"myRating\"])] |
|                                                                                                                                                                                                |
| [  .AutoFormat([Skins].Vista)]                                                                                        |
|                                                                                                                                                                                                |
| [  **.Precision([RatingPrecision].Exact**).Render();[}]]                                  |
|                                                                                                                                                                                                |
| []                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

2.   Build and run the application.

**[]** 

**[Using Properties Model]**[]

The following steps explain the setting of rating precision through Builder.

1.   In Controller, create an instance of **RatingModel**.

2.   Define the **Precision** property and pass the instance through **view-specific data** to **View**.

**[]** 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[Controller\]**                                                                                                                                                                                        |
|                                                                                                                                                                                                           |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                           |
| [public][ [ActionResult] Index()]                                                            |
|                                                                                                                                                                                                           |
| [        {]                                                                                                                                                           |
|                                                                                                                                                                                                           |
| [//Creating instance of RatingModel][           \                                                                                          |
| [RatingModel] myModel = [new] [RatingModel]();]                                                  |
|                                                                                                                                                                                                           |
| [            myModel.AutoFormat = [Skins].Vista;]                                                                                             |
|                                                                                                                                                                                                           |
| [            **myModel.Precision = [RatingPrecision].Exact;**]                                                                                |
|                                                                                                                                                                                                           |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                           |
| [            ][//passing the instance through view data to view][] |
|                                                                                                                                                                                                           |
| [ViewData\[[\"myRating\"]\] = myModel;]                                                                                                       |
|                                                                                                                                                                                                           |
| [            [return] View();]                                                                                                                   |
|                                                                                                                                                                                                           |
| [        }]                                                                                                                                                           |
|                                                                                                                                                                                                           |
| []                                                                                                                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   In **View**, invoke the rating helper with the view data key as the control ID.

 

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                           |
| [\<%][=][Html.Syncfusion().Rating([\"myRating\"]) [%\>]] |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                |
|                                                                                                                                                                                                                |
|                                                                                                                                                                                                                |
| [\@{][ Html.Syncfusion().Rating([\"myRating\"]).Render(); [}]] |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Build and run the application.

The following figure shows the rating control output.

 

{border="0"}

Figure 181: Rating with Exact Precision

 

[]{#related-topics}

