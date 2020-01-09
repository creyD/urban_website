import React from "react"
import Header from "../components/header"
var dateFormat = require("dateformat")

const GIT_OWNER = "creyD"
const GIT_REPO = "urban_website"
const GIT_URL =
  "https://api.github.com/repos/" + GIT_OWNER + "/" + GIT_REPO + "/events"
const GIT_COMMIT_URL =
  "https://github.com/" + GIT_OWNER + "/" + GIT_REPO + "/commit/"

// Format the date provided by the GitHub API
function getDateFormatted(unformated_date) {
  return dateFormat(unformated_date, "dd.mm.yyyy")
}

// Adds Git History to the site
function addGitHistory(data) {
  for (var push in data) {
    for (var commit in data[push]["payload"]["commits"]) {
      var new_li = document.createElement("li")
      var url = GIT_COMMIT_URL + data[push]["payload"]["commits"][commit].sha
      new_li.innerHTML =
        data[push]["payload"]["commits"][commit].author.name +
        " committed on " +
        getDateFormatted(data[push].created_at) +
        ": " +
        data[push]["payload"]["commits"][commit].message +
        " <a href=" +
        url +
        " target='_blanc'>(Link)</a>"
      document.getElementById("log").appendChild(new_li)
    }
  }
}

// Send HTTP request to the GitHub API to get information about this repo
const Http = new XMLHttpRequest()
Http.open("GET", GIT_URL)
Http.send()

// If the API responds call the addGitHistory function
Http.onreadystatechange = function() {
  if (this.readyState === 4 && this.status === 200) {
    addGitHistory(JSON.parse(Http.responseText))
  }
}

export default () => (
  <div>
    <Header headline="git log" />
    <p>
      You can see the full commit history{" "}
      <a href="https://github.com/creyD/urban_website/commits/master">here</a>.
    </p>
    <ul id="log"></ul>
  </div>
)
