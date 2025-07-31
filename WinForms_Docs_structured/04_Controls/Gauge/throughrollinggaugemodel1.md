---
title: throughrollinggaugemodel1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Gauge\throughrollinggaugemodel1.md
created_at: 2025-07-03
---






##### Through RollingGaugeModel {#through-rollinggaugemodel style="tab-stops: 0pt"}

[] 

Step 1:

View:

**[]** 

Add the below code in the aspx file. Here you are adding the text box for updating the gauge value dynamically in its keyup event.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[ASPX\]]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                               |
| [\<%][\--Rendering the rolling gauge\--][%\>][]                     |
|                                                                                                                                                                                                                                                                               |
| [     [\<%][=]Html.Syncfusion().RollingGauge([\"Gauge\"], [\"GaugeModel\"])[%\>]]                            |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                               |
| [    [\<%][\--Adding the text box for updating the gauge value in its keyup event\--][%\>]]                                                             |
|                                                                                                                                                                                                                                                                               |
| [    [\<%][=]Html.TextBox([\"][Value][\"], [\"Gauge\"])[%\>]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[cshtml\]]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                    |
| [@\*][\--Rendering the rolling gauge\--][\*@][]                                          |
|                                                                                                                                                                                                                                                                                                    |
| [@][Html.Syncfusion().RollingGauge([\"Gauge\"], [\"GaugeModel\"])][] |
|                                                                                                                                                                                                                                                                                                    |
| [  ]                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                    |
| [    [@\*][\--Adding the text box for updating the gauge value in its keyup event\--][\*@]]                                                                                  |
|                                                                                                                                                                                                                                                                                                    |
| [    [@]Html.TextBox([\"][Value][\"], [\"Gauge\"])[]]                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Step 2:

 

Controller:

[] 

Add the below script in the same aspx file.

 

In the below code, you are binding **UpdateGaugeValue** function with the keyup event of the textbox. In the **UpdateGaugeValue()** function, you are calling the RollingGauge clientside **SetValue** method to update the gauge value dynamically.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                           |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                           |
| [        \$(document).ready([function] () {]                                                                                                                                            |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                           |
| [        [//Binding the function for changing the gauge value dynamically with the keyup event.]]                                                                                  |
|                                                                                                                                                                                                                                                           |
| [            \$([\"#Value\"]).bind([\"keyup\"], UpdateGaugeValue);]                                                                                            |
|                                                                                                                                                                                                                                                           |
| [        });]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                           |
| [        [//Function to handle the keyup event of textbox.]]                                                                                                                       |
|                                                                                                                                                                                                                                                           |
| [        [function] UpdateGaugeValue() {]                                                                                                                                               |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                           |
| [            [//Gets the current value of the textbox.]]                                                                                                                           |
|                                                                                                                                                                                                                                                           |
| [            [var] val = \$([\"#Value\"]).val();]                                                                                                                |
|                                                                                                                                                                                                                                                           |
| [            [//Gets the gauge object.]]                                                                                                                                           |
|                                                                                                                                                                                                                                                           |
| [            [var] RollingGaugeObj = \$find([\'Gauge\']);]                                                                                                       |
|                                                                                                                                                                                                                                                           |
| [            [//Calling the SetValue function to update the rolling gauge value.]]                                                                                                 |
|                                                                                                                                                                                                                                                           |
| [            RollingGaugeObj.SetValue(val);]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                           |
| [        }]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                           |
| [            ]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                           |
| [    [\</][script][\>]]                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Step 3:

Controller:

 

Add the code below in the controller. The **Value** property is used to set the value for the Rolling Gauge.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                              |
|                                                                                                                                                                                     |
| [public][ [ActionResult] Index()]                                      |
|                                                                                                                                                                                     |
| [        {]                                                                                                                                     |
|                                                                                                                                                                                     |
| [           [RollingGaugeModel] roll_Gauge = [new] [RollingGaugeModel]();] |
|                                                                                                                                                                                     |
| []                                                                                                                                              |
|                                                                                                                                                                                     |
| [            [//Setting the value for the rolling gauge.]]                                                                |
|                                                                                                                                                                                     |
| [            roll_Gauge.Value = [\"Gauge\"];]                                                                           |
|                                                                                                                                                                                     |
| [            roll_Gauge.Height = 50;]                                                                                                           |
|                                                                                                                                                                                     |
| [            roll_Gauge.GaugeSkins = [GaugeSkins].VS2010;]                                                              |
|                                                                                                                                                                                     |
| [            roll_Gauge.SegmentCount = 5;]                                                                                                      |
|                                                                                                                                                                                     |
| []                                                                                                                                              |
|                                                                                                                                                                                     |
| [            ViewData\[[\"GaugeModel\"]\] = roll_Gauge;]                                                                |
|                                                                                                                                                                                     |
| [            [return] View();]                                                                                             |
|                                                                                                                                                                                     |
| []                                                                                                                                              |
|                                                                                                                                                                                     |
| [        }]                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Step 4:

Run the code to achieve the below output.

 

{border="0"}

Figure 148: Dynamic Updation of Value

**[]** 


{border="0"} Note: Change the value in the textbox, to update the rolling gauge value.


[]{#related-topics}

