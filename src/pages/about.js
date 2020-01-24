import React from "react"
import Header from "../components/header"
import Footer from "../components/footer"

export default () => (
  <div>
    <Header headline="About" />
    <div class="container">
      <p>
        As this is a private website, so no legal notice is required. However
        let's clarify a few things:
      </p>

      <h2>Cookies</h2>
      <p>This site uses none.</p>

      <h2>GDPR</h2>
      <p>
        As this site doesn't use any user data, it complies with GDPR
        regulations.
      </p>

      <h2>Legal</h2>
      <p>
        If you have any questions or queries regarding this website, please
        write <a herf="mailto://webmaster@urbanbrothers.de">an email.</a>
      </p>
      <a href="/">
        <button>Back to homepage</button>
      </a>

      <Footer />
    </div>
  </div>
)
