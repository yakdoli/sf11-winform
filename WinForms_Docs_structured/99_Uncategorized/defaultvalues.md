---
title: defaultvalues.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\defaultvalues.md
created_at: 2025-07-03
---






#### Default Values {#default-values style="tab-stops: 0pt"}

The rating control can be loaded with default values. **[]**

**[]** 

Properties

  -------------- ----------------------------------------------- ------------------ ---------------------- ----------------------------------------------
  Name           Description                                     Type of property   Value it accepts       Dependency
  CurrentValue   Defines the value of the rating when loading.   double             0 to double.MaxValue   CurrentValue should not exceed MaximumValue.
  -------------- ----------------------------------------------- ------------------ ---------------------- ----------------------------------------------

*[[]]{.underline}* 

Using Builder

The following steps explain how to set the default value through the Builder.

1.   In **View**, invoke the rating helper followed by the **CurrentValue** method with the desired value as an argument.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ** View\[ASPX\]**                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                |
| [\<%][=][Html.Syncfusion().Rating([\"myRating\"])] |
|                                                                                                                                                                                                                                                                |
| [  .AutoFormat([Skins].Vista)]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                |
| [.**CurrentValue(3)[%\>]**]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                |
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
| [.**CurrentValue(3)**.Render();**[}]**]                                                                           |
|                                                                                                                                                                                                |
|                                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

2.   Build and run the application.

**[]** 

Using Properties Model

 

The following steps explain how to set the default value through the properties model.

1.   In the **controller**, create an instance of **RatingModel**.

2.   Define the **CurrentValue** property and pass the instance through the **View-Specific** data to the view.

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
| [//Creating instance of RatingModel][\                                                                                                     |
| [RatingModel] myModel = [new] [RatingModel]();]                                                  |
|                                                                                                                                                                                                           |
| [            myModel.AutoFormat = [Skins].Vista;]                                                                                             |
|                                                                                                                                                                                                           |
| [            **myModel.CurrentValue = 3;**]                                                                                                                           |
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

 

3.   In **View**, invoke the rating helper with the view data key as the control ID.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[ASPXView\[aspx\]**                                                                                                                                                                                                                                         |
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

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                             |
|                                                                                                                                                                                                |
|                                                                                                                                                                                                |
|                                                                                                                                                                                                |
| [\@{][ Html.Syncfusion().Rating([\"myRating\"])] |
|                                                                                                                                                                                                |
| [  .AutoFormat([Skins].Vista)]                                                                                        |
|                                                                                                                                                                                                |
| [  **.Orientation([RatingOrientation].Vertical).Render();**[}]]                           |
|                                                                                                                                                                                                |
| []                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.   Build and run the application.

The following figure shows the output.

 

{border="0"}

Figure 179: Rating with Default Value

[]{#related-topics}

