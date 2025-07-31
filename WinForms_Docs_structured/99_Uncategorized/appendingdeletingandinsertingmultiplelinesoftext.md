---
title: appendingdeletingandinsertingmultiplelinesoftext.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\appendingdeletingandinsertingmultiplelinesoftext.md
created_at: 2025-07-03
---






#### Appending, Deleting and Inserting Multiple Lines of Text {#appending-deleting-and-inserting-multiple-lines-of-text style="tab-stops: 0pt"}

 

Edit Control offers support for text manipulation operations like append, delete and insertion of multiple lines of text, through the use of the following APIs.

 

**Appending Text**

[] 

Text can be appended to the Edit Control by using the below given method.

 


  --------------------- -------------------------------------------------------------------------------------
  Edit Control Method   Description
  AppendText            Appends the specified text to the end of the existing contents of the Edit Control.
  --------------------- -------------------------------------------------------------------------------------


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                             |
|                                                                                                                                                                            |
| []                                                                                                                       |
|                                                                                                                                                                            |
| [// Appends the given string to the end of the text in Edit Control.]                                                    |
|                                                                                                                                                                            |
| [this][.editControl1.AppendText([\" text to be appended \"]);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                      |
|                                                                                                                                                                         |
| []                                                                                                                    |
|                                                                                                                                                                         |
| [\' Appends the given string to the end of the text in the Edit Control.]                                             |
|                                                                                                                                                                         |
| [Me][.editControl1.AppendText([\" text to be appended \"])] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Inserting Text

 

The Insert mode can be enabled in the Edit Control by setting the **InsertMode** property to True.

 

Text can be inserted anywhere inside the Edit Control by using the **InsertText** method given below.

 


  --------------------- ----------------------------------------------------------------------
  Edit Control Method   Description
  InsertText            Inserts a piece of text at any desired position in the Edit Control.
  --------------------- ----------------------------------------------------------------------


 

Inserting Multiple Lines

 

Collection of text lines can be inserted by using the property given below.

 


  ---------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------
           Edit Control Property           Description
  Lines                                    Lets you specify multiple lines of text to the Edit Control in the form of a string array. This feature is similar to the one in .NET RichTextBox control.
  ---------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------


 

Inserting Text based on Conditions

 

The below given properties can be used to insert text based on conditions which have been described below.

 


+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| Edit Control Property             | Description                                                                                                             |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| AllowInsertBeforeReadOnlyNewLine  | Specifies whether inserting text should be allowed at the beginning of readonly region at the start of new line.        |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| InsertDroppedFileIntoText         | Specifies whether the outer file dragged and dropped onto the Edit Control should be inserted into the current content. |
|                                   |                                                                                                                         |
|                                   |                                                                                                                         |
|                                   |                                                                                                                         |
|                                   | When this property is set to \'False\', the current file is closed, and the dropped outer file is opened.               |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| RespectTabStopsOnInsertingText    | Specifies whether tab stops should be respected on inserting blocks of text.                                            |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                     |
| [// Set the Insert mode.]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                     |
| [this][.editControl1.InsertMode = [true];]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                     |
| [// Inserts a string at the given line and column.]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                     |
| [this][.editControl1.InsertText(1, 1, [\" text to be inserted \"]);]                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                     |
| [// Specifies multiple lines of text to the EditControl in the form of a string array. ]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                     |
| [this][.editControl1.Lines = [new] [string]\[\] {[\" first line \"], [\" second line \"], [\" third line \"]};] |
|                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                     |
| [// Allows text insertion only at the beginning of the readonly region at the start of a new line.]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                     |
| [this][.editControl1.AllowInsertBeforeReadonlyNewLine = [true];]                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                     |
| [// Specifies whether the outer file dragged and dropped onto the editcontrol should be inserted into the current content.]                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                     |
| [this][.editControl1.InsertDroppedFileIntoText = [true];]                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                |
| [\' Set the Insert mode.]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                |
| [Me][.editControl1.InsertMode = [True]]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                |
| [\' Inserts a string at the given line and column.]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                |
| [Me][.editControl1.InsertText(1, 1, [\" text to be inserted \"])]                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                |
| [\' Specifies multiple lines of text to the EditControl in the form of a string array. ]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                |
| [Me][.editControl1.Lines = [New] [String]() {[\" first line \"], [\" second line \"], [\" third line \"]}] |
|                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                |
| [\' Allows text insertion only at the beginning of the readonly region at the start of a new line.]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                |
| [Me][.editControl1.AllowInsertBeforeReadonlyNewLine = [True]]                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                |
| [\' Specifies whether the outer file dragged and dropped onto the editcontrol should be inserted into the current content.]                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                |
| [Me][.editControl1.InsertDroppedFileIntoText = [True]]                                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Deleting Text

 

Text can be deleted in the Edit Control by using the below given methods.

 


  --------------------- ------------------------------------------------------------------
  Edit Control Method   Description
  DeleteChar            Deletes a character to the right of the current cursor position.
  DeleteCharLeft        Deletes a character to the left of the current cursor position.
  DeleteWord            Deletes a word to the right of the current cursor position.
  DeleteWordLeft        Deletes a word to the left of the current cursor position.
  DeleteAll             Deletes all text in the document.
  DeleteText            Deletes the specified text.
  --------------------- ------------------------------------------------------------------


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                            |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                           |
| [// Deletes the character to the right of the cursor.]                                                                                                                                  |
|                                                                                                                                                                                                                                           |
| [this][.editControl1.DeleteChar();]                                                                                                                  |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                           |
| [// Deletes the character to the left of the cursor.]                                                                                                                                   |
|                                                                                                                                                                                                                                           |
| [this][.editControl1.DeleteCharLeft();]                                                                                                              |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                           |
| [// Deletes a word to the right of the current cursor position.]                                                                                                                        |
|                                                                                                                                                                                                                                           |
| [this][.editControl1.DeleteWord();]                                                                                                                  |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                           |
| [// Deletes a word to the left of the current cursor position.]                                                                                                                         |
|                                                                                                                                                                                                                                           |
| [this][.editControl1.DeleteWordLeft();]                                                                                                              |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                           |
| [// To delete all the text.]                                                                                                                                                            |
|                                                                                                                                                                                                                                           |
| [this][.editControl1.DeleteAll();]                                                                                                                   |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                           |
| [// To delete a selection.]                                                                                                                                                             |
|                                                                                                                                                                                                                                           |
| [this][.editControl1.DeleteText([this].editControl1.Selection.Top, [this].editControl1.Selection.Bottom);] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                 |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                                    |
| [\' Deletes the character to the right of the cursor.]                                                                                                                           |
|                                                                                                                                                                                                                                    |
| [Me][.editControl1.DeleteChar()]                                                                                                              |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                                    |
| [\' Deletes the character to the left of the cursor.]                                                                                                                            |
|                                                                                                                                                                                                                                    |
| [Me][.editControl1.DeleteCharLeft()]                                                                                                          |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [\' Deletes a word to the right of the current cursor position.]                                                                                                                 |
|                                                                                                                                                                                                                                    |
| [Me][.editControl1.DeleteWord()]                                                                                                              |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [\' Deletes a word to the left of the current cursor position.]                                                                                                                  |
|                                                                                                                                                                                                                                    |
| [Me][.editControl1.DeleteWordLeft()]                                                                                                          |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [\' Deletes all the text.]                                                                                                                                                       |
|                                                                                                                                                                                                                                    |
| [Me][.editControl1.DeleteAll()]                                                                                                               |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [\' Deletes a selection.]                                                                                                                                                        |
|                                                                                                                                                                                                                                    |
| [Me][.editControl1.DeleteText([Me].editControl1.Selection.Top, [Me].editControl1.Selection.Bottom)] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 20: Input entered for Handling Text

 

A sample which demonstrates the above features is available in the below sample installation path.

 

..\\My Documents\\Syncfusion\\EssentialStudio\\***Version Number***\\Windows\\Edit.Windows\\Samples\\2.0\\Advanced Editor Functions\\TextHandlingDemo

 

[]{#p39} 

[]{#related-topics}

