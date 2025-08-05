---
title: stylemanagerandscriptmanager7.md
original_path: WinForms_Docs/02_Concepts/stylemanagerandscriptmanager7.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






    


### StyleManager and ScriptManager {#stylemanager-and-scriptmanager style="TEXT-INDENT: -36pt; MARGIN-LEFT: 36pt; tab-stops: 36.0pt"}

StyleManager

**StyleManager** is a new CSS resource manager that helps in registering CSS files which enables Minification, Compression, Combination of CSS resources for ASP.NET MOBILE MVC web applications. The files in StyleManager resources are set to be combined, minified, and compressed (either gzip or deflate, depending on your browser) before sending to browser. All are done using a single HTTP request per resource set.

 

ScriptManager

**ScriptManager** is a new Script resource manager that helps in registering JavaScript files. The ScriptManager registers only the Syncfusion.Mvc components script files. The files in ScriptManager resources are set to be combined, minified, and compressed(either gzip and deflate, depending on your browser) before sending to browser..

**[]**  

Use Case Scenarios

StyleManager and ScriptManager enables minification, compression and combination of CSS resources and JavaScript resources respectively. These resource managers improves the performance of the website.

 

[] 

[]{#related-topics}

