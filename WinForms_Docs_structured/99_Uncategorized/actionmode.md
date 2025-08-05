---
title: actionmode.md
original_path: WinForms_Docs/99_Uncategorized/actionmode.md
created_at: 2025-08-05
---








  









## Action Mode {#action-mode style="tab-stops: 0pt"}

 

Action Mode defines the post back method that can be used by OlapGrid while communicating with MVC server.

 

OlapGrid support following action modes:

 

[·      ]Server

[·      ]Ajax

 

Server[]

[] 

In the server mode all of the communication between server and OlapGrid will be take place using complete full post back.

 

Ajax[]

[] 

In this mode, all the communication will be made using jQuery AJAX. The request will be handled by our OlapHtmlActionResult class.

 

Use Case Scenario[[]]{.Heading3Char}

Action Mode helps users to customize the action mode of OlapGrid.

More:







