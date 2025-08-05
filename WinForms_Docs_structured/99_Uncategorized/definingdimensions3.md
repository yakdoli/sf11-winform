---
title: definingdimensions3.md
original_path: WinForms_Docs/99_Uncategorized/definingdimensions3.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Defining Dimensions {#defining-dimensions style="tab-stops: 0pt"}

The Numeric text box control allows you to customize the dimensions allowing the textbox to apply any scenario.

[] 

Properties

  ------- -------------------------------------------------- ---------------------- ------------------ ------------
  Name    Description                                        Type of the property   Value it accepts   Dependency
  Width   Sets the width of the Numeric text box in pixels   Unit                   Numeric            NA
  ------- -------------------------------------------------- ---------------------- ------------------ ------------

 

Using Builder

The following steps, guides you in configuring the dimensions through the Builder:

1.   In View, invoke the Numeric textbox helper with the numeric ID as the first argument and enable the Width method with desired option as argument.

[[ [] ]]{.underline}  

+------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                             |
|                                                                                                                                                |
| [  ] [\<%] [{] |
|                                                                                                                                                |
| [        Html.MobSyncfusion().NumericTextbox([\"WebsiteNumeric\"]).Width(100)]     |
|                                                                                                                                                |
| [                          .Render();]                                                                     |
|                                                                                                                                                |
| [                      }[%\>]]                                                 |
|                                                                                                                                                |
| **[\[Razor\]]**                                                                                            |
|                                                                                                                                                |
| [\@{] []                                           |
|                                                                                                                                                |
| [     Html.MobSyncfusion().NumericTextbox([\"WebsiteNumeric\"]).Width(100)]        |
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

The following steps will guide you in setting the width through the Properties model.

1.   In the **Controller**, create an instance of MobNumericModel, define the **Width** property and pass the instance through ViewData to View as given below:

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
| [            myModel.Width = 100;]                                                                                                                                                                                   |
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
| [                          .Render();]                                                                                        |
|                                                                                                                                                                                |
| [       [}]] []              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


{border="0"}Note: The second argument of the above numeric textbox helper should match the view data key from the controller to fetch the properties.


3.   Run the application.

The following screenshot illustrates the output:

 

{border="0"}

Figure 234 Numeric textbox with Customized width

[] 

[]{#related-topics}

