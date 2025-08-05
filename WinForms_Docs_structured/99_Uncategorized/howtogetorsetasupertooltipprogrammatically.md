---
title: howtogetorsetasupertooltipprogrammatically.md
original_path: WinForms_Docs/99_Uncategorized/howtogetorsetasupertooltipprogrammatically.md
created_at: 2025-08-05
---






##### How to get or set a SuperToolTip programmatically? {#how-to-get-or-set-a-supertooltip-programmatically style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

We can get or set the SuperToolTip programmatically using the below two methods.

[] 


  --------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  SuperToolTip Method   Description
  GetToolTip            Gets the ToolTipInfo for any control. If the ToolTip properties change dynamically in an application, you can use this method to find out what information is exhibited at any point, depending upon the state of the application.
  SetToolTip            Sets the ToolTipInfo for any control.
  --------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [private void][ buttonAdv1_Click(][object][ sender, EventArgs e) ]                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [{ ]                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [   ][ // Gets][ the ][text set for][ the ][Body of TextBox tooltip. ] |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [    MessageBox.Show (][this][.superToolTip1.GetToolTip(][this][.textBox1).Body.Text.ToString ()); ]                       |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [}  ]                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [// To add a ToolTip through code. ]                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [this][.superToolTip1.SetToolTip(][this][.textBox1, \"ToolTipText\"); ][]                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p1203}[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Private Sub][ buttonAdv1_Click(][ByVal][ sender ][As Object][, ][ByVal][ e ][As][ EventArgs) ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [  \' Gets the text set for the Body of TextBox tooltip. ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [MessageBox.Show(][Me][.superToolTip1.GetToolTip(][Me][.textBox1).Body.Text.ToString) ]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [End Sub  ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\' To add a ToolTip through code. ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Me][.superToolTip1.SetToolTip(][Me][.textBox1, \"ToolTipText\")][]                                                                                                                                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

**[]** 

Figure 1469: ToolTip Sample

**[]** 

{border="0"}

[] 

Figure 1470: MessageBox Displaying the ToolTipText of the Body part Using GetToolTip Method

**[]** 


[] 

{border="0"} Note: You can also set tooltip using[ ][[UpdateToolTip Event]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_SuperToolTip_Events)[.]


 

 

 

 

[]{#related-topics}

