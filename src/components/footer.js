import React from "react"
import { Link } from "gatsby"

export default () => (
  <div style={{ textAlign: `center` }}>
    <a target="_blanc" href="ts3server://urbanbrothers.de">
      ts
    </a>
    .
    <a target="_blanc" href="https://discord.gg/k6TnPq">
      discord
    </a>
    .
    <a target="_blanc" href="https://steamcommunity.com/groups/urban_group">
      steam
    </a>
    .
    <a target="_blanc" href="https://github.com/creyD/urban_website">
      github
    </a>
    .<Link to="/about/">about</Link>
  </div>
)
