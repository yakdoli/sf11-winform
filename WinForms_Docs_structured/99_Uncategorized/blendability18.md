---
title: blendability18.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\blendability18.md
created_at: 2025-07-03
---






#### Blendability {#blendability style="tab-stops: 0pt"}

You can edit the CurrencyTextBox Template to give a nice look and feel by using Expression Blend.

The steps to edit the CurrencyTextBox Template by using Expression Blend are as follows:

 

1.   Create a simple WPF application in Expression Blend.

2.   Drag and drop the **CurrencyTextBox** into the application from the Assets tab.

 

{border="0"}

Figure 254: Expression Blend -- Design View[]

3.   After creating the CurrencyTextBox, select the **CurrencyTextBox** and navigate to **Object -\> Edit Style -\> Edit a Copy**, to edit the Template of the CurrencyTextBox.

[] 

{border="0"}

Figure 255: Expression Blend -- Edit Template

[] 

Another way to edit the Template is as follows:

4.   In Object and Timeline, right click the **CurrencyTextBox** control and select the **Edit Template** option, as displayed below.

[] 

{border="0"}

Figure 256: Expression Blend -- Edit Template[]

5.   This will open a dialog (below) where you can give your style a name and define exactly where you'd like to store it.

 

{border="0"}

Figure 257: Expression Blend -- Create Style Resource[]

[] 

The result of these steps is an XAML, which is placed within your application. This XAML represents the default style for the CurrencyTextBox.

 

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [\<][syncfusion][:][CurrencyTextBox][ x][:][Name][=\"currencyTextBox\"][ Height][=\"25\"][ Width][=\"150\"][ Style][=\"{][StaticResource][ CurrencyTextBoxStyle1][}\"/\>]
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 

All template items can now be found in the Objects and Timeline window.

 

{border="0"}

Figure 258: Expression Blend -- Objects and Timeline

Now you can replace the existing Template setter and Triggers with your own creation. In the Triggers tab you can select the Trigger and customize it as you want.

 

{border="0"}

Figure 259: Triggers

[] 

Here is a simple example to customize the UnFocused state of the CurrencyTextBox:

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<][Trigger][ Property][=\"IsFocused\"][ Value][=\"False\"\>][]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    ][\<][Setter][ Property][=\"Background\"][ TargetName][=\"Border\"][ Value][=\"LightGray\"/\>][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\</][Trigger][\>]                                                                                                                                                                                                                                                                                                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

When the control loses its focus, the Background color is set to LightGray. Similarly, you can customize every state and property in Expression Blend.

[] 

{border="0"}

Figure 260: CurrencyTextBox

 

See Also

[]{.UGHyperlink}



 

[]{#related-topics}

