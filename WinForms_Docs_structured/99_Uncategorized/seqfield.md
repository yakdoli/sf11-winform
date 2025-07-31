---
title: seqfield.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\seqfield.md
created_at: 2025-07-03
---






##### Seq Field {#seq-field style="tab-stops: 0pt"}

 

**WSeqField** class represents a sequence field type in the Word document. To add a sequence field in Microsoft Word, open **Insert** menu, click **Field**, and then click **Seq**. You can find information about the sequence field in the following location: [http://office.microsoft.com/en-us/word/HP051861901033.aspx].

 

You can use the **NumberFormat** property to set the numbering format for the fields, and the **CaptionName** property to set the name of the caption.

 

**Public Constructor**

 


  ------------------------------------- ----------------------------------------------------
  Name                                  Description
  WSeqField.WSeqField (IWordDocument)   Initializes a new instance of the WSeqField class.
  ------------------------------------- ----------------------------------------------------


 

Public Properties

 


+-----------------------------------+--------------------------------------------------------------------------------+
| Name                              | Description                                                                    |
+-----------------------------------+--------------------------------------------------------------------------------+
| CaptionName                       | Gets or sets caption name.                                                     |
+-----------------------------------+--------------------------------------------------------------------------------+
| EntityType                        | Gets the type of the entity.                                                   |
+-----------------------------------+--------------------------------------------------------------------------------+
| FormattingString                  | Gets the formatting string.                                                    |
+-----------------------------------+--------------------------------------------------------------------------------+
| NumberFormat                      | Gets or sets the type of caption numbering. It includes the following options. |
|                                   |                                                                                |
|                                   |                                                                                |
|                                   |                                                                                |
|                                   | Number                                                                         |
|                                   |                                                                                |
|                                   | Roman                                                                          |
|                                   |                                                                                |
|                                   | Alphabetic                                                                     |
+-----------------------------------+--------------------------------------------------------------------------------+


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                               |
| [WSeqField][ field = ( [WSeqField] )paragraph.AppendField([\"Sequence Field\"], [FieldType].FieldSequence );] |
|                                                                                                                                                                                                                                                                               |
| [field.CaptionName = [\"Sequence Field\"];]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                               |
| [field.NumberFormat = [CaptionNumberingFormat].Alphabetic;]                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                |
| [Dim][ field [As] WSeqField = [CType](paragraph.AppendField([\"Sequence Field\"], FieldType.FieldSequence), WSeqField)] |
|                                                                                                                                                                                                                                                                                |
| [field.CaptionName = [\"Sequence Field\"]]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                |
| [field.NumberFormat = CaptionNumberingFormat.Alphabetic]                                                                                                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

