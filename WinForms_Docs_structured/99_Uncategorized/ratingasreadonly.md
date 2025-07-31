---
title: ratingasreadonly.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\ratingasreadonly.md
created_at: 2025-07-03
---






#### Rating as Read-Only {#rating-as-read-only style="tab-stops: 0pt"}

The rating control supports a read-only mode, so the control will display only a predefined value, preventing the end-user from issuing a rating.

 

Properties

 

  ---------- ----------------------------------------------------------------- ------------------ ------------------ ------------
  Name       Description                                                       Type of property   Value it accepts   Dependency
  EditMode   When set to False, this property prevents end-user interaction.   bool               true/false         NA
  ---------- ----------------------------------------------------------------- ------------------ ------------------ ------------

*[[]]{.underline}* 

Using Builder

The following steps explain the making of a rating read-only using Builder.

1.   In **View**, invoke the rating helper followed by the **EditMode** method with the argument set to False.

**[]** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[ASPX\]**                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                |
| [\<%][=][Html.Syncfusion().Rating([\"myRating\"])] |
|                                                                                                                                                                                                                                                                |
| [.AutoFormat([Skins].Vista)]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                |
| [.Precision([RatingPrecision].Exact)]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                |
| [.CurrentValue(3.7)]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                |
| [.**EditMode([false])[%\>]**]                                                                                                                                |
|                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

2.   Build and run the application.

**[]** 

Using Properties Model

The following steps explain the making of a rating read-only through the properties model.

1.   In Controller, create an instance of **RatingModel**.

2.   Set the **EditMode** property and pass the instance through the **view-specific data** to **View**.

**[]** 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ** \[Controller\]**                                                                                                                                                                                       |
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
| [myModel.CurrentValue = 3.7;]                                                                                                                                         |
|                                                                                                                                                                                                           |
| [            **myModel.EditMode = [false];**]                                                                                                    |
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

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[ASPX\]**                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                           |
| [\<%][=][Html.Syncfusion().Rating([\"myRating\"]) [%\>]] |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Build and run the application.

The following figure displays the read-only rating output.

 

{border="0"}

Figure 184: Rating as Read-Only

[]{#related-topics}

