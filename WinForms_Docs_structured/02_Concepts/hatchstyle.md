---
title: hatchstyle.md
original_path: WinForms_Docs/02_Concepts/hatchstyle.md
created_at: 2025-08-05
---






##### Hatch Style {#hatch-style style="tab-stops: 0pt"}

Captcha supports customizing the background hatch style of the Captcha image.

Properties

+-------------+----------------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| Name        | Description                                        | Type of property | Value it accepts                                                                                                                                                                   | Dependency  |
+-------------+----------------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| HatchStyle  | Defines the hatch style for the captcha background | enum             | Members of [[[System.Drawing.Drawing2D.HatchStyle]]{.underline}](http://msdn.microsoft.com/en-us/library/system.drawing.drawing2d.hatchstyle%28VS.71%29.aspx) | NA          |
|             |                                                    |                  |                                                                                                                                                                                    |             |
|             |                                                    |                  |                                                                                                                                                                                    |             |
+-------------+----------------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+

*[[]]{.underline}* 

Using Builder

The following steps explain the setting of the hatch style for the captcha using builder.

1.   In **View**, invoke the captcha helper with control id as argument followed by the **HatchStyle** method with the desired style as argument.

 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                       |
|                                                                                                                                                                                                                                  |
| [\<%][=][Html.Syncfusion().CaptchaControl([\"myCaptcha\"])] |
|                                                                                                                                                                                                                                  |
| [.AutoFormat([Skins].Office2007Silver)]                                                                                                                              |
|                                                                                                                                                                                                                                  |
| [.**HatchStyle(System.Drawing.Drawing2D.[HatchStyle].ForwardDiagonal)**[%\>]]                                                            |
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
| [.AutoFormat([Skins].Office2007Silver)]                                                                                                                              |
|                                                                                                                                                                                                                                  |
| [.**HatchStyle(System.Drawing.Drawing2D.[HatchStyle].ForwardDiagonal)**.Render();]                                                                                   |
|                                                                                                                                                                                                                                  |
| **[       ]**[}]                                                                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

2.   Build and run the application.

**[]** 

Using Properties Model

The following steps explain the setting of the hatch style for the captcha using Properties model.**

1.   In the Controller, create an instance of CaptchaModel, define the **HatchStyle** property and pass the instance through view specific data to view as given below. **

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
| [            myModel.AutoFormat = [Skins].Office2007Silver;]                                                |
|                                                                                                                                                                         |
| [            myModel.HatchStyle = System.Drawing.Drawing2D.[HatchStyle].ForwardDiagonal;]                   |
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

*[[]]{.underline}* 

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

[] 

3.   Build and run the application.       

The output is shown in the following screen shot.

 

{border="0"}

Figure 99: Captcha -- Hatch Styles

 

 

[]{#related-topics}

