---
title: disablingtheresetbutton.md
original_path: WinForms_Docs/99_Uncategorized/disablingtheresetbutton.md
created_at: 2025-08-05
---






#### Disabling the Reset Button {#disabling-the-reset-button style="tab-stops: 0pt"}

The rating control supports enabling or disabling the reset button to allow the end-user to reset the rating (making the rating value zero) or to prohibit this action.

 

Properties

 

  ------------ ---------------------------------------------------------------------------------- ------------------ ------------------ ----------------------------------------------------------
  Name         Description                                                                        Type of property   Value it accepts   Dependency
  AllowReset   When set to Single, this property allows only one node to be expanded at a time.   bool               True/False         This property is enabled only with EditMode set to True.
  ------------ ---------------------------------------------------------------------------------- ------------------ ------------------ ----------------------------------------------------------

*[]* 

Using Builder

The following steps explain how to disable the reset button through the builder.

1.   In **View**, invoke the rating helper followed by the **AllowEdit** method with the argument set to False.

 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **VIew\[ASPX\]**                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                |
| [\<%][=][Html.Syncfusion().Rating([\"myRating\"])] |
|                                                                                                                                                                                                                                                                |
| [.AutoFormat([Skins].Vista)]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                |
| [.**AllowEdit([false])[%\>]**[]]                                                                                                 |
|                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                             |
|                                                                                                                                                                                                |
|                                                                                                                                                                                                |
|                                                                                                                                                                                                |
| [\@{][ Html.Syncfusion().Rating([\"myRating\"])] |
|                                                                                                                                                                                                |
| [.AutoFormat([Skins].Vista)]                                                                                          |
|                                                                                                                                                                                                |
| [.**AllowEdit([false])**.Render();**[}]**[]]                     |
|                                                                                                                                                                                                |
| []                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Build and run the application.

3.  

Using Properties Model

The following steps explain how to disable the reset button through the properties model.

1.   In the controller, create an instance of **RatingModel**.

2.   Reset the **AllowReset** property and pass the instance through the **view-specific data** to the **View**.

 

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
| [            myModel.AutoFormat = [Skins].Vista;            ]                                                                                 |
|                                                                                                                                                                                                           |
| [            **myModel.AllowReset = [false];**]                                                                                                  |
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

3.   In **View**, invoke the rating helper with the view data key as the control ID.[]

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                           |
| [\<%][=][Html.Syncfusion().Rating([\"myRating\"]) [%\>]] |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                            |
|                                                                                                                                                                                                               |
|                                                                                                                                                                                                               |
|                                                                                                                                                                                                               |
| [\@{][ Html.Syncfusion().Rating([\"myRating\"]).Render();[}]] |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.   Build and run the application.

The figure shows the reset button output.

[] 

{border="0"}

Figure 182: Rating with Reset Button Disabled

*[]* 

[]{#related-topics}

