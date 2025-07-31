---
title: listformat.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\listformat.md
created_at: 2025-07-03
---






##### List Format {#list-format style="tab-stops: 0pt"}

 

WListFormat class defines the formatting for DocIO list paragraph. The type of the list is specified by using the ListType property of WListFormat. ListLevelNumber property defines the level number for the list paragraph. CurrentListStyle property defines the list style, applied for the current list paragraph. CurrentListLevel property returns the object of the WListLevel type, which defines the formatting for the list level (paragraph). For example, a value that the list starts at (for numbered lists), list symbols, alignment of list text, and so forth.

 

[·      ]To apply default bullet or numbered style to the paragraph, use **ApplyDefBulletStyle** or **ApplyDefNumberedStyle** function.

[·      ]To apply custom style, use **ApplyStyle** function.

[·      ]**ContinueListNumbering** function is used to continue previous list numbering.

[·      ]Use **IncreaseIndentLevel** or **DecreaseIndentLevel** to increase or decrease indent for the level.

[·      ]To remove list from the paragraph use **RemoveList** function.

 

Class Hierarchy

 

FormatBase

\|

            WListFormat

 

**Public Constructor**

 


  --------------------------------------- ------------------------------------------------
  Name                                    Description
  WListFormat.WListFormat (IWParagraph)   Initializes new instance of WListFormat class.
  --------------------------------------- ------------------------------------------------


**[]** 

Public Properties

 


  ------------------ -----------------------------------------------------------------------------
  Name               Description
  CurrentListLevel   Gets or sets paragraph\'s ListLevel.
  CurrentListStyle   Gets paragraph\'s list style.
  CustomStyleName    Gets or sets name of custom style.
  ListLevelNumber    Gets or sets list nesting level.
  ListType           Gets or sets type of the list.
  RestartNumbering   Gets or sets whether numbering of the list must restart from previous list.
  ------------------ -----------------------------------------------------------------------------


 

Public Methods

 


  ----------------------- ---------------------------------------------------------
  Name                    Description
  ApplyDefBulletStyle     Applies default bullet style for current paragraph.  
  ApplyDefNumberedStyle   Applies default numbered style for current paragraph.  
  ApplyStyle              Gets or sets name of custom style.  
  ContinueListNumbering   Continues last list.  
  DecreaseIndentLevel     Decreases level indent.  
  IncreaseIndentLevel     Increases level indent.  
  RemoveList              Removes the list from current paragraph.  
  ----------------------- ---------------------------------------------------------


 

