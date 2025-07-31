---
title: frequentlyaskedquestions31.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\frequentlyaskedquestions31.md
created_at: 2025-07-03
---






##### Frequently Asked Questions {#frequently-asked-questions style="tab-stops: 0pt"}

[] 

This section discusses the following topics.

[] 

###### []{#p448}[]{#_How_to_create}3.3.6.1.5.1 How to create a transparent popup? {#how-to-create-a-transparent-popup style="tab-stops: 0pt"}

[] 

This can be done using the below code snippet.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                       |
| [private][ [void] popupControlContainer1_BeforePopup([object] sender, System.ComponentModel.[CancelEventArgs] e)] |
|                                                                                                                                                                                                                                                                       |
| [{]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                       |
| [      [// Get the popupHost which is used to host the popupControlContainer]]                                                                                                                              |
|                                                                                                                                                                                                                                                                       |
| [      [// and set the opacity.]]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                       |
| [      [this].popupControlContainer1.PopupHost.Opacity = 0.75;]                                                                                                                                              |
|                                                                                                                                                                                                                                                                       |
| [}]                                                                                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                             |
| [Private][ [Sub] popupControlContainer1_BeforePopup([ByVal] sender [As] [Object], [ByVal] e [As] System.ComponentModel.CancelEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                             |
| [      [\'Get the popupHost which is used to host the popupControlContainer]]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                             |
| [      [\'and set the opacity.]]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                             |
| [      [Me].popupControlContainer1.PopupHost.Opacity = 0.75]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                             |
| [End][ [Sub]]                                                                                                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

###### []{#p449}3.3.6.1.5.2 How to identify whether the popup is currently dropped down {#how-to-identify-whether-the-popup-is-currently-dropped-down style="tab-stops: 0pt"}

[] 

PopupControlContainer.IsShowing() method returns whether the popup is currently dropped down or not.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                          |
|                                                                                                                                                                         |
| []                                                                                                                                              |
|                                                                                                                                                                         |
| [this][.popupControlContainer1.IsShowing()][;] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                             |
|                                                                                                                                |
| []                                                                                                     |
|                                                                                                                                |
| [Me][.popupControlContainer1.IsShowing()] |
+--------------------------------------------------------------------------------------------------------------------------------+

###### []{#_How_to_show}3.3.6.1.5.3 How to show PopupControlContainer as the popup for a RichTextBox control {#how-to-show-popupcontrolcontainer-as-the-popup-for-a-richtextbox-control style="tab-stops: 0pt"}

[]{#p450}[] 

This is done by calling the ShowPopup method of PopupControlContainer control.

[] 

[·      ]Add a RichTextBox control onto the form.

[·      ]Associate it with the **ParentControl** property of PopupControlContainer as follows.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                 |
|                                                                                                                                                                                |
| []                                                                                                                                                     |
|                                                                                                                                                                                |
| [this][.popupControlContainer1.ParentControl = [this].richTextBox1;] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                        |
|                                                                                                                                                                           |
| []                                                                                                                                                |
|                                                                                                                                                                           |
| [Me][.popupControlContainer1.ParentControl = [Me].richTextBox1] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]To display the Popup at a desired location, handle **RichTextBox.MouseUp** event and call **ShowPopup()** method of PopupControlContainer as follows. The below code displays the popup just below the RichTextBox control, when the user clicks.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                 |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                |
| [this][.richTextBox1.MouseUp +=[new] [MouseEventHandler](richTextBox_MouseUp);]                 |
|                                                                                                                                                                                                                                |
| [private][ [void] richTextBox1_MouseUp([object] sender, System.Windows.Forms.MouseEventArgs e)] |
|                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                |
| [this][.popupControlContainer1.ShowPopup(Point.Empty);]                                                                                   |
|                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                             |
| [Private][ [Sub] richTextBox1_MouseUp([ByVal] sender [As] [Object], [ByVal] e [As] System.Windows.Forms.MouseEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                             |
| [    [Me].popupControlContainer1.ShowPopup(Point.Empty)]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                             |
| [End][ [Sub]]                                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

We can also display the popup at particular location.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                     |
|                                                                                                                                                                                                    |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                    |
| [this][.popupControlContainer1.ShowPopup([new] [Point](100, 100));] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                              |
|                                                                                                                                                                                                 |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                 |
| [Me][.popupControlContainer1.ShowPopup([new] [Point](100, 100))] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

At run time, right click on RichTextBox, the popup will be shown below the RichTextBox as in the below image.

[] 

{border="0"}

[] 

Figure 386: PopupControlContainer as popup for RichTextBox Editor

 

###### []{#_When_Two_PopUpControl}3.3.6.1.5.4 When Two PopUpControl Containers are Opened at the Same Time Controls like the ComboDropDown Close by Itself. {#when-two-popupcontrol-containers-are-opened-at-the-same-time-controls-like-the-combodropdown-close-by-itself. style="tab-stops: 0pt"}

###### 3.3.6.1.5.5 How to Get Around this Behavior? {#how-to-get-around-this-behavior style="tab-stops: 0pt"}

[]{#p451}[] 

In order to workaround this behavior, you can set a boolean flag and cancel the BeforeCloseUp event as shown below.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                           |
| [private bool][ bool1;]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                           |
| [  ]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                           |
| [private void][ PopupContainer_Popup(][object][ sender, EventArgs e)]               |
|                                                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                           |
| [     bool1= ][true][;]                                                                                                              |
|                                                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                           |
| [private void][ PopupContainer_BeforeCloseUp(][object][ sender, CancelEventArgs e)] |
|                                                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                           |
| [if][(bool1)]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                           |
| [e.Cancel = ][true][;]                                                                                                               |
|                                                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                           |
| [private void][ comboDropDown1_LostFocus(][object][ sender, EventArgs e)]           |
|                                                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                           |
| [bool1= ][false][;]                                                                                                                  |
|                                                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                           |
| [private void][ Form1_Click(][object][ sender, EventArgs e)]                        |
|                                                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                           |
| [bool1= ][false][;]                                                                                                                  |
|                                                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Private][ bool1 ][As Boolean ]                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Private Sub][ PopupContainer_Popup(][ByVal][ sender ][As Object][, ][ByVal][ e ][As][ EventArgs) ]               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [      bool1 = ][True][ ]                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [End Sub ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Private Sub][ PopupContainer_BeforeCloseUp(][ByVal][ sender ][As Object][, ][ByVal][ e ][As][ CancelEventArgs) ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [      ][If][ bool1 ][Then][ ]                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [          e.Cancel = ][True][ ]                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [      ][End If ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [End Sub ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Private Sub][ comboDropDown1_LostFocus(][ByVal][ sender ][As Object][, ][ByVal][ e ][As][ EventArgs) ]           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [      bool1 = ][False][ ]                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [End Sub]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Private Sub][ Form1_Click(][ByVal][ sender ][As Object][, ][ByVal][ e ][As][ EventArgs) ]                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [      bool1 = ][False][ ]                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [End Sub ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

You can set the Boolean value to be false under the Form\'s Click event and Control\'s LostFocus event so that the DropDown closes for rest of the cases.

[]{#related-topics}

