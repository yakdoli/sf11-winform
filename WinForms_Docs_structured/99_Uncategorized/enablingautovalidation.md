---
title: enablingautovalidation.md
original_path: WinForms_Docs/99_Uncategorized/enablingautovalidation.md
created_at: 2025-08-05
---






#### Enabling Auto Validation {#enabling-auto-validation style="tab-stops: 0pt"}

 

Captcha support auto validation within AJAXforms when the form fields are defined with client side validation rules. It compares the target input field with the captcha image and throws the validation message thereby updating the captcha with the new image on every post. Also, it prevents submission of forms on validation fail.

**[]** 

Properties


+--------------------------------------+---------------------------------------------------------+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+-------------+
| Name                                 | Description                                             | Type of property                                                                                 | Value it accepts                                                                                     | Dependency  |
+======================================+=========================================================+==================================================================================================+======================================================================================================+=============+
| AutoValidate                         | Enables/Disables the auto validation                    | [[bool]]{.UGHyperlink}   | [[true/false]]{.UGHyperlink} | NA          |
+--------------------------------------+---------------------------------------------------------+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+-------------+
| TargetId[] | Gets the Id of the target input element to be validated | [[string]]{.UGHyperlink} | Any string                                                                                           | NA          |
|                                      |                                                         |                                                                                                  |                                                                                                      |             |
|                                      |                                                         |                                                                                                  |                                                                                                      |             |
+--------------------------------------+---------------------------------------------------------+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+-------------+
| RequestMapper                        | Gets the action name for the captcha validation         | [[string]]{.UGHyperlink} | Action Name                                                                                          | NA          |
|                                      |                                                         |                                                                                                  |                                                                                                      |             |
|                                      |                                                         |                                                                                                  |                                                                                                      |             |
+--------------------------------------+---------------------------------------------------------+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+-------------+
| SuccessMessage                       | Defines the validation success message                  | [[string]]{.UGHyperlink} | Any string                                                                                           | NA          |
|                                      |                                                         |                                                                                                  |                                                                                                      |             |
|                                      |                                                         |                                                                                                  |                                                                                                      |             |
+--------------------------------------+---------------------------------------------------------+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+-------------+
| FailureMessage                       | Defines the validation failure message                  | [[string]]{.UGHyperlink} | Any string                                                                                           | NA          |
|                                      |                                                         |                                                                                                  |                                                                                                      |             |
|                                      |                                                         |                                                                                                  |                                                                                                      |             |
+--------------------------------------+---------------------------------------------------------+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+-------------+


 

Using Builder

The following steps explain the enabling of auto-validation for the Captcha using Builder.

1.   In **View**, create a form with the input field (with respect to which the captcha is to be validated) and invoke the captcha helper with the control id as argument followed by the **AutoValidate, TargetId, RequestMapper, SuccessMessage** and **FailureMessage** methods with the desired options as arguments.

 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                            |
