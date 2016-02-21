var DEFAULTURL = "localhost:5000/extensiontest";

// POST the data to the server using XMLHttpRequest
function analyzePage() {
    // Cancel the form submit
    event.preventDefault();
    // The URL to POST our data to
    var postUrl = DEFAULTURL;
    // Set up an asynchronous AJAX POST request
    var xhr = new XMLHttpRequest();
    // Callback function
    xhr.onreadystatechange = function() {
      if (xhr.readyState == 4 && xhr.status == 200){
        console.log(xhr.responseText);
        alert("Showing results page.");
        /* TODO: serve results page */
      }
    }
    chrome.tabs.getSelected(null, function(tab) {
        var tabID = tab.id;
        var tabUrl = tab.url;
        var keyword = document.getElementById("extensionForm").elements["keyword"];
    });
    xhr.open('POST', postUrl, true);
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhr.send("keyword="+keyword+"&url="+tabUrl);


    /*var params = 'keyword=' + keyword +
                 '&url=' + tabUrl;

    // Send the request and set status*/
    xhr.send();
}

document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('extensionForm').onsubmit = analyzePage;
}, false);
