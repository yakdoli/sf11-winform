---
title: enablingautopostback.md
original_path: WinForms_Docs/99_Uncategorized/enablingautopostback.md
created_at: 2025-08-05
---






#### Enabling Auto-Post-Back   {#enabling-auto-post-back style="tab-stops: 0pt"}

[The rating control supports auto-post-back so that server-side actions can be called when a value changes. This is useful when performing database updates and parallel actions based on rating value.]

**[Properties][]**

  --------------- ----------------------------------------------------------------------------------------------------------- ---------------------- ---------------------- -------------------------------------
  **Name**        **Description**                                                                                             **Type of property**   **Value it accepts**   **Dependency**
  AutoPostBack    When set, this property sends a post request to the action defined by RequestMapper when a value changes.   bool                   True/False             NA
  RequestMapper   Defines the action name to which the post request is to be made.                                            string                 Action name            Mandatory when AutoPostBack is set.
  --------------- ----------------------------------------------------------------------------------------------------------- ---------------------- ---------------------- -------------------------------------

*[[[]]]{.underline}* 

Using Builder

The following steps explain how to enable auto-post-back using Builder.

1.   In **View**, invoke the rating helper followed by the **AutoPostBack** and **RequestMapper** methods with the desired options as arguments.[]

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                |
| [\<%][=][Html.Syncfusion().Rating([\"myRating\"])] |
|                                                                                                                                                                                                                                                                |
| [.**AutoPostBack([true])**]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                |
| **[.RequestMapper([\"Home/Index\"])]**[ [%\>]]                                                           |
|                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[csht ml\]**                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                 |
| [\@{][ Html.Syncfusion().Rating([\"myRating\"])]                                                                  |
|                                                                                                                                                                                                                                                                 |
| [.**AutoPostBack([true])**]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                 |
| **[.RequestMapper([\"Home/Index\"])]**[.Render();][ [}]] |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In the controller, define the post action.[]

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ** \[Controller\]**                                                                                                                                                    |
|                                                                                                                                                                        |
| [//Post Action for Rating auto post back][]                         |
|                                                                                                                                                                        |
| [\[[AcceptVerbs]([HttpVerbs].Post)\]]                                              |
|                                                                                                                                                                        |
| [        [public] [ActionResult] Index([RatingParams] param)] |
|                                                                                                                                                                        |
| [        {]                                                                                                                        |
|                                                                                                                                                                        |
| [            [/\*\-\-\-\-\-\-\-\-\-\--]]                                                                     |
|                                                                                                                                                                        |
| [             Your Code]                                                                                             |
|                                                                                                                                                                        |
| [             \-\-\-\-\-\-\-\-\-\-\-\--\*/]                                                                          |
|                                                                                                                                                                        |
| [            ]                                                                                                                     |
|                                                                                                                                                                        |
| [        }]                                                                                                                        |
|                                                                                                                                                                        |
| []                                                                                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

3.   Build and run the application.

**[]** 

Using Properties Model

The following steps explain how to enable auto-post-back through the properties model.

1.   In the controller, create an instance of **RatingModel**.

2.   Reset the **AutoPostBack** and **RequestMapper** properties and pass the instance through the view-specific data to the view.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ** \[Controller\]**[]                                                                                                                                                                         |
|                                                                                                                                                                                                                    |
| [public][ [ActionResult] Index()]                                                                     |
|                                                                                                                                                                                                                    |
| [        {]                                                                                                                                                                    |
|                                                                                                                                                                                                                    |
| [//Creating an instance of RatingModel.][           \                                                                                               |
| [RatingModel] myModel = [new] [RatingModel]();                      ]                                     |
|                                                                                                                                                                                                                    |
| [            **myModel.AutoPostBack = [true];**]                                                                                                          |
|                                                                                                                                                                                                                    |
| **[            myModel.RequestMapper = [\"Home/Index\"];]**                                                                                            |
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
|                                                                                                                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ** View\[cshtml\]**                                                                                                                                                                                           |
|                                                                                                                                                                                                               |
| [\@{][ Html.Syncfusion().Rating([\"myRating\"]).Render();[}]] |
|                                                                                                                                                                                                               |
|                                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

**[]** 

4.   In Controller, define the post action.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ** \[Controller\]**                                                                                                                                                    |
|                                                                                                                                                                        |
| [//Post action for the rating auto-post-back][]                     |
|                                                                                                                                                                        |
| [\[[AcceptVerbs]([HttpVerbs].Post)\]]                                              |
|                                                                                                                                                                        |
| [        [public] [ActionResult] Index([RatingParams] param)] |
|                                                                                                                                                                        |
| [        {]                                                                                                                        |
|                                                                                                                                                                        |
| [            [/\*\-\-\-\-\-\-\-\-\-\--]]                                                                     |
|                                                                                                                                                                        |
| [             Your Code]                                                                                             |
|                                                                                                                                                                        |
| [             \-\-\-\-\-\-\-\-\-\-\-\--\*/]                                                                          |
|                                                                                                                                                                        |
| [            ]                                                                                                                     |
|                                                                                                                                                                        |
| [        }]                                                                                                                        |
|                                                                                                                                                                        |
| *[[]]{.underline}*                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

*[[]]{.underline}* 

5.   Build and run the application.

The **RatingParams** class has two properties namely:

[·      ]**CurrentValue** -- Returns the current value of the rating.

[·      ]**CustomData** -- Is user-defined additional data that can be sent upon a post request.

To learn more about CustomData, refer to the [Client-Side Methods]{.UGHyperlink} section.

[]{#related-topics}

