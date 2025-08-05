---
title: loadingandsavingcontents.md
original_path: WinForms_Docs/99_Uncategorized/loadingandsavingcontents.md
created_at: 2025-08-05
---








  









### Loading And Saving Contents {#loading-and-saving-contents style="tab-stops: 0pt"}

 

The contents of the Edit Control can be loaded and saved to a particular stream. This can be achieved by using the methods given below.

 


  -------------------------------------- ------------------------------------------------------------------------------------
           Edit Control Method           Description
  LoadStream                             Loads the stream and the corresponding configuration.
  FlushChanges                           Flushes changes to the current stream.
  SaveStream                             Saves content to the specified stream using specified encoding and line end style.
  -------------------------------------- ------------------------------------------------------------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                |
| [// Loads the content of the specified stream into the Edit Control.]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                |
| [this][.editControl1.LoadStream(streamName);]                                                                                                                                             |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                |
| [// Loads the specified stream and configuration.]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                |
| [this][.editControl1.LoadStream(streamName, config);]                                                                                                                                     |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                |
| [// Saves changes made to the contents of the Edit Control into the current stream.]                                                                                                                                         |
|                                                                                                                                                                                                                                                                                |
| [this][.editControl1.FlushChanges();]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                |
| [// Saves content to the specified stream using specified encoding and line end style.]                                                                                                                                      |
|                                                                                                                                                                                                                                                                                |
| [this][.editControl1.SaveStream(System.IO.[Stream].Null , [Encoding].BigEndianUnicode, Syncfusion.IO.[NewLineStyle].Mac);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                     |
|                                                                                                                                                                                                        |
| []                                                                                                                                                   |
|                                                                                                                                                                                                        |
| [\' Loads the content of the specified stream into the edit control.]                                                                                |
|                                                                                                                                                                                                        |
| [Me][.editControl1.LoadStream(streamName)]                                                                        |
|                                                                                                                                                                                                        |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                        |
| [\' Loads the specified stream and configuration.]                                                                                                   |
|                                                                                                                                                                                                        |
| [Me][.editControl1.LoadStream(streamName, config)]                                                                |
|                                                                                                                                                                                                        |
| []                                                                                                                                                   |
|                                                                                                                                                                                                        |
| [\' Saves changes made to the contents of the Edit Control into the current stream.]                                                                 |
|                                                                                                                                                                                                        |
| [Me][.editControl1.FlushChanges()]                                                                                |
|                                                                                                                                                                                                        |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                        |
| [\' Saves content to the specified stream using specified encoding and line end style.]                                                              |
|                                                                                                                                                                                                        |
| [Me][.editControl1.SaveStream(System.IO.Stream.Null , Encoding.BigEndianUnicode, Syncfusion.IO.NewLineStyle.Mac)] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**Getting Details of Currently Loaded File**

[] 

The name of the file that is currently loaded can be set by using the **FileName** property.

 


  ------------------------- ----------------------------------------------------
  Edit Control Property     Description
  FileName                  Gets / sets the name of the currently opened file.
  ------------------------- ----------------------------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                               |
|                                                                                                                                                              |
| []                                                                                                         |
|                                                                                                                                                              |
| [// Gets or sets the name of the file loaded in the Edit Control.]                                         |
|                                                                                                                                                              |
| [this][.editControl1.FileName = [\"Temp.txt\"];] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                        |
|                                                                                                                                                           |
| []                                                                                                      |
|                                                                                                                                                           |
| [\' Gets or sets the name of the file loaded in the Edit Control.]                                      |
|                                                                                                                                                           |
| [Me][.editControl1.FileName = [\"Temp.txt\"]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**Getting Details of Currently Loaded Stream**

 

The name of the stream that is currently loaded in the Edit Control can be set by using the **FileOpened** property.

 


  ----------------------- ------------------------------------------------------
  Edit Control Property   Description
  FileOpened              Gets / sets the filestream that is used as an input.
  ----------------------- ------------------------------------------------------


 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                      |
| [// Gets or sets the name of the stream that is currently loaded in the Edit Control.]                                                                                                                             |
|                                                                                                                                                                                                                                                                      |
| [this][.editControl1.FileOpened = [new] [FileStream]([\"Temp.txt\"], [FileMode].Create);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                  |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                |
|                                                                                                                                                                                                                     |
| [\' Gets or sets the name of the stream that is currently loaded in the Edit Control.]                                                                            |
|                                                                                                                                                                                                                     |
| [Me][.editControl1.FileOpened = [New] FileStream([\"Temp.txt\"], FileMode.Create)] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

See Also

[] 

[Creating, Loading and Saving a File]{.UGHyperlink}[, ][Saving and Cancelling Changes]{.UGHyperlink}[]

 

[]{#p88} 

[]{#related-topics}

