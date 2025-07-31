---
title: range6.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\range6.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Range {#range style="tab-stops: 0pt"}

The Percent text box supports defining range of values for the control to accept and display.

[] 

Properties

  --------------- ------------------------------------------------------------------------------------------------------ ---------------------- ------------------------------------ ------------
  Name            Description                                                                                            Type of the property   Value it accepts                     Dependency
  MinValue        Sets the minimum value.                                                                                double                 double.MinValue to double.MaxValue   NA
  MaxValue        Sets the maximum value                                                                                 double                 double.MinValue to double.MaxValue   NA
  IncrementStep   Sets the step value by which the text box value increases or decreases when spin buttons are clicked   float                  float.MinValue to float.MaxValue     NA
  --------------- ------------------------------------------------------------------------------------------------------ ---------------------- ------------------------------------ ------------

 

Using Builder

The following steps, guides you in configuring the range through the Builder:

1.   In **View**, invoke the Percent textbox helper with the control ID as the first argument and enable the **MinValue**, **MaxValue**, and **IncrementStep** methods with the desired argument.

[[ [] ]]{.underline}  

+------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                             |
|                                                                                                                                                |
| [  ] [\<%] [{] |
|                                                                                                                                                |
| [        Html.MobSyncfusion().PercentTextbox([\"WebsitePercent\"])]                |
|                                                                                                                                                |
| [                   .MinValue(50)]                                                                         |
|                                                                                                                                                |
| [                   .Maxvalue(300)]                                                                        |
|                                                                                                                                                |
| [                   .IncrementStep(10)]                                                                    |
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
| [                   .MinValue(50)]                                                                         |
|                                                                                                                                                |
| [                   .Maxvalue(300)]                                                                        |
|                                                                                                                                                |
| [                   .IncrementStep(10)]                                                                    |
|                                                                                                                                                |
| []                                                                                                         |
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

The following steps will guide you in setting the range through the Properties model:

1.   In the **Controller**, create an instance of PercentTextBoxModel; define the **MinValue**, **MaxValue**, and **IncrementStep** properties, and pass the instance through the view-specific data to the view.[]

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                         |
| [public] [ [ActionResult] Index()]                                                                                                         |
|                                                                                                                                                                                                                                                         |
| [        {]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                         |
| [           ] [PercentTextBoxModel] [ myModel = [new][PercentTextBoxModel]();] |
|                                                                                                                                                                                                                                                         |
| [            myModel.MinValue = 50;]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                         |
| [            myModel.MaxValue = 100;]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                         |
| [            myModel.IncrementStep = 10;]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                         |
| [            ViewData\[[\"myPercent\"]\] = myModel;]                                                                                                                                        |
|                                                                                                                                                                                                                                                         |
| [            [return] View();]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]**  

2.   In **View**, invoke the Percent textbox helper with the ViewData key as first argument.

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


{border="0"}Note: The second argument of the above percent textbox helper should match the view data key from the controller to fetch the properties.


3.   Run the application.

The following screenshot illustrates the output:

 

{border="0"}

Figure 243 Percent textbox with Customized Range

 

[]{#related-topics}

