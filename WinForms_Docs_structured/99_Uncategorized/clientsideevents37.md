---
title: clientsideevents37.md
original_path: WinForms_Docs/99_Uncategorized/clientsideevents37.md
created_at: 2025-08-05
---






#### Client-Side Events {#client-side-events style="tab-stops: 0pt"}

The rating control supports client-side event handling.

 

Events

  ----------------------- ------------------------------------------------------------------------------------------------------- ---------------- -----------------
  Name                    Description                                                                                             Arguments        Reference Links
  ClientSideOnLoad        This event is raised immediately after the control loads.                                               inst,currValue   NA
  ClientSideClick         This event is called when the rating is clicked but before the AJAX request (if AutoPostBack is set).   inst,currValue   NA
  ClientSideMouseOut      This event is raised upon mouse-out of the rating stars.                                                inst,currValue   NA
  ClientSideMouseOver     This event is raised upon mouse-over of the rating stars.                                               inst,currValue   NA
  ClientSideValueChange   This event is raised when the rating is changed.                                                        inst,currValue   NA
  ----------------------- ------------------------------------------------------------------------------------------------------- ---------------- -----------------

*[[]]{.underline}* 

Using Builder

The following steps explain how to handle client-side events using Builder.

1.   In **View**, invoke the rating helper followed by the **ClientSideOnLoad**, **ClientSideOnClick**, **ClientSideMouseOut**, **ClientSideMouseOver**, and **ClientSideValueChange** methods with the desired handlers as arguments.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                |
| [\<%][=][Html.Syncfusion().Rating([\"myRating\"])] |
|                                                                                                                                                                                                                                                                |
| [.**ClientSideClick([\"OnClick\"])**]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                |
| **[.ClientSideMouseOut([\"OnMouseOut\"])]**                                                                                                                                           |
|                                                                                                                                                                                                                                                                |
| **[.ClientSideMouseOver([\"OnMouseOver\"])]**                                                                                                                                         |
|                                                                                                                                                                                                                                                                |
| **[.ClientSideOnLoad([\"OnLoad\"])]**                                                                                                                                                 |
|                                                                                                                                                                                                                                                                |
| **[.ClientSideValueChange([\"OnValueChange\"])]**[%\>]                                                           |
|                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                 |
| [\@{][ Html.Syncfusion().Rating([\"myRating\"])]                                                                  |
|                                                                                                                                                                                                                                                                 |
| [.**ClientSideClick([\"OnClick\"])**]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                 |
| **[.ClientSideMouseOut([\"OnMouseOut\"])]**                                                                                                                                            |
|                                                                                                                                                                                                                                                                 |
| **[.ClientSideMouseOver([\"OnMouseOver\"])]**                                                                                                                                          |
|                                                                                                                                                                                                                                                                 |
| **[.ClientSideOnLoad([\"OnLoad\"])]**                                                                                                                                                  |
|                                                                                                                                                                                                                                                                 |
| **[.ClientSideValueChange([\"OnValueChange\"])]**[.Render();][}] |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   In JavaScript, define the handlers.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[JavaScript\]**                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                       |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                                                       |
| [       [function] OnLoad(inst, currValue) {]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                       |
| [           [//inst       - instance of rating client-side object]]                                                                                                                        |
|                                                                                                                                                                                                                                                                       |
| [           [//currValue  - current value of rating]]                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [       }]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                       |
| [       [function] OnMouseOver(inst, currValue) {]                                                                                                                                              |
|                                                                                                                                                                                                                                                                       |
| [           [//inst       - instance of rating client-side object]]                                                                                                                        |
|                                                                                                                                                                                                                                                                       |
| [           [//currValue  - current value of rating]]                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [       }]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                       |
| [       [function] OnMouseOut(inst, currValue) {]                                                                                                                                               |
|                                                                                                                                                                                                                                                                       |
| [           [//inst       - instance of rating client-side object]]                                                                                                                        |
|                                                                                                                                                                                                                                                                       |
| [           [//currValue  - current value of rating]]                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [       }]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                       |
| [       [function] OnClick(inst, currValue) {]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                       |
| [           [//inst       - instance of rating client-side object]]                                                                                                                        |
|                                                                                                                                                                                                                                                                       |
| [           [//currValue  - current value of rating]]                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [       }]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                       |
| [       [function] OnValueChange(inst, currValue) {]                                                                                                                                            |
|                                                                                                                                                                                                                                                                       |
| [           [//inst       - instance of rating client-side object]]                                                                                                                        |
|                                                                                                                                                                                                                                                                       |
| [           [//currValue  - current value of rating]]                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [       }]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                       |
| [       [\</][script][\>]]                                                                                                                          |
|                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

 

3.   Build and run the application.

**[]** 

Using Properties Model

The following steps explain how to set Syncfusion themes through the Builder.

1.   In the controller, create an instance of **RatingModel**.

2.   Reset the **ClientSideOnLoad**, **ClientSideOnClick**, **ClientSideMouseOut**, **ClientSideMouseOver**, and **ClientSideValueChange** properties and pass the instance through the view-specific data to the view.

**[]** 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[Controller\]**[]                                                                                                                                                                          |
|                                                                                                                                                                                                                    |
| [public][ [ActionResult] Index()]                                                                     |
|                                                                                                                                                                                                                    |
| [        {]                                                                                                                                                                    |
|                                                                                                                                                                                                                    |
| [//Creating an instance of RatingModel.][           \                                                                                               |
| [RatingModel] myModel = [new] [RatingModel]();                      ]                                     |
|                                                                                                                                                                                                                    |
| [           ** myModel.ClientSideClick = [\"OnClick\"];**]                                                                                             |
|                                                                                                                                                                                                                    |
| **[            myModel.ClientSideMouseOut = [\"OnMouseOut\"];]**                                                                                       |
|                                                                                                                                                                                                                    |
| **[            myModel.ClientSideMouseOver = [\"OnMouseOver\"];]**                                                                                     |
|                                                                                                                                                                                                                    |
| **[            myModel.ClientSideOnLoad = [\"OnLoad\"];]**                                                                                             |
|                                                                                                                                                                                                                    |
| **[            myModel.ClientSideValueChange = [\"OnValueChange\"];]**[]                                           |
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
| ** View\[ASPX\]**                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                           |
| [\<%][=][Html.Syncfusion().Rating([\"myRating\"]) [%\>]] |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ** View\[cshtml\]**                                                                                                                                                                                           |
|                                                                                                                                                                                                               |
| [\@{][ Html.Syncfusion().Rating([\"myRating\"]).Render();[}]] |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.   In JavaScript, define the handlers.**

           

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[JavaScript\]**                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                       |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                                                       |
| [       [function] OnLoad(inst, currValue) {]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                       |
| [           [//inst       - instance of rating client-side object]]                                                                                                                        |
|                                                                                                                                                                                                                                                                       |
| [           [//currValue  - current value of rating]]                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [       }]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                       |
| [       [function] OnMouseOver(inst, currValue) {]                                                                                                                                              |
|                                                                                                                                                                                                                                                                       |
| [           [//inst       - instance of rating client-side object]]                                                                                                                        |
|                                                                                                                                                                                                                                                                       |
| [           [//currValue  - current value of rating]]                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [       }]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                       |
| [       [function] OnMouseOut(inst, currValue) {]                                                                                                                                               |
|                                                                                                                                                                                                                                                                       |
| [           [//inst       - instance of rating client-side object]]                                                                                                                        |
|                                                                                                                                                                                                                                                                       |
| [           [//currValue  - current value of rating]]                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [       }]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                       |
| [       [function] OnClick(inst, currValue) {]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                       |
| [           [//inst       - instance of rating client-side object]]                                                                                                                        |
|                                                                                                                                                                                                                                                                       |
| [           [//currValue  - current value of rating]]                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [       }]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                       |
| [       [function] OnValueChange(inst, currValue) {]                                                                                                                                            |
|                                                                                                                                                                                                                                                                       |
| [           [//inst       - instance of rating client-side object]]                                                                                                                        |
|                                                                                                                                                                                                                                                                       |
| [           [//currValue  - current value of rating]]                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [       }]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                       |
| [       [\</][script][\>]]                                                                                                                          |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

***[[]]{.underline}*** 

5.   Build and run the application.

 

You can observer the callback methods triggering when the corresponding events are raised.

[]{#related-topics}

