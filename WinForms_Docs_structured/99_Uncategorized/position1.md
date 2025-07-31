---
title: position1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\position1.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Position {#position style="tab-stops: 0pt"}

Essential Tools MVC Percent textbox supports both horizontal and vertical position.

Properties

+-------------+--------------------------------------------------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| Name        | Description                                                  | Type of the property | Value it accepts                                                                                                                                                        | Dependency  |
+-------------+--------------------------------------------------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| Position    | Defines the position in which the control has to be rendered | [enum]{.UGHyperlink} | [MobPosition] [.Vertical]                             | NA          |
|             |                                                              |                      |                                                                                                                                                                         |             |
|             |                                                              |                      | ,[][MobPosition][.Horizontal] |             |
|             |                                                              |                      |                                                                                                                                                                         |             |
|             |                                                              |                      |                                                                                                                                                                         |             |
+-------------+--------------------------------------------------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+

*[[]]{.underline}*  

Using Builder

The following steps, guides you in configuring the position through the Builder:

1.   In **View**, invoke the percent textbox helper with the control ID as the first argument and enable the **Position** method with the desired option as argument.

[[ [] ]]{.underline}  

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                    |
| [  ] [\<%] [{]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                    |
| [        Html.MobSyncfusion().PercentTextbox([\"WebsitePercent\"]).Style([MobStyle].Normal).Position([MobPosition].Vertical).WaterMarkText([\"Enter value\"])] |
|                                                                                                                                                                                                                                                                                                    |
| [                          .Render();]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                    |
| [                      }[%\>]]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                    |
| **[\[Razor\]]**                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                    |
| [\@{] []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                    |
| [     Html.MobSyncfusion().PercentTextbox([\"WebsitePercent\"]).Style([MobStyle].Normal).Position([MobPosition].Vertical).WaterMarkText([\"Enter value\"])]    |
|                                                                                                                                                                                                                                                                                                    |
| [                          .Render();]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                    |
| [                      [}]]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[[]]{.underline}  

2.   Run the application.

 

Using Properties Model

The following steps will guide you in setting the position through the Properties model:

1.   In the **Controller**, create an instance of MobPercentModel, define the **Position** property and pass the instance through ViewData to View as given below:

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                          |
| [public] [ [ActionResult] Index()]                                                                                                          |
|                                                                                                                                                                                                                                                          |
| [        {]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                          |
| [            ] [PercentTextBoxModel] [ myModel = [new][PercentTextBoxModel]();] |
|                                                                                                                                                                                                                                                          |
| [            myModel.Position = MobPosition.Vertical;]                                                                                                                                                               |
|                                                                                                                                                                                                                                                          |
| [            ViewData\[[\"myPer\"]\] = myModel;]                                                                                                                                             |
|                                                                                                                                                                                                                                                          |
| [            [return] View();]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                          |
| [        }]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]**  

2.   In **View**, invoke the Percent textbox helper with the ViewData key as the first argument.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                             |
|                                                                                                                                                                                |
| [  ] [\<%] [{                                ] |
|                                                                                                                                                                                |
| [    Html.MobSyncfusion().PercentTextbox ([\"myPercent\")]]                                                        |
|                                                                                                                                                                                |
| [                          .Render();]                                                                                                     |
|                                                                                                                                                                                |
| [       }[%\>]]                                                                                                |
|                                                                                                                                                                                |
| **[\[Razor\]]**                                                                                                                            |
|                                                                                                                                                                                |
| [    ] [\@{] []                                |
|                                                                                                                                                                                |
| [           Html.MobSyncfusion().PercentTextbox ([\"myPercent\"])]                                                 |
|                                                                                                                                                                                |
| [                          .Render();]                                                                                                     |
|                                                                                                                                                                                |
| [       [}]] []                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


{border="0"}Note: The second argument of the above percent textbox helper should match the view data key from the controller to fetch the properties.


3.   Run the application.

The following screenshot illustrates the output:

{border="0"}

Figure 241 Percent textbox -- Vertical Position

[]{#related-topics}

