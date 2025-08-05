---
title: spinbuttonstyle.md
original_path: WinForms_Docs/02_Concepts/spinbuttonstyle.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Spin Button Style {#spin-button-style style="tab-stops: 0pt"}

The Percent text box supports displaying the Spin buttons in normal and onDemand styles.

[] 

Properties

+-------------+-----------------------------------------------------------+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| Name        | Description                                               | Type of the property | Value it accepts                                                                                                                                                   | Dependency  |
+-------------+-----------------------------------------------------------+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| Style       | Defines the style in which the control has to be rendered | [enum]{.UGHyperlink} | [MobStyle] [.Normal]                             | NA          |
|             |                                                           |                      |                                                                                                                                                                    |             |
|             |                                                           |                      | ,[][MobStyle][.OnDemand] |             |
|             |                                                           |                      |                                                                                                                                                                    |             |
|             |                                                           |                      |                                                                                                                                                                    |             |
+-------------+-----------------------------------------------------------+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+

 

Using Builder

The following steps will guide you in configuring the style through the Builder:

1.   In **View**, invoke the Percent textbox helper with the control ID as the first argument and enable the **Style** method with the desired option as argument.

[[ [] ]]{.underline}  

+------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                             |
|                                                                                                                                                |
| [  ] [\<%] [{] |
|                                                                                                                                                |
| [        Html.MobSyncfusion().PercentTextbox([\"WebsitePercent\"])]                |
|                                                                                                                                                |
| [                   .Style(MobStyle.OnDemand)                   ]                                          |
|                                                                                                                                                |
| [                          .Render();]                                                                     |
|                                                                                                                                                |
| [                      }[%\>]]                                                 |
|                                                                                                                                                |
| **[\[Razor\]]**                                                                                            |
|                                                                                                                                                |
| [\@{] []                                           |
|                                                                                                                                                |
| [     Html.MobSyncfusion().PercentTextbox([\"WebsitePercent\"])]                   |
|                                                                                                                                                |
| [                   .Style(MobStyle.OnDemand)                   ]                                          |
|                                                                                                                                                |
| [                          .Render();]                                                                     |
|                                                                                                                                                |
| [                      [}]]                                                    |
|                                                                                                                                                |
| []                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------+

[[]]{.underline}  

2.   Run the application.

 

Using Properties Model

The following steps will guide you in setting the style through the Properties model:

1.   In the **Controller**, create an instance of PercentTextBoxModel; define the **Style** property, and pass the instance through the view-specific data to the view.[]

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[Controller\]**                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                 |
| [public] [ [ActionResult] Index()]                                                                                                                       |
|                                                                                                                                                                                                                                                                                                 |
| [        {]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                 |
| [            ] [PercentTextBoxModel] [ myModel = [new][PercentTextBoxModel]();] |
|                                                                                                                                                                                                                                                                                                 |
| [            myModel.Style = MobStyle.OnDemand;] []                                                                                                                           |
|                                                                                                                                                                                                                                                                                                 |
| [            ViewData\[[\"myPercent\"]\] = myModel;] []                                                                                               |
|                                                                                                                                                                                                                                                                                                 |
| [            [return] View();] []                                                                                                                        |
|                                                                                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]**  

2.   In **View**, invoke the Percent textbox helper with the ViewData key as the first argument.

 

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
| [       [}]] []                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


{border="0"}Note: The second argument of the above percent textbox helper should match the view data key from the controller to fetch the properties.


3.   Run the application.

The following screenshot illustrates the output:

 

{border="0"}

Figure 244 Percent textbox with OnDemand style

{border="0"}

Figure 245 Percent textbox with buttons once the textbox is focussed.

[]{#related-topics}

