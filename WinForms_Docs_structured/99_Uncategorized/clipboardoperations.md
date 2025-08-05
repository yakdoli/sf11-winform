---
title: clipboardoperations.md
original_path: WinForms_Docs/99_Uncategorized/clipboardoperations.md
created_at: 2025-08-05
---








  









### Clipboard Operations {#clipboard-operations style="tab-stops: 0pt"}

 

Edit Control uses the clipboard to cut, copy or paste the text data. It stores the data in the clipboard for cut and copy operations and retrieves data from the clipboard for paste operations. The following APIs in the Edit Control facilitates these clipboard operations.

 


  --------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Edit Control Method   Description
  Copy                  Copies the selected text contents into the clipboard.
  Cut                   Cuts the selected text contents from Edit Control and places it into the clipboard.
  Paste                 Retrieves copied contents from the clipboard and pastes it into Edit Control.
  CanCopy               Indicates whether it is possible to perform copy operations in Edit Control.
  CanCut                Indicates whether it is possible to perform cut operations in Edit Control.
  CanPaste              Indicates whether it is possible to perform copy, cut and paste operations in Edit Control.
  ClearClipboard        Clears all contents in the clipboard associated with Essential Edit. This is generally used immediately after the application loads, to clear any junk from previous clipboard operations.
  --------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                           |
| [// Copies the selected text into the clipboard.]                                                                                                                                                       |
|                                                                                                                                                                                                                                                           |
| [this][.editControl1.Copy();]                                                                                                                          |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                           |
| [// Cuts the selected text contents from Edit Control and places it into the clipboard.]                                                                                                                |
|                                                                                                                                                                                                                                                           |
| [this][.editControl1.Cut();]                                                                                                                           |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                           |
| [// Retrieves copied contents from the clipboard and pastes it into Edit Control.]                                                                                                                      |
|                                                                                                                                                                                                                                                           |
| [this][.editControl1.Paste();]                                                                                                                         |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                           |
| [// Indicates whether it is possible to perform copy operation in Edit Control.]                                                                                                                        |
|                                                                                                                                                                                                                                                           |
| [bool ][canCopy =][ this][.editControl1.CanCopy;]   |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                           |
| [// Indicates whether it is possible to perform cut operation in Edit Control.]                                                                                                                         |
|                                                                                                                                                                                                                                                           |
| [bool ][canCut =][ this][.editControl1.CanCut;]     |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                           |
| [// Indicates whether it is possible to perform paste operation in Edit Control.]                                                                                                                       |
|                                                                                                                                                                                                                                                           |
| [bool ][canPaste =][ this][.editControl1.CanPaste;] |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                           |
| [// Clears all contents in the clipboard associated with Essential Edit.]                                                                                                                               |
|                                                                                                                                                                                                                                                           |
| [this][.editControl1.ClearClipboard();]                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [\' Copies the selected text into the clipboard.]                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [Me][.[editControl1.Copy()]]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [\' Cuts the selected text contents from Edit Control and places it into the clipboard. ]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [Me][.[editControl1.Cut()]]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [\' Retrieves copied contents from the clipboard and pastes it into Edit Control.]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [Me][.[editControl1.Paste()]]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [\' Indicates whether it is possible to perform copy operation in Edit Control.]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [Dim ][canCopy ][as bool ][=][ Me][.[editControl1.CanCopy]]   |
|                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [\' Indicates whether it is possible to perform cut operation in Edit Control.]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [Dim ][canCut ][as bool ][=][ Me][.[editControl1.CanCut]]     |
|                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [\' Indicates whether it is possible to perform paste operation in Edit Control.]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [Dim ][canPaste ][as bool ][=][ Me][.[editControl1.CanPaste]] |
|                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [\' Clears all contents in the clipboard associated with Essential Edit.]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [Me][.editControl1.ClearClipboard()]                                                                                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p23} 

[]{#related-topics}

