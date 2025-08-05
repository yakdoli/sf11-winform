---
title: blendability21.md
original_path: WinForms_Docs/99_Uncategorized/blendability21.md
created_at: 2025-08-05
---






#### Blendability {#blendability style="tab-stops: 0pt"}

You can edit the MaskedTextBox Template to give a nice look and feel by using Expression Blend.

The steps to edit the MaskedTextBox Template by using Expression Blend are as follows:

1.   Create a simple WPF application in Expression Blend.

2.   Drag and drop the **MaskedTextBox** into the application from the Assets tab.

[] 

{border="0"}

 

Figure 692: Expression Blend -- Design View

[] 

3.   After creating the MaskedTextBox, select the **MaskedTextBox** and navigate to **Object -\> Edit Style -\> Edit a Copy**, to edit the Template of the MaskedTextBox.

[] 

{border="0"}

 

Figure 693: Expression Blend - Edit Template

[] 

Another way to the edit the Template is as follows:

4.   In Object and Timeline, right-click the **MaskedTextBox** control and select the **Edit Template** option, as displayed below.

[] 

{border="0"}

Figure 694: Expression Blend - Edit Template[]

This will open a dialog (below) where you can give your style a name and define exactly where you'd like to store it.

[] 

{border="0"}

Figure 695: Expression Blend -- Create Style Resource[]

[] 

The result of these steps is an XAML, which is placed within your application. This XAML represents the default style for the MaskedTextBox.

[] 

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<][syncfusion][:][MaskedTextBox][ x][:][Name][=\"maskedTextBox\"][ Width][=\"150\"][ Height][=\"25\"][ ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [                          Mask][=\"00/00/0000 00:00\"][ CornerRadius][=\"4\"][ ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [                          Style][=\"{][DynamicResource][ MaskedTextBoxStyle1][}\"/\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

All template items can now be found in the Objects and Timeline window.

[] 

{border="0"}

Figure 696: Expression Blend -- Objects and Timeline

 

Now you can replace the existing Template setter and Triggers with your own creation. In the Triggers tab you can select the Trigger and customize it as you want.

[] 

{border="0"}

Figure 697: Triggers

 

Here is a simple example to customize the Focused state of the MaskedTextBox:

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<][Trigger][ Property][=\"IsFocused\"][ Value][=\"True\"\>][]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [    ][\<][Setter][ TargetName][=\"MouseOver_Border\"][ Property][=\"Visibility\"][ Value][=\"Collapsed\"/\>][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [    ][\<][Setter][ TargetName][=\"Focused_Border\"][ Property][=\"Visibility\"][ Value][=\"Visible\"/\>][]     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [    ][\<][Setter][ Property][=\"Background\"][ Value][=\"LightBlue\"/\>][]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\</][Trigger][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

When a control lost the Focus, the Background color of the MaskedTextBox will change to LightGray. Similarly, you can customize every state and property in Expression Blend.

{border="0"}

Figure 698: UnFocused Style

{border="0"}

Figure 699: Focused Style

[]{#related-topics}

