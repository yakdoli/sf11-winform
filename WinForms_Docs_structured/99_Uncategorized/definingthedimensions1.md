---
title: definingthedimensions1.md
original_path: WinForms_Docs/99_Uncategorized/definingthedimensions1.md
created_at: 2025-08-05
---






#### Defining the Dimensions {#defining-the-dimensions style="tab-stops: 0pt"}

Captcha supports customization of the image dimensions to make it fit under all scenarios.

 

Properties

  -------- ------------------------------------------ ------------------ ------------------- ------------
  Name     Description                                Type of property   Value it accepts    Dependency
  Height   Sets the height of the Captcha in pixels   int                0 to int.MaxValue   NA
  Width    Sets the width of the Captcha in pixels    int                0 to int.MaxValue   NA
  -------- ------------------------------------------ ------------------ ------------------- ------------

 

Using Builder

The following steps explain the definitions of the dimensions of Captcha using Builder.

1.   In **View**, invoke the captcha helper with the control ID as argument followed by the **Height** and **Width** methods with the desired dimensions as arguments.

 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                       |
|                                                                                                                                                                                                                                  |
| [\<%][=][Html.Syncfusion().CaptchaControl([\"myCaptcha\"])] |
|                                                                                                                                                                                                                                  |
| **[.Height(75)]**                                                                                                                                                                            |
|                                                                                                                                                                                                                                  |
| **[.Width(200)[%\>]]**                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                       |
|                                                                                                                                                                                                                                  |
| [\@{][ ][Html.Syncfusion().CaptchaControl([\"myCaptcha\"])] |
|                                                                                                                                                                                                                                  |
| **[.Height(75)]**                                                                                                                                                                            |
|                                                                                                                                                                                                                                  |
| **[.Width(200)]**                                                                                                                                                                            |
|                                                                                                                                                                                                                                  |
| [.Render();[]]                                                                                                                                                   |
|                                                                                                                                                                                                                                  |
| **[}]**                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

**[]** 

**[]** 

2.   Build and run the application.

**[]** 

Using Properties Model

The following steps explain the definition of the the dimensions of Captcha using the properties model.

1.   In the **Controller**, create an instance of **CaptchaModel**, define the **Height** and **Width** properties and pass the instance through view specific data to view as shown below. **

 

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
| [            myModel.Height = 75;]                                                                                                  |
|                                                                                                                                                                         |
| [            myModel.Width = 200;]                                                                                                  |
|                                                                                                                                                                         |
| []                                                                                                                                  |
|                                                                                                                                                                         |
| [           [//pass the instance through view data to view]]                                                  |
|                                                                                                                                                                         |
| [            ViewData\[[\"myCaptcha\"]\] = myModel;]                                                        |
|                                                                                                                                                                         |
| [            [return] View();]                                                                                 |
|                                                                                                                                                                         |
| [        }[]]                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

2.   In **View**, invoke the captcha helper with the **View Data Key** as the Control ID.

 

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                   |
| [\<%][=][Html.Syncfusion().CaptchaControl([\"myCaptcha\"])[%\>]] |
|                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                           |
| [\@{][ ][Html.Syncfusion().CaptchaControl([\"myCaptcha\"]).Render();[}]] |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Build and run the application.

 

The following screenshot illustrates the output.

 

{border="0"}

Figure 96: Captcha with increased dimensions

 

 

 

[]{#related-topics}

