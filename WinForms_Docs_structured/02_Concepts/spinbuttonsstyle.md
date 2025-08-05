---
title: spinbuttonsstyle.md
original_path: WinForms_Docs/02_Concepts/spinbuttonsstyle.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Spin Buttons Style {#spin-buttons-style style="tab-stops: 0pt"}

[The Numeric text box supports displaying the Spin buttons in normal and onDemand styles.]

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

The following steps, guides you in configuring the style through Builder:

1.   In **View**, invoke the numeric textbox helper with the numeric ID as the first argument and enable the **Style** method with desired option as argument.

[[ [] ]]{.underline}  

+------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                             |
|                                                                                                                                                |
| [  ] [\<%] [{] |
|                                                                                                                                                |
| [        Html.MobSyncfusion().NumericTextbox([\"WebsiteNumeric\"])]                |
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
| [     Html.MobSyncfusion().NumericTextbox([\"WebsiteNumeric\"])]                   |
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

The following steps will guide you in setting the style through the Properties model.

1.   In the **Controller**, create an instance of NumericTextBoxModel; define the **Style** property, and pass the instance through the view-specific data to the view.[]

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
| [            myModel.Style = MobStyle.OnDemand;]                                                                                                                                                                     |
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

2.   In **View**, invoke the numeric textbox helper with the ViewData key as the first argument.

 

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

Figure 236 Numeric textbox with OnDemand style

 

 

{border="0"}

Figure 237 Numeric textbox with buttons once the textbox is focussed.

 

**[]**  

 

[]{#related-topics}

