---
title: scrollersframe1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\scrollersframe1.md
created_at: 2025-07-03
---






#### ScrollersFrame {#scrollersframe style="tab-stops: 0pt"}

[] 

The ScrollersFrame control attaches Office2007 Style scrollbars to any scrollable control or container.

[] 

{border="0"}

[] 

Figure 1411: Office2007Style ScrollBars Attached to TreeViewControl

 

Attaching Scrollbar to a Control

 

To the Windows form, add a control, which should be attached with the Office2007Style scrollbars. Select the control in the ScrollersFrame.AttachedTo property.

[] 

{border="0"}

[] 

***[]*** 

Figure 1412: Selecting the TreeViewAdv control through AttachedTo Property

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                             |
|                                                                                                                                                                                                            |
| []                                                                                                                                                        |
|                                                                                                                                                                                                            |
| [//Attaching Scrolls using AttachedTo property]                                                                                                          |
|                                                                                                                                                                                                            |
| [this][.scrollersFrame1.AttachedTo = [this].treeViewAdv1;][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                    |
|                                                                                                                                                                                                       |
| []                                                                                                                                                  |
|                                                                                                                                                                                                       |
| [\'Attaching Scrolls using AttachedTo property]                                                                                                     |
|                                                                                                                                                                                                       |
| [Me][.scrollersFrame1.AttachedTo = [Me].treeViewAdv1][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"} Note: This property lists all the controls that are added to the form. User can the select any one control, for which scrolls needs to be attached.


[] 

See Also

[] 

[[Adding Controls to the ScrollBar]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Adding_Controls_to_1)[, ]{.UGHyperlink}[[Scroll Settings]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Scroll_Settings_in)[, ]{.UGHyperlink}[[Visual Styles]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Visual_Styles_1)[]{.UGHyperlink}

 

 

More:









