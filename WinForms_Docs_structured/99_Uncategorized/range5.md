---
title: range5.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\range5.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Range {#range style="tab-stops: 0pt"}

The Numeric text box supports defining a range of value for the control to accept and display.

[] 

Properties

  --------------- ----------------------------------------------------------------------------------------------------------- ---------------------- ------------------------------------ ------------
  Name            Description                                                                                                 Type of the property   Value it accepts                     Dependency
  MinValue        Sets the minimum value                                                                                      double                 double.MinValue to double.MaxValue   NA
  MaxValue        Sets the maximum value                                                                                      double                 double.MinValue to double.MaxValue   NA
  IncrementStep   Sets the step value by which the text box value has to increase or decrease when clicking on spin buttons   float                  float.MinValue to float.MaxValue     NA
  --------------- ----------------------------------------------------------------------------------------------------------- ---------------------- ------------------------------------ ------------

 

Using Builder

The following steps, guides you in configuring the range through Builder:

1.   In **View**, invoke the Numeric textbox helper with the numeric ID as the first argument and enable the **MinValue**, **MaxValue**, and **IncrementStep** methods with desired option as argument.

[[ [] ]]{.underline}  

+------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                             |
|                                                                                                                                                |
| [  ] [\<%] [{] |
|                                                                                                                                                |
| [        Html.MobSyncfusion().NumericTextbox([\"WebsiteNumeric\"])]                |
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
| [     Html.MobSyncfusion().NumericTextbox([\"WebsiteNumeric\"])]                   |
|                                                                                                                                                |
| [                   .MinValue(50)]                                                                         |
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

1.   In the **Controller**, create an instance of NumericTextBoxModel; define the **MinValue**, **MaxValue**, and **IncrementStep** properties, and pass the instance through the view-specific data to the view.[]

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
| [            myModel.MinValue = 50;]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                          |
| [            myModel.MaxValue = 300;]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                          |
| [            myModel.IncrementStep = 10;]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                          |
| [            ViewData\[[\"myNumeric\"]\] = myModel;]                                                                                                                                         |
|                                                                                                                                                                                                                                                          |
| [            [return] View();] [        }]                                                                                                                  |
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
| [       [}]] []              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


{border="0"}Note: The second argument of the above numeric textbox helper should match the view data key from the controller to fetch the properties.


3.   Run the application.

The following screenshot illustrates the output:

 

{border="0"}

Figure 235 Numeric textbox with Customized Range

[]{#related-topics}

