---
title: encodingtext.md
original_path: WinForms_Docs/99_Uncategorized/encodingtext.md
created_at: 2025-08-05
---






#### Encoding Text {#encoding-text style="tab-stops: 0pt"}

 

Edit Control facilitates saving the contents of a file in any desired encoding and new line style. This can be accomplished by using the below given method.

 


  --------------------- --------------------------------------
  Edit Control Method   Description
  SaveFile              Saves content to the specified file.
  --------------------- --------------------------------------


 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                |
| [this][.editControl1.SaveFile([\"EditControl\"], [Encoding].Unicode, Syncfusion.IO.[NewLineStyle].Mac);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                            |
|                                                                                                                                                                                                               |
| []                                                                                                                                                          |
|                                                                                                                                                                                                               |
| [Me][.editControl1.SaveFile([\"EditControl\"], Encoding.Unicode, Syncfusion.IO.NewLineStyle.Mac)] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Edit Control supports all the encoding styles supported by the **System.Text.Encoding** enumerator. The below given methods can be used to get / set the encoding style for the text in the Edit Control.

 


+-----------------------------------+----------------------------------------------------------+
| Edit Control Method               | Description                                              |
+-----------------------------------+----------------------------------------------------------+
| GetEncoding                       | Gets the current text encoding.                          |
+-----------------------------------+----------------------------------------------------------+
| SetEncoding                       | Sets the current text encoding. The options provided are |
|                                   |                                                          |
|                                   |                                                          |
|                                   |                                                          |
|                                   | [·      ]ASCII              |
|                                   |                                                          |
|                                   | [·      ]BigEndianUnicode   |
|                                   |                                                          |
|                                   | [·      ]Default            |
|                                   |                                                          |
|                                   | [·      ]UTF32              |
|                                   |                                                          |
|                                   | [·      ]UTF7               |
|                                   |                                                          |
|                                   | [·      ]UTF8               |
|                                   |                                                          |
|                                   | [·      ]Unicode            |
+-----------------------------------+----------------------------------------------------------+


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                 |
|                                                                                                                                                                |
| []                                                                                                           |
|                                                                                                                                                                |
| [// Gets the current text encoding.]                                                                         |
|                                                                                                                                                                |
| [this][.editControl1.GetEncoding();]                                      |
|                                                                                                                                                                |
| []                                                                                                                         |
|                                                                                                                                                                |
| [// Sets the current text encoding.]                                                                         |
|                                                                                                                                                                |
| [this][.editControl1.SetEncoding([Encoding].ASCII);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                   |
|                                                                                                                                      |
| []                                                                                 |
|                                                                                                                                      |
| [\' Gets the current text encoding.]                                               |
|                                                                                                                                      |
| [Me][.editControl1.GetEncoding()]               |
|                                                                                                                                      |
| []                                                                                               |
|                                                                                                                                      |
| [// Sets the current text encoding.]                                               |
|                                                                                                                                      |
| [Me][.editControl1.SetEncoding(Encoding.ASCII)] |
+--------------------------------------------------------------------------------------------------------------------------------------+

 

It also supports all the new line styles supported by the **Syncfusion.IO.NewLineStyle** enumerator - **Windows**, **Mac**, **Unix** and **Control**.

 


  -------------------------------- -------------
           New Line Styles         Description
  Windows                          \\r\\n
  Mac                              \\r
  Unix                             \\n\\r
  Control                          \\n
  -------------------------------- -------------


 

The **SaveFilewithDataLoss** and **SaveStreamWithDataLoss** events are fired whenever there is a data loss while saving the file by using the specified encoding format. Files or streams can be corrupted if you have some Unicode characters that cannot be saved using the specified encoding format. For example, if you have a file or stream that contains some specific characters of German language, and if you try to save it using ASCII encoding, then data loss will occur. If the save operation is not canceled here, characters will be saved incorrectly.

 

[]{#p59} 

[]{#related-topics}

