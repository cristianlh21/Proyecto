import "../css/main.css";
import htmx from "htmx.org";
import Alpine from 'alpinejs'
import "/node_modules/flyonui/flyonui.js"
window.Alpine = Alpine
 
Alpine.start()

//Accesible desde cualquier template
window.htmx = htmx;