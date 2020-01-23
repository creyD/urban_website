import React from "react"
import Header from "../components/header"
import MainEntry from "../components/main_entry"
import Footer from "../components/footer"

export default () => (
  <div>
    <Header headline="The Urban Brothers" />
    <p id="tagline">Welcome to the Urban Brothers Website</p>
    <div class="container">
      <MainEntry title="Ressources" />
      <ul>
        <a href="ts3server://urbanbrothers.de">
          <li>TeamSpeak 3 Server</li>
        </a>
        <a href="https://discord.gg/k6TnPq">
          <li>Discord Server</li>
        </a>
        <a href="https://steamcommunity.com/groups/urban_group" target="_blanc">
          <li>Steam Community Group</li>
        </a>
      </ul>
      <MainEntry title="Help" />
      <p>
        For help with any community related matters, please contact one of our
        moderators or admins on either TeamSpeak or Discord.
      </p>
    </div>
    <Footer />
  </div>
)
