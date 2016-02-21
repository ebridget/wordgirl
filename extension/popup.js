var DEFAULTURL = "localhost:5000";


  /**
 * Get the current URL.
 *
 * @param {function(string)} callback - called when the URL of the current tab
 *   is found.
 */
function getCurrentTabUrl(callback) {
  var queryInfo = {
    active: true,
    currentWindow: true
  };

  chrome.tabs.query(queryInfo, function(tabs) {
    var tab = tabs[0];
    var url = tab.url;
    console.assert(typeof url == 'string', 'tab.url should be a string');
    callback(url);
  });
}

// Global reference to the status display SPAN
var statusDisplay = null;

// POST the data to the server using XMLHttpRequest
function analyzePage() {
    alert("Analyzing page");
    // Cancel the form submit
    event.preventDefault();

    // The URL to POST our data to
    var postUrl = DEFAULTURL;

    // Set up an asynchronous AJAX POST request
    var xhr = new XMLHttpRequest();
    xhr.open('POST', postUrl, true);

    chrome.tabs.getSelected(null, function(tab) {
        var tabID = tab.id;
        var tabUrl = tab.url;
        var keyword = document.getElementById("extensionForm").elements["keyword"];
    });

    var params = 'keyword=' + keyword +
                 '&url=' + tabUrl;

    // Send the request and set status
    xhr.send(params);
    window.location.href="popup.html";
}

// When the popup HTML has loaded
window.addEventListener('load', function(evt) {
    // Cache a reference to the status display SPAN
    statusDisplay = document.getElementById('status-display');
    // Handle the bookmark form submit event with our addBookmark function
    document.getElementById('submitter').addEventListener('submit', analyzePage());
});
