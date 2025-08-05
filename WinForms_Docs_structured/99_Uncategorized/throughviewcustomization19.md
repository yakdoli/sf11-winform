---
title: throughviewcustomization19.md
original_path: WinForms_Docs/99_Uncategorized/throughviewcustomization19.md
created_at: 2025-08-05
---






##### Through View Customization {#through-view-customization style="tab-stops: 0pt"}

[] 

Step 1:

View:

 

Add the below code in the aspx file.

 

The **Value** property is used to set the value for the Rolling Gauge. Here you are adding the text box for updating the gauge value dynamically in its keyup event.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[ASPX\]]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                   |
| [\<%][\--Rendering the rolling gauge\--][%\>][]                                         |
|                                                                                                                                                                                                                                                                                                   |
| [    [\<%][=]Html.Syncfusion().RollingGauge([\"Gauge\"])]                                                                                                                            |
|                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                   |
| [            [//Specifying the value for the gauge]]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                   |
| [         .Value([\"Gauge\"])]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                   |
| [          .SegmentCount(5)]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                   |
| [         .GaugeSkins([GaugeSkins].VS2010)]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                   |
| [  .Height(50)]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                   |
| [         ]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                   |
| [    [%\>]]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                   |
| [\<%][\--Adding the text box for updating the gauge value in its keyup event\--][%\>][] |
|                                                                                                                                                                                                                                                                                                   |
| [    [\<%][=]Html.TextBox([\"Value\"], [\"Gauge\"])[%\>]]                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[cshtml\]]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                   |
| [@\*][\--Rendering the rolling gauge\--][\*@][]                                         |
|                                                                                                                                                                                                                                                                                                   |
| [    [\@{] Html.Syncfusion().RollingGauge([\"Gauge\"])]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                   |
| [            [//Specifying the value for the gauge]]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                   |
| [         .Value([\"Gauge\"])]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                   |
| [          .SegmentCount(5)]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                   |
| [         .GaugeSkins([GaugeSkins].VS2010)]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                   |
| [  .Height(50).Render();]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                   |
| [         ]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                   |
| [    [}]]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                   |
| [@\*][\--Adding the text box for updating the gauge value in its keyup event\--][\*@][] |
|                                                                                                                                                                                                                                                                                                   |
| [    [@]Html.TextBox([\"Value\"], [\"Gauge\"])]                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Step 2:

 

Controller:

[] 

Add the below script in the same aspx file.

In the below code, you are binding the **UpdateGaugeValue** function with the keyup event of the textbox. In **UpdateGaugeValue()** function, you are calling the RollingGauge clientside **SetValue** method to update the gauge value dynamically.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [        \$(document).ready([function] () {]                                                                                                                          |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [        [//Binding the function for changing the gauge value dynamically with the keyup event.]]                                                                |
|                                                                                                                                                                                                                                |
| [            \$([\"#Value\"]).bind([\"keyup\"], UpdateGaugeValue);]                                                                          |
|                                                                                                                                                                                                                                |
| [        });]                                                                                                                                                                              |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [        [//Function to handle the keyup event of textbox.]]                                                                                                     |
|                                                                                                                                                                                                                                |
| [        [function] UpdateGaugeValue() {]                                                                                                                             |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [            [//Gets the current value of the textbox.]]                                                                                                         |
|                                                                                                                                                                                                                                |
| [            [var] val = \$([\"#Value\"]).val();]                                                                                              |
|                                                                                                                                                                                                                                |
| [            [//Gets the gauge object.]]                                                                                                                         |
|                                                                                                                                                                                                                                |
| [            [var] RollingGaugeObj = \$find([\'Gauge\']);]                                                                                     |
|                                                                                                                                                                                                                                |
| [            [//Calling the SetValue function to update the rolling gauge value.]]                                                                               |
|                                                                                                                                                                                                                                |
| [            RollingGaugeObj.SetValue(val);]                                                                                                                                               |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [            ]                                                                                                                                                                             |
|                                                                                                                                                                                                                                |
| [    [\</][script][\>]]                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

Step 2:

Controller:

 

Add the code below in the controller

 

+----------------------------------------------------------------------------------------------------------------------------+
| **[]**                                                                                 |
|                                                                                                                            |
| [        [public] [ActionResult] Index()] |
|                                                                                                                            |
| [        {]                                                                            |
|                                                                                                                            |
| [            [return] View();]                                    |
|                                                                                                                            |
| [        }]                                                                            |
+----------------------------------------------------------------------------------------------------------------------------+

[] 

Step 4:

 

Run the code to achieve the following output.

 

{border="0"}

Figure 147: Dynamic Updation of Value**[]**


 

{border="0"} Note: Change the value in the textbox, to update the rolling gauge value.


**[]** 

[]{#related-topics}

