---
title: customizingdictionaryandsuggestions.md
original_path: WinForms_Docs/99_Uncategorized/customizingdictionaryandsuggestions.md
created_at: 2025-08-05
---






##### Customizing Dictionary and Suggestions {#customizing-dictionary-and-suggestions style="MARGIN-LEFT: 1.8pt; tab-stops: 1.8pt"}

[] 

The **English(en-US)** is the default dictionary that is employed which can be customized by providing the dictionary in \'.dic\' format. The lexicon being used must be placed under the folder **SpellCheck**/**Dictionary**.

[] 


  ------------ ------------------------------------------------------------------------------------------
  Property     Description
  Dictionary   Specifies the dictionary used in SpellCheckControl. The default dictionary is en_US.dic.
  ------------ ------------------------------------------------------------------------------------------


[] 

The suggestions being displayed can be set, such that only the required number of suggestions will be displayed during spell check process for the misspelled words. The number of suggestions can be set to the **MaxSuggestion** property. By default only the first 10 suggestions will be displayed in the suggestion list of the spell check dialog box.

[         ]


  --------------- --------------------------------------------------------------------------------------------------
  Property        Description
  MaxSuggestion   This property can be used to customize the number of suggestions displayed. Default value is 10.
  --------------- --------------------------------------------------------------------------------------------------


[] 

Programmatically the suggestions can be set as follows.

[] 

+--------------------------------------------------------------------------------------+
| **[\[C#\]]**                     |
|                                                                                      |
| **[]**                           |
|                                                                                      |
| [SpellCheck.MaxSuggestions = 5;] |
+--------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                               |
|                                                                                                                                                                |
| **[]**                                                                                                     |
|                                                                                                                                                                |
| [Private][ SpellCheck.MaxSuggestions = 5] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

