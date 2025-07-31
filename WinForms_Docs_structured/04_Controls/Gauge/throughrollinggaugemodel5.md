---
title: throughrollinggaugemodel5.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Gauge\throughrollinggaugemodel5.md
created_at: 2025-07-03
---






##### Through RollingGaugeModel {#through-rollinggaugemodel style="tab-stops: 0pt"}

[] 

Step 1:

View:

 

Add the below code in the aspx file. Here you are adding the dropdown list for dynamically updating the gauge unit position in its change event.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[ASPX\]]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                    |
| [     [\<%][\--Rendering the rolling gauge\--][%\>]]                                                                         |
|                                                                                                                                                                                                                                                    |
| [    ]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                    |
| [     [\<%][=]Html.Syncfusion().RollingGauge([\"Gauge\"], [\"GaugeModel\"])[%\>]] |
|                                                                                                                                                                                                                                                    |
| [    [\<%][\--Adding the dropdown list for updating the gauge unit position in its change event\--][%\>]]                    |
|                                                                                                                                                                                                                                                    |
| [    [\<%][=]Html.DropDownList([\"UnitPosition\"])[%\>]]                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[cshtml\]]                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                            |
| [     [@\*][\--Rendering the rolling gauge\--][\*@]]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                            |
| [  ][@][Html.Syncfusion().RollingGauge([\"Gauge\"], [\"GaugeModel\"])][] |
|                                                                                                                                                                                                                                                                                                                                            |
| [  ]                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                            |
| [    [@\*][\--Adding the dropdown list for updating the gauge unit position in its change event\--][\*@]]                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                            |
| [    [@]Html.DropDownList([\"UnitPosition\"])[]]                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

**[]** 

Step 2:

[] 

Add the below script in the same aspx file.

 

In the below code, you are binding the **UpdateUnitPosition** function with the change event of the dropdown list. In the **UpdateUnitPosition ()** function, you are calling the RollingGauge's clientside **SetUnitPosition** method to update the unitposition dynamically.

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
| [        [//Binding the function for changing the unit position dynamically with the change event.]]                                                             |
|                                                                                                                                                                                                                                |
| [            \$([\"#UnitPosition\"]).bind([\"change\"], UpdateUnitPosition);]                                                                |
|                                                                                                                                                                                                                                |
| [        });]                                                                                                                                                                              |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [        [//Function to handle the change event of dropdown.]]                                                                                                   |
|                                                                                                                                                                                                                                |
| [        [function] UpdateUnitPosition() {]                                                                                                                           |
|                                                                                                                                                                                                                                |
| [           ]                                                                                                                                                                              |
|                                                                                                                                                                                                                                |
| [            [//Gets the current selected value of the dropdown.]]                                                                                               |
|                                                                                                                                                                                                                                |
| [            [var] Position = \$([\"#UnitPosition\"]).val();]                                                                                  |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [            [//Gets the gauge object.]]                                                                                                                         |
|                                                                                                                                                                                                                                |
| [            [var] RollingGaugeObj = \$find([\'Gauge\']);]                                                                                     |
|                                                                                                                                                                                                                                |
| [            [//Calling the SetUnitPosition function to update the rolling gauge unit position.]]                                                                |
|                                                                                                                                                                                                                                |
| [            **RollingGaugeObj.SetUnitPosition(Position);**]                                                                                                                               |
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

Step 3:

Controller:

 

Add the code below in the controller. The **Value** property is used to set the value for the Rolling Gauge.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                              |
|                                                                                                                                                                                              |
| [public][ [ActionResult] Index()]                             |
|                                                                                                                                                                                              |
| [        {]                                                                                                                                     |
|                                                                                                                                                                                              |
| [           [RollingGaugeModel] roll_Gauge = [new] [RollingGaugeModel]();] |
|                                                                                                                                                                                              |
| []                                                                                                                                              |
|                                                                                                                                                                                              |
| [            roll_Gauge.Value = [\"Gauge\"];]                                                                           |
|                                                                                                                                                                                              |
| [            roll_Gauge.Unit = [\"KM\"];]                                                                               |
|                                                                                                                                                                                              |
| [            [//Setting the position of the unit.]]                                                                       |
|                                                                                                                                                                                              |
| **[            roll_Gauge.UnitPosition = [UnitPosition].End;]**                                                         |
|                                                                                                                                                                                              |
| [            roll_Gauge.IsAutomaticSegmentCountEnabled = [true];]                                                          |
|                                                                                                                                                                                              |
| [            roll_Gauge.Height = 50;]                                                                                                           |
|                                                                                                                                                                                              |
| [            roll_Gauge.GaugeSkins = [GaugeSkins].VS2010;]                                                              |
|                                                                                                                                                                                              |
| [            ViewData\[[\"GaugeModel\"]\] = roll_Gauge;]                                                                |
|                                                                                                                                                                                              |
| [            [return] View();]                                                                                             |
|                                                                                                                                                                                              |
| []                                                                                                                                              |
|                                                                                                                                                                                              |
| [        }]                                                                                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Step 4:

Run the code to achieve the below output.

[] 

{border="0"}

Figure 156: Unit Positon**[]**

[                                    ]


{border="0"} Note: Change the dropdown list value for dynamically updating the unit position of the rolling gauge.


[]{#related-topics}

