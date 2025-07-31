---
title: creatingloadingsavinganddroppingfiles.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\creatingloadingsavinganddroppingfiles.md
created_at: 2025-07-03
---








  









### Creating, Loading, Saving And Dropping Files {#creating-loading-saving-and-dropping-files style="tab-stops: 0pt"}

 

This section discusses the file operations supported in Edit Control.

 

**Creating Files**

 

The **New** and **NewFile** methods are used to create a new stream or file, and optionally allow you to set the language to be used by specifying the appropriate configuration settings.

 


  --------------------- ---------------------------------------------------------------
  Edit Control Method   Description
  New                   Creates an empty stream and allows the editor to for editing.
  NewFile               Creates new empty file with specified coloring.
  --------------------- ---------------------------------------------------------------


[] 

+------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                           |
|                                                                                                                                          |
| []                                                                                     |
|                                                                                                                                          |
| [// Creates a new stream with default configuration settings.]                         |
|                                                                                                                                          |
| [this][.editControl.New();]                         |
|                                                                                                                                          |
| []                                                                                                   |
|                                                                                                                                          |
| [// Creates a new file with default configuration settings.]                           |
|                                                                                                                                          |
| [this][.editControl.NewFile();]                     |
|                                                                                                                                          |
| []                                                                                                   |
|                                                                                                                                          |
| [// Creates a new stream with specified configuration settings.]                       |
|                                                                                                                                          |
| [this][.editControl.New(ConfigLanguage lang);]      |
|                                                                                                                                          |
| []                                                                                                   |
|                                                                                                                                          |
| [// Creates a new file with specified configuration settings.]                         |
|                                                                                                                                          |
| [this][.editControl.NewFile(IConfigLanguage lang);] |
+------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                        |
|                                                                                                                           |
| []                                                                      |
|                                                                                                                           |
| [\' Creates a new file.]                                                |
|                                                                                                                           |
| [Me][.editControl1.NewFile()]        |
|                                                                                                                           |
| []                                                                                    |
|                                                                                                                           |
| [Me][.editControl1.\[New\]()]        |
|                                                                                                                           |
| []                                                                                    |
|                                                                                                                           |
| [\' \"config\" is Configuration Settings file of type IConfigLanguage.] |
|                                                                                                                           |
| [Me][.editControl1.NewFile(config)]  |
|                                                                                                                           |
| []                                                                                    |
|                                                                                                                           |
| [Me][.editControl1.\[New\](config)]  |
+---------------------------------------------------------------------------------------------------------------------------+

**[]** 

Loading Files

[] 

The **LoadFile** method loads the content of any desired file into the Edit Control.

[] 


  --------------------- -----------------------------------------------------------------
  Edit Control Method   Description
  LoadFile              Shows open file dialog to the user and opens the selected file.
  --------------------- -----------------------------------------------------------------


[] 


{border="0"}Note:[ ]The character encoding for the text can also be specified while loading the file.


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                     |
|                                                                                                                                                                                                    |
| []                                                                                                                                               |
|                                                                                                                                                                                                    |
| [// Displays the Open File dialog.]                                                                                                              |
|                                                                                                                                                                                                    |
| [this][.editControl1.LoadFile();]                                                                             |
|                                                                                                                                                                                                    |
| []                                                                                                                                                             |
|                                                                                                                                                                                                    |
| [// Loads the content of the specified file.]                                                                                                    |
|                                                                                                                                                                                                    |
| [this][.editControl1.LoadFile([\"Temp.txt\"], [Encoding].ASCII);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                       |
|                                                                                                                                                                          |
| []                                                                                                                     |
|                                                                                                                                                                          |
| [\' Displays the Open File dialog.]                                                                                    |
|                                                                                                                                                                          |
| [Me][.editControl1.LoadFile()]                                                      |
|                                                                                                                                                                          |
| []                                                                                                                                   |
|                                                                                                                                                                          |
| [\' Loads the content of the specified file. ]                                                                         |
|                                                                                                                                                                          |
| [Me][.editControl1.LoadFile([\"Temp.txt\"], Encoding.ASCII)] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Saving Files

[] 

The following methods are used to save a file in the Edit Control.

[] 


  --------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Edit Control Method   Description
  SaveFile              Saves the contents of the Edit Control to a specified file.
  Save                  Invokes the save file dialog box and lets you save the contents of the Edit Control to the specified file.
  SaveAs                Opens **SaveAs** dialog and prompts you to enter the name of the file.
  SaveModified          Saves the file only if it was modified and prompts for filename if needed. This is especially useful when the application is about to be closed or a new file is being loaded into the Edit Control.
  --------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                 |
| [// Saves the contents of the file.]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                 |
| [this][.editControl1.SaveFile([\"Temp.txt\"], [Encoding].Unicode, Syncfusion.IO.[NewLineStyle].Control);] |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                 |
| [// Displays the Save File dialog.]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                 |
| [this][.editControl1.Save();]                                                                                                                                              |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                 |
| [// Displays the SaveAs dialog. ]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                 |
| [this][.editControl1.SaveAs();]                                                                                                                                            |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                 |
| [// Saves the contents of the file after modification, when a new file is loaded, or when a file is closed.]                                                                                                  |
|                                                                                                                                                                                                                                                                 |
| [this][.editControl1.SaveModified();]                                                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                             |
|                                                                                                                                                                                                                |
| []                                                                                                                                                           |
|                                                                                                                                                                                                                |
| [\' Saves the contents of the file.]                                                                                                                         |
|                                                                                                                                                                                                                |
| [Me][.editControl1.SaveFile([\"Temp.txt\"], Encoding.Unicode, Syncfusion.IO.NewLineStyle.Control)] |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [\' Displays the Save File dialog.]                                                                                                                          |
|                                                                                                                                                                                                                |
| [Me][.editControl1.Save()]                                                                                                |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [\' Displays the SaveAs dialog. ]                                                                                                                            |
|                                                                                                                                                                                                                |
| [Me][.editControl1.SaveAs()]                                                                                              |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [\' Saves the contents of the file after modification, when a new file is loaded, or when a file is closed.]                                                 |
|                                                                                                                                                                                                                |
| [Me][.editControl1.SaveModified()]                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Dropping Files

[] 

[Files can be dropped onto the Edit Control by using the properties given below.]

[] 


+-----------------------------------+-----------------------------------------------------------------------------------------+
| Edit Control Property             | Description                                                                             |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| DropAllFiles                      | Gets / sets value indicating whether all files can be dropped onto Edit Control.        |
|                                   |                                                                                         |
|                                   |                                                                                         |
|                                   |                                                                                         |
|                                   | If set to False, only files with extensions contained in FileExtensions can be dropped. |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| FileExtensions                    | Gets / sets extensions of files that can be dropped to Edit Control.                    |
+-----------------------------------+-----------------------------------------------------------------------------------------+


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                      |
| [// Drops all files onto Edit Control.]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                      |
| [this][.editControl1.DropAllFiles = [true];]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                      |
| [// Specifies the file extensions of files that can be dropped onto Edit Control. ]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                      |
| [this][.editControl1.FileExtensions = [new] [string]\[\] {[\".cs\"], [\".sql\"], [\".vb\"], [\".xml\"]};] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                  |
| [\' Drops all files onto Edit Control.]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                  |
| [Me][.editControl1.DropAllFiles = [True]]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                  |
| [\' Specifies the file extensions of files that can be dropped onto Edit Control.]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                  |
| [Me][.editControl1.FileExtensions = [New] [String]() {[\".cs\"], [\".sql\"], [\".vb\"], [\".xml\"]} ] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#p87} 

[]{#related-topics}

