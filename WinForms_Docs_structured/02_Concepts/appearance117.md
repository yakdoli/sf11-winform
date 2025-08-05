---
title: appearance117.md
original_path: WinForms_Docs/02_Concepts/appearance117.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Appearance {#appearance style="tab-stops: 0pt"}

Percent textbox supports in-built themes that gives high visual appeal that are suitable for various layouts. Percent textbox supports the following four in-built Syncfusion themes to enhance the look and feel:

[·      ]BlueLight

[·      ]DarkNight

[·      ]MetroBlue

[·      ]Spinach

Properties

 

+-------------+---------------------------+----------------------+-----------------------------------------------+-------------+
| Name        | Description               | Type of the property | Value it accepts                              | Dependency  |
+-------------+---------------------------+----------------------+-----------------------------------------------+-------------+
| AutoFormat  | Defines the mobile themes | enum                 | [MobSkins].BlueLight, | NA          |
|             |                           |                      |                                               |             |
|             |                           |                      | [MobSkins].DarkNight, |             |
|             |                           |                      |                                               |             |
|             |                           |                      | [MobSkins].MetroBlue, |             |
|             |                           |                      |                                               |             |
|             |                           |                      | [MobSkins].Spinach    |             |
|             |                           |                      |                                               |             |
|             |                           |                      |                                               |             |
+-------------+---------------------------+----------------------+-----------------------------------------------+-------------+

**[]**  

Using Builder

The following steps, explains the appearance of Percent textbox control using the Builder:

1.   In **View**, invoke the percent textbox helper with the Control ID as first argument followed by the AutoFormat method with desired theme as the argument.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                |
| [\<%] [{]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                |
| [                              Html.MobSyncfusion().PercentTextbox([\"myNum\"]).AutoFormat([MobSkins].BlueLight).WaterMarkText([\"Enter value\"])] |
|                                                                                                                                                                                                                                                                |
| [                              .Render();]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                |
| [                          }[%\>]]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                |
| [      []]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                |
| **[\[Razor\]]**                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                |
| [    [\@{]]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                |
| [        Html.MobSyncfusion().PercentTextbox([\"myNum\"]).AutoFormat([MobSkins].BlueLight).WaterMarkText([\"Enter value\"])]                       |
|                                                                                                                                                                                                                                                                |
| [                              .Render();]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                |
| [    [}]] []                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   Build and run the application.

**[]**  

Using Properties Model

The following steps, explains the appearance of Percent textbox control using the Properties model:

1.   In the **Controller**, create an instance for the **MobPercentModel** and pass the instance through **ViewData** to **View** as given below:**

*[[ [] ]]{.underline}*  

*[[ [] ]]{.underline}*  

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                          |
| [public] [ [ActionResult] Index()]                                                                                                          |
|                                                                                                                                                                                                                                                          |
| [        {]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                          |
| [            ] [PercentTextBoxModel] [ myModel = [new][PercentTextBoxModel]();] |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                          |
| [            myModel.AutoFormat = [MobSkins].BlueLight;]                                                                                                                                     |
|                                                                                                                                                                                                                                                          |
| [            ViewData\[[\"myPercent\"]\] = myModel;]                                                                                                                                         |
|                                                                                                                                                                                                                                                          |
| [            [return] View();]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                          |
| [        }]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In **View**, invoke the Percent textbox helper with the ViewData key as the first argument.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                             |
|                                                                                                                                                                                |
| [  ] [\<%] [{                                ] |
|                                                                                                                                                                                |
| [    Html.MobSyncfusion().PercentTextbox([\"myPercent\")]]                                                         |
|                                                                                                                                                                                |
| [                          .Render();]                                                                                                     |
|                                                                                                                                                                                |
| [       }[%\>]]                                                                                                |
|                                                                                                                                                                                |
| **[\[Razor\]]**                                                                                                                            |
|                                                                                                                                                                                |
| [    ] [\@{] []                                |
|                                                                                                                                                                                |
| [           Html.MobSyncfusion().PercentTextbox([\"myPercent\"])]                                                  |
|                                                                                                                                                                                |
| [                          .Render();]                                                                                                     |
|                                                                                                                                                                                |
| [       [}]] []                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Build and run the application.

 

The output is shown in the following screenshot:[]

{border="0"}

Figure 246 Percent Textbox Control with BlueLight Theme

[]{#related-topics}

