---
title: inputinputtag.md
original_path: WinForms_Docs/99_Uncategorized/inputinputtag.md
created_at: 2025-08-05
---








  









### INPUT - Input Tag {#input---input-tag style="tab-stops: 0pt"}

[] 

The **Input** tag is used to receive some inputs from the user. The input tag uses the following attributes to provide a value for the specified input elements from the user.

[] 

[·      ]**type**: Specifies the type of input control to be placed in the document. HTMLUI control supports the following input elements:

[] 


  ----------------- --------------------------------
  Attribute Value   Control that will be Displayed
  Text              Text Box
  Button            Button
  CheckBox          Check Box
  Radio             Radio Button
  Password          Password Box
  Reset             Reset Button
  Submit            Submit Button
  ----------------- --------------------------------


[] 

[·      ]**value**: Specifies the default text that will appear on the control after being rendered on the document

[·      ]**size**: Specifies the size of the input document

[·      ]**name**: Specifies a unique name to the control. In HTMLUI the **Control.Name** property will access the name given to the control in code and not the value of this name attribute. The user has to access this value with the help of the **Control.Attributes\[\"name\"\].Value** property. This will return the value of this attribute.

[·      ]**maxlength**: Specifies the maximum number of characters that can be displayed inside the text fields

[·      ]**disabled**: Disables the control. Any change that the user makes in the control will not be updated in the control.

[·      ]**checked**: Displays the checkbox or the radio button selected by default in the document

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[HTML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| *[]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [File Location and Name:  C:\\MyProjects\\input\\input.html]                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][html][\>]                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][body][\>]                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][input][ [type][=\"text\"] [value][=\"textbox\"] [size][=\"20\"] [maxlength][=\"5\"] [/\>\<][br][/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][input][ [type][=\"button\"] [value][=\"button element\"/\>\<][br][/\>]]                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][input][ [type][=\"checkbox\"] [value][=\"checkbox\"] [checked][/\>\<][br][/\>]]                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][input][ [type][=\"password\"] [value][=\"password\"] [size][=\"20\"/\>\<][br][/\>]]                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][input][ [type][=\"radio\"] [value][=\"radio\"/\>\<][br][/\>]]                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][input][ [type][=\"reset\"] [value][=\"reset\"/\>\<][br][/\>]]                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][input][ [type][=\"submit\"] [value][=\"submit\"] [size][=\"50\"/\>\<][br][/\>]]                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\</][body][\>]                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\</][html][\>]                                                                                                                                                                                                                                                                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                          |
|                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                |
|                                                                                                                                                                                                                         |
| [this][.htmluiControl.LoadHTML([@\"C:\\MyProjects\\input\\input.html\"]);] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                   |
|                                                                                                                                                                                                                      |
| **[]**                                                                                                                                             |
|                                                                                                                                                                                                                      |
| [Me][.htmluiControl.LoadHTML(@[\"C:\\MyProjects\\input\\input.html\"])] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p87} 

[]{#related-topics}

