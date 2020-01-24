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
                <a
                    href="https://steamcommunity.com/groups/urban_group"
                    target="_blanc"
                >
                    <li>Steam Community Group</li>
                </a>
            </ul>
            <MainEntry title="Contribute" />
            <p>
                As it was requested by some people over the last years, we
                finally created a{" "}
                <a href="https://paypal.me/pools/c/89fz0b2YFk" target="_blanc">
                    donation link (PayPal).
                </a>{" "}
                All the donated money will go 100% towards keeping up the
                servers and running other community related projects in the
                future. However our services will continue to be freely
                available for anyone. -{" "}
                <b>Thank you to everyone who donated.</b>
            </p>
            <MainEntry title="Help" />
            <p>
                For help with any community related matters, please contact one
                of our moderators or admins on either TeamSpeak or Discord.
            </p>
        </div>
        <Footer />
    </div>
)
