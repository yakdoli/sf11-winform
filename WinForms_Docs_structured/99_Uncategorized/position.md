---
title: position.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\position.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Position {#position style="tab-stops: 0pt"}

Essential Tools MVC Numeric textbox supports both horizontal and vertical position.

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

The following steps, guides you in configuring the position through Builder:

1.   In View, invoke the Numeric textbox helper with the numeric ID as the first argument and enable the Position method with the desired option as argument.

[[ [] ]]{.underline}  

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                   |
| [\<%] [{        Html.MobSyncfusion().NumericTextbox([\"WebsiteNumeric\"]).Style([MobStyle].Normal).Position([MobPosition].Vertical).WaterMarkText([\"Enter value\"])] |
|                                                                                                                                                                                                                                                                                                                                                                   |
| [.Render();  }[%\>]]                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                   |
| **[\[Razor\]]**                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                   |
| [\@{] [     Html.MobSyncfusion().NumericTextbox([\"WebsiteNumeric\"]).Style([MobStyle].Normal).Position([MobPosition].Vertical).WaterMarkText([\"Enter value\"])]     |
|                                                                                                                                                                                                                                                                                                                                                                   |
| [.Render();   [}]]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[[]]{.underline}  

2.   Run the application.

 

Using Properties Model

The following steps will guide you in setting the position through the Properties model:

1.   In the **Controller**, create an instance of MobNumericModel, define the **Position** property and pass the instance through ViewData to View as given below:

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                          |
| [public] [ [ActionResult] Index()]                                                                                                          |
|                                                                                                                                                                                                                                                          |
| [        {]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                          |
| [            ] [NumericTextBoxModel] [ myModel = [new][NumericTextBoxModel]();] |
|                                                                                                                                                                                                                                                          |
| [            myModel.Position = MobPosition.Vertical;]                                                                                                                                                               |
|                                                                                                                                                                                                                                                          |
| [            ViewData\[[\"myNumeric\"]\] = myModel;]                                                                                                                                         |
|                                                                                                                                                                                                                                                          |
| [            [return] View();]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                          |
| [        }]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]**  

2.   In **View**, invoke the Numeric textbox helper with the ViewData key as the first argument.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                             |
|                                                                                                                                                                                |
| [  ] [\<%] [{                                ] |
|                                                                                                                                                                                |
| [    Html.MobSyncfusion().NumericTextbox([\"myNumeric\")]]                                                         |
|                                                                                                                                                                                |
| [                          .Render();]                                                                                                     |
|                                                                                                                                                                                |
| [       }[%\>]]                                                                                                |
|                                                                                                                                                                                |
| **[\[Razor\]]**                                                                                                                            |
|                                                                                                                                                                                |
| [    ] [\@{] []                                |
|                                                                                                                                                                                |
| [           Html.MobSyncfusion().NumericTextbox([\"myNumeric\"])]                                                  |
|                                                                                                                                                                                |
| [                          .Render();]                                                                                                     |
|                                                                                                                                                                                |
| [       [}]] []                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


{border="0"}Note: The second argument of the above numeric textbox helper should match the view data key from the controller to fetch the properties.


3.   Run the application.

The following screenshot illustrates the output:

{border="0"}

Figure 233: Numeric textbox -- Vertical Position

[]{#related-topics}

