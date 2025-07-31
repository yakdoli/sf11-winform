---
title: clientsidemethods16.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\clientsidemethods16.md
created_at: 2025-07-03
---








  









### Client-Side Methods {#client-side-methods style="tab-stops: 0pt"}

Methods

[] 


+-----------------+-----------------+-----------------+------------------------------------------------------+
| Method          | Parameters      | Return type     | Descriptions                                         |
+-----------------+-----------------+-----------------+------------------------------------------------------+
| setText(string) | string          | void            | Sets the text to the multicolumn drop-down text box. |
|                 |                 |                 |                                                      |
|                 |                 |                 |                                                      |
|                 |                 |                 |                                                      |
|                 |                 |                 |                                                      |
+-----------------+-----------------+-----------------+------------------------------------------------------+
| getOldText()    | No parameter    | string          | Returns the previously displayed text.               |
|                 |                 |                 |                                                      |
|                 |                 |                 |                                                      |
+-----------------+-----------------+-----------------+------------------------------------------------------+
| showPopup()     | No parameter    | void            | Opens the pop-up panel.                              |
+-----------------+-----------------+-----------------+------------------------------------------------------+
| hidePopup()     | No parameter    | Void            | Closes the pop-up panel.                             |
+-----------------+-----------------+-----------------+------------------------------------------------------+


[] 

Include the following code snippet in the view page to set the text in a multicolumn drop-down text box.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                      |
| [  [\<][input] [type][=\"text\"] [value][=\"\"] [id][=\"SetDropDowntext\"] [/\>]]    |
|                                                                                                                                                                                                                                                                                                                      |
| [   [\<][input] [type][=\"button\"] [value][=\"Set Text\"] [id][=\"setText\"] [/\>]] |
|                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                      |
| [\<][script][ [type][=\"text/javascript\"\>]]                                                                                       |
|                                                                                                                                                                                                                                                                                                                      |
| [       \$([\"#setText\"]).bind([\'click\'], [function] () {]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                      |
| [           [var] multiDD = \$find([\"MultiColumnDropdown\"]);]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                      |
| [           multiDD.setText(\$([\'#SetDropDowntext\']).val());]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                      |
| [       });]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                      |
| [  [\</][script][\>]]                                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Include the following code snippet in the view to get the old text and show/hide the pop-up panel.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                |
| [       \$([\"#setText\"]).bind([\'click\'], [function] () {]                                                           |
|                                                                                                                                                                                                                                |
| [           [var] multiDD = \$find([\"MultiColumnDropdown\"]);]                                                                                |
|                                                                                                                                                                                                                                |
| [           multiDD.setText(\$([\'#SetDropDowntext\']).val());]                                                                                                     |
|                                                                                                                                                                                                                                |
| [       });]                                                                                                                                                                               |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [       [function] GetOldText() {]                                                                                                                                    |
|                                                                                                                                                                                                                                |
| [           [var] oldText = \$find([\"MultiColumnDropdown\"]).getOldText();]                                                                   |
|                                                                                                                                                                                                                                |
| [       }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                |
| [       [function] ShowPopupPanel() {]                                                                                                                                |
|                                                                                                                                                                                                                                |
| [           \$find([\"MultiColumnDropdown\"]).showPopup();]                                                                                                         |
|                                                                                                                                                                                                                                |
| [       }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                |
| [       [function] HidePopupPanel() {]                                                                                                                                |
|                                                                                                                                                                                                                                |
| [           \$find([\"MultiColumnDropdown\"]).hidePopup();]                                                                                                         |
|                                                                                                                                                                                                                                |
| [       }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                |
| [  [\</][script][\>]]                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

