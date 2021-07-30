/* When editing static files, remember to run PYTHON MANAGE.PY COLLECTSTATIC afterwards */


/* Fade out messages after 5000 milliseconds */
setTimeout(function () {
   $("#message").fadeOut("slow");
}, 5000);


/* Toggle search customer by ID */
function showSearch() {
   const s = document.getElementById("show-search");

   if (s.style.display == "none") {
      s.style.display = "block";
   } else {
      s.style.display = "none";
   }
}


/* Prompt delete "Are you sure?" "Yes" */
function promptDelete() {
   const a = document.getElementById("answer-yes");
   const d = document.getElementById("prompt-delete");

   if (a.style.display == "none") {
      a.style.display = "inline-block";
   } else {
      a.style.display = "none";
   }

   d.innerHTML = "Delete.";
   d.style.pointerEvents = "None";
   d.style.cursor = "default";
   d.style.color = "#81898F";
}