import React from "react"
import Header from "../components/header"
import MainEntry from "../components/main_entry"
import Footer from "../components/footer"

export default () => (
    <div>
        <Header headline="The Urban Brothers" />
        <p id="tagline">Welcome to the Urban Brothers Website</p>
        <div class="container">
            <MainEntry title="Help" />
            <p>For help with any community related matters, please contact one of our moderators or admins on either TeamSpeak or Discord.</p>
        </div>
        <Footer />
    </div>
)
