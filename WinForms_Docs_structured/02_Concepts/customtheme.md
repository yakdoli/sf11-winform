---
title: customtheme.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\customtheme.md
created_at: 2025-07-03
---






##### Custom theme {#custom-theme style="tab-stops: 0pt"}

The custom theme feature allows you to set the background color, fore color and text color of the captcha image.

 

Properties

 

+---------------------+---------------------------------------------------------+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| Name                | Description                                             | Type of property                                                                                 | Value it accepts                                                                                                                                     | Dependency                                              |
+---------------------+---------------------------------------------------------+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| BackgroundBackColor | Defines the background back color for the captcha image | [[struct]]{.UGHyperlink} | Properties of [[[System.Drawing.Color]]{.underline}](http://msdn.microsoft.com/en-us/library/system.drawing.color_members.aspx) | Requires                                                |
|                     |                                                         |                                                                                                  |                                                                                                                                                      |                                                         |
|                     |                                                         |                                                                                                  |                                                                                                                                                      | AutoFormat to be *[Skins].None* |
+---------------------+---------------------------------------------------------+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| BackgroundForeColor | Defines the background fore color for the captcha image | [[struct]]{.UGHyperlink} | Properties of [[[System.Drawing.Color]]{.underline}](http://msdn.microsoft.com/en-us/library/system.drawing.color_members.aspx) | Requires                                                |
|                     |                                                         |                                                                                                  |                                                                                                                                                      |                                                         |
|                     |                                                         |                                                                                                  |                                                                                                                                                      | AutoFormat to be *[Skins].None* |
+---------------------+---------------------------------------------------------+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| TextColor           | Defines the text color for the captcha image            | [[struct]]{.UGHyperlink} | Properties of [[[System.Drawing.Color]]{.underline}](http://msdn.microsoft.com/en-us/library/system.drawing.color_members.aspx) | Requires                                                |
|                     |                                                         |                                                                                                  |                                                                                                                                                      |                                                         |
|                     |                                                         |                                                                                                  |                                                                                                                                                      | AutoFormat to be *[Skins].None* |
+---------------------+---------------------------------------------------------+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+

*[[]]{.underline}* 

Using Builder

The following steps explain the setting of custom theme for the captcha using builder.

1.   In **View**, invoke the captcha helper with the control id as argument followed by the **AutoFormat** method with the argument **Skins.None** and **BackgroundBackColor**, **BackgroundForeColor** and **TextColor** methods with the desired colors as argument.

 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                       |
|                                                                                                                                                                                                                                  |
| [\<%][=][Html.Syncfusion().CaptchaControl([\"myCaptcha\"])] |
|                                                                                                                                                                                                                                  |
| [.**AutoFormat([Skins].None)**]                                                                                                                                      |
|                                                                                                                                                                                                                                  |
| **[.BackgroundBackColor(System.Drawing.[Color].White)]**                                                                                                             |
|                                                                                                                                                                                                                                  |
| **[.BackgroundForeColor(System.Drawing.[Color].White)]**                                                                                                             |
|                                                                                                                                                                                                                                  |
| **[.TextColor(System.Drawing.[Color].Brown)]**[%\>]                                                          |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                       |
|                                                                                                                                                                                                                                  |
| [\@{][ ][Html.Syncfusion().CaptchaControl([\"myCaptcha\"])] |
|                                                                                                                                                                                                                                  |
| [.**AutoFormat([Skins].None)**]                                                                                                                                      |
|                                                                                                                                                                                                                                  |
| **[.BackgroundBackColor(System.Drawing.[Color].White)]**                                                                                                             |
|                                                                                                                                                                                                                                  |
| **[.BackgroundForeColor(System.Drawing.[Color].White)]**                                                                                                             |
|                                                                                                                                                                                                                                  |
| **[.TextColor(System.Drawing.[Color].Brown).Render();]**                                                                                                             |
|                                                                                                                                                                                                                                  |
| **[        ]**[}]                                                                                                                    |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   Build and run the application.

**[]** 

Using Properties Model

The following steps explain the setting of the custom theme for the captcha using Properties model.

1.   In the Controller, create an instance of the CaptchaModel, set the **AutoFormat** property to **Skins.None**, define the **BackgroundBackColor**, **BackgroundForeColor** and **TextColor** properties and pass the instance through view specific data to View as given in the following code. **

 

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
| [            **myModel.AutoFormat = [Skins].None;**]                                                        |
|                                                                                                                                                                         |
| **[            myModel.BackgroundBackColor = System.Drawing.[Color].White;]**                               |
|                                                                                                                                                                         |
| **[            myModel.BackgroundForeColor = System.Drawing.[Color].White;]**                               |
|                                                                                                                                                                         |
| **[            myModel.TextColor = System.Drawing.[Color].Brown;]**                                         |
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

[] 

[] 

2.   In **View**, invoke the captcha helper with the view data key as the control id.

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

The output is shown in the following screen shot.

{border="0"}

Figure 98: Captcha -- Custom style

**[]** 

[]{#related-topics}

