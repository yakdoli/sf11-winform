---
title: throughrollinggaugemodel2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Gauge\throughrollinggaugemodel2.md
created_at: 2025-07-03
---






##### Through RollingGaugeModel {#through-rollinggaugemodel style="tab-stops: 0pt"}

[] 

Step 1:

View:

 

Add the below code in the aspx file. Here we are adding the text box for updating the gauge unit value dynamically in its keyup event.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[ASPX\]]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                           |
| [\<%][\--Rendering the rolling gauge\--][%\>][] |
|                                                                                                                                                                                                                                                           |
| [     [\<%][=]Html.Syncfusion().RollingGauge([\"Gauge\"], [\"GaugeModel\"])[%\>]]        |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| [    [\<%][\--Adding the text box for updating the gauge unit value in its keyup event\--][%\>]]                                    |
|                                                                                                                                                                                                                                                           |
| [    [\<%][=]Html.TextBox([\"Unit\"], [\"KM\"])[%\>]]                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[cshtml\]]                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                               |
| [@\*][\--Rendering the rolling gauge\--][\*@][]                                                                                     |
|                                                                                                                                                                                                                                                                                                                                               |
| [     ][@][Html.Syncfusion().RollingGauge([\"Gauge\"], [\"GaugeModel\"])][] |
|                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                               |
| [    [@\*][\--Adding the text box for updating the gauge unit value in its keyup event\--][\*@]]                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                               |
| [   [@]Html.TextBox([\"Unit\"], [\"KM\"])[]]                                                                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

**[]** 

Step 2:

[] 

Add the below script in the same aspx file.

In the below code, you are binding the **UpdateUnitValue** function with the keyup event of the textbox. In the UpdateUnitValue  function, you are calling the RollingGauge's clientside **SetUnit** method to update the gauge value dynamically.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                                |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [        \$(document).ready([function] () {]                                                                                                                          |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [        [//Binding the function for changing the gauge value dynamically with the keyup event.]]                                                                |
|                                                                                                                                                                                                                                |
| [            \$([\"#Unit\"]).bind([\"keyup\"], UpdateUnitValue);]                                                                            |
|                                                                                                                                                                                                                                |
| [        });]                                                                                                                                                                              |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [        [//Function to handle the keyup event of textbox.]]                                                                                                     |
|                                                                                                                                                                                                                                |
| [        [function] UpdateUnitValue() {]                                                                                                                              |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [            [//Gets the current value of the textbox.]]                                                                                                         |
|                                                                                                                                                                                                                                |
| [            [var] val = \$([\"#Unit\"]).val();]                                                                                               |
|                                                                                                                                                                                                                                |
| [            [//Gets the gauge object.]]                                                                                                                         |
|                                                                                                                                                                                                                                |
| [            [var] RollingGaugeObj = \$find([\'Gauge\']);]                                                                                     |
|                                                                                                                                                                                                                                |
| [            [//Calling the ]SetUnit[ function to update the rolling gauge value.]]                                                    |
|                                                                                                                                                                                                                                |
| [            RollingGaugeObj.SetUnit(val);]                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [            ]                                                                                                                                                                             |
|                                                                                                                                                                                                                                |
| [    [\</][script][\>]]                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Step 3:

Controller:

 

Add the code below in the controller. The **Unit** property is used to set the unit value for the Rolling Gauge.

 

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
| [            roll_Gauge.Value = [\"100\"];]                                                                             |
|                                                                                                                                                                                     |
| []                                                                                                                                              |
|                                                                                                                                                                                     |
| [            [//Setting the unit value for the rolling gauge.]]                                                           |
|                                                                                                                                                                                     |
| [            roll_Gauge.Unit = [\"KM\"];]                                                                               |
|                                                                                                                                                                                     |
| [            roll_Gauge.Height = 50;]                                                                                                           |
|                                                                                                                                                                                     |
| [            roll_Gauge.GaugeSkins = [GaugeSkins].VS2010;]                                                              |
|                                                                                                                                                                                     |
| [            roll_Gauge.SegmentCount = 3;]                                                                                                      |
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

[] 

Step 4:

 Run the code to achieve the below output.

 

{border="0"}

Figure 150: Dynamic Updation of Unit**[]**

[                                                           ]


 

{border="0"} Note: Change the unit value in the textbox, to update the rolling gauge unit value.

 


[]{#related-topics}

