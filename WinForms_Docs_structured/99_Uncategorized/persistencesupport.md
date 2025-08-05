---
title: persistencesupport.md
original_path: WinForms_Docs/99_Uncategorized/persistencesupport.md
created_at: 2025-08-05
---






##### Persistence Support {#persistence-support style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

The PersistTabState property specifies the value which determines whether the TabState (ActivePage, TabOrder and Text) should be automatically persisted or not. The default value is set to False.

[] 


  ------------------------ -------------------------------------------------------------------------------------------------------
  TabControlAdv Property   Description
  PersistTabState          Gets / sets the value which determines whether the TabState should be automatically persisted or not.
  ------------------------ -------------------------------------------------------------------------------------------------------


[          ]


  --------------------------- -------------------------------------------------------------------------------------
  Methods                     Description
  TabControlAdv.SaveState()   Persists the TabState (ActivePage, TabOrder and Text).
  TabControlAdv.LoadState()   Gets / sets the previously serialized TabState using the AppStateSerializer object.
  --------------------------- -------------------------------------------------------------------------------------


 

 

 

 

[]{#related-topics}

