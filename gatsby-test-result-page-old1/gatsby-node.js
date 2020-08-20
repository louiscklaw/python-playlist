// https://www.mrozilla.cz/blog/gatsby-eslint-vscode-import-alias/

const path = require("path");

exports.onCreateWebpackConfig = ({ actions }) => {
  actions.setWebpackConfig({
    resolve: {
      alias: {
        "~components": path.resolve(__dirname, "src/components"),
        "~contexts": path.resolve(__dirname, "src/contexts"),
        // "~constants": path.resolve(__dirname, "src/constants"),
        "~scss": path.resolve(__dirname, "src/scss"),
        "~utils": path.resolve(__dirname, "src/utils"),
      }
    }
  });
};

exports.onCreatePage = async ({ page, actions }) => {
  const { createPage } = actions

  // Only update the `/app` page.
  if (page.path.match(/^\/app/)) {
    // page.matchPath is a special key that's used for matching pages
    // with corresponding routes only on the client.
    page.matchPath = "/*"

    // Update the page.
    createPage(page)
  }
}
