---
title: builtindialogs.md
original_path: WinForms_Docs/99_Uncategorized/builtindialogs.md
created_at: 2025-08-05
---






##### Built-in Dialogs {#built-in-dialogs style="tab-stops: 0pt"}

[] 

Essential Tools Window Control provides built-in dialogs for alert, confirm, and prompt boxes. The syntax of these boxes are mentioned below.

[] 

+------------------------------------------------------------------------------------------------------------------------+
| **[\[JS\]]**                                                                       |
|                                                                                                                        |
| **[]**                                                                             |
|                                                                                                                        |
| [SFAlert( sText, sCaption, nWidth, nHeight );]                                     |
|                                                                                                                        |
| [SFPrompt( sText, fnCallbackFunction, sCaption, sDefaultValue, nWidth, nHeight );] |
|                                                                                                                        |
| [SFConfirm( sText, fnCallbackFunction, sCaption, nWidth, nHeight );]               |
+------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: These parameters are nullable.


[] 

For example, the following code snippet can be used to display the boxes.

**[]** 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[aspx\]]**                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][input][ [type][=\"button\"] [onclick][=\"onbuttonclick(0)\"] [value][=\"SFAlert\"] [/\>]]   |
|                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][input][ [type][=\"button\"] [onclick][=\"onbuttonclick(1)\"] [value][=\"SFPrompt\"] [/\>]]  |
|                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][input][ [type][=\"button\"] [onclick][=\"onbuttonclick(2)\"] [value][=\"SFConfirm\"] [/\>]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JS\]]**                                                                                                       |
|                                                                                                                                                        |
| **[]**                                                                                                             |
|                                                                                                                                                        |
| [function][ onbuttonclick(nIdx)]                                  |
|                                                                                                                                                        |
| [{]                                                                                                                |
|                                                                                                                                                        |
| [    [var] sText = document.getElementById( [\"dialogtext\"] ).value;] |
|                                                                                                                                                        |
| [    [if]( nIdx == 0 )]                                                                       |
|                                                                                                                                                        |
| [    {]                                                                                                            |
|                                                                                                                                                        |
| [        SFAlert( sText, [\"Warning\"] );]                                                  |
|                                                                                                                                                        |
| [    }]                                                                                                            |
|                                                                                                                                                        |
| [    [else] [if]( nIdx == 1 )]                                           |
|                                                                                                                                                        |
| [    {]                                                                                                            |
|                                                                                                                                                        |
| [        SFPrompt( sText, fnCallback,[\"Enter a number\"] );]                               |
|                                                                                                                                                        |
| [    }]                                                                                                            |
|                                                                                                                                                        |
| [    [else] [if]( nIdx == 2 )]                                           |
|                                                                                                                                                        |
| [    {]                                                                                                            |
|                                                                                                                                                        |
| [        SFConfirm( sText, fnCallback, [\"Confirm\"] );]                                    |
|                                                                                                                                                        |
| [    }    ]                                                                                                        |
|                                                                                                                                                        |
| [}]                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The return value of the prompt / confirm dialog boxes can be found as shown below.

[] 

+---------------------------------------------------------------------------------------------------------------------+
| **[\[JS\]]**                                                                    |
|                                                                                                                     |
| []                                                                              |
|                                                                                                                     |
| [function][ fnCallback( arg )] |
|                                                                                                                     |
| [{]                                                                             |
|                                                                                                                     |
| [    SFAlert( [\"return value: \"] + arg );]             |
|                                                                                                                     |
| [}]                                                                             |
+---------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

