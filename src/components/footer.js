import React from "react"
import { Link } from "gatsby"

export default () => (
    <div style={{ textAlign: `center` }}>
        <a target="_blanc" href="ts3server://urbanbrothers.de">
            ts
        </a>
        .
        <a target="_blanc" href="https://discord.gg/aYcvtWE">
            discord
        </a>
        .
        <a target="_blanc" href="https://github.com/creyD/urban_website">
            github
        </a>
        .
        <a target="_blanc" href="https://paypal.me/pools/c/89fz0b2YFk">
            donate
        </a>
        .<Link to="/about/">about</Link>
    </div>
)
