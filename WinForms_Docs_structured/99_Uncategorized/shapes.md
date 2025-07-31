---
title: shapes.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\shapes.md
created_at: 2025-07-03
---






#### Shapes {#shapes style="tab-stops: 0pt"}

 

Shape is a subdocument of the Word document. Shape is a general name for a group of elements. Shapes can be added to the document with the help of Microsoft Word. The AutoShapes combo box lists the group of shapes. Picture and TextBox are shapes too.

 

Every shape is represented in Word Document with a special shape marker (among text block) and a block of information about the shape, which is situated in the other part of the document.

 

DocIO has four classes which represent shapes.

 

[·      ]ShapeObject

[·      ]InlineShapeObject

[·      ]WPicture

[·      ]WTextBox

 

You have full access to the WPicture and WTextBox classes, i.e., you can read, modify, and create pictures and text boxes. Other shapes are only preserved by DocIO (user cannot create or modify them).

 

ShapeObject and InlineShapeObject

 

ShapeObject class represents all types of Word document shapes except pictures and text boxes.

 


Note: ShapeObject and InlineShapeObject classes are \"read only\" classes. You cannot modify shapes. An exception to this is the picture and textbox shape. All shapes except pictures and textbox shapes are only preserved.


 

ShapeObject class has only one public property -- **EntityType**. This property defines the type of the entity, and returns the EntityType.Shape for this class.

 

InlineShapeObject represent[s] all the inline shape objects (except inline textboxes and pictures). Inline shape objects are shape objects which have Inline with text layout.

 

Class Hierarchy

 

ParagraphItem

               \|

            ShapeObject

                   \|             

              InlineShapeObject

 

ShapeObject Public Property

 


  ------------ ------------------------------
  **Name**     **Description**
  EntityType   Gets the type of the entity.
  ------------ ------------------------------


More:









