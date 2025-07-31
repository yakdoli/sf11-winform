---
title: validatingacaptcha.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\validatingacaptcha.md
created_at: 2025-07-03
---






#### Validating a Captcha {#validating-a-captcha style="tab-stops: 0pt"}

Captcha supports in-built validation methods to validate it with respect to an input field.

 

Methods

+--------------------------------------------------+------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------+---------------+
| Name                                             | Parameters                                                             | Return type | Description                                                                 | Refernce Link |
+--------------------------------------------------+------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------+---------------+
| [CaptchaService].IsValid | string expectedText -- the encrypted text of the Captcha               | bool        | Returns the validation state of the Captcha with respect to the input field | \-            |
|                                                  |                                                                        |             |                                                                             |               |
|                                                  | string actualText -- the text from the text box to be validated        |             |                                                                             |               |
|                                                  |                                                                        |             |                                                                             |               |
|                                                  | bool  caseSensitive -- true/false:enables or disables case sensitivity |             |                                                                             |               |
+--------------------------------------------------+------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------+---------------+

 

The following steps explain the validation of a Captcha.

1.   In **View**, create a form with an input field (with respect to which the captcha is to be validated), Captcha and a **Submit** button. **[]**

**[]** 

**[]** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                    |
| [\<%][using][ (Html.Syncfusion().BeginForm())]                                                                                                        |
|                                                                                                                                                                                                                                                                                                    |
| [      { [%\>]]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                    |
| [            [\<%][=]Html.Syncfusion().CaptchaControl([\"myCaptcha\"])[%\>]]                                                                              |
|                                                                                                                                                                                                                                                                                                    |
| [            Word Verification: [\<%][=]Html.TextBox([\"myTextbox\"])[%\>]]                                                                               |
|                                                                                                                                                                                                                                                                                                    |
| [            [\<%][=]Html.Syncfusion().ValidationMessage([\"myTextbox\"]) [%\>][]]                                                |
|                                                                                                                                                                                                                                                                                                    |
| [            [\<][input] [type][=\"submit\"] [value][=\"Submit\"] [id][=\"Submit\"/\>]] |
|                                                                                                                                                                                                                                                                                                    |
| [      [\<%]} [%\>]]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

**[]** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                         |
| [@][using][ (Html.BeginForm())]                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                         |
| [    {]                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                         |
| [        ][\@{][ ][Html.Syncfusion().CaptchaControl([\"myCaptcha\"]).Render();[}]] |
|                                                                                                                                                                                                                                                                                                                         |
| [            Word Verification: [@]Html.TextBox([\"myTextbox\"])]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                         |
| [            [@]Html.Syncfusion().ValidationMessage([\"myTextbox\"])[]]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                         |
| [            [\<][input] [type][=\"submit\"] [value][=\"Submit\"] [id][=\"Submit\"/\>]]                      |
|                                                                                                                                                                                                                                                                                                                         |
| [        }][]                                                                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

2.   In the Controller, add the validation rules using the **IsValid** method as shown below in the form's post action.

 

 

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                                                   |
|                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                 |
|                                                                                                                                                                                                            |
| [/\*Post Action for the Login Form\*/][]                                                                             |
|                                                                                                                                                                                                            |
| [        \[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                          |
|                                                                                                                                                                                                            |
| [        [public] [ActionResult] Index([string] myCaptcha, [string] myTextbox)] |
|                                                                                                                                                                                                            |
| [        {]                                                                                                                                                            |
|                                                                                                                                                                                                            |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                            |
| [            [if] (\![CaptchaService].IsValid(myCaptcha, myTextbox, [true]))]                        |
|                                                                                                                                                                                                            |
| [                ModelState.AddModelError([\"myTextbox\"], [\"Invalid characters.Try again\"]);]                       |
|                                                                                                                                                                                                            |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                            |
| [            [return] View();]                                                                                                                    |
|                                                                                                                                                                                                            |
| [        }]                                                                                                                                                            |
|                                                                                                                                                                                                            |
| []                                                                                                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

3.   Build and run the application.

The output is shown in the following screenshot.

 

{border="0"}

Figure 94: A form with captcha

 

On form submit, when the entered characters within the input field matches the image text, the form passes the validation, else it fails. The output on validation fail is shown in the following screenshot.

 

{border="0"}

Figure 95: A form on validation fails

 

 

[]{#related-topics}

