---
title: blockindentandoutdent.md
original_path: WinForms_Docs/99_Uncategorized/blockindentandoutdent.md
created_at: 2025-08-05
---








  









### Block Indent and Outdent {#block-indent-and-outdent style="tab-stops: 0pt"}

 

Edit Control supports VS.NET-like Block Indent and Outdent. In other words, when a block of text is selected, and the TAB or SPACE keys are pressed, appropriate number of tabs or spaces are added to the beginning of each line in the selected block. This will move the selected section of the code by the appropriate number of tabs or spaces to the right. Similarly, when the SHIFT+TAB keys combination is pressed, the tabs or spaces added gets removed, i.e., the previous action performed by the TAB or SPACE keys gets undone. Hence, pressing the SHIFT+TAB keys combination, moves the selected text by the appropriate number of tabs or spaces, to the left.

 

You can also set the tab size to the desired number of spaces using the **TabSize** property of the Edit Control as shown below. By default, the TabSize property value is set to **2**.

 

+-------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                          |
|                                                                                                                         |
| []                                                                    |
|                                                                                                                         |
| [// \"n\" is the integer value specifying the number of spaces.]      |
|                                                                                                                         |
| [this][.editControl1.TabSize = n;] |
+-------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                   |
|                                                                                                                      |
| []                                                                 |
|                                                                                                                      |
| [\' \"n\" is the integer value specifying the number of spaces.]   |
|                                                                                                                      |
| [Me][.editControl1.TabSize = n] |
+----------------------------------------------------------------------------------------------------------------------+

 

**Indent and Outdent Text Programmatically**

 

The following methods are used to indent and outdent text in the Edit Control.

 


  ------------------------- ---------------------------------------
  Edit Control Method       Description
  IndentText                Indents text in the specified range.
  IndentSelection           Indents selected text.
  OutdentText               Outdents text in the specified range.
  OutdentSelection          Outdents selected text.
  ------------------------- ---------------------------------------


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                         |
| [// Indents text in the specified range.]                                                                                                                                                             |
|                                                                                                                                                                                                                                                         |
| [this][.editControl1.IndentText([new] [Point](5, 5), [new] [Point](10, 10));]  |
|                                                                                                                                                                                                                                                         |
| [// Indents selected text.]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                         |
| [this][.editControl1.IndentSelection();]                                                                                                                           |
|                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                         |
| [// Outdents text in the specified range.]                                                                                                                                                            |
|                                                                                                                                                                                                                                                         |
| [this][.editControl1.OutdentText([new] [Point](5, 5), [new] [Point](10, 10));] |
|                                                                                                                                                                                                                                                         |
| [// Outdents selected text.]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                         |
| [this][.editControl1.OutdentSelection();]                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                     |
|                                                                                                                                                                                                        |
| []                                                                                                                                                   |
|                                                                                                                                                                                                        |
| [\' Indents text in the specified range.]                                                                                                            |
|                                                                                                                                                                                                        |
| [Me][.editControl1.IndentText([New] Point(5, 5), [New] Point(10, 10))]  |
|                                                                                                                                                                                                        |
| [\' Indents selected text.]                                                                                                                          |
|                                                                                                                                                                                                        |
| [Me][.editControl1.IndentSelection()]                                                                             |
|                                                                                                                                                                                                        |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                        |
| [\' Outdents text in the specified range.]                                                                                                           |
|                                                                                                                                                                                                        |
| [Me][.editControl1.OutdentText([New] Point(5, 5), [New] Point(10, 10))] |
|                                                                                                                                                                                                        |
| [\' Outdents selected text.]                                                                                                                         |
|                                                                                                                                                                                                        |
| [Me][.editControl1.OutdentSelection()]                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p28} 

[]{#related-topics}

