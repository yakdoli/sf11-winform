---
title: languagebasemembers.md
original_path: WinForms_Docs/99_Uncategorized/languagebasemembers.md
created_at: 2025-08-05
---








  









###   LanguageBase Members  {#languagebase-members style="tab-stops: 0pt"}

LanguageBase class in Syncfusion.Windows.Edit namespace plays a vital role in the implementation of language support in EditControl. In order to include a support for a new or custom language, a class inherited from LanguageBase or its sub classes need to be implemented. LanguageBase contains a number of properties and methods to enable the custom language developers configure their languages easily. This topic discusses about the properties and methods available in the LanguageBase class.

**[]** 

Properties

The following table lists the properties available in LanguageBase class and its usage.

[] 

Table 9: LanguageBase Properties


  ----------------------------------- ------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Property Name                       Type          Description
  ApplyColoring                       Boolean       Gets or sets a value indicating if the language supports syntax highlighting.
  BlockEnd                            String        Gets or sets a value indicating the end text that denotes end of a block in code.
  BlockStart                          String        Gets or sets a value indicating the start text that denotes start of a block in code.
  CaseSensitive                       Boolean       Gets or sets a value indicating whether the Language has case sensitive or not.
  CommitsIntellisenseItemOnSpaceBar   Boolean       Gets or sets a value indicating whether the selected intellisense items to be appended when space bar is pressed.
  EllipsisText                        String        Gets or sets a value indicating the text to be displayed when a block is collapsed. By default its set to \"\...\".
  FileExtension                       String        Gets or sets File Extension supported by the language.
  Formats                             IEnumerable   Gets or Sets a collection of type of IFormat indicating the language configurations. It has been modified to IEnumerable type to allow the users to binding a custom collection as language formats.
  IntellisenseCommitCharacters        String        Gets or sets a value indicating when the selected intellisense items to be appended. The string given will be converted to individual characters internally and verified to append the selected item to text.
  IntellisenseDrillDownChar           Char          Gets or sets a value indicating a char on which the sub-items of the intellisense items to displayed.
  IsSplitTextToWords                  Boolean       Gets or sets a value indicating if the text in lines has to be spitted in to tokens.
  Lexem                               IEnumerable   Gets or Sets a collection of type of ILexem indicating the language configurations. It has been modified to IEnumerable type to allow the users to binding a custom collection as language lexems.
  Name                                String        Gets or sets Name of the Language.
  ParentControl                       EditControl   Gets a value indicating the parent EditControl's reference.
  SplitLinesRegex                     String        Gets or sets a value indicating the Regex to be applied for splitting the text in lines.
  SplitWordsRegex                     String        Gets or sets a value indicating the Regex to be applied for splitting the lines into individual tokens.
  SupportsIntellisense                Boolean       Gets or sets a value indicating whether the language supports IntelliSense or not.
  SupportsOutlining                   Boolean       Gets or Sets a value indicating whether the language supports outlining.
  TextForeground                      Brush         Gets or sets foreground brush to be applied when no Lexems are applicable for the text.
  ----------------------------------- ------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


[] 

[] 

[] 

Methods

The following table lists the methods available in LanguageBase class and its purpose.

[] 

[] 

Table 10: LanguageBase Methods


+----------------------------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Method                                             | Return Type           | Description                                                                                                                                                                                                                                                                                                        |
+----------------------------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ApplyColor(string text, int line);                 | IFormat               | Helper method to apply coloring to the text based on the Lexems in the Language configurations. It is a protected method and can be overridden in the sub classes. The method is used to manipulate the Format to be applied to a particular token in a line.                                                      |
+----------------------------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ApplyExpandCollapse(ApplyExpandCollapseArgs args)  | Void                  | Helper method for perform expand collapse for line items. This method can be overridden if custom expand collapse logics has be implemented. This method runs in a background thread to overcome performance hits, usage of any properties and methods outside the scope of the thread may result in an exception. |
+----------------------------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ApplyExpandItems()                                 | Void                  | Helper method to Apply Expansions for the content in the EditControl. This method can be called if the expand collapse has to be refreshed for entire text in EditControl.                                                                                                                                         |
+----------------------------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| HideIntellisensePopup()                            | Void                  | Method to Hide Intellisense Popup.                                                                                                                                                                                                                                                                                 |
+----------------------------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| InitializeExpandCollapse()                         | Void                  | This method can gets called before the ApplyExpandCollapse and can be used to perform any initialization operations.                                                                                                                                                                                               |
+----------------------------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PositionIntellisensePopup(int line, int index)     | Void                  | Method to adjust the position of the intellisense box. Line value in parameter                                                                                                                                                                                                                                     |
|                                                    |                       |                                                                                                                                                                                                                                                                                                                    |
|                                                    |                       | represents the line number (starts of 0)                                                                                                                                                                                                                                                                           |
|                                                    |                       |                                                                                                                                                                                                                                                                                                                    |
|                                                    |                       | and index in the parameter                                                                                                                                                                                                                                                                                         |
|                                                    |                       |                                                                                                                                                                                                                                                                                                                    |
|                                                    |                       | represents the cursor index                                                                                                                                                                                                                                                                                        |
+----------------------------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| RefreshExpandItems(int line)                       | Void                  | Helper method to refresh lines expansions from a specified line number. Line value in parameter refers to the index (starts from 0)                                                                                                                                                                                |
+----------------------------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ShowIntellisenseBox(EditIntellisenseArgs args)     | Void                  | Helper method to Show the Intellisense popup.                                                                                                                                                                                                                                                                      |
+----------------------------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SplitTextToLines()                                 | Void                  | A helper method to split the text in the EditControl in to individual lines.                                                                                                                                                                                                                                       |
+----------------------------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

[] 

[]{#related-topics}