The following example illustrates how to use the WListFormat and list styles in DocIO.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                         |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [//Write default numbered list          ]                                                                                                                            |
|                                                                                                                                                                                                                        |
| [IWParagraph][ paragraph = section.AddParagraph();]                                                                               |
|                                                                                                                                                                                                                        |
| [paragraph.AppendText( [\"First Numbered ( level 0 )\"] );      ]                                                                                           |
|                                                                                                                                                                                                                        |
| [paragraph.ListFormat.ApplyDefNumberedStyle();]                                                                                                                                    |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [paragraph = section.AddParagraph();]                                                                                                                                              |
|                                                                                                                                                                                                                        |
| [paragraph.AppendText( [\"Level 1\"] ); ]                                                                                                                   |
|                                                                                                                                                                                                                        |
| [paragraph.ListFormat.ContinueListNumbering();]                                                                                                                                    |
|                                                                                                                                                                                                                        |
| [paragraph.ListFormat.IncreaseIndentLevel();]                                                                                                                                      |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [paragraph = section.AddParagraph();]                                                                                                                                              |
|                                                                                                                                                                                                                        |
| [paragraph.AppendText( [\"Level 0\"] ); ]                                                                                                                   |
|                                                                                                                                                                                                                        |
| [paragraph.ListFormat.ContinueListNumbering();]                                                                                                                                    |
|                                                                                                                                                                                                                        |
| [paragraph.ListFormat.DecreaseIndentLevel();]                                                                                                                                      |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [section.AddParagraph();]                                                                                                                                                          |
|                                                                                                                                                                                                                        |
| [section.AddParagraph();]                                                                                                                                                          |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [//Write default bulleted list  ]                                                                                                                                    |
|                                                                                                                                                                                                                        |
| [paragraph = section.AddParagraph();]                                                                                                                                              |
|                                                                                                                                                                                                                        |
| [paragraph.AppendText( [\"First bulleted ( level 0 )\"] );      ]                                                                                           |
|                                                                                                                                                                                                                        |
| [paragraph.ListFormat.ApplyDefBulletStyle();]                                                                                                                                      |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [paragraph = section.AddParagraph();]                                                                                                                                              |
|                                                                                                                                                                                                                        |
| [paragraph.AppendText( [\"Level 1\"] ); ]                                                                                                                   |
|                                                                                                                                                                                                                        |
| [paragraph.ListFormat.ContinueListNumbering();]                                                                                                                                    |
|                                                                                                                                                                                                                        |
| [paragraph.ListFormat.IncreaseIndentLevel();]                                                                                                                                      |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [paragraph = section.AddParagraph();]                                                                                                                                              |
|                                                                                                                                                                                                                        |
| [paragraph.AppendText( [\"Level 0\"] ); ]                                                                                                                   |
|                                                                                                                                                                                                                        |
| [paragraph.ListFormat.ContinueListNumbering();]                                                                                                                                    |
|                                                                                                                                                                                                                        |
| [paragraph.ListFormat.DecreaseIndentLevel();]                                                                                                                                      |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [section.AddParagraph();]                                                                                                                                                          |
|                                                                                                                                                                                                                        |
| [section.AddParagraph();]                                                                                                                                                          |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [//Write mixed bulleted and numbered list ]                                                                                                                          |
|                                                                                                                                                                                                                        |
| [ListStyle][ myStyle = doc.AddListStyle( [ListType].Numbered, [\"UserStyle\"]);]      |
|                                                                                                                                                                                                                        |
| [WListLevel][ listLevel1 = myStyle.Levels\[ 0 \];]                                                                                |
|                                                                                                                                                                                                                        |
| [listLevel1.FollowCharacter = [FollowCharacterType].Tab;]                                                                                                     |
|                                                                                                                                                                                                                        |
| [listLevel1.TextPosition = 80f;]                                                                                                                                                   |
|                                                                                                                                                                                                                        |
| [listLevel1.NumberAlignment = [ListNumberAlignment].Right;]                                                                                                   |
|                                                                                                                                                                                                                        |
| [listLevel1.TabSpaceAfter = 40f;]                                                                                                                                                  |
|                                                                                                                                                                                                                        |
| [listLevel1.StartAt = 3;]                                                                                                                                                          |
|                                                                                                                                                                                                                        |
| [listLevel1.NumberPrefix = [\"(((\"];]                                                                                                                      |
|                                                                                                                                                                                                                        |
| [listLevel1.NumberSufix = [\"\*\*\*.\"];]                                                                                                                   |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [paragraph = section.AddParagraph();]                                                                                                                                              |
|                                                                                                                                                                                                                        |
| [paragraph.AppendText( [\"First numbered\"] );]                                                                                                             |
|                                                                                                                                                                                                                        |
| [paragraph.ListFormat.ApplyStyle( [\"UserStyle\"] );]                                                                                                       |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [paragraph = section.AddParagraph();]                                                                                                                                              |
|                                                                                                                                                                                                                        |
| [ListStyle][ bulletStyle = doc.AddListStyle( [ListType].Bulleted, [\"UserStyle1\"]);] |
|                                                                                                                                                                                                                        |
| [WListLevel][ level = bulletStyle.Levels\[ 0 \];]                                                                                 |
|                                                                                                                                                                                                                        |
| [level.NumberPosition = 30f;]                                                                                                                                                      |
|                                                                                                                                                                                                                        |
| [level.TabSpaceAfter = 15f;]                                                                                                                                                       |
|                                                                                                                                                                                                                        |
| [level.FollowCharacter = [FollowCharacterType].Tab;]                                                                                                          |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [paragraph.AppendText( [\"First bullet\"] );      ]                                                                                                         |
|                                                                                                                                                                                                                        |
| [paragraph.ListFormat.ApplyStyle( [\"UserStyle1\"] );     ]                                                                                                 |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [paragraph = section.AddParagraph();]                                                                                                                                              |
|                                                                                                                                                                                                                        |
| [paragraph.AppendText( [\"Bulleted level 1\"] );      ]                                                                                                     |
|                                                                                                                                                                                                                        |
| [paragraph.ListFormat.ContinueListNumbering();]                                                                                                                                    |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [paragraph = section.AddParagraph();]                                                                                                                                              |
|                                                                                                                                                                                                                        |
| [paragraph.AppendText( [\"Numbered level 0 again\"] );             ]                                                                                        |
|                                                                                                                                                                                                                        |
| [paragraph.ListFormat.ApplyStyle( [\"UserStyle\"] );]                                                                                                       |
|                                                                                                                                                                                                                        |
| [section.AddParagraph();]                                                                                                                                                          |
|                                                                                                                                                                                                                        |
| [section.AddParagraph();]                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                          |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                                             |
| [\'Write default numbered list          ]                                                                                                                                 |
|                                                                                                                                                                                                                             |
| [Dim][ paragraph [As] IWParagraph = section.AddParagraph()]                                                       |
|                                                                                                                                                                                                                             |
| [paragraph.AppendText([\"First Numbered ( level 0 )\"])]                                                                                                         |
|                                                                                                                                                                                                                             |
| [paragraph.ListFormat.ApplyDefNumberedStyle()]                                                                                                                                          |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [paragraph = section.AddParagraph()]                                                                                                                                                    |
|                                                                                                                                                                                                                             |
| [paragraph.AppendText([\"Level 1\"])]                                                                                                                            |
|                                                                                                                                                                                                                             |
| [paragraph.ListFormat.ContinueListNumbering()]                                                                                                                                          |
|                                                                                                                                                                                                                             |
| [paragraph.ListFormat.IncreaseIndentLevel()]                                                                                                                                            |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [paragraph = section.AddParagraph()]                                                                                                                                                    |
|                                                                                                                                                                                                                             |
| [paragraph.AppendText([\"Level 0\"])]                                                                                                                            |
|                                                                                                                                                                                                                             |
| [paragraph.ListFormat.ContinueListNumbering()]                                                                                                                                          |
|                                                                                                                                                                                                                             |
| [paragraph.ListFormat.DecreaseIndentLevel()]                                                                                                                                            |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [section.AddParagraph()]                                                                                                                                                                |
|                                                                                                                                                                                                                             |
| [section.AddParagraph()]                                                                                                                                                                |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [\'Write default bulleted list  ]                                                                                                                                         |
|                                                                                                                                                                                                                             |
| [paragraph = section.AddParagraph()]                                                                                                                                                    |
|                                                                                                                                                                                                                             |
| [paragraph.AppendText([\"First bulleted ( level 0 )\"])]                                                                                                         |
|                                                                                                                                                                                                                             |
| [paragraph.ListFormat.ApplyDefBulletStyle()]                                                                                                                                            |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [paragraph = section.AddParagraph()]                                                                                                                                                    |
|                                                                                                                                                                                                                             |
| [paragraph.AppendText([\"Level 1\"])]                                                                                                                            |
|                                                                                                                                                                                                                             |
| [paragraph.ListFormat.ContinueListNumbering()]                                                                                                                                          |
|                                                                                                                                                                                                                             |
| [paragraph.ListFormat.IncreaseIndentLevel()]                                                                                                                                            |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [paragraph = section.AddParagraph()]                                                                                                                                                    |
|                                                                                                                                                                                                                             |
| [paragraph.AppendText([\"Level 0\"])]                                                                                                                            |
|                                                                                                                                                                                                                             |
| [paragraph.ListFormat.ContinueListNumbering()]                                                                                                                                          |
|                                                                                                                                                                                                                             |
| [paragraph.ListFormat.DecreaseIndentLevel()]                                                                                                                                            |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [section.AddParagraph()]                                                                                                                                                                |
|                                                                                                                                                                                                                             |
| [section.AddParagraph()]                                                                                                                                                                |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [\'Write mixed bulleted and numbered list ]                                                                                                                               |
|                                                                                                                                                                                                                             |
| [Dim][ myStyle [As] ListStyle = doc.AddListStyle(ListType.Numbered, [\"UserStyle\"])]      |
|                                                                                                                                                                                                                             |
| [Dim][ listLevel1 [As] WListLevel = myStyle.Levels(0)]                                                            |
|                                                                                                                                                                                                                             |
| [listLevel1.FollowCharacter = FollowCharacterType.Tab]                                                                                                                                  |
|                                                                                                                                                                                                                             |
| [listLevel1.TextPosition = 80f]                                                                                                                                                         |
|                                                                                                                                                                                                                             |
| [listLevel1.NumberAlignment = ListNumberAlignment.Right]                                                                                                                                |
|                                                                                                                                                                                                                             |
| [listLevel1.TabSpaceAfter = 40f]                                                                                                                                                        |
|                                                                                                                                                                                                                             |
| [listLevel1.StartAt = 3]                                                                                                                                                                |
|                                                                                                                                                                                                                             |
| [listLevel1.NumberPrefix = [\"(((\"]]                                                                                                                            |
|                                                                                                                                                                                                                             |
| [listLevel1.NumberSufix = [\"\*\*\*.\"]]                                                                                                                         |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                       |
|                                                                                                                                                                                                                             |
| [paragraph = section.AddParagraph()]                                                                                                                                                    |
|                                                                                                                                                                                                                             |
| [paragraph.AppendText([\"First numbered\"])]                                                                                                                     |
|                                                                                                                                                                                                                             |
| [paragraph.ListFormat.ApplyStyle([\"UserStyle\"])]                                                                                                               |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [paragraph = section.AddParagraph()]                                                                                                                                                    |
|                                                                                                                                                                                                                             |
| [Dim][ bulletStyle [As] ListStyle = doc.AddListStyle(ListType.Bulleted, [\"UserStyle1\"])] |
|                                                                                                                                                                                                                             |
| [Dim][ level [As] WListLevel = bulletStyle.Levels(0)]                                                             |
|                                                                                                                                                                                                                             |
| [level.NumberPosition = 30f]                                                                                                                                                            |
|                                                                                                                                                                                                                             |
| [level.TabSpaceAfter = 15f]                                                                                                                                                             |
|                                                                                                                                                                                                                             |
| [level.FollowCharacter = FollowCharacterType.Tab]                                                                                                                                       |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [paragraph.AppendText([\"First bullet\"])]                                                                                                                       |
|                                                                                                                                                                                                                             |
| [paragraph.ListFormat.ApplyStyle([\"UserStyle1\"])]                                                                                                              |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [paragraph = section.AddParagraph()]                                                                                                                                                    |
|                                                                                                                                                                                                                             |
| [paragraph.AppendText([\"Bulleted level 1\"])]                                                                                                                   |
|                                                                                                                                                                                                                             |
| [paragraph.ListFormat.ContinueListNumbering()]                                                                                                                                          |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [paragraph = section.AddParagraph()]                                                                                                                                                    |
|                                                                                                                                                                                                                             |
| [paragraph.AppendText([\"Numbered level 0 again\"])]                                                                                                             |
|                                                                                                                                                                                                                             |
| [paragraph.ListFormat.ApplyStyle([\"UserStyle\"])]                                                                                                               |
|                                                                                                                                                                                                                             |
| [section.AddParagraph()]                                                                                                                                                                |
|                                                                                                                                                                                                                             |
| [section.AddParagraph()]                                                                                                                                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

