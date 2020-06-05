import React from "react"
import Header from "../components/header"
import Footer from "../components/footer"

export default () => (
    <div class="container">
        <Header headline="Communication" />
        <h2>Discord</h2>
        <p>
            Feel free to join our Urban Discord <a href="https://discord.gg/k6TnPq">here</a>.
        </p>
        <h2>TeamSpeak 3</h2>
        <p>
            You may also join our TeamSpeak server, accessible under this same <a href="ts3server://urbanbrothers.de">urbanbrothers.de</a> domain.
        </p>
        <h2>Steam</h2>
        The{" "}
        <a href="https://steamcommunity.com/groups/urban_group" target="_blanc">
            steam community group
        </a>{" "}
        is rarely used for communications, but you may use it to show off the clan tag and join in with other members.
        <Footer />
    </div>
)
