---
title: ratingrange.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\ratingrange.md
created_at: 2025-07-03
---






#### Rating Range {#rating-range style="tab-stops: 0pt"}

The rating control allows you to define a rating range by setting the rating intervals and the maximum rating value.

Properties

  --------------- ------------------------------------------------ ------------------ ---------------------- ---------------------------------------------------------------------------------------------
  Name            Description                                      Type of property   Value it accepts       Dependency
  IncrementStep   Defines the rating interval between two stars.   double             0 to double.MaxValue   IncrementValue cannot be greater than MaximumValue and cannot be less than or equal to zero
  MaximumValue    Defines the maximum value of the rating.         double             0 to double.MaxValue   NA
  --------------- ------------------------------------------------ ------------------ ---------------------- ---------------------------------------------------------------------------------------------

*[[]]{.underline}* 

Using Builder

The following steps explain how to set the rating range through the builder.

1.   In **View**, invoke the rating helper followed by the **MaximumValue** and **IncrementStep** methods with the desired values as arguments.[]

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                |
| [\<%][=][Html.Syncfusion().Rating([\"myRating\"])] |
|                                                                                                                                                                                                                                                                |
| [.AutoFormat([Skins].Vista)]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                |
| [.**MaximumValue(10)**]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                |
| **[.IncrementStep(20)]**[ ][%\>][]     |
|                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                        |
|                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                           |
| [\@{][ Html.Syncfusion().Rating([\"myRating\"])]                            |
|                                                                                                                                                                                                                           |
| [.AutoFormat([Skins].Vista)]                                                                                                                     |
|                                                                                                                                                                                                                           |
| [.**MaximumValue(10)**]                                                                                                                                                  |
|                                                                                                                                                                                                                           |
| **[.IncrementStep(20]**[).Render();][ [}]] |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

2.   Build and run the application.

 

**[Using Properties Model]**[]

The following steps explain the setting of the rating range through Builder.

1.   In the controller, create an instance of **RatingModel**.

2.   Define the **MaximumValue** and **Increment Step** properties and pass the instance through the view-specific data to the view.

**[]** 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ** \[Controller\]**                                                                                                                                                                                                |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                    |
| [public][ [ActionResult] Index()]                                                                     |
|                                                                                                                                                                                                                    |
| [        {]                                                                                                                                                                    |
|                                                                                                                                                                                                                    |
| [            ][//Creating an instance of RatingModel.][]                    |
|                                                                                                                                                                                                                    |
| [RatingModel][ myModel = [new] [RatingModel]();]                              |
|                                                                                                                                                                                                                    |
| [            myModel.AutoFormat = [Skins].Vista;]                                                                                                      |
|                                                                                                                                                                                                                    |
| [            **myModel.MaximumValue = 100;**]                                                                                                                                  |
|                                                                                                                                                                                                                    |
| **[            myModel.IncrementStep = 10;]**                                                                                                                                  |
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

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                           |
| [\<%][=][Html.Syncfusion().Rating([\"myRating\"]) [%\>]] |
|                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                |
|                                                                                                                                                                                                                |
|                                                                                                                                                                                                                |
| [\@{][ Html.Syncfusion().Rating([\"myRating\"]).Render(); [}]] |
|                                                                                                                                                                                                                |
|                                                                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.   Build and run the application.

 

The output is shown in the following figure where you can observe that 10 stars are each generated with values of 10 and a maximum value of 100.

 

{border="0"}

Figure 178: Rating with Customized Range

*[]* 

[]{#related-topics}

