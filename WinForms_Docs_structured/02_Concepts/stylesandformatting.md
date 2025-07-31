---
title: stylesandformatting.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\stylesandformatting.md
created_at: 2025-07-03
---








  









### Styles and Formatting {#styles-and-formatting style="tab-stops: 0pt"}

 

[]{#p66}Every word document contains a number of styles. They are as follows.

 

[·      ]Character Style

[·      ]Paragraph Style

[·      ]Table Style

 

In Word document style hierarchy, there is also a base style, **Normal**.

 

DocIO has three classes which represent Word styles.

 

[·      ]**CharacterStyle**: represents Word character style

[·      ]**WParagraphStyle**: represents Word paragraph style

[·      ]**ListStyle**: represents list properties in the Word paragraph style

 


Note: DocIO does not support table styles.


 

DocIO gives user an opportunity to add user-defined paragraph and list styles to the document. For details, see 

 

Collection of DocIO character and paragraph styles is accessible through the **WordDocument.Styles** property. Collection of list styles is accessible through the **WordDocument.ListStyles** property.

 

DocIO **Style** class is a base class for the CharacterStyle and WParagraphStyle classes. Style is an abstract class. **CharacterFormat** property of Style class defines character formatting. This property returns the object of WCharacterFormat type. **Name** property specifies the name of the style. **BaseStyle** property defines the base style (style inherits formatting of base style). User can apply one of the built-in Word styles by using the **WParagraph.ApplyStyle** method. The built-in styles are accessible through the **BuiltinStyle** enumeration.

 

**Public Properties**

 


  ----------------- --------------------------------
  Name              Description
  CharacterFormat   Gets the character format.    
  Name              Gets or sets style name.  
  StyleType         Gets the type of the style.  
  ----------------- --------------------------------


 

Public Methods

 


  ---------------- -------------------------------------
  Name             Description
  ApplyBaseStyle   Apply base style for current style.
  Clone            Clones itself.
  ---------------- -------------------------------------


More:

















