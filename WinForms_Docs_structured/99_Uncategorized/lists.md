---
title: lists.md
original_path: WinForms_Docs/99_Uncategorized/lists.md
created_at: 2025-08-05
---






#### Lists {#lists style="tab-stops: 0pt"}

 

**ListStyle** class represents list properties in the Word paragraph style. Collection of list styles is accessible through the **WordDocument.ListStyles** property.

 

You can create your own list style. To add a list style by using DocIO, use the **WordDocument.AddListStyle** method. Every list style has its own name. You can use the **Name** property to access the style name. There are list styles of two types.

 

[·      ]Numbered

[·      ]Bulleted

 

You can specify the type of the list style by using the **ListType** property. Every ListStyle object contains the collection of list levels. This collection can contain from one to nine levels (maximum number of list levels). Collection of list levels is accessible through the **Levels** property. This property returns the ListLevelCollection object. List Level Collection (ListLevelCollection class) contains objects of the WListLevel class.

 

List Styles in MS Word

 

{border="0"}

Figure 74[: Create New Custom List Style]

 

**** 

{border="0"}

Figure 75[: Numbered List Style]

[]{#p71} 

{border="0"}

Figure 76: Bulleted List Style

 

**** 

Public Properties

 


  ----------------------------------------------- ----------------------------------------------------
  Name                                            Description
  Levels                                          Gets list levels collection.  
  ListType                                        Gets or sets list type.  
  Name                                            Gets style name.  
  StyleType                                       Gets the type of the style.  
  ListStyle.ListStyle (IWordDocument, ListType)   Initializes a new instance of the ListStyle class.
  ----------------------------------------------- ----------------------------------------------------


 

Public Methods

 


  ---------------------- ------------------------------------------
  Name                   Description
  Clone                  Clones current style object.  
  CreateEmptyListStyle   Static method. Creates empty list style.
  ---------------------- ------------------------------------------


 

**WListLevel** class represents list level in the Word document. By using the WListLevel class, you can customize the list level options.

 

**Public Constructor**

**[]** 


  ----------------------------------- -----------------------------------------------
  Name                                Description
  WListLevel.WListLevel (ListStyle)   Initializes new instance of WListLevel class.
  ----------------------------------- -----------------------------------------------


**[]** 

Public Methods

**[]** 


  ----------------- --------------------------------------------
  Name              Description
  Clone             Clones this instance.  
  GetListItemText   Gets list symbol for specified item index.
  ----------------- --------------------------------------------


**[]** 

Public Properties

**[]** 


  ----------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------
  Name                    Description
  BulletCharacter         Gets or sets bullet pattern.  
  CharacterFormat         Gets or sets character formats of list symbol.  
  FollowCharacter         Gets or sets the type of character following the number text for the paragraph.  
  IsLegalStyleNumbering   Gets or sets ArabicNumberFormat property ( true if the level turns all inherited numbers to arabic, false if it preserves their number format code ).  
  NoRestartByHigher       True if the level\'s number sequence is not restarted by higher (more significant) levels in the list.  
  NumberAlignment         Gets or sets alignment (left, right, or centered) of the paragraph number.  
  NumberPosition          Gets or sets the number / bullet position for current listlevel (in points).
  NumberPrefix            Gets or sets prefix pattern for numbered level.  
  NumberSuffix            Gets or sets suffix pattern for numbered level.  
  ParagraphFormat         Gets or sets paragraph format of list level.  
  PatternType             Gets or sets list numbering type.  
  StartAt                 Gets or sets start at value.  
  TabSpaceAfter           Gets or sets spacing after list level\'s number or bullet ( tab position if follow character is tab ).  
  TextPosition            Gets or sets the left listlevel indent (in points).
  UsePrevLevelPattern     When true, number generated will include previous levels (used for legal numbering).  
  ----------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------


 

The following example illustrates how to create user-defined list styles and apply it to the paragraph.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                      |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                |
|                                                                                                                                                                                                                     |
| [//User bullet list style]                                                                                                                                        |
|                                                                                                                                                                                                                     |
| [ListStyle][ bulStyle = doc.AddListStyle([ListType].Bulleted, [\"BulletStyle\"]);] |
|                                                                                                                                                                                                                     |
| [WListLevel][ bulLevel1 = bulStyle.Levels\[0\];]                                                                               |
|                                                                                                                                                                                                                     |
| [bulLevel1.FollowCharacter = [FollowCharacterType].Space;]                                                                                                 |
|                                                                                                                                                                                                                     |
| [bulLevel1.TextPosition = 40f;]                                                                                                                                                 |
|                                                                                                                                                                                                                     |
| [bulLevel1.NumberAlignment = [ListNumberAlignment].Right;]                                                                                                 |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [WListLevel][ bulLevel2 = bulStyle.Levels\[1\];]                                                                               |
|                                                                                                                                                                                                                     |
| [bulLevel2.FollowCharacter = [FollowCharacterType].Space;]                                                                                                 |
|                                                                                                                                                                                                                     |
| [bulLevel2.TextPosition = 60f;]                                                                                                                                                 |
|                                                                                                                                                                                                                     |
| [bulLevel2.NumberAlignment = [ListNumberAlignment].Right;]                                                                                                 |
|                                                                                                                                                                                                                     |
| [bulLevel2.TabSpaceAfter = 40f;]                                                                                                                                                |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [paragraph = section.AddParagraph();]                                                                                                                                           |
|                                                                                                                                                                                                                     |
| [paragraph.AppendText([\"First bulleted ( level 0 )\"]);]                                                                                                |
|                                                                                                                                                                                                                     |
| [paragraph.ListFormat.ApplyStyle([\"BulletStyle\"]);]                                                                                                    |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [paragraph = section.AddParagraph();]                                                                                                                                           |
|                                                                                                                                                                                                                     |
| [paragraph.AppendText([\"Level 1\"]);]                                                                                                                   |
|                                                                                                                                                                                                                     |
| [paragraph.ListFormat.ContinueListNumbering();]                                                                                                                                 |
|                                                                                                                                                                                                                     |
| [paragraph.ListFormat.IncreaseIndentLevel();]                                                                                                                                   |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [paragraph = section.AddParagraph();]                                                                                                                                           |
|                                                                                                                                                                                                                     |
| [paragraph.AppendText([\"Level 0\"]);]                                                                                                                   |
|                                                                                                                                                                                                                     |
| [paragraph.ListFormat.ContinueListNumbering();]                                                                                                                                 |
|                                                                                                                                                                                                                     |
| [paragraph.ListFormat.DecreaseIndentLevel();]                                                                                                                                   |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [//User numbered list style]                                                                                                                                      |
|                                                                                                                                                                                                                     |
| [ListStyle][ newStyle = doc.AddListStyle([ListType].Numbered, [\"NewStyle\"]);]    |
|                                                                                                                                                                                                                     |
| [WListLevel][ listLevelNew = newStyle.Levels\[0\];]                                                                            |
|                                                                                                                                                                                                                     |
| [listLevelNew.FollowCharacter = [FollowCharacterType].Tab;]                                                                                                |
|                                                                                                                                                                                                                     |
| [listLevelNew.TextPosition = 80f;]                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [listLevelNew.NumberAlignment = [ListNumberAlignment].Right;]                                                                                              |
|                                                                                                                                                                                                                     |
| [listLevelNew.TabSpaceAfter = 40f;]                                                                                                                                             |
|                                                                                                                                                                                                                     |
| [listLevelNew.StartAt = 2;]                                                                                                                                                     |
|                                                                                                                                                                                                                     |
| [listLevelNew.NumberPrefix = [\"\>\>\"];]                                                                                                                |
|                                                                                                                                                                                                                     |
| [listLevelNew.NumberSufix = [\"\<\<\"];]                                                                                                                 |
|                                                                                                                                                                                                                     |
| [listLevelNew.CharacterFormat.FontSize = 15;]                                                                                                                                   |
|                                                                                                                                                                                                                     |
| [listLevelNew.CharacterFormat.TextColor = [Color].Blue;]                                                                                                   |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [WListLevel][ listLevelNew1 = newStyle.Levels\[1\];]                                                                           |
|                                                                                                                                                                                                                     |
| [listLevelNew1.IsLegalStyleNumbering = [true];]                                                                                                            |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [WListLevel][ listLevelNew2 = newStyle.Levels\[2\];]                                                                           |
|                                                                                                                                                                                                                     |
| [listLevelNew1.NoRestartByHigher = [true];]                                                                                                                |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [paragraph = section.AddParagraph();]                                                                                                                                           |
|                                                                                                                                                                                                                     |
| [paragraph.AppendText([\"First Numbered ( level 0 )\"]);]                                                                                                |
|                                                                                                                                                                                                                     |
| [paragraph.ListFormat.ApplyStyle([\"NewStyle\"]);]                                                                                                       |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [paragraph = section.AddParagraph();]                                                                                                                                           |
|                                                                                                                                                                                                                     |
| [paragraph.AppendText([\"Level 1\"]);]                                                                                                                   |
|                                                                                                                                                                                                                     |
| [paragraph.ListFormat.ContinueListNumbering();]                                                                                                                                 |
|                                                                                                                                                                                                                     |
| [paragraph.ListFormat.IncreaseIndentLevel();]                                                                                                                                   |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [paragraph = section.AddParagraph();]                                                                                                                                           |
|                                                                                                                                                                                                                     |
| [paragraph.AppendText([\"Level 0\"]);]                                                                                                                   |
|                                                                                                                                                                                                                     |
| [paragraph.ListFormat.ContinueListNumbering();]                                                                                                                                 |
|                                                                                                                                                                                                                     |
| [paragraph.ListFormat.ListLevelNumber = 0;]                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                        |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                                           |
| [\'User bullet list style]                                                                                                                                              |
|                                                                                                                                                                                                                           |
| [Dim][ bulStyle [As] ListStyle = doc.AddListStyle(ListType.Bulleted, [\"BulletStyle\"])] |
|                                                                                                                                                                                                                           |
| [Dim][ bulLevel1 [As] WListLevel = bulStyle.Levels(0)]                                                          |
|                                                                                                                                                                                                                           |
| [bulLevel1.FollowCharacter = FollowCharacterType.Space]                                                                                                                               |
|                                                                                                                                                                                                                           |
| [bulLevel1.TextPosition = 40f]                                                                                                                                                        |
|                                                                                                                                                                                                                           |
| [bulLevel1.NumberAlignment = ListNumberAlignment.Right]                                                                                                                               |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [Dim][ bulLevel2 [As] WListLevel = bulStyle.Levels(1)]                                                          |
|                                                                                                                                                                                                                           |
| [bulLevel2.FollowCharacter = FollowCharacterType.Space]                                                                                                                               |
|                                                                                                                                                                                                                           |
| [bulLevel2.TextPosition = 60f]                                                                                                                                                        |
|                                                                                                                                                                                                                           |
| [bulLevel2.NumberAlignment = ListNumberAlignment.Right]                                                                                                                               |
|                                                                                                                                                                                                                           |
| [bulLevel2.TabSpaceAfter = 40f]                                                                                                                                                       |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [paragraph = section.AddParagraph()]                                                                                                                                                  |
|                                                                                                                                                                                                                           |
| [paragraph.AppendText([\"First bulleted ( level 0 )\"])]                                                                                                       |
|                                                                                                                                                                                                                           |
| [paragraph.ListFormat.ApplyStyle([\"BulletStyle\"])]                                                                                                           |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [paragraph = section.AddParagraph()]                                                                                                                                                  |
|                                                                                                                                                                                                                           |
| [paragraph.AppendText([\"Level 1\"])]                                                                                                                          |
|                                                                                                                                                                                                                           |
| [paragraph.ListFormat.ContinueListNumbering()]                                                                                                                                        |
|                                                                                                                                                                                                                           |
| [paragraph.ListFormat.IncreaseIndentLevel()]                                                                                                                                          |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [paragraph = section.AddParagraph()]                                                                                                                                                  |
|                                                                                                                                                                                                                           |
| [paragraph.AppendText([\"Level 0\"])]                                                                                                                          |
|                                                                                                                                                                                                                           |
| [paragraph.ListFormat.ContinueListNumbering()]                                                                                                                                        |
|                                                                                                                                                                                                                           |
| [paragraph.ListFormat.DecreaseIndentLevel()]                                                                                                                                          |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [\'User numbered list style]                                                                                                                                            |
|                                                                                                                                                                                                                           |
| [Dim][ newStyle [As] ListStyle = doc.AddListStyle(ListType.Numbered, [\"NewStyle\"])]    |
|                                                                                                                                                                                                                           |
| [Dim][ listLevelNew [As] WListLevel = newStyle.Levels(0)]                                                       |
|                                                                                                                                                                                                                           |
| [listLevelNew.FollowCharacter = FollowCharacterType.Tab]                                                                                                                              |
|                                                                                                                                                                                                                           |
| [listLevelNew.TextPosition = 80f]                                                                                                                                                     |
|                                                                                                                                                                                                                           |
| [listLevelNew.NumberAlignment = ListNumberAlignment.Right]                                                                                                                            |
|                                                                                                                                                                                                                           |
| [listLevelNew.TabSpaceAfter = 40f]                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [listLevelNew.StartAt = 2]                                                                                                                                                            |
|                                                                                                                                                                                                                           |
| [listLevelNew.NumberPrefix = [\"\>\>\"]]                                                                                                                       |
|                                                                                                                                                                                                                           |
| [listLevelNew.NumberSufix = [\"\<\<\"]]                                                                                                                        |
|                                                                                                                                                                                                                           |
| [listLevelNew.CharacterFormat.FontSize = 15]                                                                                                                                          |
|                                                                                                                                                                                                                           |
| [listLevelNew.CharacterFormat.TextColor = Color.Blue]                                                                                                                                 |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [listLevelNew1 [As] WListLevel = newStyle.Levels(1)]                                                                                                             |
|                                                                                                                                                                                                                           |
| [listLevelNew1.IsLegalStyleNumbering = [True]]                                                                                                                   |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                       |
|                                                                                                                                                                                                                           |
| [listLevelNew2 [As] WListLevel = newStyle.Levels(2)]                                                                                                             |
|                                                                                                                                                                                                                           |
| [listLevelNew1.NoRestartByHigher = [True]]                                                                                                                       |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                       |
|                                                                                                                                                                                                                           |
| [paragraph = section.AddParagraph()]                                                                                                                                                  |
|                                                                                                                                                                                                                           |
| [paragraph.AppendText([\"First Numbered ( level 0 )\"])]                                                                                                       |
|                                                                                                                                                                                                                           |
| [paragraph.ListFormat.ApplyStyle([\"NewStyle\"])]                                                                                                              |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [paragraph = section.AddParagraph()]                                                                                                                                                  |
|                                                                                                                                                                                                                           |
| [paragraph.AppendText([\"Level 1\"])]                                                                                                                          |
|                                                                                                                                                                                                                           |
| [paragraph.ListFormat.ContinueListNumbering()]                                                                                                                                        |
|                                                                                                                                                                                                                           |
| [paragraph.ListFormat.IncreaseIndentLevel()]                                                                                                                                          |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [paragraph = section.AddParagraph()]                                                                                                                                                  |
|                                                                                                                                                                                                                           |
| [paragraph.AppendText([\"Level 0\"])]                                                                                                                          |
|                                                                                                                                                                                                                           |
| [paragraph.ListFormat.ContinueListNumbering()]                                                                                                                                        |
|                                                                                                                                                                                                                           |
| [paragraph.ListFormat.ListLevelNumber = 0]                                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

More:





