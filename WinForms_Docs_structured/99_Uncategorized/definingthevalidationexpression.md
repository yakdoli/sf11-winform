---
title: definingthevalidationexpression.md
original_path: WinForms_Docs/99_Uncategorized/definingthevalidationexpression.md
created_at: 2025-08-05
---






#### Defining the Validation Expression {#defining-the-validation-expression style="tab-stops: 0pt"}

Client-side Validator has a few in-built validation expressions. The in-built validation expressions are as follows:

[·      ]Date

[·      ]Email

[·      ]IPAddress

[·      ]Number

[·      ]Postal Code

[·      ]Time

[·      ]URL

[·      ]USDate

**[]** 

Properties

+----------------------+---------------------------------------------------------------------------------------------------+----------------------+--------------------------------------------------------------------------------------------+-------------+
| Name                 | Description                                                                                       | Type of the property | Value it accepts                                                                           | Dependency  |
+----------------------+---------------------------------------------------------------------------------------------------+----------------------+--------------------------------------------------------------------------------------------+-------------+
| ValidationExpression | Used to set one of the eight pre -defined validation expressions i.e. the reference of validation | enum                 | [ValidatorModel].[Expressions] .Date,      | NA          |
|                      |                                                                                                   |                      |                                                                                            |             |
|                      |                                                                                                   |                      | [ValidatorModel].[Expressions].Email,      |             |
|                      |                                                                                                   |                      |                                                                                            |             |
|                      |                                                                                                   |                      | [ValidatorModel].[Expressions].IPAddress,  |             |
|                      |                                                                                                   |                      |                                                                                            |             |
|                      |                                                                                                   |                      | [ValidatorModel].[Expressions].Number,     |             |
|                      |                                                                                                   |                      |                                                                                            |             |
|                      |                                                                                                   |                      | [ValidatorModel].[Expressions].PostalCode, |             |
|                      |                                                                                                   |                      |                                                                                            |             |
|                      |                                                                                                   |                      | [ValidatorModel].[Expressions].Time,       |             |
|                      |                                                                                                   |                      |                                                                                            |             |
|                      |                                                                                                   |                      | [ValidatorModel].[Expressions].URL,        |             |
|                      |                                                                                                   |                      |                                                                                            |             |
|                      |                                                                                                   |                      | [ValidatorModel].[Expressions].USDate      |             |
+----------------------+---------------------------------------------------------------------------------------------------+----------------------+--------------------------------------------------------------------------------------------+-------------+

*[[]]{.underline}* 

Using Builder

The following steps explain the definition of the validation expression for the client side valditor using Builder.

1.   In **View**, create an input field (which is to be validated) and invoke the validator helper with the id of the input field as the first argument followed by the **ValidationExpression** method with the desired expression as argument.

 

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                |
| [EmailAddress: [\<%][=]Html.TextBox([\"EmailAddress\"])[%\>]]                         |
|                                                                                                                                                                                                                                |
| [\<%][=][Html.Syncfusion().Validator([\"EmailAddress\"])] |
|                                                                                                                                                                                                                                |
| **[.ValidationExpression([ValidatorModel].[Expressions].Email)]**[%\>]             |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                  |
| [EmailAddress: [@]Html.TextBox([\"EmailAddress\"])]                                                                                                                      |
|                                                                                                                                                                                                                                                                  |
| [\@{][ Html.Syncfusion().Validator([\"EmailAddress\"])]                                                                                      |
|                                                                                                                                                                                                                                                                  |
| **[.ValidationExpression([ValidatorModel].[Expressions].Email).]**[Render();][}] |
|                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

 

 

2.   Build and run the application.

**[]** 

Using Properties Model

The following steps explain the definition of the validation expression for the client side valditor using the Properties model.

 

1.   In the **Controller**, create an instance of **ValidatorModel**, define the **ValidationExpression** property and pass the instance through view specific data to view as given below.

 

 

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                    |
|                                                                                                                                                                             |
| **[]**                                                                                                                                  |
|                                                                                                                                                                             |
| [public][ [ActionResult] Index()]                              |
|                                                                                                                                                                             |
| [        {]                                                                                                                             |
|                                                                                                                                                                             |
| [            [//create an instance of ValidatorModel]]                                                            |
|                                                                                                                                                                             |
| [            [ValidatorModel] myModel = [new] [ValidatorModel]();] |
|                                                                                                                                                                             |
| [            myModel.ValidationExpression = [ValidatorModel].[Expressions].Email;]      |
|                                                                                                                                                                             |
| []                                                                                                                                      |
|                                                                                                                                                                             |
| [            [//pass the instance through view data to the view]]                                                 |
|                                                                                                                                                                             |
| [            ViewData\[[\"validatorModel\"]\] = myModel;]                                                       |
|                                                                                                                                                                             |
| [            [return] View();]                                                                                     |
|                                                                                                                                                                             |
| [        }]                                                                                                                             |
|                                                                                                                                                                             |
| []                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   In **View**, create an input field (which is to be validated) and invoke the validator helper with the ID of the input field as the first argument and the view data key as the second argument.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                               |
| [EmailAddress:  [\<%][=]Html.Syncfusion().TextBox(\"[EmailAddress]\")[%\>]]                                                          |
|                                                                                                                                                                                                                                                                               |
| [                         [\<%][=]Html.Syncfusion().Validator(\"[EmailAddress]\",\"[validatorModel]\")[%\>]] |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                       |
| [EmailAddress:  [@]Html.Syncfusion().TextBox(\"[EmailAddress]\")]                                                                                                                             |
|                                                                                                                                                                                                                                                                                       |
| [                         [\@{][ ]Html.Syncfusion().Validator(\"[EmailAddress]\",\"[validatorModel]\").Render();[}]] |
|                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

3.   Build and run the application.

 

 

[]{#related-topics}

