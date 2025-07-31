---
title: userdictionary1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\userdictionary1.md
created_at: 2025-07-03
---






#### User Dictionary {#user-dictionary style="tab-stops: 0pt"}

Spell Checker can also look into the specified user dictionary for spell checking.

 

Methods

**[]** 


+---------------------------------------------------------------+-----------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Method                                                        | Prototype                                                                   | Description                                                                                                                                                                                                                   |
+---------------------------------------------------------------+-----------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [SetUserDictionary]                     | [SetUserDictionary(string dicName),]                  | [SetUserDictionary is an overloaded method. You can set the UserDictionary by passing the file name of the dictionary to this method or you can pass UserDictionary instance to this method]            |
|                                                               |                                                                             |                                                                                                                                                                                                                               |
|                                                               | [SetUserDictionary(UserDictionary userDic)]           |                                                                                                                                                                                                                               |
+---------------------------------------------------------------+-----------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [SetIncludeUserDictionaryInSuggestions] | [SetIncludeUserDictionaryInSuggestions(bool include)] | [The UserDictionary will be taken into account only if we pass true to this method. If we pass false as its argument, the SpellChecker will not look into the UserDictionary while checking spellings.] |
+---------------------------------------------------------------+-----------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

Setting User Dictionary  

Create a SpellChecker instance and set the user dictionary as given in the below code.

**** 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                           |
|                                                                                                                                                                                            |
| [SpellChecker][ SpellCheck = [new] [SpellChecker]();] |
|                                                                                                                                                                                            |
| [SpellCheck.] [      SetUserDictionary("D:\\custom");]                                                             |
|                                                                                                                                                                                            |
| [SpellCheck.] [      SetIncludeUserDiction-aryInSuggestions(true);]                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Sample Link

To access the sample link:

1.   Open the Synfusion Dashboard.

2.   Select **User Interface**.

3.   Click the WPF drop-down list and select **Explore Samples**.

4.   Navigate to **Tools** -\> **SpellChecker** -\> **SpellCheckerDemo**.

 

[]{#related-topics}

