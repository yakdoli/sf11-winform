---
title: textandhtml.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\textandhtml.md
created_at: 2025-07-03
---






##### [Text and Html] {#text-and-html style="tab-stops: 0pt"}

[] 

Accessing the control\'s HTML

[] 

The **Html** property allows you to get / set the HTML content of the control. It always reflects the latest content edited by the user. Changes made to this property will be reflected in the browser when the page gets loaded in the browser.

[] 


  ---------- ---------------------------------------
  Property   Description
  Html       Specifies the editor content in html.
  ---------- ---------------------------------------


[] 

Programmatically the html text can be set and retrieved as follows.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                  |
|                                                                                                                                   |
| []                                                               |
|                                                                                                                                   |
| [RichTextEditor1.Html = [\"\<b\>Sample Text\</b\>\"];] |
|                                                                                                                                   |
| [TextBox1.Text = RichTextEditor1.Html;]                                       |
+-----------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                            |
|                                                                                                                                                                                                             |
| []                                                                                                                                         |
|                                                                                                                                                                                                             |
| [Private][ RichTextEditor1.Html = [\"\<b\>Sample Text\</b\>\"]] |
|                                                                                                                                                                                                             |
| [Private][ TextBox1.Text = RichTextEditor1.Html]                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Accessing the control\'s unformatted Text

[] 

The unformatted editor text can be obtained at run time by using the **Text** property.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                            |
|                                                                                                                                                                             |
| **[]**                                                                                                                  |
|                                                                                                                                                                             |
| [TextBox1.Text = RichTextEditor1.Text;][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                      |
|                                                                                                                                                                       |
| []                                                                                                   |
|                                                                                                                                                                       |
| [Private TextBox1.Text = RichTextEditor1.Text][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Switching between HTML and Edit mode in the designer

[] 

Use the following button to switch between Edit and HTML modes in the client.

[] 


  ------------------------------------------- ---------------------------------
  Button                                      Description
  {border="0"}   Views the content in Edit mode.
  {border="0"}   Views the content in Html mode.
  ------------------------------------------- ---------------------------------


 

[]{#related-topics}

