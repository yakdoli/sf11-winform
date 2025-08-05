---
title: textselection1.md
original_path: WinForms_Docs/99_Uncategorized/textselection1.md
created_at: 2025-08-05
---








  









## Text Selection[] {#text-selection style="tab-stops: 0pt"}

 

An interesting feature of the HTMLUI control is its ability to access the selected text. This feature helps the user to select required texts available in the HTMLUI control and use the selected text in the applications. The **SelectedText** property of the HTMLUI control is used for this purpose.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                         |
|                                                                                                                                                                                                        |
| **[]**                                                                                                                               |
|                                                                                                                                                                                                        |
| [// Return the selected text displayed in  the control]                                                                              |
|                                                                                                                                                                                                        |
| [this][.label1.Text = [this].htmluiControl1.SelectedText;  ] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                              |
|                                                                                                                                                                                                 |
| **[]**                                                                                                                        |
|                                                                                                                                                                                                 |
| [\' Return the selected text displayed in the control]                                                                        |
|                                                                                                                                                                                                 |
| [Me][.label1.Text = [Me].HtmluiControl1.SelectedText] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

CopyTextToClipBoard

[] 

The HTMLUI control allows the user to copy the text selected in the HTMLUI control to the Clipboard, and paste it in other applications. The following code snippet shows how this feature is implemented with the HTMLUI control.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                            |
|                                                                                                                                                                                                           |
| **[]**                                                                                                                                  |
|                                                                                                                                                                                                           |
| [string][ text = [this].htmluiControl.SelectedText.ToString();] |
|                                                                                                                                                                                                           |
| [if][ (text != [\"\"])]                                      |
|                                                                                                                                                                                                           |
| [{]                                                                                                                                                   |
|                                                                                                                                                                                                           |
| [//Copying the selected text to the ClipBoard]                                                                                          |
|                                                                                                                                                                                                           |
| [Clipboard][.SetDataObject(text);]                                                |
|                                                                                                                                                                                                           |
| [}  ]                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                 |
| [Private][ text [As] [String] = [Me].htmluiControl.SelectedText.ToString()] |
|                                                                                                                                                                                                                                                                 |
| [If][ text \<\> [\"\"] [Then]]                                                                |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                 |
| [\' Copying the selected text to the ClipBoard]                                                                                                                                               |
|                                                                                                                                                                                                                                                                 |
| [Clipboard.SetDataObject(text)]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                 |
| [End][ [If]]                                                                                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p179} 

More:





