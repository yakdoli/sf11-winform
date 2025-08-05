---
title: methods18.md
original_path: WinForms_Docs/99_Uncategorized/methods18.md
created_at: 2025-08-05
---








  









### Methods {#methods style="tab-stops: 0pt"}

The following table lists the methods available in EditControl class and its purpose.

[] 

Table 6: EditControl Methods


  ---------------------------------- --------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Methods                            Type      Description
    ExpandLine(int index)            Void      Expands a line, index in the argument refers the index of the line to be expanded (0 based value).
  ExpandLineUpTopLevel(int index);   Void      Expands  a line and its parent line up to top most level. Index in the argument refers to the index of the line to be expanded (0 based value).
  GetTextRange(int start, int end)   String    Returns the text between start and end lines. Start and End denotes the index of the Start and End lines (0 based values).
  LoadFile()                         Boolean   **LoadFile** method is used to open a file in the EditControl. It shows up a **OpenFileDialog** in order for the users to select the file to be opened using EditControl and returns a **bool** value stating whether file open was successful.
  LoadFile(string filename)          Boolean   This method does not display **OpenFileDialog** and loads the file specified as the parameter of the method. It returns a **boo**l value stating the file open was successful.
  SaveFile()                         Boolean   Save method is used to save the text in the EditControl under a file name with different supported file types.
  ---------------------------------- --------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


[] 

 

[]{#p14} 

 

[]{#related-topics}

