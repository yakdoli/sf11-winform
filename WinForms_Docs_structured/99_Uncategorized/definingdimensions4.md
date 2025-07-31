---
title: definingdimensions4.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\definingdimensions4.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Defining Dimensions {#defining-dimensions style="tab-stops: 0pt"}

The Percent text box control allows you to customize the dimensions, allowing the text box to apply  any scenario.

[] 

Properties

 

  ------- -------------------------------------------------- ---------------------- ------------------ ------------
  Name    Description                                        Type of the property   Value it accepts   Dependency
  Width   Sets the width of the percent text box in pixels   Unit                   Numeric            NA
  ------- -------------------------------------------------- ---------------------- ------------------ ------------

 

Using Builder

The following steps, guides you in configuring the dimensions through the Builder:

1.   In **View**, invoke the Percent textbox helper with the control ID as the first argument and enable the **Width** method with the desired option as argument.

[[ [] ]]{.underline}  

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                  |
|                                                                                                                                                                     |
| [  ] [\<%] [{]                      |
|                                                                                                                                                                     |
| [        Html.MobSyncfusion().PercentTextbox([\"WebsitePercent\"]).Width(100)]                          |
|                                                                                                                                                                     |
| [                          .Render();]                                                                                          |
|                                                                                                                                                                     |
| [                      }[%\>]]                                                                      |
|                                                                                                                                                                     |
| **[\[Razor\]]**                                                                                                                 |
|                                                                                                                                                                     |
| [\@{] []                                                                |
|                                                                                                                                                                     |
| [     Html.MobSyncfusion().PercentTextbox([\"WebsitePercent\"]).Width(100)]                             |
|                                                                                                                                                                     |
| [                          .Render();]                                                                                          |
|                                                                                                                                                                     |
| [                      [}]] [] |
|                                                                                                                                                                     |
| []                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[[]]{.underline}  

2.   Run the application.

 

Using Properties Model

The following steps will guide you in setting the width through the Properties model:

1.   In the **Controller**, create an instance of MobPercentModel, define the **Width** property and pass the instance through ViewData to View as given below:

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                           |
| [public] [ [ActionResult] Index()]                                                                                                           |
|                                                                                                                                                                                                                                                           |
| [        {]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                           |
| [            ] [PercentTextBoxModel] [ myModel = [new][PercentTextBoxModel] ();] |
|                                                                                                                                                                                                                                                           |
| [            myModel.Width = 100;]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| [            ViewData\[[\"myPercent\"]\] = myModel;]                                                                                                                                          |
|                                                                                                                                                                                                                                                           |
| [            [return] View();] [        }] []                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]**  

2.   In **View**, invoke the Percent textbox helper with the ViewData key as the first argument.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                             |
|                                                                                                                                                                                |
| [  ] [\<%] [{                                ] |
|                                                                                                                                                                                |
| [    Html.MobSyncfusion().PercentTextbox([\"myPercent \")]]                                                        |
|                                                                                                                                                                                |
| [                          .Render();]                                                                                                     |
|                                                                                                                                                                                |
| [       }[%\>]]                                                                                                |
|                                                                                                                                                                                |
| **[\[Razor\]]**                                                                                                                            |
|                                                                                                                                                                                |
| [    ] [\@{] []                                |
|                                                                                                                                                                                |
| [           Html.MobSyncfusion().PercentTextbox ([\"myPercent \"])]                                                |
|                                                                                                                                                                                |
| [                          .Render();]                                                                                                     |
|                                                                                                                                                                                |
| [       [}]] []                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


{border="0"}Note: The second argument of the above percent textbox helper should match the view data key from the controller to fetch the properties.


3.   Run the application.

The following screenshot illustrates the output:

 

{border="0"}

Figure 242 Percent textbox with Customized width

[] 

[]{#related-topics}

