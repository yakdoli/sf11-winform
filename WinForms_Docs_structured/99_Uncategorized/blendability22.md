---
title: blendability22.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\blendability22.md
created_at: 2025-07-03
---






#### Blendability {#blendability style="tab-stops: 0pt"}

You can edit the PercentTextBox Template to give a nice look and feel by using Expression Blend.

The steps to edit the PercentTextBox Template by using Expression Blend are as follows:

1.  Create a simple WPF application in Expression Blend.

2.   Drag and drop the **PercentTextBox** into the application from the Assets tab.

[] 

{border="0"}

 

Figure 797: Expression Blend -- Design View

[] 

3.   After creating the PercentTextBox, select the **PercentTextBox** and navigate to **Object -\> Edit Style -\> Edit a Copy**, to edit the Template of the PercentTextBox.

[] 

{border="0"}

 

Figure 798: Expression Blend -- Edit Template

[] 

Another way to edit the Template is as follows:[]

4.   In Object and Timeline, right-click the PercentTextBox control and select the Edit Template option, as displayed below.

[] 

{border="0"}

 

Figure 799: Expression Blend -- Edit Template

[] 

This will open a dialog (below) where you can give your style a name and define exactly where you'd like to store it.

[] 

{border="0"}

 

Figure 800: Expression Blend -- Create Style Resource

[] 

The result of these steps is an XAML, which is placed within your application. This XAML represents the default style for the PercentTextBox.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<][syncfusion][:][PercentTextBox][ x][:][Name][=\"percentTextBox\"][ Height][=\"25\"][ Width][=\"150\"][ ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [                           [ CornerRadius][=\"2\"][ Style][=\"{][StaticResource][ ]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [                            PercentTextBoxStyle1][}\"/\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

All template items can now be found in the Objects and Timeline window.

 

{border="0"}

 

Figure 801: Expression Blend -- Objects and Timeline

 

Now you can replace the existing Template setter and Triggers with your own creation. In the Triggers tab you can select the Trigger and customize it as you want.

{border="0"}

 

Figure 802: Triggers

 

Here is a simple example to customize the UnFocused state of the PercentTextBox:

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<][Trigger][ Property][=\"IsFocused\"][ Value][=\"False\"\>][]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [    ][\<][Setter][ Property][=\"Background\"][ TargetName][=\"Border\"][ Value][=\"LightGray\"/\>][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\</][Trigger][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

When the control loses its focus, the Background color is set to LightGray. Similarly, you can customize every state and property in Expression Blend.

 

{border="0"}

 

Figure 803: UnFocused Style

 

 

{border="0"}

 

Figure 804: Focused Style

[]{#related-topics}

