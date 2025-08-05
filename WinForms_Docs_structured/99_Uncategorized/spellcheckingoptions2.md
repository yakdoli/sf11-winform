---
title: spellcheckingoptions2.md
original_path: WinForms_Docs/99_Uncategorized/spellcheckingoptions2.md
created_at: 2025-08-05
---






#### Spell Checking Options {#spell-checking-options style="tab-stops: 0pt"}

The Spell Checking engine can also be customized to ignore certain text or words from being spell checked. By setting the respective properties, these words will be overlooked and will not indicate them as misspelled words. This option will be effective when there are a number of  email id\'s and addresses, filenames, htmltags, combination of words and numbers, combination of upper and lower case words that are used frequently in the document.

 

Properties

**[]** 

  --------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Property                                                                                      Description
  [ExcludeEmailAddress][]   [Specifies whether or not to ignore email address during Spell Ceck. Default value is True.][]
  [ExcludeFilenames]                                                      [Specifies whether or not to ignore file names during Spell Check. Default value is True.]
  [ExcludeHtmlTags]                                                       [Specifies whether or not to ignore html tags during Spell Check. Default value is True.]
  [ExcludeInternetAddress]                                                [Specifies whether or not to ignore internet address during Spell Check. Default value is True.]
  [ExcludeWordsInMixedCase]                                               [Specifies whether or not to ignore mixed case words during Spell Check.  Default value is False.]
  [ExcludeWordsInUpperCase]                                               [Specifies whether or not to ignore uppercase words during Spell Check. Default value is True.]
  [ExcludeWordsWithNumbers]                                               [Specifies whether or not to Spell Check numbers or words with numbers during Spell Check. Default value is True.]
  --------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------

[] 

[] 

Setting Spell Checking options  

Create a spell checker instance and set the spell checking options as given below:

**** 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                           |
|                                                                                                                                                                                            |
| [SpellChecker][ SpellCheck = [new] [SpellChecker]();] |
|                                                                                                                                                                                            |
| [SpellCheck.ExcludeEmailAddress = [true];]                                                                                        |
|                                                                                                                                                                                            |
| [SpellCheck.ExcludeFileNames = [true];]                                                                                           |
|                                                                                                                                                                                            |
| [SpellCheck.ExcludeHtmlTags = [true];]                                                                                            |
|                                                                                                                                                                                            |
| [SpellCheck.ExcludeInternetAddresses = [true];]                                                                                   |
|                                                                                                                                                                                            |
| [SpellCheck.ExcludeWordsInMixedCase = [true];]                                                                                    |
|                                                                                                                                                                                            |
| [SpellCheck.ExcludeWordsInUpperCase = [true];]                                                                                    |
|                                                                                                                                                                                            |
| [SpellCheck.ExcludeWordsWithNumbers = [true];][]                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Sample Link

To access the sample link:

1.   Open the Synfusion Dashboard.

2.   Select **User Interface**.

3.   Click the WPF drop-down list and select **Explore Samples**.

4.   Navigate to **Tools** -\> **SpellChecker** -\> **SpellCheckerDemo**.

[]{#related-topics}

