---
title: definingthecustomvalidationexpression.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\definingthecustomvalidationexpression.md
created_at: 2025-07-03
---






#### Defining the Custom Validation Expression {#defining-the-custom-validation-expression style="tab-stops: 0pt"}

Client side validator supports custom validation expression. The expression can be normal regex expressions.

**[]** 

Properties

  ---------------------------- --------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------- ----------------------- ------------
  Name                         Description                                                                 Type of property                                                                                   Value it accepts        Dependency
  CustomValidationExpression   Used to define the validation expression i.e. the reference of validation   [[string]]{.UGHyperlink}   Any regex expressions   NA
  ---------------------------- --------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------- ----------------------- ------------

*[[]]{.underline}* 

Using Builder

The following steps explain the definition of the custom validation expression for the client side valditor using Builder.

1.   In **View**, create an input field (which is to be validated) and invoke the validator helper with the ID of the input field as the first argument followed by the **ValidationExpression** method with desired expression as argument.

 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                                   |
|                                                                                                                                                                                                          |
| **[]**                                                                                                                                                               |
|                                                                                                                                                                                                          |
| [Single Digit No.:[\<%][=]Html.TextBox([\"numeric\"])[%\>]    ] |
|                                                                                                                                                                                                          |
| [                        [\<%][=]Html.Syncfusion().Validator([\"numeric\"])]                |
|                                                                                                                                                                                                          |
| [    **.CustomValidationExpression([\"\^\[0-9\]\$\"])**[%\>]]                                                    |
|                                                                                                                                                                                                          |
| []                                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                  |
|                                                                                                                                                                                           |
| **[]**                                                                                                                                                |
|                                                                                                                                                                                           |
| [Single Digit No.:[@]Html.TextBox([\"numeric\"])]                                                 |
|                                                                                                                                                                                           |
| [                        [\@{][ ]Html.Syncfusion().Validator([\"numeric\"])] |
|                                                                                                                                                                                           |
| [    **.CustomValidationExpression([\"\^\[0-9\]\$\"]).**Render();[}]]                             |
|                                                                                                                                                                                           |
| []                                                                                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

2.   Build and run the application.

**[]** 

Using Properties Model

The following steps explain defining the custom validation expression for the client side valditor using properties model.

1.   In the Controller, create an instance of **ValidatorModel**, define the **ValidationExpression** property and pass the instance through **view specific data** to **View** as given below.

 

 

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
| [            **myModel**.**CustomValidationExpression** = **[\"\^\[0-9\]\$\"]**;]                               |
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

 

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                              |
| [Single Digit No:  [\<%][=]Html.TextBox(\"[numeric]\")[%\>]]                                                                        |
|                                                                                                                                                                                                                                                                              |
| [                            [\<%][=]Html.Syncfusion().Validator(\"[numeric] \",\"[validatorModel]\")[%\>]] |
|                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                      |
| [Single Digit No:  [@]Html.TextBox(\"[numeric]\")]                                                                                                                                           |
|                                                                                                                                                                                                                                                                                      |
| [                            [\@{][ ]Html.Syncfusion().Validator(\"[numeric] \",\"[validatorModel]\").Render();[}]] |
|                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

3.   Build and run the application.

 

Now the validator validates the textbox for a single digit number on focus out.

[]{#related-topics}

