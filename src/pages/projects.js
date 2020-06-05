import React from "react"
import Header from "../components/header"
import Footer from "../components/footer"

export default () => (
    <div class="container">
        <Header headline="Projects" />
        <h2>Minecraft</h2>
        <p>Our small Minecraft server is hosted on this server. This project currently works with a whitelist of people.</p>
        <h2>League/ TFT</h2>
        <p>Most of the times, there are people who play League or TFT in the respecting channels.</p>
        <h2>More</h2>
        <p>More projects are coming regularly (kind of) so stay tuned!</p>
        <Footer />
    </div>
)
