---
title: syncfusionthemes1.md
original_path: WinForms_Docs/02_Concepts/syncfusionthemes1.md
created_at: 2025-08-05
---






##### Syncfusion Themes {#syncfusion-themes style="tab-stops: 0pt"}

Captcha supports fourteen pre-defined skins.

 

Properties

+-------------+---------------------------------------------+----------------------+---------------------------------------------------+-------------+
| Name        | Description                                 | Type of the property | Value it accepts                                  | Dependency  |
+-------------+---------------------------------------------+----------------------+---------------------------------------------------+-------------+
| AutoFormat  | Defines one of the fourteen in-built themes | enum                 | [Skins].Office2007Blue,   | NA          |
|             |                                             |                      |                                                   |             |
|             |                                             |                      | [Skins].Office2007Silver, |             |
|             |                                             |                      |                                                   |             |
|             |                                             |                      | [Skins].Office2007Black,  |             |
|             |                                             |                      |                                                   |             |
|             |                                             |                      | [Skins].Vista,            |             |
|             |                                             |                      |                                                   |             |
|             |                                             |                      | [Skins].Almond,           |             |
|             |                                             |                      |                                                   |             |
|             |                                             |                      | [Skins].Blueberry,        |             |
|             |                                             |                      |                                                   |             |
|             |                                             |                      | [Skins].Blend,            |             |
|             |                                             |                      |                                                   |             |
|             |                                             |                      | [Skins].Olive,            |             |
|             |                                             |                      |                                                   |             |
|             |                                             |                      | [Skins].Turquoise,        |             |
|             |                                             |                      |                                                   |             |
|             |                                             |                      | [Skins].Monochrome,       |             |
|             |                                             |                      |                                                   |             |
|             |                                             |                      | [Skins].Sandune,          |             |
|             |                                             |                      |                                                   |             |
|             |                                             |                      | [Skins].VS2010,           |             |
|             |                                             |                      |                                                   |             |
|             |                                             |                      | [Skins].Marble,           |             |
|             |                                             |                      |                                                   |             |
|             |                                             |                      | [Skins].Midnight          |             |
+-------------+---------------------------------------------+----------------------+---------------------------------------------------+-------------+

*[[]]{.underline}* 

Using Builder

The following steps explain the setting of the Syncfusion theme for the Captcha using Builder.

1.   In **View**, invoke the captcha helper with the control id as argument, followed by the **AutoFormat** method with the desired theme as argument.

[] 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                       |
|                                                                                                                                                                                                                                  |
| [\<%][=][Html.Syncfusion().CaptchaControl([\"myCaptcha\"])] |
|                                                                                                                                                                                                                                  |
| [.**AutoFormat([Skins].Midnight)**[%\>]]                                                                                                 |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                      |
|                                                                                                                                                                               |
| **[]**                                                                                                                                    |
|                                                                                                                                                                               |
| [\@{][ Html.Syncfusion().CaptchaControl([\"myCaptcha\"])] |
|                                                                                                                                                                               |
| [.**AutoFormat([Skins].Midnight).Render();**[}]]                                      |
|                                                                                                                                                                               |
| []                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

2.   Build and run the application.

**[]** 

Using Properties Model

The following steps explain the setting of the Syncfusion theme for the Captcha using properties model.

1.   In the Controller, create an instance of the CaptchaModel, define the **AutoFormat** properties and pass the instance through **view specific data** to **View** as given below. **

 

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
| [            myModel.AutoFormat = [Skins].Midnight;]                                                        |
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

 

The output is as shown in the following screenshot.

{border="0"}

Figure 97: Captcha with Midnight theme

 

[]{#related-topics}

