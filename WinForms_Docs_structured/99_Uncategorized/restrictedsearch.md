---
title: restrictedsearch.md
original_path: WinForms_Docs/99_Uncategorized/restrictedsearch.md
created_at: 2025-08-05
---






##### Restricted Search {#restricted-search style="MARGIN-LEFT: 1.8pt; tab-stops: 1.8pt"}

[] 

The spell checking engine can also be customized to ignore certain text or words from being spell checked. By setting the respective properties, these words will be overlooked and will not indicate them as misspelled words. This option will be effective when there are lot of email id\'s and address, filenames, htmltags, combination of words and numbers, combination of upper and lower case words are used frequently in the document.

[] 


{border="0"}Note: Spell check can be performed only on the required part of the input text, by selecting that part in the textbox, which performs spell check on the selected text alone.


[] 


+-----------------------------------+------------------------------------------------------------------------------------------------------------------+
|                                   |                                                                                                                  |
|                                   |                                                                                                                  |
| Property                          | Description                                                                                                      |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------+
| ExcludeEmailAddress               | Specifies whether or not to ignore email address during spell check. Default value is True.                      |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------+
| ExcludeFilenames                  | Specifies whether or not to ignore file names during spell check. Default value is True.                         |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------+
| ExcludeHtmlTags                   | Specifies whether or not to ignore html tags during spell check. Default value is True.                          |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------+
| ExcludeInternetAddress            | Specifies whether or not to ignore internet address during spell check. Default value is True.                   |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------+
| ExcludeRepeatedWords              | Specifies whether or not to ignore repeated words during spell check. Default value is False.                    |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------+
| ExcludeWordsInMixedCase           | Specifies whether or not to ignore mixed case words during spell check.  Default value is False.                 |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------+
| ExcludeWordsInUpperCase           | Specifies whether or not to ignore uppercase words during spell check. Default value is True.                    |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------+
| ExcludeWordsWithNumbers           | Specifies whether or not to spell check numbers or words with numbers during spell check. Default value is True. |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------+


[] 

{border="0"}

[] 

Figure 91: URL being skipped on setting ExcludeInternetAddress

[] 

Programmatically the exclude properties can be set as follows.

[] 

+-------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                        |
|                                                                                                                         |
| **[]**                                                              |
|                                                                                                                         |
| [SpellCheck.ExcludeEmailAddress = [true];]     |
|                                                                                                                         |
| [SpellCheck.ExcludeFileNames = [true];]        |
|                                                                                                                         |
| [SpellCheck.ExcludeHtmlTags = [true];]         |
|                                                                                                                         |
| [SpellCheck.ExcludeInternetAddress = [true];]  |
|                                                                                                                         |
| [SpellCheck.ExcludeRepeatedWords = [true];]    |
|                                                                                                                         |
| [SpellCheck.ExcludeWordsInMixedCase = [true];] |
|                                                                                                                         |
| [SpellCheck.ExcludeWordsInUpperCase = [true];] |
|                                                                                                                         |
| [SpellCheck.ExcludeWordsWithNumbers = [true];] |
+-------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                  |
|                                                                                                                                                                                                   |
| **[]**                                                                                                                                        |
|                                                                                                                                                                                                   |
| [Private][ SpellCheck.ExcludeEmailAddress = [True]]     |
|                                                                                                                                                                                                   |
| [Private][ SpellCheck.ExcludeFileNames = [True]]        |
|                                                                                                                                                                                                   |
| [Private][ SpellCheck.ExcludeHtmlTags = [True]]         |
|                                                                                                                                                                                                   |
| [Private][ SpellCheck.ExcludeInternetAddress = [True]]  |
|                                                                                                                                                                                                   |
| [Private][ SpellCheck.ExcludeRepeatedWords = [True]]    |
|                                                                                                                                                                                                   |
| [Private][ SpellCheck.ExcludeWordsInMixedCase = [True]] |
|                                                                                                                                                                                                   |
| [Private][ SpellCheck.ExcludeWordsInUpperCase = [True]] |
|                                                                                                                                                                                                   |
| [Private][ SpellCheck.ExcludeWordsWithNumbers = [True]] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

