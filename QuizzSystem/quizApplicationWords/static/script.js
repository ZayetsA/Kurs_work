window.onload = initall;
var  saveBookButton ;
function initall() {
    saveBookButton=document.getElementById('save_ans')
    saveBookButton.onclick = save_ans;
}
function save_ans() {
    var ans = $("input:radio[name=name]:checked").val()
    var url = '/save_ans?ans='+ans
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
    }
  };
  req.open("GET", url, true);
  req.send();
}