---
title: tabs1.md
original_path: WinForms_Docs/99_Uncategorized/tabs1.md
created_at: 2025-08-05
---






##### Tabs {#tabs style="tab-stops: 0pt"}

 

**Tabs** class represents a tab collection within a paragraph. **Tab** class represents a single tab within the tab collection.

 

**Class Hierarchy**

 

WParagraphFormat

   \|

    Tabs

 

Public Properties

 


  --------------- --------------------------------------
  Name            Description
  Justification   Gets or sets the tab justification.
  TabLeader       Gets or sets the tab leader.
  Position        Gets or sets the tab position.
  DeletePostion   Gets or sets the Clear tab position.
  --------------- --------------------------------------


 

Public Methods

 


  ------------------------------------------------------------------------- ---------------------------------------------------------------------------------
  Name                                                                      Description
  AddTab()                                                                  Adds default tab to the paragraph.
  AddTab(float position)                                                    Adds tab at the specfied position.
  AddTab(float position, TabJustification justification TabLeader leader)   Adds tab at specified location with the specified tab justification and leader.
  RemoveAt(int index)                                                       Removes tab at specified index from the tab collection.
  RemoveByTabPosition(float position)                                       Removes tab at specified tab position from the tab collection.
  ------------------------------------------------------------------------- ---------------------------------------------------------------------------------


 

The following code examples illustrate how to add the tab to the paragraph and delete the tab from the paragraph.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                |
|                                                                                                                                                                                                               |
| **[]**                                                                                                                                                      |
|                                                                                                                                                                                                               |
| [//Create a new instance for the word document]                                                                                                             |
|                                                                                                                                                                                                               |
| [WordDocument][ document = [new] [WordDocument]();]                      |
|                                                                                                                                                                                                               |
| [//Add one section to the document]                                                                                                                         |
|                                                                                                                                                                                                               |
| [IWSection][ section=document .AddSection ();]                                                                        |
|                                                                                                                                                                                                               |
| [//Add one paragraph to the section]                                                                                                                        |
|                                                                                                                                                                                                               |
| [IWParagraph][ paragraph=section.AddParagraph ();]                                                                    |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [//Add tab stop at the postion 36 with tab justification\[left\] and tab leader\[dotted\]]                                                                  |
|                                                                                                                                                                                                               |
| [paragraph .ParagraphFormat .Tabs.AddTab(36,[TabJustification] .Left ,Syncfusion.DocIO.DLS.[TabLeader] .Dotted );]        |
|                                                                                                                                                                                                               |
| [//Add tab stop at the postion 80 with tab justification\[Right\] and tab leader\[Hyphenated\]]                                                             |
|                                                                                                                                                                                                               |
| [paragraph .ParagraphFormat .Tabs.AddTab(80,[TabJustification] .Right ,Syncfusion.DocIO.DLS.[TabLeader].Hyphenated  );]   |
|                                                                                                                                                                                                               |
| [//Add tab stop at the postion 144 with tab justification\[Center\] and with no tab leader]                                                                 |
|                                                                                                                                                                                                               |
| [paragraph .ParagraphFormat .Tabs.AddTab(144,[TabJustification] .Centered ,Syncfusion.DocIO.DLS.[TabLeader] .NoLeader );] |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [//Remove tab at index 1 from the tab collection][]                                                                     |
|                                                                                                                                                                                                               |
| [paragraph .ParagraphFormat .Tabs .RemoveAt (1);]                                                                                                                         |
|                                                                                                                                                                                                               |
| [//Remove tab at the position 144]                                                                                                                          |
|                                                                                                                                                                                                               |
| [paragraph .ParagraphFormat .Tabs .RemoveByTabPosition (144);]                                                                                                            |
|                                                                                                                                                                                                               |
| [//Append tab character]                                                                                                                                    |
|                                                                                                                                                                                                               |
| [paragraph.AppendText([\"\\t\"]);]                                                                                                                |
|                                                                                                                                                                                                               |
| [//Append Text to the paragraph]                                                                                                                            |
|                                                                                                                                                                                                               |
| [paragraph.AppendText([\"Tabs are added and removed\"]);]                                                                                         |
|                                                                                                                                                                                                               |
| [//Save the word document]                                                                                                                                  |
|                                                                                                                                                                                                               |
| [document .Save ([\"Sample.doc\"],[FormatType].Doc  );][]                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                            |
|                                                                                                                                                                           |
| []                                                                                                                                                  |
|                                                                                                                                                                           |
| [\'Create a new instance for the word document]                                                                         |
|                                                                                                                                                                           |
| [Dim][ document [As] [New] WordDocument()] |
|                                                                                                                                                                           |
| [\'Add one section to the document]                                                                                     |
|                                                                                                                                                                           |
| [Dim][ section [As] IWSection = document.AddSection()]          |
|                                                                                                                                                                           |
| [\'Add one paragraph to the section]                                                                                    |
|                                                                                                                                                                           |
| [Dim][ paragraph [As] IWParagraph = section.AddParagraph()]     |
|                                                                                                                                                                           |
| []                                                                                                                                    |
|                                                                                                                                                                           |
| []                                                                                                                                    |
|                                                                                                                                                                           |
| [\'Add tab stop at the postion 36 with tab justification\[left\] and tab leader\[dotted\]]                              |
|                                                                                                                                                                           |
| [paragraph.ParagraphFormat.Tabs.AddTab(36, TabJustification.Left, Syncfusion.DocIO.DLS.TabLeader.Dotted)]                             |
|                                                                                                                                                                           |
| [\'Add tab stop at the postion 80 with tab justification\[Right\] and tab leader\[Hyphenated\]]                         |
|                                                                                                                                                                           |
| [paragraph.ParagraphFormat.Tabs.AddTab(80, TabJustification.Right, Syncfusion.DocIO.DLS.TabLeader.Hyphenated)]                        |
|                                                                                                                                                                           |
| [\'Add tab stop at the postion 144 with tab justification\[Center\] and with no tab leader]                             |
|                                                                                                                                                                           |
| [paragraph.ParagraphFormat.Tabs.AddTab(144, TabJustification.Centered, Syncfusion.DocIO.DLS.TabLeader.NoLeader)]                      |
|                                                                                                                                                                           |
| []                                                                                                                                    |
|                                                                                                                                                                           |
| []                                                                                                                                    |
|                                                                                                                                                                           |
| [\'Remove tab at index 1 from the tab collection]                                                                       |
|                                                                                                                                                                           |
| [paragraph.ParagraphFormat.Tabs.RemoveAt(1)]                                                                                          |
|                                                                                                                                                                           |
| [\'Remove tab at the position 144][]                                                |
|                                                                                                                                                                           |
| [paragraph.ParagraphFormat.Tabs.RemoveByTabPosition(144)]                                                                             |
|                                                                                                                                                                           |
| [\'Append tab character]                                                                                                |
|                                                                                                                                                                           |
| [paragraph.AppendText([\"\\t\"])]                                                                             |
|                                                                                                                                                                           |
| [\'Append Text to the paragraph]                                                                                        |
|                                                                                                                                                                           |
| [paragraph.AppendText([\"Tabs are added and removed\"])]                                                      |
|                                                                                                                                                                           |
| [\'Save the word document]                                                                                              |
|                                                                                                                                                                           |
| [document.Save([\"Sample.doc\"], FormatType.Doc)][]                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

