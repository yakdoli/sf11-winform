---
title: scriptelement.md
original_path: WinForms_Docs/99_Uncategorized/scriptelement.md
created_at: 2025-08-05
---








  









### SCRIPT Element {#script-element style="tab-stops: 0pt"}

[] 

The **SCRIPT** element is used to define scripts to the HTML document. This makes the document self-contained. It does not require any other external ways to define the operation of the document\'s elements. The **SCRIPTElementImpl** class is used to determine the properties and methods for this element.

[] 

Properties

[] 

[·      ]**IsVisible**: Gets / sets a value indicating whether the script is shown / hidden

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                    |
| [// Gets or sets a value indicating whether the script  is visible or not.]                                                                                                                      |
|                                                                                                                                                                                                                                                                    |
| [Hashtable][ htmlelements = [this].htmluiControl1.Document.GetElementsByUserIdHash();]                                |
|                                                                                                                                                                                                                                                                    |
| [this][.script = htmlelements\[[\"script\"]\] [as] [SCRIPTElementImpl];] |
|                                                                                                                                                                                                                                                                    |
| [this][.label1.Text = [\"\\nScript(IsVisible):\"] + [this].script.IsVisible.ToString();]         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\' Gets or sets a value indicating whether the script is visible or not.]                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Private][ htmlelements [As] Hashtable = [Me].HtmluiControl1.Document.GetElementsByUserIdHash()]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Private][ [Me].script = [Ctype](IIf([TypeOf] htmlelements([\"script\"]) [Is] SCRIPTElementImpl, htmlelements([\"script\"]), [Nothing]), SCRIPTElementImpl)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Private][ [Me].label1.Text = Constants.vbLf & [\"Script(IsVisible):\"] & [Me].script.IsVisible.ToString()  ]                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Methods

[] 

[·      ]**GetScriptCode**: Gets the string format of the script code

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                             |
|                                                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                            |
| [MessageBox][.Show([\"ScriptCode:\\n\"] + [this].script.GetScriptCode().ToString());] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                               |
|                                                                                                                                                                                                  |
| **[]**                                                                                                                         |
|                                                                                                                                                                                                  |
| [MessageBox.Show([\"ScriptCode:\"] & Constants.vbLf+[Me].script.GetScriptCode().ToString())   ] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p60} 

[]{#related-topics}

