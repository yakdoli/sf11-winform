---
title: htmlelements.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\htmlelements.md
created_at: 2025-07-03
---








  









## HTML Elements {#html-elements style="tab-stops: 0pt"}

[[[]]]{.underline} 

HTMLUI supports various elements in an HTML document for rendering and presenting them to the user and also allows the user to dynamically access the elements to produce rich, customized user interfaces. Each HTML element defines properties and methods which can be used for customization. 

 

The property **SupportedEvents** and the method **MergeSupportedEvents** are common to most HTML elements.

[] 

SupportedEvents

[] 

This property returns an array of events supporting the element.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                    |
| [// SupportedEvents property returns an array of events supporting the element. ]                                                                                                                |
|                                                                                                                                                                                                                                                                    |
| [Hashtable htmlelements = [this].htmluiControl1.Document.GetElementsByUserIdHash();]                                                                                                      |
|                                                                                                                                                                                                                                                                    |
| [BRElementImpl][ br = htmlelements\[[\"br\"]\] [as] [BRElementImpl];] |
|                                                                                                                                                                                                                                                                    |
| [this][.label1.Text = [this].br.SupportedEvents.Length.ToString(); ]                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\' SupportedEvents property returns an array of events supporting the element. ]                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Private][ htmlelements [As] Hashtable = [Me].HtmluiControl1.Document.GetElementsByUserIdHash()]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Private][ tr [As] BRElementImpl = [CType](IIf([TypeOf] htmlelements([\"br\"]) [Is] BRElementImpl, htmlelements([\"br\"]), [Nothing]), BRElementImpl)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Private][ [Me].label1.Text = [Me].br.SupportedEvents.Length.ToString()]                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

MergeSupportedEvents[ ]

[] 

The **MergeSupportedEvents** method is used to merge the standard and special events.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                            |
| [// MergeSupportedEvents method is to merge the standard and special events.]                                                                                                                            |
|                                                                                                                                                                                                                                                                            |
| [Hashtable][ htmlelements = [this].htmluiControl1.Document.GetElementsByUserIdHash();]                                        |
|                                                                                                                                                                                                                                                                            |
| [INPUTElementImpl][ txt = htmlelements\[[\"txt\"]\] [as] [INPUTElementImpl];] |
|                                                                                                                                                                                                                                                                            |
| [string][\[\] specialEvents = [new] [string]\[2\];]                                                         |
|                                                                                                                                                                                                                                                                            |
| [specialEvents\[0\] = [\"Yes\"];]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                            |
| [specialEvents\[1\] = [\"No\"];]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                            |
| [MessageBox][.Show([\"Before Merging:\"] + [this].txt.SupportedEvents.Length.ToString());]            |
|                                                                                                                                                                                                                                                                            |
| [this][.txt.MergeSupportedEvents(specialEvents);]                                                                                                     |
|                                                                                                                                                                                                                                                                            |
| [MessageBox][.Show([\"After Merging:\"] + [this].txt.SupportedEvents.Length.ToString());]             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\' MergeSupportedEvents method is to merge the standard and special events.]                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Private][ htmlelements [As] Hashtable = [Me].HtmluiControl1.Document.GetElementsByUserIdHash()]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Private][ txt [As] INPUTElementImpl = [CType](IIf([TypeOf] htmlelements([\"txt\"]) [Is] INPUTElementImpl, htmlelements([\"txt\"]), [Nothing]), INPUTElementImpl)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Private][ specialEvents [As] [String]() = [New] [String](1) {}]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Private][ specialEvents(0) = [\"Yes\"]]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Private][ specialEvents(1) = [\"No\"]]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [MessageBox.Show([\"Before Merging:\"] + [Me].txt.SupportedEvents.Length.ToString())]                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Me][.txt.MergeSupportedEvents(specialEvents)]                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [MessageBox.Show([\"After Merging:\"] + [Me].txt.SupportedEvents.Length.ToString())]                                                                                                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p36} 

More:









































