| [\<%][using][ (Ajax.BeginForm([\"Index\"], [new] [AjaxOptions] { }))]                                    |
|                                                                                                                                                                                                                                                                                                                            |
| [            { [%\>]]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                            |
| [\<%][=][Html.Syncfusion().CaptchaControl([\"myCaptcha\"])]                                                                                           |
|                                                                                                                                                                                                                                                                                                                            |
| [.**AutoValidate([true])**]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                            |
| **[.TargetId([\"myTextbox\"])]**                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                            |
| **[.RequestMapper([\"Home/Index\"])]**                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                            |
| **[.SuccessMessage([\"Valid\"])]**                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                            |
| **[.FailureMessage([\"Inavalid characters.Try again!\"])]**[%\>][]                                                                                                 |
|                                                                                                                                                                                                                                                                                                                            |
| [            Word Verification:]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                            |
| [            [\<%][=]Html.TextBox([\"myTextbox\"])[%\>]]                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                            |
| [            [\<%][=]Html.ValidationMessage([\"myTextbox\"])[%\>]]                                                                                                                |
|                                                                                                                                                                                                                                                                                                                            |
| [            [\<][input] [type][=\"submit\"] [value][=\"Submit\"] [id][=\"Submit\"] [/\>]] |
|                                                                                                                                                                                                                                                                                                                            |
| [      [\<%]} [%\>]]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [    ]                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [@][using][ (Ajax.BeginForm([\"Index\"], [new] [AjaxOptions] { }))]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [            { ]                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [@][{Html.Syncfusion().CaptchaControl([\"myCaptcha\"])]                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [.**AutoValidate([true])**]                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **[.TargetId([\"myTextbox\"])]**                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **[.RequestMapper([\"Home/Index\"])]**                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **[.SuccessMessage([\"Valid\"])]**                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **[                     .FailureMessage([\"Inavalid characters.Try again!\"])]**                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [.Render();}]                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [          ][Word Verification:][]                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [              [@]Html.TextBox([\"myTextbox\"])]                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [              [@]Html.ValidationMessage([\"myTextbox\"])]                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [             ][\<][input][ [type][=\"submit\"] [value][=\"Submit\"] [id][=\"Submit\"] [/\>]][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [      ]                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [      } ]                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

2.   In the **Controller**, invoke the Captcha actions within the action specified by the **Request Mapper** method.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                     |
|                                                                                                                                                                              |
| **[]**                                                                                                                                   |
|                                                                                                                                                                              |
| [\[[AcceptVerbs]([HttpVerbs].Post)\]]                                                    |
|                                                                                                                                                                              |
| [        [public] [ActionResult] Index([CaptchaParams] parameters)] |
|                                                                                                                                                                              |
| [        {]                                                                                                                              |
|                                                                                                                                                                              |
| [            [return] parameters.CaptchaActions();]                                                                 |
|                                                                                                                                                                              |
| [        } ]                                                                                                                             |
|                                                                                                                                                                              |
| []                                                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

3.   Build and run the application.

**[]** 

Using Properties Model

The following steps explain enabling of auto-validation for the captcha using the Properties model.

1.   In the Controller, create an instance of CaptchaModel, define the **AutoValidate, TargetId, RequestMapper, SuccessMessage** and **FailureMessage** properties and pass the instance through view specific data to the view as given below. **

 

*[[]]{.underline}* 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                |
|                                                                                                                                                                         |
| **[]**                                                                                                                              |
|                                                                                                                                                                         |
| [public][ [ActionResult] Index()]                          |
|                                                                                                                                                                         |
| [        {]                                                                                                                         |
|                                                                                                                                                                         |
| [            [//create instance of CaptchaModel]]                                                             |
|                                                                                                                                                                         |
| [            [CaptchaModel] myModel = [new] [CaptchaModel]();] |
|                                                                                                                                                                         |
| [            **myModel.AutoValidate = [true];**]                                                               |
|                                                                                                                                                                         |
| **[            myModel.TargetId = [\"textbox1\"];]**                                                        |
|                                                                                                                                                                         |
| **[            myModel.RequestMapper = [\"Home/Index\"];]**                                                 |
|                                                                                                                                                                         |
| **[            myModel.SuccessMessage = [\"Valid\"];]**                                                     |
|                                                                                                                                                                         |
| **[            myModel.FailureMessage = [\"Invalid characters.Try again!\"];]**                             |
|                                                                                                                                                                         |
| []                                                                                                                                  |
|                                                                                                                                                                         |
| [           [//pass the instance through view data to view]]                                                  |
|                                                                                                                                                                         |
| [            ViewData\[[\"myCaptcha\"]\] = myModel;]                                                        |
|                                                                                                                                                                         |
| [            [return] View();]                                                                                 |
|                                                                                                                                                                         |
| [        }]                                                                                                                         |
|                                                                                                                                                                         |
| []                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

[] 

2.   In **View**, create a form with the input field (with respect to which the captcha is to be validated) and invoke the captcha helper with the view data key as the control id.

 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                            |
| [\<%][using][ (Ajax.BeginForm([\"Index\"], [new] [AjaxOptions] { }))]                                    |
|                                                                                                                                                                                                                                                                                                                            |
| [            { [%\>]]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                            |
| [\<%][=][Html.Syncfusion().CaptchaControl([\"myCaptcha\"])[%\>]]                                                          |
|                                                                                                                                                                                                                                                                                                                            |
| [            Word Verification:]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                            |
| [            [\<%][=]Html.Syncfusion().TextBox([\"myTextbox\"])[%\>]]                                                                                                             |
|                                                                                                                                                                                                                                                                                                                            |
| [            [\<%][=]Html.Syncfusion().ValidationMessage([\"myTextbox\"])[%\>]]                                                                                                   |
|                                                                                                                                                                                                                                                                                                                            |
| [            [\<][input] [type][=\"submit\"] [value][=\"Submit\"] [id][=\"Submit\"] [/\>]] |
|                                                                                                                                                                                                                                                                                                                            |
| [      [\<%]} [%\>]]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [@][using][ (Ajax.BeginForm([\"Index\"], [new] [AjaxOptions] { }))]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [            { ]                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [@][{Html.Syncfusion().CaptchaControl([\"myCaptcha\"]).Render();[}]]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [          ][Word Verification:][]                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [              [@]Html.TextBox([\"myTextbox\"])]                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [              [@]Html.ValidationMessage([\"myTextbox\"])]                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [             ][\<][input][ [type][=\"submit\"] [value][=\"Submit\"] [id][=\"Submit\"] [/\>]][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [      ]                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [      } ]                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

3.   In the Controller, invoke the Captcha actions within the action specified by the Request Mapper property.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                     |
|                                                                                                                                                                              |
| **[]**                                                                                                                                   |
|                                                                                                                                                                              |
| [\[[AcceptVerbs]([HttpVerbs].Post)\]]                                                    |
|                                                                                                                                                                              |
| [        [public] [ActionResult] Index([CaptchaParams] parameters)] |
|                                                                                                                                                                              |
| [        {]                                                                                                                              |
|                                                                                                                                                                              |
| [            [return] parameters.CaptchaActions();]                                                                 |
|                                                                                                                                                                              |
| [        } ]                                                                                                                             |
|                                                                                                                                                                              |
| []                                                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

4.   Build and run the application.


[] 

{border="0"}[Note: ]


[·      ]The **CaptchaActions**() is to be invoked within the action defined in by the RequestMapper.

[·      ]**CaptchaActions**() can also be called in the same post action which the form shares. The captcha post action and the default form post can be differentiated with the RequestType property of **CaptchaParams**

 

[]{#related-topics}

