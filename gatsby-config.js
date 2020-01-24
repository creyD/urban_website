/**
  Urban Brothers site config
 */

module.exports = {
    siteMetadata: {
        title: `Urban Brothers Website`,
        siteURL: `https://www.urbanbrothers.de`,
        description: `Homepage of the Urban Brothers`,
    },
    // pathPrefix: ``, // URL prefix of the whole site
    plugins: [
        {
            resolve: `gatsby-plugin-manifest`,
            options: {
                name: `Urban Brothers Homepage`,
                short_name: `Urban Website`,
                start_url: `/`,
                background_color: `#6b37bf`,
                theme_color: `#6b37bf`,
                // Enables "Add to Homescreen" prompt and disables browser UI (including back button)
                display: `standalone`,
                icon: `src/images/icon.png`, // This path is relative to the root of the site.
            },
        },
    ],
}
