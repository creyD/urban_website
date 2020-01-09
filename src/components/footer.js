import React from "react"
import { Link } from "gatsby"

export default () => (
  <div style={{ textAlign: `center` }}>
    <a href="ts3server://urbanbrothers.de">ts</a>.
    <a href="https://discord.gg/k6TnPq">discord</a>.
    <a href="https://steamcommunity.com/groups/urban_group">steam</a>.
    <a href="https://github.com/creyD/urban_website">github</a>.
    <Link to="/about/">about</Link>
  </div>
)
