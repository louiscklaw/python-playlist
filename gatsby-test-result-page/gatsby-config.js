module.exports = {
  siteMetadata: {
    title: `Gatsby Sourcing from JSON or YAML`,
    description: `Gatsby Source with JSON OR YAML`,
    author: `@gatsbyjs`,
  },
  plugins: [
    `gatsby-plugin-sass`,
    {
      resolve: `gatsby-plugin-google-fonts`,
      options: {
        fonts: [
          `Noto Sans TC`,
          `Indie Flower`,
          `source sans pro\:300,400,400i,700` // you can also specify font weights and styles
        ],
        display: 'swap'
      }
    }
  ],
}
