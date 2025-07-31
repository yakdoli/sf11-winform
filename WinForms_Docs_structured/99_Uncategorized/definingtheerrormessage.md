---
title: definingtheerrormessage.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\definingtheerrormessage.md
created_at: 2025-07-03
---






#### Defining the Error Message {#defining-the-error-message style="tab-stops: 0pt"}

Client Side Validator support to customize the error message to be thrown on validation fail.

Property

  -------------- ------------------------------------------------------------ ------------------ ------------------ ------------
  Name           Description                                                  Type of property   Value it accepts   Dependency
  ErrorMessage   Used to define the message to be thrown on validation fail   string             Any string         NA
  -------------- ------------------------------------------------------------ ------------------ ------------------ ------------

 

Using Builder

The following steps explain defining the error message for the client side valditor using bBuilder.

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
| [                        **.ErrorMessage([\"Invalid Email Address! Try again!\"])**[%\>]]                      |
|                                                                                                                                                                                                        |
| []                                                                                                                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                      |
|                                                                                                                                                                                               |
| **[]**                                                                                                                                                    |
|                                                                                                                                                                                               |
| [EmailAddress: [@]Html.TextBox([\"EmailAddress\"])[%\>]]                  |
|                                                                                                                                                                                               |
| [                  [\@{][ ]Html.Syncfusion().Validator([\"EmailAddress\"])]      |
|                                                                                                                                                                                               |
| [                            .ValidationExpression([ValidatorModel].[Expressions].Email)]                 |
|                                                                                                                                                                                               |
| [                        **.ErrorMessage([\"Invalid Email Address! Try again!\"]).**Render()**;**[}]] |
|                                                                                                                                                                                               |
| []                                                                                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

**[]** 

2.   Build and run the application.

**[]** 

Using Properties Model

The following steps explain defining the error message for the client side valditor using Properties model.

1.   In the **Controller**, create an instance of **ValidatorModel**, define the **ErrorMessage** property and pass the instance using V**iew Specific Data** to **View** as given below.

 

 

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
| [           myModel. **ErrorMessage** = **[\"Invalid Email Address! Try again!\"]**;]                           |
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

 

 

2.   In **View**, create an input field (which is to be validated) and invoke the validator helper with the id of the input field as the first argument and the view data key as the second argument.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[aspx\]**                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                         |
| [EmailAddress:  [\<%][=]Html.TextBox(\"[EmailAddress]\")[%\>]]                                                                    |
|                                                                                                                                                                                                                                                                                         |
| [                      [\<%][=]Html.Syncfusion().Validator(\"[EmailAddress]\",\"[validatorModel]\")[%\>]] |
|                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

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

 

[] 

3.   Build and run the application.

Now the validator throws the defined error message when the input field fails the validation.

 

[]{#related-topics}

