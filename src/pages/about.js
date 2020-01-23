import React from "react"
import Header from "../components/header"
import Footer from "../components/footer"

export default () => (
  <div>
    <Header headline="About" />
    <div class="container">
      <p>
        As this is a private website, it doesn't need an imprint. However let's
        clarify a few things:
      </p>

      <h2>Cookies</h2>
      <p>This site uses none.</p>

      <h2>GDPR</h2>
      <p>
        As this site doesn't use any user data, it complies with GDPR
        regulations.
      </p>

      <a href="/">
        <button>Back to homepage</button>
      </a>

      <Footer />
    </div>
  </div>
)
