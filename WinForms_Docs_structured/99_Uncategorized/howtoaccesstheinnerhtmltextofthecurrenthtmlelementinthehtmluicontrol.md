---
title: howtoaccesstheinnerhtmltextofthecurrenthtmlelementinthehtmluicontrol.md
original_path: WinForms_Docs/99_Uncategorized/howtoaccesstheinnerhtmltextofthecurrenthtmlelementinthehtmluicontrol.md
created_at: 2025-08-05
---








  









## How To Access the Inner HTML Text Of the Current HTML Element In the HTMLUI Control? {#how-to-access-the-inner-html-text-of-the-current-html-element-in-the-htmlui-control style="tab-stops: 0pt"}

[] 

You can access the inner HTML text of the current HTML element in the HTMLUI control by using the **InnerHTML** property of the HTMLUI control. This property also allows access to the child elements of the HTML elements.

The following HTML document contains a div element. The code snippet shows how the inner text of the element is accessed and displayed in the output at run time.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[HTML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<!\--][ HTML Document ][\--\>]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][html][\>]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [       \<][body][\>]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [              \<][div][ ][id][=][\"[div1]\"[\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                     Have an issue you need to contact Syncfusion about? Use our state of the art incident management]                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                     system - Direct-Trac.]                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [              \</][div][\>]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [       \</][body][\>]                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\</][html][\>]                                                                                                                                                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                               |
| [Hashtable][ htmlelements = [this].htmluiControl1.Document.GetElementsByUserIdHash();]                                                              |
|                                                                                                                                                                                                                                                                                               |
| [DIVElementImpl][ div1 = [this].htmlelements\[[\"div1\"]\] [as] [DIVElementImpl];] |
|                                                                                                                                                                                                                                                                                               |
| [MessageBox][.Show(div1.InnerHTML.ToString());]                                                                                                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [Private][ htmlelements [As] Hashtable = [Me].htmluiControl1.Document.GetElementsByUserIdHash()]                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [Private][ div1 [As] DIVElementImpl = [CType](IIf([TypeOf] [Me].htmlelements([\"div1\"]) [Is] DIVElementImpl, ] |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [Me][.htmlelements([\"div1\"]), [Nothing]), DIVElementImpl)]                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [MessageBox.Show(div1.InnerHTML.ToString())]                                                                                                                                                                                                                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p184} 

 

[]{#related-topics}

