/**
  Urban Brothers site config
 */

module.exports = {
  resolve: `gatsby-plugin-manifest`,
  options: {
    name: `Urban Brothers Homepage`,
    short_name: `Urban Website`,
    start_url: `/`,
    background_color: `#6b37bf`,
    theme_color: `#6b37bf`,
    // Enables "Add to Homescreen" prompt and disables browser UI (including back button)
    // see https://developers.google.com/web/fundamentals/web-app-manifest/#display
    display: `standalone`,
    icon: `src/images/icon.png`, // This path is relative to the root of the site.
  },
  siteMetadata: {
    title: `Urban Brothers Website`,
    siteURL: `https://urbanbrothers.de`,
    description: `Homepage of the Urban Brothers`,
  },
  // pathPrefix: ``, // URL prefix of the whole site
}
