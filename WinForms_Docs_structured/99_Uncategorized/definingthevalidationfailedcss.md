---
title: definingthevalidationfailedcss.md
original_path: WinForms_Docs/99_Uncategorized/definingthevalidationfailedcss.md
created_at: 2025-08-05
---






#### Defining the validation failed css {#defining-the-validation-failed-css style="tab-stops: 0pt"}

Client side validator support to customize the style of the error message, is thrown when validation fails.

**[]** 

Property

  --------------------- ---------------------------------------------------- -------------------------------------------------------------------------------------------------- ------------------ ------------
  Name                  Description                                          Type of the property                                                                               Value it accepts   Dependency
  ValidationFailedCSS   Used to define the css class for the error message   [[string]]{.UGHyperlink}   Any string         NA
  --------------------- ---------------------------------------------------- -------------------------------------------------------------------------------------------------- ------------------ ------------

 

Using Builder

The following steps explain defining the validation failed css for the client side valditor using builder.

1.   In **View**, create an input field (which is to be validated) and invoke the validator helper with the id of the input field as the first argument followed by the **ErrorMessge** method with desired message as argument.

 

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                                 |
|                                                                                                                                                                                                        |
| **[]**                                                                                                                                                             |
|                                                                                                                                                                                                        |
| [EmailAddress: [\<%][=]Html.TextBox([\"EmailAddress\"])[%\>]] |
|                                                                                                                                                                                                        |
| [                  [\<%][=]Html.Syncfusion().Validator([\"EmailAddress\"])]               |
|                                                                                                                                                                                                        |
| [                            .ValidationExpression([ValidatorModel].[Expressions].Email)]                          |
|                                                                                                                                                                                                        |
| [                        **.ValidationFailedCSS([\"validation-error\"])**[%\>]]                                |
|                                                                                                                                                                                                        |
| []                                                                                                                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                        |
|                                                                                                                                                                                 |
| **[]**                                                                                                                                      |
|                                                                                                                                                                                 |
| [EmailAddress: [@]Html.Syncfusion().TextBox([\"EmailAddress\"])]                        |
|                                                                                                                                                                                 |
| [                  [\@{] Html.Syncfusion().Validator([\"EmailAddress\"])]               |
|                                                                                                                                                                                 |
| [                            .ValidationExpression([ValidatorModel].[Expressions].Email)]   |
|                                                                                                                                                                                 |
| [                        **.ValidationFailedCSS([\"validation-error\"]).**Render();[}]] |
|                                                                                                                                                                                 |
| []                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

**[]** 

2.   In the stylesheet, define the css as below:

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Style\]]**                                                                                                                                                                    |
|                                                                                                                                                                                                                        |
| [\<][style][ [type][=\"text/css\"\>]] |
|                                                                                                                                                                                                                        |
| [        [.validation-error]]                                                                                                                               |
|                                                                                                                                                                                                                        |
| [        {]                                                                                                                                                                        |
|                                                                                                                                                                                                                        |
| [            [color]:[Green];]                                                                                                            |
|                                                                                                                                                                                                                        |
| [            [font-weight]:[bold];]                                                                                                       |
|                                                                                                                                                                                                                        |
| [            [font-style]:[italic];]                                                                                                      |
|                                                                                                                                                                                                                        |
| [        }]                                                                                                                                                                        |
|                                                                                                                                                                                                                        |
| [      [\</][style][\>]]                                                                                          |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

 

3.   Build and run the application.

**[]** 

Using Properties Model

The following steps explain defining the validation failed css for the client side valditor using Properties model.

1.   In the Controller, create an instance of ValidatorModel, define the **ErrorMessage** property and pass the instance through **view specific data** to **View** as given below.

 

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
| [           myModel.**ValidationFailedCSS** = **[\"validation-error\"]**;]                                      |
|                                                                                                                                                                             |
| []                                                                                                                                      |
|                                                                                                                                                                             |
| [            [//pass the instance through view data to the view]]                                                 |
|                                                                                                                                                                             |
| [            ViewData\[[\"validatorModel\"]\] = myModel;]                                                       |
|                                                                                                                                                                             |
| [            [return] View();]                                                                                     |
|                                                                                                                                                                             |
| [        }]                                                                                                                             |
|                                                                                                                                                                             |
| []                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   In **View**, create an input field (which is to be validated) and invoke the validator helper with the ID of the input field as the first argument and the view data key as the second argument.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[ASPX\]]**                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                               |
| [EmailAddress:  [\<%][=]Html.TextBox(\"[EmailAddress]\")[%\>]]                                                                       |
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
| [EmailAddress:  [@]Html.TextBox(\"[EmailAddress]\")]                                                                                                                                          |
|                                                                                                                                                                                                                                                                                       |
| [                         [\@{][ ]Html.Syncfusion().Validator(\"[EmailAddress]\",\"[validatorModel]\").Render();[}]] |
|                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

3.   In the stylesheet, define the **Cascading Style Sheet** (CSS) as given below:

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Style\]]**                                                                                                                                                                    |
|                                                                                                                                                                                                                        |
| **[]**                                                                                                                                                                             |
|                                                                                                                                                                                                                        |
| [\<][style][ [type][=\"text/css\"\>]] |
|                                                                                                                                                                                                                        |
| [        [.validation-error]]                                                                                                                               |
|                                                                                                                                                                                                                        |
| [        {]                                                                                                                                                                        |
|                                                                                                                                                                                                                        |
| [            [color]:[Green];]                                                                                                            |
|                                                                                                                                                                                                                        |
| [            [font-weight]:[bold];]                                                                                                       |
|                                                                                                                                                                                                                        |
| [            [font-style]:[italic];]                                                                                                      |
|                                                                                                                                                                                                                        |
| [        }]                                                                                                                                                                        |
|                                                                                                                                                                                                                        |
| [      [\</][style][\>]]                                                                                          |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

 

4.   Build and run the application.

 

Now the validator throws the error message with the specified styles.

[]{#related-topics}

