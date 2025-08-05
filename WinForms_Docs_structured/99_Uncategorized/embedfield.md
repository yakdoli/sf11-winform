---
title: embedfield.md
original_path: WinForms_Docs/99_Uncategorized/embedfield.md
created_at: 2025-08-05
---






##### Embed Field {#embed-field style="tab-stops: 0pt"}

[]{#p46} 

**WEmbedField** class represents an embed field type in the Word document. Word does not allow to create an embed field type manually (using Microsoft Word interface). This field is used when the document has embedded objects. This field usually points to the container in the document which encloses the embedded object.

 


{border="0"}Note: Modification of WEmbedField properties can cause document corruption or incorrect document preservation. DocIO preserves only fields of this type.


 

**Class Hierarchy**

 

WTextRange

            \|

            WField

                        \|

                       WEmbedField

 

**Public Property**

 


  ------------ --------------------------------
  Name         Description
  EntityType   Gets the type of the entity.  
  ------------ --------------------------------


[]{#related-topics}

